document.addEventListener('DOMContentLoaded', function () {
  const root = document.documentElement;
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Mavzu: kunduzgi <-> tungi (boshlang'ich holatni <head> dagi skript qo'yadi)
  const themeToggle = document.getElementById('theme-toggle');
  const themeColorMeta = document.getElementById('meta-theme-color');
  function syncThemeUi() {
    const dark = root.getAttribute('data-theme') === 'dark';
    if (themeToggle) {
      const label = dark ? themeToggle.dataset.labelToLight : themeToggle.dataset.labelToDark;
      themeToggle.setAttribute('aria-pressed', dark ? 'true' : 'false');
      themeToggle.setAttribute('aria-label', label);
      themeToggle.setAttribute('title', label);
    }
    if (themeColorMeta) themeColorMeta.setAttribute('content', dark ? '#0b0f17' : '#fafaf7');
  }
  syncThemeUi();
  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('theme', next); } catch (e) { /* saqlab bo'lmasa ham ishlayveradi */ }
      syncThemeUi();
    });
  }

  // Mobil menyu
  const navToggle = document.getElementById('nav-toggle');
  const navLinks = document.getElementById('nav-links');
  if (navToggle && navLinks) {
    const setOpen = (open) => {
      navToggle.classList.toggle('open', open);
      navLinks.classList.toggle('open', open);
      navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    };
    navToggle.addEventListener('click', () => setOpen(!navLinks.classList.contains('open')));
    navLinks.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setOpen(false)));
  }

  // Menyuda hozirgi bo'limni ko'rsatish (scrollspy). /projects/ sahifalarida "Loyihalar" server tomonda belgilanadi.
  const spyLinks = Array.from(document.querySelectorAll('.nav-links a[data-section]'));
  const spySections = spyLinks
    .map(a => ({ link: a, el: document.getElementById(a.dataset.section) }))
    .filter(x => x.el);
  if (spySections.length) {
    const setActive = (active) => {
      spyLinks.forEach(a => {
        const on = a === active;
        a.classList.toggle('active', on);
        if (on) a.setAttribute('aria-current', 'location'); else a.removeAttribute('aria-current');
      });
    };
    let ticking = false;
    const update = () => {
      ticking = false;
      const line = 140; // kapsula balandligi + zaxira
      let current = null;
      spySections.forEach(x => { if (x.el.getBoundingClientRect().top <= line) current = x.link; });
      if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 4) {
        current = spySections[spySections.length - 1].link;
      }
      setActive(current);
    };
    const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } };
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    spyLinks.forEach(a => a.addEventListener('click', () => setActive(a)));
    update();
  }

  // "Menga yozing" dropdown: tashqariga bosilsa yoki Escape bosilsa yopiladi
  const hireMenu = document.getElementById('hire-menu');
  if (hireMenu) {
    document.addEventListener('click', (e) => {
      if (!hireMenu.contains(e.target)) hireMenu.removeAttribute('open');
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') hireMenu.removeAttribute('open');
    });
    hireMenu.querySelectorAll('.hire-dropdown a').forEach(a => {
      a.addEventListener('click', () => hireMenu.removeAttribute('open'));
    });
  }

  // Scroll reveal (JS ishlamasa elementlar ko'rinaveradi — .reveal faqat JS bor paytda yashiriladi)
  const revealEls = document.querySelectorAll('.reveal');
  if (reduceMotion || !('IntersectionObserver' in window)) {
    revealEls.forEach(el => el.classList.add('visible'));
  } else {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    revealEls.forEach(el => observer.observe(el));
  }

  // Galereya lightbox
  const lightbox = document.getElementById('lightbox');
  const links = Array.from(document.querySelectorAll('[data-lightbox]'));
  if (lightbox && links.length && typeof lightbox.showModal === 'function') {
    const img = document.getElementById('lightbox-img');
    let index = 0;
    const show = (i) => {
      index = (i + links.length) % links.length;
      img.src = links[index].getAttribute('href');
      img.alt = links[index].querySelector('img').alt;
    };
    links.forEach((a, i) => a.addEventListener('click', (e) => {
      e.preventDefault();
      show(i);
      lightbox.showModal();
    }));
    lightbox.querySelector('[data-lb-close]').addEventListener('click', () => lightbox.close());
    lightbox.querySelector('[data-lb-prev]').addEventListener('click', () => show(index - 1));
    lightbox.querySelector('[data-lb-next]').addEventListener('click', () => show(index + 1));
    lightbox.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') show(index - 1);
      if (e.key === 'ArrowRight') show(index + 1);
    });
    lightbox.addEventListener('click', (e) => { if (e.target === lightbox) lightbox.close(); });
  }
});
