"""Shared layout for the Lickity Split site. Run tools/build.py to write every page."""
import io, json, os, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = json.load(io.open(os.path.join(ROOT, "tools", "src.json"), encoding="utf-8"))
STAGING = os.environ.get("STAGING", "1") == "1"
SITE = "https://lickitysplitweb.com/"
CHEV = '<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M2 4l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
LOGO = '<img src="logo.svg" alt="" width="218" height="40"/>'
LOGO_FOOT = '<img src="logo-light.svg" alt="" width="218" height="40" loading="lazy"/>'
CALL = "https://calendly.com/arlikoudis/30min"

def header(cur):
    c = lambda k: ' aria-current="page"' if k == cur else ''
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
  <div class="wrap head-in">
    <a class="logo" href="./" aria-label="Lickity Split Web Design, home">{LOGO}</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav class="site-nav" id="site-nav" aria-label="Main">
      <ul>
        <li><a href="work"{c("work")}>Portfolio</a></li>
        <li class="has-sub">
          <button class="sub-btn" type="button" aria-expanded="false" aria-controls="sub-websites">Websites {CHEV}</button>
          <ul class="sub" id="sub-websites">
            <li><a href="website-design"{c("website-design")}>Website Design</a></li>
            <li><a href="author-website-design"{c("author")}>Author Websites</a></li>
            <li><a href="composer-musician-websites"{c("music")}>Musician &amp; Composer Websites</a></li>
            <li><a href="publisher-website-design"{c("publisher")}>Publisher &amp; Journal Websites</a></li>
            <li><a href="nonprofit-website-design"{c("nonprofit")}>Nonprofit Websites</a></li>
            <li><a href="parish-ministry-websites"{c("parish")}>Parish &amp; Ministry Websites</a></li>
            <li><a href="wix-to-custom-website"{c("migrate")}>Website Migrations</a></li>
          </ul>
        </li>
        <li><a href="technology-consulting"{c("tech")}>Technology Consulting</a></li>
        <li><a href="pricing"{c("pricing")}>Pricing</a></li>
        <li><a href="about"{c("about")}>About</a></li>
        <li><a href="contact"{c("contact")}>Contact</a></li>
        <li class="nav-cta"><a class="btn btn-primary" href="contact">Get an Estimate</a></li>
      </ul>
    </nav>
  </div>
</header>'''

FOOTER = f'''<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-about">
        <a class="logo" href="./" aria-label="Lickity Split Web Design, home">{LOGO_FOOT}</a>
        <p>Website design and technology consulting. Based in Baltimore, working with clients around the country.</p>
        <a class="foot-ig" href="https://www.instagram.com/lickitysplitweb/" target="_blank" rel="noopener">{SRC["ig"]}<span>Instagram</span></a>
      </div>
      <nav aria-label="Explore">
        <div class="foot-h">Explore</div>
        <ul>
          <li><a href="work">Portfolio</a></li>
          <li><a href="gallery">Gallery</a></li>
          <li><a href="pricing">Pricing</a></li>
          <li><a href="about">About</a></li>
          <li><a href="resources">Resources</a></li>
        </ul>
      </nav>
      <nav aria-label="Services">
        <div class="foot-h">Services</div>
        <ul>
          <li><a href="website-design">Website Design</a></li>
          <li><a href="author-website-design">Author Websites</a></li>
          <li><a href="composer-musician-websites">Musician Websites</a></li>
          <li><a href="publisher-website-design">Publisher Websites</a></li>
          <li><a href="nonprofit-website-design">Nonprofit Websites</a></li>
          <li><a href="parish-ministry-websites">Parish Websites</a></li>
          <li><a href="wix-to-custom-website">Website Migrations</a></li>
          <li><a href="technology-consulting">Technology Consulting</a></li>
        </ul>
      </nav>
      <nav aria-label="Contact">
        <div class="foot-h">Contact</div>
        <ul>
          <li><a href="contact">Get an Estimate</a></li>
          <li><a href="{CALL}" target="_blank" rel="noopener">Book a Call</a></li>
          <li><a href="mailto:hello@lickitysplitweb.com">hello@lickitysplitweb.com</a></li>
        </ul>
      </nav>
    </div>
    <div class="foot-bar">
      <span>&copy; 2026 Lickity Split Web Design &middot; Likoudis Legacy LLC dba Likoudis Ventures</span>
      <span>Baltimore, Maryland &middot; <a class="foot-arc" href="archive" rel="nofollow">Archive</a></span>
    </div>
  </div>
</footer>'''

NAVJS = '''<script>(function(){var b=document.querySelector('.menu-btn'),n=document.getElementById('site-nav'),s=document.querySelector('.sub-btn');
function sub(o){s.setAttribute('aria-expanded',o?'true':'false')}
b.addEventListener('click',function(){var o=!n.classList.contains('open');n.classList.toggle('open',o);b.setAttribute('aria-expanded',o?'true':'false');b.textContent=o?'Close':'Menu'});
s.addEventListener('click',function(){sub(s.getAttribute('aria-expanded')!=='true')});
document.addEventListener('keydown',function(e){if(e.key==='Escape'){if(s.getAttribute('aria-expanded')==='true'){sub(false);s.focus()}else if(n.classList.contains('open')){b.click();b.focus()}}});
document.addEventListener('click',function(e){if(!e.target.closest('.has-sub'))sub(false)});
s.parentNode.addEventListener('focusout',function(e){if(!s.parentNode.contains(e.relatedTarget))sub(false)});
})();</script>
<script>if(/(^|\\.)lickitysplitweb\\.com$/.test(location.hostname)){window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}gtag('js',new Date());gtag('config','G-KPPCZHKHC2');window.addEventListener('load',function(){setTimeout(function(){var s=document.createElement('script');s.async=true;s.src='https://www.googletagmanager.com/gtag/js?id=G-KPPCZHKHC2';document.head.appendChild(s)},2500)})}</script>'''

BAJS = '''<script>(function(){var els=document.querySelectorAll('[data-ba]');if(!els.length)return;var still=window.matchMedia('(prefers-reduced-motion: reduce)').matches;els.forEach(function(el){var r=el.querySelector('.ba-range'),touched=false;function set(v){el.style.setProperty('--p',v+'%')}r.addEventListener('input',function(){touched=true;set(r.value)});if(still||!('IntersectionObserver' in window))return;set(100);r.value=100;var io=new IntersectionObserver(function(en){if(!en[0].isIntersecting)return;io.disconnect();var t0=null;function step(t){if(touched)return;if(t0===null)t0=t;var k=Math.min(1,(t-t0)/1100),e=1-Math.pow(1-k,3),v=100-50*e;set(v);r.value=Math.round(v);if(k<1)requestAnimationFrame(step)}setTimeout(function(){requestAnimationFrame(step)},350)},{threshold:.55});io.observe(el)})})();</script>'''

def cta(h="Have a project in mind?", p="Tell me what you&rsquo;re working on and what you need. I&rsquo;ll review the details and give you an estimate.", b="Get an Estimate", href="contact"):
    return f'''  <section class="cta">
    <div class="wrap cta-in">
      <div><h2>{h}</h2><p>{p}</p></div>
      <a class="btn" href="{href}">{b}</a>
    </div>
  </section>'''

def page(fname, title, desc, body, cur="", ld="", scripts="", noindex=False, base=""):
    url = SITE + ("" if fname == "index.html" else fname[:-5])
    robots = '\n  <meta name="robots" content="noindex, nofollow"/>' if (STAGING or noindex) else ''
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>{base and chr(10) + '  <base href="' + base + '"/>'}
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>{robots}
  <title>{title}</title>
  <meta name="description" content="{desc}"/>
  <link rel="canonical" href="{url}"/>
  <meta property="og:type" content="website"/>
  <meta property="og:url" content="{url}"/>
  <meta property="og:title" content="{title}"/>
  <meta property="og:description" content="{desc}"/>
  <meta property="og:image" content="{SITE}og.jpg"/>
  <meta property="og:image:width" content="2400"/>
  <meta property="og:image:height" content="1260"/>
  <meta property="og:site_name" content="Lickity Split Web Design"/>
  <meta name="twitter:card" content="summary_large_image"/>
  <meta name="twitter:title" content="{title}"/>
  <meta name="twitter:description" content="{desc}"/>
  <meta name="twitter:image" content="{SITE}og.jpg"/>
  <link rel="icon" href="favicon.svg" type="image/svg+xml"/>
  <link rel="icon" href="favicon-32.png" sizes="32x32" type="image/png"/>
  <link rel="icon" href="favicon-16.png" sizes="16x16" type="image/png"/>
  <link rel="apple-touch-icon" href="apple-touch-icon.png"/>
  <link rel="preload" as="font" type="font/woff2" href="fonts/Lora-500.woff2" crossorigin/>
  <link rel="preload" as="font" type="font/woff2" href="fonts/Manrope-var.woff2" crossorigin/>
  <link rel="preload" as="font" type="font/woff2" href="fonts/SourceSans3-var.woff2" crossorigin/>
  <link rel="stylesheet" href="fonts.css?v=1"/>
  <link rel="stylesheet" href="v2.css?v=9"/>
{ld}</head>
<body>
{header(cur).replace('href="#main"', 'href="' + fname[:-5] + '#main"') if base else header(cur)}
<main id="main">
{body}
</main>
{FOOTER}
{NAVJS}
{scripts}
<!-- View desktop version toggle (Lickity Split) -->
{SRC["toggle"]}
</body>
</html>
'''
    os.makedirs(os.path.dirname(os.path.join(ROOT, fname)), exist_ok=True)
    io.open(os.path.join(ROOT, fname), "w", encoding="utf-8").write(doc)
    return fname

def hero(h1, leads, actions=""):
    ps = "\n".join(f'      <p class="lead">{x}</p>' for x in leads)
    act = f'\n      <div class="hero-actions">{actions}</div>' if actions else ""
    return f'''  <section class="page-hero">
    <div class="wrap">
      <h1>{h1}</h1>
{ps}{act}
    </div>
  </section>'''

def ul(items): return "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"

def steps():
    data = [("Tell me what you need", "Send a short description of your project and any website you already have."),
            ("Get an estimate", "I&rsquo;ll review the scope, ask any questions that need answering, and give you a price."),
            ("Review the site", "You&rsquo;ll see a private preview and have a chance to request revisions before launch."),
            ("Go live", "I&rsquo;ll connect the domain, check that everything is working, and explain how to make updates.")]
    return '<ol class="steps">' + "".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in data) + "</ol>"

# Projects: one record per site, used by the homepage, portfolio, gallery and service pages.
P = {
 "dcsocial": dict(name="DC Social Collective", alt="DC Social Collective homepage"),
 "larocca": dict(name="Frank La Rocca", alt="Frank La Rocca homepage"),
 "icjf": dict(name="International Catholic Jurists Forum", alt="International Catholic Jurists Forum homepage"),
 "adan": dict(name="Ad&aacute;n Fern&aacute;ndez", alt="Adán Fernández homepage"),
 "roxane": dict(name="Roxane Salonen", alt="Roxane Salonen homepage"),
 "brushsoul": dict(name="Brush &amp; Soul Studio", alt="Brush and Soul Studio storefront"),
 "bruna": dict(name="Bruna Ribeiro", alt="Bruna Ribeiro homepage"),
 "llf": dict(name="Likoudis Legacy Foundation", alt="Likoudis Legacy Foundation homepage"),
 "traddyland": dict(name="Traddyland", alt="Traddyland homepage"),
 "collin": dict(name="Collin Westerlund", alt="Collin Westerlund homepage"),
 "lapenna": dict(name="Michael LaPenna", alt="Michael LaPenna homepage"),
}
for k, v in P.items(): v.update(SRC["cases"][k])

# Case study pages, one per featured project
CASEURL = {"dcsocial": "projects/dc-social-collective", "larocca": "projects/frank-la-rocca",
           "icjf": "projects/international-catholic-jurists-forum", "roxane": "projects/roxane-salonen"}

def card(pid, cat, desc, link_label="View Project", href=None, name=None):
    p = P[pid]; href = href or CASEURL.get(pid, f"work#{pid}"); name = name or p["name"]
    if pid in CASEURL and link_label == "View Project": link_label = "Read the Case Study"
    plain = html.unescape(name)
    return f'''        <article class="proj">
          <a class="proj-shot" href="{href}" tabindex="-1" aria-hidden="true"><img src="screenshots/{p["shot"]}" alt="" width="{p["w"]}" height="{p["h"]}" loading="lazy" decoding="async"></a>
          <p class="label">{cat}</p>
          <h3><a href="{href}">{name}</a></h3>
          <p class="desc">{desc}</p>
          <a class="tlink" href="{href}" aria-label="{link_label}, {html.escape(plain)}">{link_label}</a>
        </article>'''
