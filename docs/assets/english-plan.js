(() => {
  'use strict';
  const key = 'english-plan-v1';
  const boxes = [...document.querySelectorAll('[data-day]')];
  let completed = new Set();
  const unavailable = () => { document.getElementById('storage-note').textContent = '浏览器存储不可用，本次记录不会在关闭页面后保存；任务仍可正常阅读。'; };
  try { const value = JSON.parse(localStorage.getItem(key) || '[]'); if (Array.isArray(value)) completed = new Set(value.filter(x => Number.isInteger(x) && x >= 1 && x <= 28)); } catch { unavailable(); }
  function update() {
    const count = boxes.filter(x => x.checked).length;
    document.getElementById('progress').value = count;
    document.getElementById('progress').textContent = `${count}/28`;
    document.getElementById('progress-label').textContent = `完成记录：${count} / 28 天`;
  }
  boxes.forEach(box => {
    box.checked = completed.has(Number(box.dataset.day));
    box.addEventListener('change', () => {
      update();
      try { localStorage.setItem(key, JSON.stringify(boxes.filter(x => x.checked).map(x => Number(x.dataset.day)))); } catch { unavailable(); }
    });
  });
  function reveal() {
    const id = location.hash.slice(1);
    if (!/^day-\d+$/.test(id)) return;
    const target = document.getElementById(id);
    if (target) { target.open = true; target.scrollIntoView({block:'start'}); }
  }
  update(); reveal(); window.addEventListener('hashchange', reveal);
})();
