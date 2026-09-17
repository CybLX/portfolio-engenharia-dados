(() => {
  'use strict';
  document.querySelectorAll('[data-tabs]').forEach(group => {
    const tabs = [...group.querySelectorAll('[role="tab"]')];
    const select = tab => {
      tabs.forEach(item => {
        const selected = item === tab;
        item.setAttribute('aria-selected', String(selected));
        item.tabIndex = selected ? 0 : -1;
        const panel = document.getElementById(item.getAttribute('aria-controls'));
        if (panel) panel.hidden = !selected;
      });
    };
    tabs.forEach((tab, index) => {
      tab.addEventListener('click', () => select(tab));
      tab.addEventListener('keydown', event => {
        let next;
        if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
        if (event.key === 'ArrowLeft') next = (index - 1 + tabs.length) % tabs.length;
        if (event.key === 'Home') next = 0;
        if (event.key === 'End') next = tabs.length - 1;
        if (next !== undefined) {
          event.preventDefault();
          select(tabs[next]);
          tabs[next].focus();
        }
      });
    });
  });
  const diagramDialog = document.getElementById('diagram-dialog');
  if (diagramDialog) {
    document.querySelectorAll('[data-expand-diagram]').forEach(button => {
      button.addEventListener('click', () => {
        const source = document.getElementById(button.dataset.expandDiagram);
        const target = diagramDialog.querySelector('img');
        if (!source || !target) return;
        target.src = source.src;
        target.alt = source.alt;
        document.getElementById('diagram-dialog-title').textContent = source.alt;
        diagramDialog.showModal();
      });
    });
  }
  document.querySelectorAll('[data-close-dialog]').forEach(button => {
    button.addEventListener('click', () => button.closest('dialog').close());
  });
  const caseDialog = document.getElementById('case-dialog');
  if (caseDialog) {
    document.querySelectorAll('[data-open-case]').forEach(link => {
      link.addEventListener('click', event => {
        event.preventDefault();
        caseDialog.showModal();
        caseDialog.scrollTop = 0;
      });
    });
  }
})();
