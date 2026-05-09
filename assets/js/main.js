/* =====================================================
   JMO Portfolio — main.js
   Cursor, navbar, partículas, reveal, magnetic, contadores
   ===================================================== */

document.addEventListener('DOMContentLoaded', () => {

    /* ----- Marca link ativo na navbar ----- */
    (function() {
        const path = window.location.pathname.replace(/\/+$/, '') || '/';
        document.querySelectorAll('.nav-link').forEach(link => {
            const href = link.getAttribute('href').replace(/\/+$/, '') || '/';
            const fileName = href.split('/').pop();
            const currentName = path.split('/').pop();
            if (href === path || fileName === currentName ||
                (path === '/' && (href === '/' || href === 'index.html')) ||
                (currentName === 'index.html' && (href === '/' || href === 'index.html'))) {
                link.classList.add('is-active');
            }
        });
    })();

    /* ----- Custom cursor ----- */
    (function() {
        if (window.matchMedia('(max-width: 991px)').matches) return;
        const dot = document.getElementById('cursor-dot');
        const ring = document.getElementById('cursor-ring');
        if (!dot || !ring) return;

        let mouseX = window.innerWidth / 2, mouseY = window.innerHeight / 2;
        let ringX = mouseX, ringY = mouseY;

        window.addEventListener('mousemove', (e) => {
            mouseX = e.clientX; mouseY = e.clientY;
            dot.style.transform = `translate(${mouseX - 3}px, ${mouseY - 3}px)`;
        });

        function tickRing() {
            ringX += (mouseX - ringX) * 0.18;
            ringY += (mouseY - ringY) * 0.18;
            ring.style.transform = `translate(${ringX - 18}px, ${ringY - 18}px)`;
            requestAnimationFrame(tickRing);
        }
        tickRing();

        const hoverSelectors = 'a, button, [data-cursor="hover"], .magnetic, .stack-card, .area-card, .project, .stat-card, .skill-pill, .gallery-item';
        document.addEventListener('mouseover', (e) => {
            if (e.target.closest(hoverSelectors)) ring.classList.add('is-hover');
        });
        document.addEventListener('mouseout', (e) => {
            if (e.target.closest(hoverSelectors)) ring.classList.remove('is-hover');
        });
    })();

    /* ----- Magnetic hover ----- */
    (function() {
        if (window.matchMedia('(max-width: 991px)').matches) return;
        document.querySelectorAll('.magnetic').forEach((el) => {
            el.addEventListener('mousemove', (e) => {
                const rect = el.getBoundingClientRect();
                const x = e.clientX - rect.left - rect.width / 2;
                const y = e.clientY - rect.top - rect.height / 2;
                el.style.transform = `translate(${x * 0.25}px, ${y * 0.25}px)`;
            });
            el.addEventListener('mouseleave', () => {
                el.style.transform = 'translate(0, 0)';
            });
        });
    })();

    /* ----- Navbar scroll + scroll progress ----- */
    (function() {
        const nav = document.getElementById('nav-shell');
        const progress = document.getElementById('scroll-progress');
        if (!nav) return;

        function onScroll() {
            const y = window.scrollY;
            nav.classList.toggle('is-scrolled', y > 30);
            if (progress) {
                const max = document.documentElement.scrollHeight - window.innerHeight;
                progress.style.width = max > 0 ? ((y / max) * 100) + '%' : '0%';
            }
        }
        window.addEventListener('scroll', onScroll, { passive: true });
        onScroll();
    })();

    /* ----- Mobile menu toggle ----- */
    (function() {
        const toggle = document.getElementById('nav-toggle');
        const shell = document.getElementById('nav-shell');
        if (!toggle || !shell) return;
        toggle.addEventListener('click', () => {
            const open = shell.classList.toggle('is-open');
            toggle.classList.toggle('is-open', open);
        });
        document.querySelectorAll('.nav-link').forEach(l => {
            l.addEventListener('click', () => {
                shell.classList.remove('is-open');
                toggle.classList.remove('is-open');
            });
        });
    })();

    /* ----- Particle network ----- */
    (function() {
        const canvas = document.getElementById('particles-canvas');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        let particles = [];

        function resize() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        resize();
        window.addEventListener('resize', resize);

        function spawn() {
            const count = Math.min(90, Math.floor(window.innerWidth / 16));
            particles = [];
            for (let i = 0; i < count; i++) {
                particles.push({
                    x: Math.random() * canvas.width,
                    y: Math.random() * canvas.height,
                    vx: (Math.random() - 0.5) * 0.35,
                    vy: (Math.random() - 0.5) * 0.35,
                    r: Math.random() * 1.6 + 0.4,
                    a: Math.random() * 0.4 + 0.2
                });
            }
        }
        spawn();
        window.addEventListener('resize', spawn);

        let mouse = { x: -9999, y: -9999 };
        window.addEventListener('mousemove', (e) => { mouse.x = e.clientX; mouse.y = e.clientY; });

        function tick() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            for (let p of particles) {
                p.x += p.vx; p.y += p.vy;
                if (p.x < 0) p.x = canvas.width;
                if (p.x > canvas.width) p.x = 0;
                if (p.y < 0) p.y = canvas.height;
                if (p.y > canvas.height) p.y = 0;
                ctx.fillStyle = `rgba(0, 212, 255, ${p.a})`;
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
                ctx.fill();
            }
            for (let i = 0; i < particles.length; i++) {
                for (let j = i + 1; j < particles.length; j++) {
                    const dx = particles[i].x - particles[j].x;
                    const dy = particles[i].y - particles[j].y;
                    const d = Math.sqrt(dx * dx + dy * dy);
                    if (d < 130) {
                        ctx.strokeStyle = `rgba(139, 92, 246, ${0.12 * (1 - d / 130)})`;
                        ctx.lineWidth = 0.6;
                        ctx.beginPath();
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.stroke();
                    }
                }
                const mdx = particles[i].x - mouse.x;
                const mdy = particles[i].y - mouse.y;
                const md = Math.sqrt(mdx * mdx + mdy * mdy);
                if (md < 160) {
                    ctx.strokeStyle = `rgba(0, 212, 255, ${0.25 * (1 - md / 160)})`;
                    ctx.lineWidth = 0.7;
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(mouse.x, mouse.y);
                    ctx.stroke();
                }
            }
            requestAnimationFrame(tick);
        }
        tick();
    })();

    /* ----- Scroll reveal ----- */
    (function() {
        const els = document.querySelectorAll('[data-reveal]');
        const obs = new IntersectionObserver((entries) => {
            entries.forEach(en => {
                if (en.isIntersecting) {
                    en.target.classList.add('is-visible');
                    obs.unobserve(en.target);
                }
            });
        }, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });
        els.forEach(el => obs.observe(el));
    })();

    /* ----- Counter animation ----- */
    (function() {
        const counters = document.querySelectorAll('[data-counter]');
        const obs = new IntersectionObserver((entries) => {
            entries.forEach(en => {
                if (!en.isIntersecting) return;
                const el = en.target;
                const target = parseInt(el.dataset.counter, 10);
                const dur = 1400;
                const start = performance.now();
                const suffix = el.dataset.counterSuffix || '';
                function step(now) {
                    const t = Math.min(1, (now - start) / dur);
                    const eased = 1 - Math.pow(1 - t, 3);
                    el.textContent = Math.floor(eased * target) + suffix;
                    if (t < 1) requestAnimationFrame(step);
                }
                requestAnimationFrame(step);
                obs.unobserve(el);
            });
        }, { threshold: 0.4 });
        counters.forEach(c => obs.observe(c));
    })();

    /* ----- 3D tilt ----- */
    (function() {
        if (window.matchMedia('(max-width: 991px)').matches) return;
        document.querySelectorAll('[data-tilt]').forEach((el) => {
            const wrap = el.parentElement;
            wrap.addEventListener('mousemove', (e) => {
                const r = wrap.getBoundingClientRect();
                const x = (e.clientX - r.left) / r.width - 0.5;
                const y = (e.clientY - r.top) / r.height - 0.5;
                el.style.transform = `perspective(900px) rotateY(${x * 8}deg) rotateX(${-y * 8}deg) translateZ(0)`;
            });
            wrap.addEventListener('mouseleave', () => {
                el.style.transform = 'perspective(900px) rotateY(0) rotateX(0)';
            });
        });
    })();

    /* ----- Type rotator (apresentação) ----- */
    (function() {
        const target = document.getElementById('typed');
        if (!target) return;
        const words = JSON.parse(target.dataset.words || '["Full Stack Developer"]');
        let i = 0, j = 0, deleting = false;
        function tick() {
            const w = words[i];
            target.textContent = deleting ? w.slice(0, --j) : w.slice(0, ++j);
            let speed = deleting ? 35 : 75;
            if (!deleting && j === w.length) { speed = 1800; deleting = true; }
            else if (deleting && j === 0) { deleting = false; i = (i + 1) % words.length; speed = 300; }
            setTimeout(tick, speed);
        }
        tick();
    })();

    /* ----- Filtros (projetos) ----- */
    (function() {
        const buttons = document.querySelectorAll('.filter-btn');
        const list = document.getElementById('projects-list');
        if (!list || !buttons.length) return;
        const projects = list.querySelectorAll('.project');

        buttons.forEach(btn => {
            btn.addEventListener('click', () => {
                buttons.forEach(b => b.classList.remove('is-active'));
                btn.classList.add('is-active');
                const filter = btn.dataset.filter;
                let visible = 0;
                projects.forEach(p => {
                    const tags = p.dataset.tags || '';
                    const match = filter === 'all' || tags.includes(filter);
                    p.style.display = match ? '' : 'none';
                    if (match) visible++;
                });
                list.classList.toggle('is-empty', visible === 0);
            });
        });
    })();

    /* ----- Toggle de detalhes do projeto ----- */
    (function() {
        document.querySelectorAll('.project-toggle').forEach((btn) => {
            btn.addEventListener('click', () => {
                const card = btn.closest('.project');
                const expanded = card.classList.toggle('is-expanded');
                const txt = btn.querySelector('.toggle-text');
                if (txt) txt.textContent = expanded ? 'Recolher detalhes' : 'Ver detalhes completos';
            });
        });
    })();

    /* ----- Lightbox ----- */
    (function() {
        const lightbox = document.getElementById('lightbox');
        const lbImg = document.getElementById('lightbox-img');
        const lbClose = document.getElementById('lightbox-close');
        if (!lightbox || !lbImg) return;

        document.querySelectorAll('[data-lightbox]').forEach(item => {
            item.addEventListener('click', (e) => {
                e.preventDefault();
                lbImg.src = item.dataset.lightbox;
                lightbox.classList.add('is-open');
                document.body.style.overflow = 'hidden';
            });
        });

        function close() {
            lightbox.classList.remove('is-open');
            document.body.style.overflow = '';
        }
        if (lbClose) lbClose.addEventListener('click', close);
        lightbox.addEventListener('click', (e) => { if (e.target === lightbox) close(); });
        document.addEventListener('keydown', (e) => { if (e.key === 'Escape') close(); });
    })();

});
