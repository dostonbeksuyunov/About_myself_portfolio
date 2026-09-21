document.addEventListener('DOMContentLoaded', function () {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Preloader
  const preloader = document.getElementById('preloader');
  const bar = document.getElementById('preloader-bar');
  const percent = document.getElementById('preloader-percent');
  if (preloader) {
    // Fail-safe: never let it block the page forever
    setTimeout(() => preloader.classList.add('hidden'), 4000);

    if (reduceMotion) {
      preloader.classList.add('hidden');
    } else {
      let p = 0;
      const interval = setInterval(() => {
        p += Math.random() * 18 + 6;
        if (p >= 100) {
          p = 100;
          clearInterval(interval);
          setTimeout(() => preloader.classList.add('hidden'), 300);
        }
        if (bar) bar.style.width = p + '%';
        if (percent) percent.textContent = Math.floor(p) + '%';
      }, 140);
    }
  }

  // Mobile nav toggle
  const navToggle = document.getElementById('nav-toggle');
  const navLinksMobile = document.getElementById('nav-links');
  if (navToggle && navLinksMobile) {
    navToggle.addEventListener('click', () => {
      navToggle.classList.toggle('open');
      navLinksMobile.classList.toggle('open');
    });
    navLinksMobile.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => {
        navToggle.classList.remove('open');
        navLinksMobile.classList.remove('open');
      });
    });
  }

  // Custom cursor
  const cursorDot = document.getElementById('cursor-dot');
  const cursorRing = document.getElementById('cursor-ring');
  if (cursorDot && cursorRing && window.matchMedia('(pointer: fine)').matches) {
    let ringX = 0, ringY = 0, mouseX = 0, mouseY = 0;
    window.addEventListener('mousemove', (e) => {
      mouseX = e.clientX; mouseY = e.clientY;
      cursorDot.style.left = mouseX + 'px';
      cursorDot.style.top = mouseY + 'px';
    });
    function animateRing() {
      ringX += (mouseX - ringX) * 0.18;
      ringY += (mouseY - ringY) * 0.18;
      cursorRing.style.left = ringX + 'px';
      cursorRing.style.top = ringY + 'px';
      requestAnimationFrame(animateRing);
    }
    animateRing();
    document.querySelectorAll('a, button, .btn').forEach(el => {
      el.addEventListener('mouseenter', () => cursorRing.classList.add('active'));
      el.addEventListener('mouseleave', () => cursorRing.classList.remove('active'));
    });
  } else if (cursorDot && cursorRing) {
    cursorDot.style.display = 'none';
    cursorRing.style.display = 'none';
  }

  // Scroll reveal
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

  // Scroll progress bar
  const progressBar = document.getElementById('progress-bar');
  function updateProgress() {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    if (progressBar) progressBar.style.width = progress + '%';
  }
  window.addEventListener('scroll', updateProgress, { passive: true });
  updateProgress();
});
