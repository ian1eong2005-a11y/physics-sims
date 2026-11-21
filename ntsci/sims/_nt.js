/* Kit for the G1 / N(T) Science applets. One config object per applet: NT.sim({...}) or NT.match({...}).
   Everything is big, tap-friendly and uses few words. No dependencies. */
window.NT = (() => {
  const C = { ink: '#16222e', mute: '#5d6d7c', line: '#cfd8e0', soft: '#eef3f7', white: '#ffffff', sky: '#e3f2ff',
    red: '#e4572e', blue: '#2a7de1', green: '#2e9e5b', yellow: '#f4b400', orange: '#f08a24', purple: '#7b5ea7',
    brown: '#8a5a2b', pink: '#e86a92', grey: '#9aa7b3', dark: '#3a4652' };
  const FONT = '"Segoe UI", system-ui, -apple-system, Roboto, Arial, sans-serif';
  const EMO = '"Segoe UI Emoji", "Apple Color Emoji", "Noto Color Emoji", sans-serif';
  const el = (tag, cls, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (html !== undefined) e.innerHTML = html; return e; };
  const esc = v => String(v).replace(/[&<>"]/g, m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[m]));
  const hash = str => { let h = 7; for (const ch of String(str)) h = (h * 31 + ch.charCodeAt(0)) % 9973; return h; };
  const mix = arr => arr.map((v, i) => [hash(JSON.stringify(v) + i), v]).sort((a, b) => a[0] - b[0]).map(x => x[1]);   // fixed "shuffle"
  const shuffle = arr => { const a = arr.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const postHeight = () => { try { window.parent.postMessage({ isStreamlitMessage: true, type: 'streamlit:setFrameHeight', height: Math.ceil(document.documentElement.scrollHeight) + 4 }, '*'); } catch (e) { /* not embedded */ } };

  // ---------- drawing helper ----------
  function pen(cv) {
    const x = cv.getContext('2d');
    const paint = o => { if (o.alpha !== undefined) x.globalAlpha = o.alpha; if (o.fill) { x.fillStyle = o.fill; x.fill(); }
      if (o.stroke) { x.strokeStyle = o.stroke; x.lineWidth = o.lw || 3; x.setLineDash(o.dash || []); x.lineJoin = 'round'; x.stroke(); x.setLineDash([]); } x.globalAlpha = 1; };
    const P = {
      ctx: x, W: cv.width, H: cv.height, C,
      clear(bg) { x.setTransform(1, 0, 0, 1, 0, 0); x.globalAlpha = 1; x.clearRect(0, 0, cv.width, cv.height); if (bg) { x.fillStyle = bg; x.fillRect(0, 0, cv.width, cv.height); } },
      text(str, px, py, o = {}) { x.font = (o.bold === false ? '' : '700 ') + (o.size || 22) + 'px ' + FONT; x.fillStyle = o.color || C.ink; x.textAlign = o.align || 'center'; x.textBaseline = o.base || 'middle'; if (o.alpha !== undefined) x.globalAlpha = o.alpha; x.fillText(str, px, py); x.globalAlpha = 1; },
      emoji(ch, px, py, size = 48, o = {}) { x.save(); x.font = size + 'px ' + EMO; x.textAlign = 'center'; x.textBaseline = 'middle'; x.fillStyle = '#000'; if (o.alpha !== undefined) x.globalAlpha = o.alpha; x.translate(px, py); if (o.rot) x.rotate(o.rot); if (o.flip) x.scale(-1, 1); x.fillText(ch, 0, 0); x.restore(); },
      rect(px, py, w, h, o = {}) { x.beginPath(); if (o.r && x.roundRect) x.roundRect(px, py, w, h, o.r); else x.rect(px, py, w, h); paint(o); },
      circle(px, py, r, o = {}) { x.beginPath(); x.arc(px, py, Math.max(0, r), 0, 6.2832); paint(o); },
      oval(px, py, rx, ry, o = {}) { x.beginPath(); x.ellipse(px, py, Math.max(0, rx), Math.max(0, ry), o.rot || 0, 0, 6.2832); paint(o); },
      poly(pts, o = {}) { x.beginPath(); pts.forEach((q, i) => (i ? x.lineTo(q[0], q[1]) : x.moveTo(q[0], q[1]))); if (o.close !== false) x.closePath(); paint(o); },
      curve(pts, o = {}) { x.beginPath(); pts.forEach((q, i) => (i ? x.lineTo(q[0], q[1]) : x.moveTo(q[0], q[1]))); x.lineCap = 'round'; paint({ stroke: o.color || C.ink, lw: o.lw || 4, dash: o.dash, alpha: o.alpha }); },
      line(x1, y1, x2, y2, o = {}) { x.beginPath(); x.moveTo(x1, y1); x.lineTo(x2, y2); x.lineCap = 'round'; paint({ stroke: o.color || C.ink, lw: o.lw || 3, dash: o.dash, alpha: o.alpha }); },
      arrow(x1, y1, x2, y2, o = {}) { const col = o.color || C.ink, lw = o.lw || 5, a = Math.atan2(y2 - y1, x2 - x1), hd = o.head || lw * 3.2;
        P.line(x1, y1, x2 - Math.cos(a) * hd * 0.7, y2 - Math.sin(a) * hd * 0.7, { color: col, lw });
        P.poly([[x2, y2], [x2 - hd * Math.cos(a - 0.45), y2 - hd * Math.sin(a - 0.45)], [x2 - hd * Math.cos(a + 0.45), y2 - hd * Math.sin(a + 0.45)]], { fill: col }); },
      // label on a coloured pill
      tag(str, px, py, o = {}) { const size = o.size || 20; x.font = '700 ' + size + 'px ' + FONT; const w = x.measureText(str).width + size * 1.1, h = size * 1.7;
        P.rect(px - w / 2, py - h / 2, w, h, { fill: o.bg || C.ink, r: h / 2, stroke: o.stroke, lw: 2 }); P.text(str, px, py + 1, { size, color: o.color || '#fff' }); return w; },
      // vertical bar that fills from the bottom: frac 0..1
      bar(px, py, w, h, frac, o = {}) { const f = Math.max(0, Math.min(1, frac)); P.rect(px, py, w, h, { fill: C.soft, r: 6 }); if (f > 0) P.rect(px, py + h * (1 - f), w, h * f, { fill: o.color || C.blue, r: 6 });
        P.rect(px, py, w, h, { stroke: C.dark, lw: 2, r: 6 }); if (o.label) P.text(o.label, px + w / 2, py + h + 18, { size: o.size || 18 }); if (o.value !== undefined) P.text(o.value, px + w / 2, py - 16, { size: o.size || 18, color: o.color || C.blue }); },
      // a digital meter box
      meter(px, py, value, o = {}) { const w = o.w || 150, h = o.h || 70; P.rect(px - w / 2, py - h / 2, w, h, { fill: o.bg || '#fff8d6', stroke: C.dark, lw: 4, r: 12 });
        P.text(value, px, py + (o.label ? 8 : 0), { size: o.size || 28, color: C.ink }); if (o.label) P.text(o.label, px, py - h / 2 + 14, { size: 14, color: C.mute }); },
      // glass container with liquid: level 0..1
      beaker(px, py, w, h, o = {}) { const lv = Math.max(0, Math.min(1, o.level === undefined ? 0.6 : o.level)); if (lv > 0) P.rect(px + 3, py + h * (1 - lv), w - 6, h * lv - 3, { fill: o.color || '#bfe3ff', r: 4, alpha: o.alpha });
        P.poly([[px, py], [px, py + h], [px + w, py + h], [px + w, py]], { stroke: C.dark, lw: 4, close: false }); if (o.label) P.text(o.label, px + w / 2, py + h + 20, { size: o.size || 18 }); },
      // test tube
      tube(px, py, w, h, o = {}) { const lv = Math.max(0, Math.min(1, o.level === undefined ? 0.5 : o.level)), r = w / 2, top = py + (h - r) * (1 - lv);
        x.save(); x.beginPath(); x.moveTo(px, py); x.lineTo(px, py + h - r); x.arc(px + r, py + h - r, r, Math.PI, 0, true); x.lineTo(px + w, py); x.closePath(); x.clip();
        if (lv > 0) { x.fillStyle = o.color || '#bfe3ff'; x.fillRect(px, top, w, py + h - top); } if (o.inside) o.inside(top); x.restore();
        x.beginPath(); x.moveTo(px, py); x.lineTo(px, py + h - r); x.arc(px + r, py + h - r, r, Math.PI, 0, true); x.lineTo(px + w, py); paint({ stroke: C.dark, lw: 4 });
        if (o.label) P.text(o.label, px + r, py + h + 20, { size: o.size || 18 }); },
      // lamp: bright 0..1
      lamp(px, py, r, bright) { const b = Math.max(0, Math.min(1, bright)); if (b > 0.02) { const g = x.createRadialGradient(px, py, r * 0.3, px, py, r * (1.3 + 1.5 * b)); g.addColorStop(0, 'rgba(255,214,60,' + (0.35 + 0.6 * b) + ')'); g.addColorStop(1, 'rgba(255,214,60,0)'); x.fillStyle = g; x.beginPath(); x.arc(px, py, r * 3, 0, 6.2832); x.fill(); }
        P.circle(px, py, r, { fill: b > 0.02 ? 'rgb(255,' + Math.round(244 - 30 * (1 - b)) + ',' + Math.round(170 - 110 * b) + ')' : '#f2f4f6', stroke: C.dark, lw: 4 });
        P.line(px - r * 0.6, py - r * 0.6, px + r * 0.6, py + r * 0.6, { color: C.dark, lw: 3 }); P.line(px - r * 0.6, py + r * 0.6, px + r * 0.6, py - r * 0.6, { color: C.dark, lw: 3 }); },
      // simple graph frame: returns functions to map values to pixels
      graph(gx, gy, gw, gh, o = {}) { const xm = o.xmax || 10, ym = o.ymax || 10, X = v => gx + (v / xm) * gw, Y = v => gy + gh - (v / ym) * gh;
        P.rect(gx, gy, gw, gh, { fill: '#fff' }); const nx = o.nx || 5, ny = o.ny || 5;
        for (let i = 0; i <= nx; i++) { P.line(gx + (gw * i) / nx, gy, gx + (gw * i) / nx, gy + gh, { color: C.line, lw: 1 }); P.text(String(Math.round((xm * i) / nx * 10) / 10), gx + (gw * i) / nx, gy + gh + 16, { size: 15, color: C.mute, bold: false }); }
        for (let i = 0; i <= ny; i++) { P.line(gx, gy + (gh * i) / ny, gx + gw, gy + (gh * i) / ny, { color: C.line, lw: 1 }); P.text(String(Math.round((ym * (ny - i)) / ny * 10) / 10), gx - 8, gy + (gh * i) / ny, { size: 15, color: C.mute, align: 'right', bold: false }); }
        P.line(gx, gy, gx, gy + gh, { color: C.ink, lw: 3 }); P.line(gx, gy + gh, gx + gw, gy + gh, { color: C.ink, lw: 3 });
        if (o.xl) P.text(o.xl, gx + gw / 2, gy + gh + 40, { size: 17 }); if (o.yl) { x.save(); x.translate(gx - 46, gy + gh / 2); x.rotate(-Math.PI / 2); P.text(o.yl, 0, 0, { size: 17 }); x.restore(); }
        return { X, Y }; },
      // moving dots along a path (charge in a wire, blood in a vessel): off = distance moved so far, gap = space between dots
      flow(pts, off, gap, o = {}) { let acc = 0, d = ((off % gap) + gap) % gap; for (let i = 1; i < pts.length; i++) { const x1 = pts[i - 1][0], y1 = pts[i - 1][1], x2 = pts[i][0], y2 = pts[i][1], len = Math.hypot(x2 - x1, y2 - y1); if (!len) continue;
        while (d <= acc + len) { const f = (d - acc) / len; P.circle(x1 + (x2 - x1) * f, y1 + (y2 - y1) * f, o.r || 5, { fill: o.color || C.yellow, stroke: o.stroke === undefined ? C.dark : o.stroke, lw: 1 }); d += gap; } acc += len; } },
      // a simple plant: h = height in px, droop 0..1 (wilting), leaf = leaf size factor, pot false for crops in a field
      plant(px, base, h, o = {}) { const col = o.color || '#3aa655', edge = o.edge || '#2f7d3f', n = Math.max(1, Math.round(h / 36)), droop = o.droop || 0, tipx = px + droop * h * 0.55, tipy = base - h * (1 - droop * 0.5);
        if (o.pot !== false) { P.poly([[px - 34, base], [px + 34, base], [px + 26, base + 46], [px - 26, base + 46]], { fill: '#c9773f', stroke: C.dark, lw: 3 }); P.rect(px - 38, base - 8, 76, 14, { fill: '#b5652f', stroke: C.dark, lw: 3, r: 4 }); }
        if (h < 4) return;
        x.beginPath(); x.moveTo(px, base - 6); x.quadraticCurveTo(px, base - h * 0.6, tipx, tipy); x.lineCap = 'round'; paint({ stroke: edge, lw: Math.max(4, h / 30) });
        for (let i = 1; i <= n; i++) { const f = i / (n + 0.5), qx = px + (tipx - px) * f * f, qy = base - 6 + (tipy - base + 6) * f, len = Math.min(38, 12 + h * 0.12) * (o.leaf || 1), side = i % 2 ? 1 : -1;
          P.oval(qx + side * len * 0.85, qy - 4 + droop * 14, len, len * 0.42, { fill: col, stroke: edge, lw: 2, rot: side * (-0.45 + droop * 1.0) }); }
        P.oval(tipx, tipy - 4, 11, 7, { fill: col, stroke: edge, lw: 2 }); },
      // little bubbles rising inside a box (for fizzing, boiling)
      bubbles(px, py, w, h, n, t, o = {}) { for (let i = 0; i < n; i++) { const u = ((t * (0.25 + (i % 5) * 0.07) + i * 0.37) % 1), bx = px + ((i * 53) % 100) / 100 * w, by = py + h - u * h; P.circle(bx, by, (o.r || 4) + (i % 3), { stroke: o.color || '#fff', lw: 2, alpha: 0.9 * (1 - u * 0.5) }); } },
    };
    return P;
  }

  function frameShell(cfg) {
    const root = document.getElementById('nt') || document.body.appendChild(el('div'));
    root.className = 'nt'; root.innerHTML = '';
    root.appendChild(el('div', 'nt-head', '<span class="nt-emo">' + (cfg.emoji || '🔬') + '</span><h1>' + esc(cfg.title || '') + '</h1>'));
    if (window.ResizeObserver) new ResizeObserver(postHeight).observe(document.body);
    return root;
  }

  // =====================================================================  NT.sim
  function sim(cfg) {
    const OPTS = window.SIM_OPTS || {};
    const root = frameShell(cfg);
    const inqList = cfg.inquiry || [];
    const inqOn = !!OPTS.inq && inqList.length > 0;
    const controls = cfg.controls || [], readings = cfg.readings || [];
    const s = {};
    controls.forEach(c => { s[c.id] = c.value !== undefined ? c.value : (c.options ? c.options[0][0] : c.min); });
    if (cfg.init) cfg.init(s);
    let t = 0, p = cfg.go ? 0 : 1, running = false, done = !cfg.go, last = performance.now(), sel = null, test = null;
    const goLabel = (cfg.go && cfg.go.label) || 'Go';
    const dur = () => (cfg.go ? (typeof cfg.go.time === 'function' ? cfg.go.time(s) : cfg.go.time || 4) : 1);

    const main = el('div', 'nt-main' + (inqOn ? ' inq' : '')); root.appendChild(main);
    const stage = el('div', 'nt-stage'); main.appendChild(stage);
    const cv = el('canvas'); cv.width = cfg.w || 900; cv.height = cfg.h || 480; stage.appendChild(cv);
    const P = pen(cv);
    const sayBox = el('div', 'nt-say'); stage.appendChild(sayBox);
    const infoBox = el('div', 'nt-info'); stage.appendChild(infoBox);
    const ctlBox = el('div', 'nt-ctl'); stage.appendChild(ctlBox);
    const actBox = el('div', 'nt-act'); stage.appendChild(actBox);
    const readBox = el('div', 'nt-read'); stage.appendChild(readBox);
    if (cfg.idea && !inqOn) stage.appendChild(el('div', 'nt-idea', '💡 ' + esc(cfg.idea)));
    const panel = el('div', 'nt-inq'); if (inqOn) main.appendChild(panel);

    // ---------- inquiry state ----------
    let inq = null, step = 0, guess = null, sameSel = new Set(), sameOK = false, sameMsg = '', rows = {}, foundSel = [], foundOK = false, foundMsg = '', recMsg = '';
    const ctlOf = id => controls.find(c => c.id === id);
    const rdOf = id => readings.find(r => r.id === id);
    const optLabel = (c, v) => { const o = (c.options || []).find(q => q[0] === v); return o ? ((o[2] ? o[2] + ' ' : '') + o[1]) : String(v); };
    const testsOf = () => inq.tests || ctlOf(inq.change).options.map(o => o[0]);
    const locked = id => !!(inq && inq.fix && id in inq.fix);

    // ---------- controls ----------
    function reset() { p = cfg.go ? 0 : 1; running = false; done = !cfg.go; recMsg = ''; if (cfg.reset) cfg.reset(s); refresh(); }
    function setVal(id, v) { if (locked(id)) return; s[id] = v; reset(); if (inqOn) renderInq(); }
    function buildControls() {
      ctlBox.innerHTML = '';
      controls.forEach(c => {
        const row = el('div', 'nt-row'); row.dataset.id = c.id;
        row.appendChild(el('span', 'nt-lbl', esc(c.label)));
        if (c.type === 'range') {
          const wrap = el('div', 'nt-range');
          const minus = el('button', 'nt-step', '−'), plus = el('button', 'nt-step', '+'), inp = el('input'), val = el('span', 'nt-val');
          inp.type = 'range'; inp.min = c.min; inp.max = c.max; inp.step = c.step || 1; inp.value = s[c.id];
          const upd = v => { v = Math.max(c.min, Math.min(c.max, Math.round(v / (c.step || 1)) * (c.step || 1))); v = Math.round(v * 1000) / 1000; inp.value = v; setVal(c.id, v); };
          inp.addEventListener('input', () => upd(+inp.value)); minus.addEventListener('click', () => upd(s[c.id] - (c.step || 1))); plus.addEventListener('click', () => upd(s[c.id] + (c.step || 1)));
          wrap.append(minus, inp, plus, val); row.appendChild(wrap);
        } else {
          const seg = el('div', 'nt-seg');
          c.options.forEach(o => { const b = el('button', '', (o[2] ? '<span class="nt-be">' + o[2] + '</span>' : '') + '<span>' + esc(o[1]) + '</span>'); b.dataset.v = JSON.stringify(o[0]); b.addEventListener('click', () => setVal(c.id, o[0])); seg.appendChild(b); });
          row.appendChild(seg);
        }
        ctlBox.appendChild(row);
      });
      actBox.innerHTML = '';
      if (cfg.go) { const b = el('button', 'nt-go'); b.id = 'ntGo'; b.addEventListener('click', () => { if (running) return; if (cfg.reset) cfg.reset(s); p = 0; done = false; running = true; recMsg = ''; refresh(); if (inqOn) renderInq(); }); actBox.appendChild(b); }
      if (cfg.spots && cfg.testMe !== false) { const b = el('button', 'nt-test'); b.id = 'ntTest'; b.addEventListener('click', () => { test ? endTest() : startTest(); }); actBox.appendChild(b); }
      (cfg.buttons || []).forEach(bt => { const b = el('button', 'nt-btn', esc(bt.label)); b.addEventListener('click', () => { bt.click(s, api); refresh(); }); actBox.appendChild(b); });
    }
    function refresh() {
      controls.forEach(c => {
        const row = ctlBox.querySelector('[data-id="' + c.id + '"]'); if (!row) return;
        row.style.display = c.show && !c.show(s) ? 'none' : '';
        row.classList.toggle('locked', locked(c.id));
        if (c.type === 'range') { row.querySelector('input').value = s[c.id]; row.querySelector('.nt-val').textContent = (c.fmt ? c.fmt(s[c.id]) : s[c.id]) + (c.unit ? ' ' + c.unit : ''); }
        else row.querySelectorAll('button').forEach(b => b.setAttribute('aria-pressed', b.dataset.v === JSON.stringify(s[c.id])));
      });
      const go = document.getElementById('ntGo'); if (go) { go.textContent = running ? '⏳ …' : done ? '↺ Again' : '▶ ' + goLabel; go.disabled = running; }
      const tb = document.getElementById('ntTest'); if (tb) tb.textContent = test ? '✖ Stop the test' : '🎯 Test me';
      readBox.innerHTML = readings.filter(r => !r.hide).map(r => '<div class="nt-rd' + (done || r.always ? ' on' : '') + '"><small>' + esc(r.label) + '</small><b>' + (done || r.always ? esc(fmt(r).txt) : '?') + '</b></div>').join('');
      readBox.style.display = readings.some(r => !r.hide) ? '' : 'none';
      const sayTxt = cfg.say ? cfg.say(s, done, p) : ''; sayBox.innerHTML = sayTxt ? '👀 ' + sayTxt : ''; sayBox.style.display = sayTxt ? '' : 'none';
      renderInfo();
    }
    function fmt(r) { const v = r.get(s, p, t), u = typeof r.unit === 'function' ? r.unit(s) : r.unit;
      if (r.text) return { txt: r.text(s, p, t), num: typeof v === 'number' ? v : null };
      if (typeof v === 'number') { const n = r.dp !== undefined ? v.toFixed(r.dp) : String(Math.round(v * 100) / 100); return { txt: n + (u ? ' ' + u : ''), num: v }; } return { txt: String(v), num: null }; }

    // ---------- tap-to-learn spots ----------
    const spots = () => (typeof cfg.spots === 'function' ? cfg.spots(s) : cfg.spots || []);
    function renderInfo() {
      if (!cfg.spots) { infoBox.style.display = 'none'; return; }
      infoBox.style.display = '';
      if (test) { const sp = test.order[test.i]; infoBox.className = 'nt-info test'; infoBox.innerHTML = '<div class="nt-ask">🎯 Tap: <b>' + esc(sp.name) + '</b></div>' + (test.msg ? '<div>' + test.msg + '</div>' : '') + '<small>' + (test.i + 1) + ' of ' + test.order.length + '</small>'; return; }
      infoBox.className = 'nt-info';
      const chips = '<div class="nt-chips">' + spots().map((sp, i) => '<button data-spot="' + i + '" aria-pressed="' + (sel === sp.id) + '">' + (i + 1) + ' ' + esc(sp.name) + '</button>').join('') + '</div>';
      const cur = spots().find(sp => sp.id === sel);
      infoBox.innerHTML = (cur ? '<div class="nt-card"><b>' + (cur.emoji ? cur.emoji + ' ' : '') + esc(cur.name) + '</b><span>' + cur.info + '</span></div>' : '<div class="nt-card hint">👆 Tap a number to find out what it does.</div>') + chips + (infoBox.dataset.result ? '<div class="nt-card ok">' + infoBox.dataset.result + '</div>' : '');
    }
    infoBox.addEventListener('click', e => { const b = e.target.closest('[data-spot]'); if (!b) return; pick(spots()[+b.dataset.spot]); });
    function pick(sp) {
      if (!sp) return;
      if (test) { const want = test.order[test.i];
        if (sp.id === want.id) { if (!test.missed) test.right++; test.i++; test.missed = false; test.msg = '✅ Yes!'; if (test.i >= test.order.length) { infoBox.dataset.result = '⭐ You got ' + test.right + ' of ' + test.order.length + ' right first time.'; endTest(); return; } }
        else { test.missed = true; test.msg = '❌ That is the ' + esc(sp.name) + '. Try again.'; }
        renderInfo(); return; }
      sel = sp.id; s._spot = sp.id; infoBox.dataset.result = ''; if (cfg.onSpot) cfg.onSpot(sp, s); refresh();
    }
    function startTest() { test = { order: shuffle(spots()), i: 0, right: 0, missed: false, msg: '' }; sel = null; s._spot = null; s._test = true; infoBox.dataset.result = ''; refresh(); }
    function endTest() { test = null; s._test = false; refresh(); }
    function drawSpots() {
      if (!cfg.spots) return;
      spots().forEach((sp, i) => { const on = sel === sp.id && !test, r = 17;
        if (on) P.circle(sp.x, sp.y, r + 7 + 2 * Math.sin(t * 5), { stroke: C.orange, lw: 4 });
        P.circle(sp.x, sp.y, r, { fill: on ? C.orange : C.ink, stroke: '#fff', lw: 3 }); P.text(test ? '?' : String(i + 1), sp.x, sp.y + 1, { size: 18, color: '#fff' }); });
    }
    cv.addEventListener('click', e => {
      const r = cv.getBoundingClientRect(), k = cv.width / r.width, px = (e.clientX - r.left) * k, py = (e.clientY - r.top) * k;
      if (cfg.spots) { let best = null, bd = 1e9; spots().forEach(sp => { const d = Math.hypot(px - sp.x, py - sp.y); if (d < (sp.r || 46) && d < bd) { bd = d; best = sp; } }); if (best) { pick(best); return; } }
      if (cfg.click) { cfg.click(px, py, s, api); refresh(); if (inqOn) renderInq(); }
    });

    // ---------- inquiry panel ----------
    const STEPS = ['My guess', 'Fair test', 'Test', 'What I found'];
    function startInq(i) { inq = inqList[i]; step = 0; guess = null; sameSel = new Set(); sameOK = false; sameMsg = ''; rows = {}; foundSel = []; foundOK = false; foundMsg = ''; recMsg = '';
      Object.assign(s, inq.fix || {}); s[inq.change] = testsOf()[0]; reset(); renderInq(); }
    function sameItems() { const c = ctlOf(inq.change), m = rdOf([].concat(inq.measure)[0]); return mix([...inq.same.map(v => [v, true]), [c.noun || c.label.toLowerCase(), false], [inq.dv || m.noun || m.label.toLowerCase(), false]]); }
    function renderInq() {
      const c = ctlOf(inq.change), ms = [].concat(inq.measure).map(rdOf), tests = testsOf();
      let h = '';
      if (inqList.length > 1) h += '<div class="nt-pick">' + inqList.map((q, i) => '<button data-inq="' + i + '" aria-pressed="' + (q === inq) + '">' + esc(q.name || 'Investigation ' + (i + 1)) + '</button>').join('') + '</div>';
      h += '<div class="nt-q">❓ ' + esc(inq.q) + '</div>';
      h += '<div class="nt-steps">' + STEPS.map((n, i) => '<span class="' + (i === step ? 'on' : i < step ? 'ok' : '') + '">' + (i < step ? '✓' : i + 1) + '</span>').join('') + '</div>';
      h += '<h2>' + (step + 1) + ' · ' + STEPS[step] + '</h2>';
      let canNext = false;
      if (step === 0) {
        h += '<p>What do you think will happen? Tap one.</p><div class="nt-opts">' + inq.guess.map((g, i) => '<button data-guess="' + i + '" aria-pressed="' + (guess === i) + '">' + esc(g) + '</button>').join('') + '</div>';
        canNext = guess !== null;
      } else if (step === 1) {
        h += '<p>🔧 I change: <b>' + esc(c.noun || c.label.toLowerCase()) + '</b></p><p>📏 I measure: <b>' + esc(inq.dv || ms.map(m => m.noun || m.label.toLowerCase()).join(' and ')) + '</b></p><p>🔒 To be fair, what must stay <b>the same</b>? Tick them.</p><div class="nt-ticks">' +
          sameItems().map(it => '<label><input type="checkbox" data-same="' + esc(it[0]) + '"' + (sameSel.has(it[0]) ? ' checked' : '') + (sameOK ? ' disabled' : '') + '> ' + esc(it[0]) + '</label>').join('') + '</div>' +
          (sameOK ? '' : '<button class="nt-check" data-act="same">Check</button>') + (sameMsg ? '<div class="nt-msg ' + (sameOK ? 'ok' : 'bad') + '">' + sameMsg + '</div>' : '');
        canNext = sameOK;
      } else if (step === 2) {
        const filled = tests.filter(v => rows[JSON.stringify(v)]).length;
        h += '<p>For each row: choose it, ' + (cfg.go ? 'press <b>' + esc(goLabel) + '</b>, then ' : '') + 'press <b>Record</b>.</p>';
        h += '<table class="nt-tbl"><tr><th>' + esc(c.label) + '</th>' + ms.map(m => '<th>' + esc(m.label) + '</th>').join('') + '</tr>' +
          tests.map(v => { const k = JSON.stringify(v), row = rows[k], cur = JSON.stringify(s[inq.change]) === k; return '<tr class="' + (cur ? 'cur' : '') + '"><td>' + (cur ? '👉 ' : '') + esc(optLabel(c, v)) + '</td>' + ms.map((m, j) => '<td>' + (row ? esc(row[j].txt) : '') + '</td>').join('') + '</tr>'; }).join('') + '</table>';
        h += '<button class="nt-check" data-act="rec">📋 Record</button>' + (recMsg ? '<div class="nt-msg ' + (recMsg[0] === '✅' ? 'ok' : 'bad') + '">' + recMsg + '</div>' : '');
        if (filled === tests.length) {
          const nums = tests.map(v => rows[JSON.stringify(v)][0].num);
          if (nums.every(n => n !== null)) { const mx = Math.max(...nums, 1e-9); h += '<div class="nt-chart"><small>' + esc(ms[0].label) + '</small>' + tests.map((v, i) => '<div><span>' + esc(optLabel(c, v)) + '</span><i style="width:' + Math.max(2, (nums[i] / mx) * 62) + '%"></i><em>' + esc(rows[JSON.stringify(v)][0].txt) + '</em></div>').join('') + '</div>'; }
        }
        canNext = filled === tests.length;
      } else {
        let k = 0;
        h += '<p>Look at your results. Choose the right words.</p><div class="nt-found">' + inq.found.map(part => { if (typeof part === 'string') return esc(part); const i = k++; return '<select data-found="' + i + '"' + (foundOK ? ' disabled' : '') + '><option value="">choose…</option>' + part.map((o, j) => '<option value="' + j + '"' + (foundSel[i] === j ? ' selected' : '') + '>' + esc(o) + '</option>').join('') + '</select>'; }).join('') + '</div>';
        h += (foundOK ? '' : '<button class="nt-check" data-act="found">Check</button>') + (foundMsg ? '<div class="nt-msg ' + (foundOK ? 'ok' : 'bad') + '">' + foundMsg + '</div>' : '');
        if (foundOK) h += '<div class="nt-why">🧠 ' + esc(inq.why) + '</div>' + (inq.guessAns !== undefined ? '<div class="nt-msg ' + (guess === inq.guessAns ? 'ok' : '') + '">' + (guess === inq.guessAns ? '👍 Your guess was right.' : '🙂 Your guess was different. That is OK. Scientists change their ideas when they see the results.') + '</div>' : '') + '<div class="nt-star">⭐ Investigation done! Now try the Quiz.</div>';
      }
      h += '<div class="nt-nav"><button data-act="back"' + (step === 0 ? ' disabled' : '') + '>◀ Back</button>' + (step < 3 ? '<button class="nt-next" data-act="next"' + (canNext ? '' : ' disabled') + '>Next ▶</button>' : '<button data-act="redo">↺ Start again</button>') + '</div>';
      panel.innerHTML = h;
      refresh();
    }
    function record() {
      const tests = testsOf(), v = s[inq.change], k = JSON.stringify(v);
      if (!tests.some(q => JSON.stringify(q) === k)) { recMsg = 'Choose one of the rows in the table first.'; return; }
      if (!done) { recMsg = 'Press ' + goLabel + ' first, and wait until it finishes.'; return; }
      rows[k] = [].concat(inq.measure).map(id => fmt(rdOf(id)));
      const left = tests.filter(q => !rows[JSON.stringify(q)]);
      recMsg = left.length ? '✅ Recorded. Next: ' + optLabel(ctlOf(inq.change), left[0]) + '.' : '✅ All done. Look at the bars, then press Next.';
    }
    panel.addEventListener('click', e => {
      const b = e.target.closest('button'); if (!b) return;
      if (b.dataset.inq !== undefined) { startInq(+b.dataset.inq); return; }
      if (b.dataset.guess !== undefined) { guess = +b.dataset.guess; renderInq(); return; }
      const act = b.dataset.act;
      if (act === 'same') { const items = sameItems(), wrong = items.filter(it => !it[1] && sameSel.has(it[0])), missing = items.filter(it => it[1] && !sameSel.has(it[0]));
        if (!wrong.length && !missing.length) { sameOK = true; sameMsg = '✅ Yes. That is a fair test.'; }
        else sameMsg = wrong.length ? '❌ Not "' + esc(wrong[0][0]) + '". That is what you change or measure.' : '❌ Not yet. Tick everything else that could change the result.'; }
      else if (act === 'rec') record();
      else if (act === 'found') { const n = inq.found.filter(q => typeof q !== 'string').length; let ok = true; for (let i = 0; i < n; i++) if (foundSel[i] !== inq.foundAns[i]) ok = false;
        foundOK = ok; foundMsg = ok ? '✅ Correct!' : (foundSel.filter(v => v !== undefined).length < n ? '❌ Choose a word for every box.' : '❌ Not yet. Look at your table again.'); }
      else if (act === 'next') step = Math.min(3, step + 1);
      else if (act === 'back') step = Math.max(0, step - 1);
      else if (act === 'redo') { startInq(inqList.indexOf(inq)); return; }
      renderInq();
    });
    panel.addEventListener('change', e => {
      const q = e.target; if (q.dataset.same !== undefined) { q.checked ? sameSel.add(q.dataset.same) : sameSel.delete(q.dataset.same); sameMsg = ''; }
      if (q.dataset.found !== undefined) { foundSel[+q.dataset.found] = q.value === '' ? undefined : +q.value; foundMsg = ''; }
    });

    // ---------- loop ----------
    const api = { s, set: setVal, done: () => done, running: () => running, refresh, P };
    let liveT = 0, errd = false;
    function frame(now) {
      const dt = Math.min(0.05, Math.max(0, (now - last) / 1000)); last = now; t += dt;
      if (running) { p = Math.min(1, p + dt / dur()); if (p >= 1) { running = false; done = true; refresh(); if (inqOn) renderInq(); } }
      if (cfg.tick) cfg.tick(s, dt, api);
      P.clear(cfg.bg || '#ffffff');
      try { cfg.draw(P, s, p, t, api); drawSpots(); } catch (err) { if (!errd) { errd = true; (window.__errs = window.__errs || []).push('draw: ' + err.message); console.error(err); } }
      if (cfg.live) { liveT += dt; if (liveT > 0.25) { liveT = 0; refresh(); } }
      requestAnimationFrame(frame);
    }
    buildControls();
    if (inqOn) startInq(0); else refresh();
    requestAnimationFrame(frame);
    window.__nt = { s, api, state: () => ({ p, done, running, step, guess, rows, sameOK, foundOK, test }), cfg };
    return api;
  }

  // =====================================================================  NT.match: sort the cards into the right boxes
  function match(cfg) {
    const root = frameShell(cfg);
    const main = el('div', 'nt-match'); root.appendChild(main);
    let deck = [], i = 0, right = 0, missed = false, msg = '', placed = {}, wrongBin = null;
    function start() { deck = shuffle(cfg.cards).slice(0, cfg.count || cfg.cards.length); i = 0; right = 0; missed = false; msg = ''; placed = {}; wrongBin = null; cfg.bins.forEach(b => (placed[b.id] = [])); render(); }
    function render() {
      const card = deck[i];
      let h = '<div class="nt-intro">' + (cfg.intro || '') + '</div>';
      if (card) h += '<div class="nt-deck"><small>Card ' + (i + 1) + ' of ' + deck.length + '</small><div class="nt-cardbig"><span>' + (card.emoji || '') + '</span><b>' + esc(card.t) + '</b></div><div class="nt-ask">' + esc(cfg.ask || 'Where does it go? Tap a box.') + '</div>' + (msg ? '<div class="nt-msg ' + (msg[0] === '✅' ? 'ok' : 'bad') + '">' + msg + '</div>' : '') + '</div>';
      else h += '<div class="nt-deck"><div class="nt-star">⭐ Finished! ' + right + ' of ' + deck.length + ' right first time.</div><button class="nt-go" data-act="again">↺ Play again</button></div>';
      h += '<div class="nt-bins' + (cfg.bins.length > 4 ? ' many' : '') + '">' + cfg.bins.map(b => '<button class="nt-bin' + (wrongBin === b.id ? ' shake' : '') + '" data-bin="' + esc(b.id) + '"' + (card ? '' : ' disabled') + '><span class="nt-binemo">' + (b.emoji || '') + '</span><b>' + esc(b.label) + '</b>' + (b.sub ? '<small>' + esc(b.sub) + '</small>' : '') + '<div class="nt-in">' + placed[b.id].map(cd => '<i>' + (cd.emoji || '') + ' ' + esc(cd.t) + '</i>').join('') + '</div></button>').join('') + '</div>';
      main.innerHTML = h;
    }
    main.addEventListener('click', e => {
      const b = e.target.closest('button'); if (!b) return;
      if (b.dataset.act === 'again') { start(); return; }
      const card = deck[i]; if (!card || b.dataset.bin === undefined) return;
      const ok = [].concat(card.bin).includes(b.dataset.bin);
      if (ok) { if (!missed) right++; placed[b.dataset.bin].push(card); msg = '✅ ' + (card.why || 'Yes!'); i++; missed = false; wrongBin = null; }
      else { missed = true; wrongBin = b.dataset.bin; msg = '❌ Not that one. Try again.'; }
      render();
    });
    start();
    window.__nt = { state: () => ({ i, right, n: deck.length, card: deck[i] }), cfg };
  }

  return { sim, match, C, pen };
})();
