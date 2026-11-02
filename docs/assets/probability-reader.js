(() => {
  const select = document.getElementById('page-select');
  const previous = document.getElementById('prev');
  const next = document.getElementById('next');
  const status = document.getElementById('status');
  const zoom = document.getElementById('zoom');
  const main = document.querySelector('main');
  const pages = [...document.querySelectorAll('figure')];
  let current = 1;
  function update(n) {
    current = Math.max(1, Math.min(pages.length, n));
    select.value = String(current);
    previous.disabled = current === 1;
    next.disabled = current === pages.length;
    status.textContent = `第 ${current} / ${pages.length} 页`;
  }
  function go(n) {
    update(n);
    history.replaceState(null, '', `#page-${current}`);
    const top = window.scrollY + pages[current - 1].getBoundingClientRect().top;
    window.scrollTo({top: top - document.querySelector('nav').offsetHeight - 12});
  }
  select.addEventListener('change', () => go(Number(select.value)));
  previous.addEventListener('click', () => go(current - 1));
  next.addEventListener('click', () => go(current + 1));
  zoom.addEventListener('click', () => {
    const page = current;
    const enabled = main.classList.toggle('zoomed');
    zoom.setAttribute('aria-pressed', String(enabled));
    zoom.textContent = enabled ? '适合屏幕' : '放大阅读';
    go(page);
  });
  function restore() {
    const match = location.hash.match(/^#page-(\d+)$/);
    if (match) go(Number(match[1])); else update(1);
  }
  window.addEventListener('hashchange', restore);
  restore();
})();
