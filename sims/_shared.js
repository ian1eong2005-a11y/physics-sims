// Shared UX layer, injected into every applet by core/embed.py.
// Zoom: Ctrl+wheel or pinch on the canvas, the +/− buttons, or plain wheel when "scroll = zoom" is on.
// Hotkeys: Space = play/pause, R = reset (when focus is not in a control).
(() => {
  const stage = document.querySelector('.stage'), cv = stage && stage.querySelector('canvas');
  if (!stage || !cv) return;
  stage.style.position = 'relative'; stage.style.overflow = 'auto';
  let zoom = 1, wheelZoom = false;
  const bar = document.createElement('div'); bar.className = 'zoombar';
  bar.innerHTML = '<button data-z="-" title="Zoom out (Ctrl + scroll down)">−</button><button data-z="0" title="Fit to width">100%</button><button data-z="+" title="Zoom in (Ctrl + scroll up)">+</button><button data-z="w" title="Zoom with the scroll wheel instead of scrolling the page" aria-pressed="false">scroll = zoom</button>';
  stage.appendChild(bar);
  const pct = bar.children[1];
  function setZoom(z, ax, ay) {
    z = Math.max(0.5, Math.min(4, z));
    const r = cv.getBoundingClientRect(); const sr = stage.getBoundingClientRect();
    const fx = ax === undefined ? 0.5 : (ax - r.left) / r.width, fy = ay === undefined ? 0.5 : (ay - r.top) / r.height;
    const oldW = r.width, oldH = r.height;
    zoom = z; cv.style.width = (100 * z) + '%';
    const nr = cv.getBoundingClientRect();
    stage.scrollLeft += fx * (nr.width - oldW); stage.scrollTop += fy * (nr.height - oldH);
    pct.textContent = Math.round(z * 100) + '%';
    bar.classList.toggle('zoomed', z !== 1);
  }
  bar.addEventListener('click', e => { const b = e.target.closest('button'); if (!b) return; const k = b.dataset.z;
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
})();
