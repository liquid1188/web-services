from core import *

def quote_fig(t):
    return f'''        <figure class="quote">
          <blockquote>{t["quote"]}</blockquote>
          <figcaption><img src="{t["img"]}" alt="" width="96" height="96" loading="lazy"><div class="who">{t["name"]}<span>{t["role"]}</span></div></figcaption>
        </figure>'''

EDJS = r"""<script>(function(){
var P={event:{h:'New event',lbl:'Upcoming event',btn:'Get tickets',f:[['title','Title','Autumn Concert'],['date','Date and time','Saturday, October 24, 7:30 pm'],['place','Venue','Parish Hall'],['text','Description','An evening of choral music for the season, with a reception to follow.']]},
book:{h:'New book',lbl:'New release',btn:'Order the book',f:[['title','Title','The Quiet Season'],['date','Publication date','Spring 2027'],['place','Publisher','Riverside Press'],['text','Description','A collection of essays on faith, family, and the small hours of ordinary life.']]},
post:{h:'New post',lbl:'From the blog',btn:'Read more',f:[['title','Title','Notes from the Road'],['date','Date','November 26, 2026'],['place','Category','Reflections'],['text','Excerpt','A few thoughts from a week of speaking at schools and libraries.']]}};
var cur='event',fields=document.getElementById('ed-fields');if(!fields)return;
var card=document.getElementById('ed-card'),draft=document.getElementById('ed-draft'),pub=document.getElementById('ed-pub');
function esc(t){var d=document.createElement('div');d.textContent=t;return d.innerHTML}
function val(k){var e=document.getElementById('ed-'+k);return e?e.value:''}
function render(){var p=P[cur];card.className='ed-card'+(draft.checked?' is-draft':'');
card.innerHTML=(draft.checked?'<span class="ed-badge">Draft, only you can see this</span>':'')+'<p class="ed-c-lbl">'+p.lbl+'</p><h3>'+esc(val('title')||'Untitled')+'</h3><p class="ed-c-meta">'+esc(val('date'))+(val('place')?' &middot; '+esc(val('place')):'')+'</p><p class="ed-c-text">'+esc(val('text'))+'</p><span class="ed-c-btn">'+p.btn+'</span>'}
function load(k){cur=k;var p=P[k];document.getElementById('ed-h').textContent=p.h;
fields.innerHTML=p.f.map(function(f){var tag=f[0]==='text'?'textarea':'input';return '<div class="ed-f"><label for="ed-'+f[0]+'">'+f[1]+'</label><'+tag+' id="ed-'+f[0]+'"'+(tag==='input'?' type="text" value="'+esc(f[2]).replace(/"/g,'&quot;')+'">':' rows="3">'+esc(f[2])+'</textarea>')+'</div>'}).join('');
document.querySelectorAll('[data-preset]').forEach(function(b){var on=b.getAttribute('data-preset')===k;b.classList.toggle('on',on);b.setAttribute('aria-pressed',on?'true':'false')});pub.textContent='Publish';render()}
fields.addEventListener('input',render);draft.addEventListener('change',function(){pub.textContent=draft.checked?'Save draft':'Publish';render()});
document.querySelectorAll('[data-preset]').forEach(function(b){b.addEventListener('click',function(){load(b.getAttribute('data-preset'))})});
pub.addEventListener('click',function(){var t=pub.textContent;pub.textContent=draft.checked?'Draft saved':'Published';pub.disabled=true;setTimeout(function(){pub.textContent=t;pub.disabled=false},1400)});
load('event')})();</script>"""

def home():
    T = {t["name"]: t for t in SRC["tests"]}
    three = [T["Christopher Byrne"], T["Roxane B. Salonen"], T["Adán Alejándro Fernández"]]
    cards = "\n".join([
        card("dcsocial", "Events and Community", "A new website for DC Social Collective, with live ticketing, venue information, and an archive of more than 6,000 photographs from past events."),
        card("larocca", "Music and Publishing", "A composer&rsquo;s website with 59 works, individual pages for scores and recordings, and a downloadable press kit."),
        card("icjf", "Nonprofit and Publishing", "A redesign that brought over 99 pages and 535 news posts, with a searchable archive of the forum&rsquo;s publications, events, and documents."),
        card("roxane", "Writing and Publishing", "An author website that brings together her books, columns, and more than 2,300 migrated blog posts."),
    ])
    body = f'''
  <section class="hero">
    <div class="wrap hero-in">
      <div class="hero-copy">
        <p class="label hero-eyebrow">Independent web design and technology consulting</p>
        <h1>Websites built around your work.</h1>
        <p>Custom websites for authors, artists, musicians, businesses, and nonprofits. From the writing and design to the technical details, I handle the whole project myself.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="work">View My Work</a>
          <a class="btn btn-ghost" href="contact">Get an Estimate</a>
        </div>
        <p class="hero-note">Projects from $300 &middot; Working with clients nationwide</p>
      </div>
      <div class="hero-art" aria-hidden="true">
        <div class="frame frame-a"><img src="screenshots/dcsocial.webp" alt="" width="1280" height="853" fetchpriority="high"></div>
        <div class="frame frame-b"><img src="screenshots/larocca.webp" alt="" width="1280" height="853"></div>
      </div>
    </div>
  </section>

  <section class="sec sec-stone" id="recent-work">
    <div class="wrap">
      <div class="sec-head">
        <h2>Recent work</h2>
        <p>A few of the websites I&rsquo;ve built, from a composer&rsquo;s catalog to an events platform with thousands of photographs and years of material to organize.</p>
      </div>
      <figure class="reel">
        <div class="frame reel-wide"><video controls playsinline preload="none" poster="reel/showreel-poster.webp?v=2" width="1920" height="1080" aria-label="Lickity Split Web showreel, under a minute, with music"><source src="reel/showreel.mp4?v=2" type="video/mp4"></video></div>
        <div class="frame reel-tall"><video controls playsinline preload="none" poster="reel/showreel-vertical-poster.webp?v=2" width="1080" height="1920" aria-label="Lickity Split Web showreel, under a minute, with music"><source src="reel/showreel-vertical.mp4?v=2" type="video/mp4"></video></div>
        <figcaption class="label">The sites in motion, in under a minute. Real pages, clicked and scrolled the way a visitor would.</figcaption>
      </figure>
      <div class="proj-grid">
{cards}
      </div>
      <div class="sec-foot"><a class="btn btn-ghost" href="work">See All Projects</a></div>
    </div>
  </section>

  <section class="sec" id="services">
    <div class="wrap">
      <div class="sec-head"><h2>What I can help with</h2></div>
      <div class="cols3">
        <div class="col"><h3>Website Design</h3><p>New websites for writers, artists, businesses, and organizations. I can handle a straightforward professional site or something larger with publications, archives, or other features.</p><a class="tlink" href="website-design">Explore Website Design</a></div>
        <div class="col"><h3>Website Migrations</h3><p>If you already have a website, I can help move it, reorganize the material, and rebuild it around what you need now.</p><a class="tlink" href="wix-to-custom-website">Website Migrations</a></div>
        <div class="col"><h3>Technology Consulting</h3><p>Help with email, shared files, online accounts, AI assistants, automation, and the systems your organization uses every day.</p><a class="tlink" href="technology-consulting">Technology Consulting</a></div>
      </div>
    </div>
  </section>


  <section class="sec sec-stone" id="editor">
    <div class="wrap ed-wrap">
      <div class="prose">
        <h2>Update it yourself, without learning a website builder</h2>
        <p>Custom Websites and Full Builds come with an editor made for your site. It has presets for the things you add most, so a new event, book, concert, album, or post is a short form to fill in, not a blank page to design.</p>
        <p>The fields match your content. An event asks for a date, a venue, and a ticket link. A book asks for a publication date, a description, and where to buy it. The site handles the layout, so every new page looks like it belongs.</p>
        <p>You can save a draft before it goes live, and earlier versions of the site can be restored. If you&rsquo;d rather send me the change, that works too.</p>
      </div>
      <figure class="ed-demo">
        <div class="ed-win">
          <div class="ed-bar"><span>Example editor</span><span class="ed-hint">Try it. Nothing here is saved.</span></div>
          <div class="ed-body">
            <div class="ed-side" role="group" aria-label="Choose a preset">
              <button type="button" class="on" data-preset="event" aria-pressed="true">Event</button>
              <button type="button" data-preset="book" aria-pressed="false">Book</button>
              <button type="button" data-preset="post" aria-pressed="false">Post</button>
            </div>
            <form class="ed-form" id="ed-form" onsubmit="return false">
              <p class="ed-h" id="ed-h">New event</p>
              <div id="ed-fields"></div>
              <div class="ed-foot"><label class="ed-toggle"><input type="checkbox" id="ed-draft"> Save as draft</label><button type="button" class="ed-pub" id="ed-pub">Publish</button></div>
            </form>
          </div>
        </div>
        <div class="ed-prev" aria-live="polite">
          <p class="ed-prev-lbl">How it appears on your site</p>
          <article class="ed-card" id="ed-card"></article>
        </div>
        <figcaption>An example of the kind of editor I set up. Each site gets presets built around what that client publishes.</figcaption>
      </figure>
    </div>
  </section>

  <section class="sec" id="about">
    <div class="wrap about-strip">
      <img src="andrew.webp?v=3" alt="Andrew Likoudis" width="780" height="975" loading="lazy" decoding="async">
      <div class="prose">
        <h2>You&rsquo;ll work directly with me.</h2>
        <p>I&rsquo;m Andrew, the person behind Lickity Split. My background is in business, communications, and publishing, and I bring that experience to web design.</p>
        <p>I handle the design, development, and launch myself. I also help with the writing, which can be just as important as getting the technical details right.</p>
        <a class="btn btn-ghost" href="about">More About Me</a>
      </div>
    </div>
  </section>

  <section class="sec sec-stone" id="research">
    <div class="wrap">
      <div class="sec-head"><h2>A few things I pay attention to</h2></div>
      <div class="cols3">
        <div class="col"><h3>Speed</h3><p>In Portent&rsquo;s 2022 research, B2B websites loading in one second had three times the conversion rate of sites loading in five seconds.</p><p>That doesn&rsquo;t mean every faster website will triple its business, but it is a good reason to take loading performance seriously.</p><p class="src"><a href="https://portent.com/blog/analytics/research-site-speed-hurting-everyones-revenue.htm" target="_blank" rel="noopener">Portent, 2022</a></p></div>
        <div class="col"><h3>Accessibility</h3><p>WebAIM&rsquo;s 2026 analysis found automatically detectable accessibility failures on 95.9% of one million homepages.</p><p>I pay attention to readable text, properly labeled forms, keyboard navigation, and other basics that make websites easier to use.</p><p class="src"><a href="https://webaim.org/projects/million/" target="_blank" rel="noopener">WebAIM, 2026</a></p></div>
        <div class="col"><h3>Search</h3><p>Each page gets its own title and description, written so people searching can tell what they&rsquo;ll find.</p><p>When a site moves, I keep existing page addresses where I can and redirect the rest.</p></div>
      </div>
    </div>
  </section>

  <section class="sec" id="testimonials">
    <div class="wrap">
      <div class="sec-head"><h2>What clients have said</h2></div>
      <div class="quotes">
{chr(10).join(quote_fig(t) for t in three)}
      </div>
      <div class="sec-foot"><a class="tlink" href="work">Read more from clients on the Portfolio page</a></div>
    </div>
  </section>

  <section class="sec sec-stone" id="pricing">
    <div class="wrap">
      <div class="sec-head">
        <h2>What does a website cost?</h2>
        <p>A simple starter website costs $300 to $500. Most custom websites cost between $500 and $1,200. Larger projects with archives, event systems, or other features start at $1,200 and are priced by scope.</p>
        <p>I&rsquo;ll give you an estimate before any work begins.</p>
      </div>
      <div class="cols3">
        <div class="col"><h3>Starter Site</h3><p class="price-tag">$300&ndash;$500</p><p>A single page or a few simple pages for a professional online presence.</p></div>
        <div class="col"><h3>Custom Website</h3><p class="price-tag">$500&ndash;$1,200</p><p>A more complete website designed around your work. Most projects fall here.</p></div>
        <div class="col"><h3>Full Build</h3><p class="price-tag">$1,200&ndash;$2,500+</p><p>Larger websites with archives, catalogs, event systems, or online stores.</p></div>
      </div>
      <div class="sec-foot"><a class="btn btn-ghost" href="pricing">View Pricing</a></div>
    </div>
  </section>

  <section class="sec" id="process">
    <div class="wrap">
      <div class="sec-head"><h2>How we get started</h2></div>
      {steps()}
    </div>
  </section>

{cta("Have a website in mind?", "Tell me what you&rsquo;re working on and what you need the site to do. I&rsquo;ll let you know what I recommend and what it would cost.")}'''
    ld = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"ProfessionalService","@id":"https://lickitysplitweb.com/#business","name":"Lickity Split Web Design","url":"https://lickitysplitweb.com/","image":"https://lickitysplitweb.com/og.jpg","description":"Custom websites for authors, musicians, small businesses, and nonprofits. Based in Baltimore, serving clients nationwide. Starter sites from $300.","email":"hello@lickitysplitweb.com","priceRange":"$300+","founder":{"@type":"Person","name":"Andrew Likoudis"},"address":{"@type":"PostalAddress","addressLocality":"Baltimore","addressRegion":"MD","addressCountry":"US"},"areaServed":[{"@type":"City","name":"Baltimore"},{"@type":"Country","name":"United States"}],"knowsAbout":["Web design","Website migrations","Website accessibility","Technology consulting","AI consulting"]}
</script>
'''
    return page("index.html", "Affordable Custom Website Design | Lickity Split Web Design",
                "Custom websites for authors, musicians, small businesses, and nonprofits. Based in Baltimore, serving clients nationwide. Starter sites from $300.", body, cur="home", ld=ld, scripts=EDJS)

# ---------- Portfolio ----------
CASES = [
 ("dcsocial", "Events, Ticketing, and Community",
  "DC Social Collective hosts social events for young adults around Washington, DC. Its website needed to handle upcoming events and ticketing while making several years of photographs, videos, and press coverage accessible.",
  ["I moved the organization from Squarespace to a custom website with individual event pages, ticketing links, directions, calendar integration, and inquiry forms for venues and sponsors.",
   "The archive now includes 43 photo galleries, more than 6,000 photographs, and 20 recap videos.",
   "Each new event can be added to the site and incorporated into the archive afterward."],
  ["43 galleries", "6,000+ photographs", "Live ticketing", "Venue and sponsor inquiries"], ""),
 ("larocca", "Composer and Music Publishing",
  "Composer Frank La Rocca needed a website that brought together his compositions, recordings, scores, and press coverage.",
  ["I organized his catalog of 59 works into individual pages, with recordings, score information, and program notes.",
   "The site also includes a discography, a press section, a downloadable press kit, and a custom visual mark based on musical material from the Miserere."],
  ["59 compositions", "Recordings and scores", "Discography", "Press kit"], ""),
 ("icjf", "Nonprofit and Research",
  "The International Catholic Jurists Forum needed a redesigned website that could accommodate its publications, conferences, documents, and years of accumulated news.",
  ["I rebuilt the website while migrating 99 pages and 535 news posts. The new site includes pages for the forum&rsquo;s books, conferences, and projects, along with embedded videos, downloadable documents, search functionality, and donation information.",
   "The redesign also preserves the existing content and important page addresses."],
  ["99 pages migrated", "535 news posts", "Site search", "Before-and-after redesign"], ""),
 ("adan", "Music and Performance",
  "A bilingual website for an organist, conductor, and music director, bringing together recordings, concerts, scholarship, and teaching.",
  ["The site includes English and Spanish content, recordings, a concert calendar, a press kit, photographs, and an interactive pipe organ on the homepage.",
   "It also provides a central place for presenters, parishes, and students to learn about his work."],
  ["English and Spanish", "Interactive pipe organ", "Recordings", "Concert calendar"], ""),
 ("roxane", "Writing and Publishing",
  "Roxane Salonen&rsquo;s writing was spread across a long-running blog, newspaper columns, and Substack. She needed a website that brought the material together without losing her existing archive.",
  ["I migrated more than 2,300 blog posts into a new author website with book information, writing archives, speaking information, and contact details.",
   "The site also includes an editor for new content and an automatic feed of recent Substack writing."],
  ["2,300+ posts migrated", "Author website", "Substack integration", "Content editor"], ""),
 ("brushsoul", "Art and E-commerce",
  "An online store for an artist selling original paintings and prints.",
  ["I set up and designed a Shopify storefront with individual product listings, galleries, and a way for prospective buyers to inquire about commissions.",
   "The design emphasizes the artwork itself and makes it easy to browse what is available."],
  ["Shopify storefront", "Original artwork", "Prints", "Commission inquiries"], ""),
 ("bruna", "Professional Services",
  "A Portuguese-language website, with an English toggle, for a psychologist in Maring&aacute;, Brazil, offering online therapy.",
  ["The website includes information about her practice, written reflections, frequently asked questions, a contact form, and a WhatsApp inquiry option.",
   "The design incorporates visual details connected to her existing identity."],
  ["Portuguese and English", "Reflections", "FAQ", "WhatsApp contact"], ""),
 ("llf", "Nonprofit and Publishing",
  "A website for a Catholic nonprofit working in Christian unity, religious liberty, and related areas of research and public engagement.",
  ["The site brings together the foundation&rsquo;s programs, publications, events, organizational information, and giving options.",
   "It also provides space for the foundation&rsquo;s continuing work as new projects and publications are introduced."],
  ["Programs", "Publications", "Events", "Donations"], "I founded the Likoudis Legacy Foundation, so this is my own organization&rsquo;s website."),
 ("traddyland", "Author and Book Launch",
  "A website for Lou Massett&rsquo;s memoir, with space for press coverage, speaking information, and a reader forum.",
  ["I moved the website from Wix, organized the press material, and brought over an existing forum containing approximately 20 essays and their comments."],
  ["Wix migration", "Book launch", "Press", "Reader forum"], ""),
 ("collin", "Music and Publishing",
  "A website for a Baltimore songwriter and producer, bringing together his recordings, record label, photographs, and press material.",
  ["The site includes a discography, an Arkansas House Records page, photographs, a notebook, a downloadable press kit, and booking information."],
  ["Discography", "Record label", "Photography", "Press kit"], ""),
 ("lapenna", "Author and Young Readers",
  "An author website for the LaRosa Sisters mystery series, including book information and school, library, and bookstore visit inquiries.",
  ["The site has every book in the series, a page for arranging school, library, and bookstore visits, creative writing workshops, and a contact form that goes straight to Michael."],
  ["Book series", "Author visits", "Workshops", "Content editor"], ""),
]

def media(pid):
    p = P[pid]; plain = html.escape(html.unescape(p["name"]))
    host = p["url"].split("//")[1].strip("/").replace("www.", "")
    if not p["before"]:
        return f'''<a class="shot" href="{p["url"]}" target="_blank" rel="noopener" aria-label="Visit the {plain} website"><img src="screenshots/{p["shot"]}" alt="{p["alt"]}" width="{p["w"]}" height="{p["h"]}" loading="lazy" decoding="async"></a>'''
    return f'''<div class="shot" data-ba style="--p:50%">
            <div class="ba-stage">
              <img src="screenshots/{p["shot"]}" alt="{p["alt"]} after the rebuild" width="{p["w"]}" height="{p["h"]}" loading="lazy" decoding="async">
              <div class="ba-before"><img src="screenshots/{p["before"]}" alt="{p["alt"]} before the rebuild" width="2560" height="1706" loading="lazy" decoding="async"></div>
              <span class="ba-tag ba-tag-b" aria-hidden="true">Before</span><span class="ba-tag ba-tag-a" aria-hidden="true">After</span>
              <div class="ba-handle" aria-hidden="true"><span></span></div>
              <input class="ba-range" type="range" min="0" max="100" value="50" step="1" aria-label="Compare {plain} before and after. Use the arrow keys or drag.">
            </div>
          </div>
          <p class="ba-help">Drag the handle, or use the arrow keys, to compare before and after.</p>
          <details class="ba-static"><summary>Show both versions side by side</summary>
            <div class="ba-pair">
              <figure><img src="screenshots/{p["before"]}" alt="{p["alt"]} before the rebuild" width="2560" height="1706" loading="lazy"><figcaption>Before</figcaption></figure>
              <figure><img src="screenshots/{p["shot"]}" alt="{p["alt"]} after the rebuild" width="{p["w"]}" height="{p["h"]}" loading="lazy"><figcaption>After</figcaption></figure>
            </div>
          </details>'''

def project(pid, cat, intro, built, facts, note):
    p = P[pid]
    q = ""
    if p["quote"]:
        who = p["attrib"].replace(" &middot; ", ", ", 1)
        q = f'\n          <blockquote>{p["quote"]}</blockquote>\n          <p class="by">{who}</p>'
    nt = f'\n          <p class="note">{note}</p>' if note else ""
    return f'''      <article class="project" id="{pid}">
        <div class="media">
          {media(pid)}
        </div>
        <div>
          <p class="label">{cat}</p>
          <h2>{p["name"]}</h2>
          <p class="intro">{intro}</p>{nt}
          <div class="built"><h3>What I built</h3>{"".join(f"<p>{x}</p>" for x in built)}</div>
          <ul class="facts-row">{"".join(f"<li>{x}</li>" for x in facts)}</ul>{q}
          <div class="proj-actions">{f'<a class="btn btn-primary" href="{CASEURL[pid]}">Read the Case Study</a>' if pid in CASEURL else ""}<a class="btn btn-ghost" href="{p["url"]}" target="_blank" rel="noopener">Visit Website</a></div>
        </div>
      </article>'''

def mini(img, w, h, name, desc, href, label, tag=""):
    t = f'<span class="tag">{tag}</span>' if tag else ""
    return f'''        <article class="proj">
          <a class="proj-shot" href="{href}" target="_blank" rel="noopener" tabindex="-1" aria-hidden="true"><img src="screenshots/{img}" alt="" width="{w}" height="{h}" loading="lazy" decoding="async"></a>
          {t}<h3>{name}</h3>
          <p class="desc">{desc}</p>
          <a class="tlink" href="{href}" target="_blank" rel="noopener" aria-label="{label}, {html.escape(html.unescape(name))}">{label}</a>
        </article>'''

CUF = "https://liquid1188.github.io/cuf-redesign-concept/"

GROUPS = [("music-arts", "Music and the arts", "Composers, performers, songwriters, and artists.", ["larocca", "adan", "collin", "brushsoul"]),
          ("organizations", "Organizations and events", "Nonprofits, research institutes, and an events company.", ["icjf", "dcsocial", "llf"]),
          ("authors", "Authors and writers", "Writers with books to launch, archives to keep, and readers to reach.", ["roxane", "traddyland", "lapenna"]),
          ("professional", "Professional services", "Independent professionals who need a clear, trustworthy first impression.", ["bruna"])]

def work():
    C = {c[0]: c for c in CASES}
    jump = '<nav class="jump" aria-label="Project types">' + "".join(f'<a href="work#{g}">{h}</a>' for g, h, _, _ in GROUPS) + '</nav>'
    secs = []
    for i, (g, h, d, ids) in enumerate(GROUPS):
        secs.append(f'''  <section class="sec work-group{" sec-stone" if i % 2 else ""}" id="{g}">
    <div class="wrap">
      <div class="sec-head group-head"><h2>{h}</h2><p>{d}</p></div>
{chr(10).join(project(*C[x]) for x in ids)}
    </div>
  </section>''')
    body = f'''{hero("Selected projects", ["I&rsquo;ve built websites for authors, musicians, artists, businesses, and nonprofit organizations. Some projects began with a simple idea. Others involved redesigning an existing website or moving a substantial archive.", "The work is grouped by the kind of client. Four projects have full case studies."], jump)}

{chr(10).join(secs)}

  <section class="sec" id="smaller-projects">
    <div class="wrap">
      <div class="sec-head"><h2>Smaller projects</h2></div>
      <div class="mini-grid">
{mini("andrew.webp", 1280, 853, "Andrew Likoudis", "An author and speaker website bringing together books, essays, media appearances, and speaking information.", "https://andrewlikoudis.com/", "Visit Website")}
{mini("cuf.webp", 1280, 853, "Catholics United for the Faith", "An independent redesign concept for a Catholic apologetics organization, emphasizing publications and archived material. This was not commissioned client work.", CUF, "View Concept", "Redesign concept")}
      </div>
    </div>
  </section>

  <section class="sec sec-stone">
    <div class="wrap">
      <div class="sec-head"><h2>More of my work</h2><p>The gallery includes additional websites and smaller projects, including author sites, music portfolios, online stores, and nonprofit websites.</p></div>
      <a class="btn btn-ghost" href="gallery">View Full Gallery</a>
    </div>
  </section>

{cta()}'''
    return page("work.html", "Web Design Portfolio and Client Projects | Lickity Split",
                "Explore custom websites for authors, musicians, businesses, and nonprofits, including archives, online stores, and event platforms.", body, cur="work", scripts=BAJS)

def gallery():
    G = [("dcsocial", "Events, ticketing, venue information, and an archive of photo galleries and videos."),
         ("larocca", "A searchable catalog of 59 compositions, with scores, recordings, and press information."),
         ("icjf", "A nonprofit redesign with 99 pages and 535 news posts migrated into a searchable website."),
         ("bruna", "A Portuguese-language website, with an English toggle, for a psychology practice in Brazil."),
         ("adan", "A bilingual musician&rsquo;s website with recordings, a concert calendar, and an interactive pipe organ."),
         ("lapenna", "An author website featuring the LaRosa Sisters mystery series and visit inquiries."),
         ("traddyland", "A memoir website with press coverage, speaking information, and a migrated forum."),
         ("brushsoul", "A Shopify store for original paintings, prints, and commissions."),
         ("llf", "A nonprofit website with programs, publications, events, and giving options."),
         ("roxane", "An author website with more than 2,300 migrated blog posts."),
         ("collin", "A musician&rsquo;s website with recordings, a discography, and press materials.")]
    items = []
    for pid, d in G:
        p = P[pid]
        items.append(mini(p["shot"], p["w"], p["h"], p["name"], d, p["url"], "Visit Website"))
    items.append(mini("andrew.webp", 1280, 853, "Andrew Likoudis", "An author website with books, essays, speaking information, and media appearances.", "https://andrewlikoudis.com/", "Visit Website"))
    items.append(mini("cuf.webp", 1280, 853, "Catholics United for the Faith", "An independent redesign concept focused on publications and archives.", CUF, "View Concept", "Redesign concept"))
    body = f'''{hero("More websites I&rsquo;ve built", ["A broader selection of websites for authors, artists, musicians, businesses, and organizations. Open a project to see the finished site.", "The gallery also includes one independent redesign concept, identified separately from commissioned work."])}

  <section class="sec">
    <div class="wrap">
      <div class="gal-grid">
{chr(10).join(items)}
      </div>
    </div>
  </section>

{cta()}'''
    return page("gallery.html", "Website Gallery | Lickity Split Web Design",
                "Browse websites built for authors, artists, musicians, businesses, and nonprofit organizations.", body, cur="gallery")
