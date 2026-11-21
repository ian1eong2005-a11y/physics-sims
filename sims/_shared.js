// Shared UX layer, injected into every applet by core/embed.py (in <head>, before the applet's own code).
// Zoom: Ctrl+wheel or pinch on the canvas, the +/− buttons, or plain wheel when "scroll = zoom" is on.
// Hotkeys: Space = play/pause, R = reset (when focus is not in a control).
//
// Show / hide layers (focus mode). An applet declares its parts once:
//   window.SIM_LAYERS = [{id:'lines', label:'Field lines', modes:['bar'], simple:true, input:'lines'}, …]
//     id      short name, used in page opts and URLs (?show=lines,compass)
//     label   what the checklist shows
//     modes   the applet modes (#modeSeg data-v) it belongs to; leave out for every mode
//     simple  true (or a list of modes): kept on by the Simple preset
//     on      false to start hidden (default true)
//     input   id of an existing checkbox in the panel that already does this job; the two stay in step
// Canvas code asks layer('lines') before drawing that part. HTML parts carry data-layer="id".
// A "What to notice" box (.notice) gets a layer of its own automatically.
// Start view (page opts or URL): show=[ids] (only these), hide=[ids], preset='simple'|'all'|'default', mode='<data-v>'.
// Each viewer's own choices are kept in localStorage per applet and mode; page or URL settings win over them.
(() => {
  const OPTS = () => {
    const o = Object.assign({}, window.SIM_OPTS || {});
    try { // a stand-alone page (harness, plain http server) can take the same settings from its own URL
      const q = new URLSearchParams(location.search);
      for (const k of ['show', 'hide', 'preset', 'mode']) if (q.get(k) && o[k] === undefined) o[k] = q.get(k);
    } catch (e) {}
    return o;
  };
  const list = v => v == null ? [] : (Array.isArray(v) ? v : String(v).split(',')).map(s => String(s).trim()).filter(Boolean);
  const simName = () => OPTS()._sim || (location.pathname.split('/').pop() || '').replace(/\.html$/, '') || document.title;
  let defs = null, focusUsed = {};
  const state = {};
  function getDefs() {
    if (defs) return defs;
    const raw = (window.SIM_LAYERS || []).slice();
    if (!raw.some(l => l.id === 'notice') && document.querySelector('.notice')) { raw.push({ id: 'notice', label: '“What to notice” box' }); document.querySelectorAll('.notice:not([data-layer])').forEach(n => { n.dataset.layer = 'notice'; }); }
    defs = raw.map(l => Object.assign({ on: true }, l));
    return defs;
  }
  function curMode() {
    if (typeof window.SIM_MODE === 'function') { try { return String(window.SIM_MODE()); } catch (e) {} }
    const b = document.querySelector('#modeSeg [aria-pressed="true"]');
    return b ? b.dataset.v : 'all';
  }
  const inMode = (l, m) => !l.modes || l.modes.includes(m);
  const isSimple = (l, m) => l.simple === true || (Array.isArray(l.simple) && l.simple.includes(m));
  const modeDefs = m => getDefs().filter(l => inMode(l, m));
  const key = m => 'simlayers:v1:' + simName() + ':' + m;
  function load(m) { try { const s = localStorage.getItem(key(m)); return s ? JSON.parse(s) : null; } catch (e) { return null; } }
  function save(m) { if (OPTS().save === false) return; try { localStorage.setItem(key(m), JSON.stringify(state[m])); } catch (e) {} }
  function presetState(p, m) { const st = {}; modeDefs(m).forEach(l => { st[l.id] = p === 'simple' ? isSimple(l, m) : p === 'all' ? true : l.on !== false; }); return st; }
  function resolve(m) {
    const ls = modeDefs(m), o = OPTS();
    let st = presetState('default', m);
    const show = list(o.show).filter(id => ls.some(l => l.id === id)), hide = list(o.hide);
    if (o.preset || show.length || hide.length) {
      if (o.preset === 'simple' || o.preset === 'all') st = presetState(o.preset, m);
      if (show.length) ls.forEach(l => { st[l.id] = show.includes(l.id); });
      hide.forEach(id => { if (id in st) st[id] = false; });
    } else {
      const saved = load(m);
      if (saved) for (const k in saved) if (k in st) st[k] = !!saved[k];
    }
    return st;
  }
  function modeState(m) { if (!state[m]) state[m] = resolve(m); const st = state[m]; modeDefs(m).forEach(l => { if (!(l.id in st)) st[l.id] = l.on !== false; }); return st; }
  // layer(id): should this part be drawn now? Parts that are not in the current mode's list are never hidden.
  function layer(id) { const m = curMode(), st = modeState(m); return id in st ? st[id] : true; }

  let applying = false;
  function apply() {
    const m = curMode(), st = modeState(m);
    document.querySelectorAll('[data-layer]').forEach(el => { const id = el.dataset.layer; el.classList.toggle('layer-off', id in st && !st[id]); });
    applying = true;
    modeDefs(m).forEach(l => { if (!l.input) return; const el = document.getElementById(l.input); if (el && el.checked !== st[l.id]) { el.checked = st[l.id]; el.dispatchEvent(new Event('input', { bubbles: true })); el.dispatchEvent(new Event('change', { bubbles: true })); } });
    applying = false;
    if (ui) ui.refresh();
    window.dispatchEvent(new CustomEvent('simlayers', { detail: { mode: m } }));
  }
  function set(id, on, user) { const m = curMode(); modeState(m)[id] = !!on; if (user) save(m); apply(); }
  function preset(p, user) { const m = curMode(); state[m] = presetState(p, m); if (user) save(m); apply(); }
  window.layer = layer;
  window.SIM = Object.assign(window.SIM || {}, { layer, setLayer: set, preset, layers: () => modeDefs(curMode()), mode: curMode, applyLayers: apply });

  let ui = null;
  function initLayers(stage, bar) {
    defs = null; for (const k in state) delete state[k]; getDefs();
    const o = OPTS();
    if (o.mode) { const b = document.querySelector('#modeSeg [data-v="' + String(o.mode).replace(/"/g, '') + '"]'); if (b && b.getAttribute('aria-pressed') !== 'true') b.click(); }
    // a panel checkbox bound to a layer: ticking it by hand is a viewer choice
    getDefs().forEach(l => { if (!l.input) return; const el = document.getElementById(l.input); if (el) el.addEventListener('change', () => { if (applying) return; const m = curMode(); if (inMode(l, m)) { modeState(m)[l.id] = el.checked; save(m); apply(); } }); });
    const btn = document.createElement('button');
    btn.className = 'lyrbtn'; btn.type = 'button'; btn.setAttribute('aria-expanded', 'false'); btn.setAttribute('aria-haspopup', 'dialog');
    btn.title = 'Choose which parts of the applet to show';
    bar.insertBefore(btn, bar.firstChild);
    const pop = document.createElement('div');
    pop.className = 'lyrpop'; pop.setAttribute('role', 'dialog'); pop.setAttribute('aria-label', 'Show or hide parts of the applet'); pop.hidden = true;
    pop.innerHTML = '<div class="lyrhead"><b>Show / hide</b><button type="button" class="lyrx" aria-label="Close">×</button></div>' +
      '<div class="lyrpre"><button type="button" data-p="simple" title="Only the one or two key parts">Simple</button><button type="button" data-p="all" title="Every part on">Everything</button></div><div class="lyrlist"></div>';
    document.body.appendChild(pop);
    const lst = pop.querySelector('.lyrlist');
    function place() { // under the button, or above it when there is more room there
      const r = btn.getBoundingClientRect(), W = window.innerWidth, H = window.innerHeight;
      const below = H - r.bottom - 14, above = r.top - 14;
      if (below < 260 && above > below) { pop.style.top = 'auto'; pop.style.bottom = (H - r.top + 6) + 'px'; pop.style.maxHeight = Math.max(160, above) + 'px'; }
      else { pop.style.bottom = 'auto'; pop.style.top = (r.bottom + 6) + 'px'; pop.style.maxHeight = Math.max(160, below) + 'px'; }
      if (W < 480) { pop.style.left = '8px'; pop.style.right = '8px'; }
      else { pop.style.left = 'auto'; pop.style.right = Math.max(8, W - r.right) + 'px'; }
    }
    function open(v) { pop.hidden = !v; btn.setAttribute('aria-expanded', v); if (v) { ui.refresh(); place(); } }
    ui = {
      refresh() {
        const m = curMode(), ls = modeDefs(m), st = modeState(m);
        btn.hidden = !ls.length;
        const off = ls.filter(l => !st[l.id] && l.on !== false).length; // parts hidden that are normally shown
        btn.textContent = off ? 'Show / hide · ' + off + ' off' : 'Show / hide';
        btn.classList.toggle('some-off', off > 0);
        const same = p => { const ps = presetState(p, m); return ls.every(l => ps[l.id] === st[l.id]); };
        pop.querySelectorAll('[data-p]').forEach(b => b.setAttribute('aria-pressed', same(b.dataset.p)));
        if (pop.hidden) return;
        const sig = m + '|' + ls.map(l => l.id).join(',');
        if (lst.dataset.sig !== sig) {
          lst.dataset.sig = sig;
          lst.innerHTML = '';
          ls.forEach(l => { const row = document.createElement('label'); row.className = 'lyrrow'; const cb = document.createElement('input'); cb.type = 'checkbox'; cb.dataset.id = l.id; const sp = document.createElement('span'); sp.textContent = l.label || l.id; row.append(cb, sp); lst.appendChild(row); });
        }
        lst.querySelectorAll('input').forEach(cb => { cb.checked = !!st[cb.dataset.id]; });
      }
    };
    btn.addEventListener('click', e => { e.stopPropagation(); open(pop.hidden); });
    pop.addEventListener('click', e => { const p = e.target.closest('[data-p]'); if (p) preset(p.dataset.p, true); if (e.target.closest('.lyrx')) open(false); });
    lst.addEventListener('change', e => { const cb = e.target.closest('input[data-id]'); if (cb) set(cb.dataset.id, cb.checked, true); });
    document.addEventListener('pointerdown', e => { if (!pop.hidden && !pop.contains(e.target) && e.target !== btn) open(false); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && !pop.hidden) { open(false); btn.focus(); } });
    window.addEventListener('resize', () => { if (!pop.hidden) place(); });
    stage.addEventListener('scroll', () => { if (!pop.hidden) place(); });
    // switching the applet's own mode shows that mode's parts
    const seg = document.getElementById('modeSeg');
    if (seg) seg.addEventListener('click', () => setTimeout(apply, 0));
    window.addEventListener('simmode', () => setTimeout(apply, 0));
    apply();
  }

  function initUX() {
    const stage = document.querySelector('.stage'), cv = stage && stage.querySelector('canvas');
    if (!stage || !cv) return;
    stage.style.position = 'relative'; stage.style.overflow = 'auto';
    let zoom = 1, wheelZoom = false;
    const bar = document.createElement('div'); bar.className = 'zoombar';
    bar.innerHTML = '<button data-z="-" title="Zoom out (Ctrl + scroll down)">−</button><button data-z="0" title="Fit to width">100%</button><button data-z="+" title="Zoom in (Ctrl + scroll up)">+</button><button data-z="w" title="Zoom with the scroll wheel instead of scrolling the page" aria-pressed="false">scroll = zoom</button>';
    stage.appendChild(bar);
    const pct = bar.querySelector('[data-z="0"]');
    function setZoom(z, ax, ay) {
      z = Math.max(0.5, Math.min(4, z));
      const r = cv.getBoundingClientRect();
      const fx = ax === undefined ? 0.5 : (ax - r.left) / r.width, fy = ay === undefined ? 0.5 : (ay - r.top) / r.height;
      const oldW = r.width, oldH = r.height;
      zoom = z; cv.style.width = (100 * z) + '%';
      const nr = cv.getBoundingClientRect();
      stage.scrollLeft += fx * (nr.width - oldW); stage.scrollTop += fy * (nr.height - oldH);
      pct.textContent = Math.round(z * 100) + '%';
      bar.classList.toggle('zoomed', z !== 1);
    }
    bar.addEventListener('click', e => { const b = e.target.closest('button[data-z]'); if (!b) return; const k = b.dataset.z;
      if (k === '-') setZoom(zoom / 1.25); else if (k === '+') setZoom(zoom * 1.25); else if (k === '0') setZoom(1);
      else { wheelZoom = !wheelZoom; b.setAttribute('aria-pressed', wheelZoom); } });
    cv.addEventListener('wheel', e => { if (e.ctrlKey || e.metaKey || wheelZoom) { e.preventDefault(); setZoom(zoom * (e.deltaY < 0 ? 1.12 : 1 / 1.12), e.clientX, e.clientY); } }, { passive: false });
    // pinch on touch screens
    let pinch = null;
    cv.addEventListener('touchstart', e => { if (e.touches.length === 2) pinch = { d: Math.hypot(e.touches[0].clientX - e.touches[1].clientX, e.touches[0].clientY - e.touches[1].clientY), z: zoom }; }, { passive: true });
    cv.addEventListener('touchmove', e => { if (pinch && e.touches.length === 2) { e.preventDefault(); const d = Math.hypot(e.touches[0].clientX - e.touches[1].clientX, e.touches[0].clientY - e.touches[1].clientY); setZoom(pinch.z * d / pinch.d, (e.touches[0].clientX + e.touches[1].clientX) / 2, (e.touches[0].clientY + e.touches[1].clientY) / 2); } }, { passive: false });
    cv.addEventListener('touchend', () => { pinch = null; });
    // hotkeys
    document.addEventListener('keydown', e => { const tag = (e.target.tagName || '').toLowerCase(); if (['input', 'select', 'textarea', 'button'].includes(tag)) return;
      if (e.code === 'Space') { const b = document.getElementById('play'); if (b) { e.preventDefault(); b.click(); } }
      if (e.key === 'r' || e.key === 'R') { const b = document.getElementById('reset'); if (b) b.click(); } });
    // make every panel control explain itself on hover
    document.querySelectorAll('.panel .ctl').forEach(c => { const l = c.querySelector('label, .lbl'); if (l && !c.title) c.title = l.textContent.trim(); });
    initLayers(stage, bar);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initUX); else initUX();
})();
