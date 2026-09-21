document.addEventListener('DOMContentLoaded', function () {
  const body = document.getElementById('terminal-body');
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const lines = [
    { type: 'prompt', text: '$ whoami' },
    { type: 'out', text: 'dostonbek_suyunov — backend developer' },
    { type: 'prompt', text: '$ python manage.py runserver' },
    { type: 'out', text: "Server ishga tushdi. Loyihalarni ko'rishga tayyor." },
  ];

  function renderStatic() {
    lines.forEach(l => {
      const el = document.createElement('div');
      el.className = 'line';
      const span = document.createElement('span');
      span.className = l.type === 'prompt' ? 'prompt' : 'out';
      span.textContent = l.text;
      el.appendChild(span);
      body.appendChild(el);
    });
  }

  function typeLines() {
    let i = 0;
    function nextLine() {
      if (i >= lines.length) return;
      const lineEl = document.createElement('div');
      lineEl.className = 'line';
      const span = document.createElement('span');
      span.className = lines[i].type === 'prompt' ? 'prompt' : 'out';
      lineEl.appendChild(span);
      body.appendChild(lineEl);
      let charIndex = 0;
      const text = lines[i].text;
      (function typeChar() {
        if (charIndex <= text.length) {
          span.textContent = text.slice(0, charIndex);
          charIndex++;
          setTimeout(typeChar, 22);
        } else {
          i++;
          setTimeout(nextLine, 300);
        }
      })();
    }
    nextLine();
  }

  if (body) {
    reduceMotion ? renderStatic() : typeLines();
  }

  const revealEls = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });
  revealEls.forEach(el => observer.observe(el));
});
