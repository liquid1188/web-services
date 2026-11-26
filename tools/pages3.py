from core import *
from pages2 import faq_block

def sec(inner, stone=False, ident=""):
    i = f' id="{ident}"' if ident else ""
    return f'''  <section class="sec{" sec-stone" if stone else ""}"{i}>
    <div class="wrap">
{inner}
    </div>
  </section>'''

def prose(h, paras, items=None, level=2):
    lis = ul(items) if items else ""
    return f'<div class="prose"><h{level}>{h}</h{level}>' + "".join(f"<p>{p}</p>" for p in paras) + lis + "</div>"

def examples(ids_with_copy, heading="Examples"):
    cards = "\n".join(card(pid, cat, d) for pid, cat, d in ids_with_copy)
    return f'''      <div class="sec-head"><h2>{heading}</h2></div>
      <div class="ex-grid">
{cards}
      </div>'''

def price_block(paras, h="What does it cost?", btn="Get an Estimate"):
    return f'''      <div class="prose"><h2>{h}</h2>{"".join(f"<p>{p}</p>" for p in paras)}<p style="margin-top:1.6rem"><a class="btn btn-primary" href="contact">{btn}</a> &nbsp; <a class="tlink" href="pricing">View Pricing</a></p></div>'''

def cols(items, n=3, link=False):
    out = []
    for it in items:
        h, ps = it[0], it[1]
        out.append(f'<div class="col"><h3>{h}</h3>' + "".join(f"<p>{p}</p>" for p in ps) + "</div>")
    return f'<div class="cols{n}">' + "".join(out) + "</div>"

def tech():
    services = [("Technology Reviews", ["I&rsquo;ll look at the software, subscriptions, accounts, and other tools your organization uses, identify what is working and what isn&rsquo;t, and recommend what to keep, change, or eliminate."]),
                ("Email and Workspace Setup", ["Help with Google Workspace, Microsoft 365, calendars, shared files, permissions, and email accounts."]),
                ("Automation", ["Connecting forms, spreadsheets, calendars, newsletters, and other services to reduce repeated administrative work."]),
                ("AI Consulting and Training", ["Help choosing AI tools, configuring them for useful tasks, and understanding their limitations."]),
                ("Website and Content Migrations", ["Moving websites, archives, files, and other material between platforms."]),
                ("Basic Security Setup", ["Assistance with password managers, two-factor authentication, backups, and account security.", "This is practical setup assistance rather than a substitute for a specialized cybersecurity assessment."])]
    ai = [("AI Setup", ["Choosing and configuring an assistant for a particular person or organization."]),
          ("Workflow Review", ["Looking at repeated tasks and determining whether AI or ordinary automation could make them easier."]),
          ("Supervised Automation", ["Setting up a limited process with clear permissions, human review, and a way to stop or change it."]),
          ("Staff Training", ["Working through actual tasks with staff, including where the tools perform well and where they need checking."]),
          ("AI Guidelines", ["Helping draft straightforward policies on approved tools, confidential information, and human oversight."])]
    recent = [("Moving client forms to a new service", ["When the form service behind my clients&rsquo; contact forms announced it was shutting down in 2026, I set up a replacement, Web3Forms, with a separate key for each client tied to their own email, so their messages never pass through my accounts."]),
              ("An upload page for an events company", ["DC Social Collective adds each event&rsquo;s photos and video from one page. The original files are stored at full quality, and the site builds the album and download links on its own."]),
              ("New writing that appears on its own", ["Roxane Salonen publishes on Substack, and her newest posts appear on her website automatically, so she only has to post once."]),
              ("Moving a domain without moving the owner", ["For Frank La Rocca, I moved his website to new hosting and sorted out conflicting settings from an old provider, while his domain stayed registered in his own name."])]
    arts = [            ("Leo XIV Issues First Encyclical, Calling AI a &lsquo;Change of Epoch&rsquo; for the Human Person", "Where Peter Is, May 2026", "https://wherepeteris.com/leo-xiv-issues-first-encyclical-calling-ai-a-change-of-epoch-for-the-human-person/"),
            ("&lsquo;Neuralink&rsquo; vs. Imago Dei: Catholic Anthropology and AI", "National Catholic Register, September 2025", "https://www.ncregister.com/news/neuralink-vs-imago-dei"),
            ("Smart Glasses Offer a Glimpse of the Future, But the Church Sees More Clearly", "National Catholic Register, August 2025", "https://www.ncregister.com/news/smart-glasses-offer-a-glimpse-of-the-future-but-the-church-sees-more-clearly")]
    body = f'''{hero("Technology help for small organizations", ["I help small businesses, nonprofits, and offices get more out of the technology they already use.", "That might mean sorting out email accounts and shared files, connecting different services, setting up an AI assistant, or figuring out why a particular system has become difficult to manage.", "I can review what you have, recommend changes, and help put them into practice."], '<a class="btn btn-primary" href="contact">Discuss a Project</a><a class="btn btn-ghost" href="#services">See Services</a>')}

{sec('<div class="sec-head"><h2>What I can help with</h2></div>' + cols(services), ident="services")}

{sec(prose("Using AI at work", ["AI tools can be useful for drafting, research, organizing information, and routine administrative tasks. They can also introduce mistakes, privacy concerns, and extra work when they&rsquo;re set up badly.", "I help organizations decide where these tools might be useful, what information they should have access to, and how their work should be checked.", "Sometimes the best recommendation is not to automate something at all."]) + '<div style="margin-top:2.5rem">' + cols(ai) + '</div>', stone=True, ident="ai-consulting")}

{sec('<div class="two"><div class="prose" id="ai-setup"><h2>AI Setup and Training</h2><p class="price-tag">$200</p><p>If you&rsquo;ve been experimenting with ChatGPT, Claude, or another AI assistant but aren&rsquo;t sure how to make it useful for your work, I can help.</p><p>We&rsquo;ll choose or configure one assistant, go through its settings, and work through a few tasks you regularly handle.</p><p>I&rsquo;ll also explain where the tool is likely to make mistakes and what information you should avoid sharing.</p><p>The goal is that you&rsquo;ll know how to use it independently by the time we&rsquo;re finished.</p><p style="margin-top:1.5rem"><a class="btn btn-primary" href="contact">Ask About AI Setup</a></p></div>'
     '<div class="prose"><h2>Defined engagements</h2><p>Each engagement has a set starting price, so you know the cost before we begin.</p><dl class="defs" style="margin-top:1rem"><div><dt>Initial consultation</dt><dd>$75 for up to one hour</dd></div><div><dt>Technology assessment</dt><dd>From $150. A review of your accounts, tools, and subscriptions, with written recommendations.</dd></div><div><dt>AI setup and individual training</dt><dd>$200</dd></div><div><dt>Email and workspace setup</dt><dd>From $250</dd></div><div><dt>Small-team AI workshop</dt><dd>From $350</dd></div><div><dt>Workflow automation</dt><dd>From $400</dd></div><div><dt>Larger technology projects</dt><dd>Written fixed-price estimate</dd></div><div><dt>Additional consulting</dt><dd>$65&ndash;$85 per hour</dd></div></dl></div></div>')}

{sec('<div class="sec-head"><h2>What the research says about AI</h2><p>Small organizations are adopting AI, but many are still figuring out how to use it effectively.</p></div>'
     '<div class="cols2">'
     '<div class="col"><h3>Nearly 70% say they need more training</h3><p>Thryv&rsquo;s 2026 survey found that nearly seven in ten small-business owners felt they needed additional AI skills or training.</p><p>Rather than introducing a collection of new tools, I prefer to begin with the tasks and services a client already uses.</p><p class="src"><a href="https://www.thryv.com/blog/ai-for-small-business-2026-report/" target="_blank" rel="noopener">Thryv, 2026</a></p></div>'
     '<div class="col"><h3>Workflow changes matter</h3><p>McKinsey&rsquo;s 2026 State of AI survey found that nearly three-quarters of its highest-performing AI adopters had fundamentally redesigned workflows, compared with approximately one-quarter of other respondents. The survey includes large organizations and is not research exclusively about small businesses.</p><p>For my clients, the practical question is usually simpler. What task is taking too much time, and is AI actually the right way to improve it?</p><p class="src"><a href="https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai" target="_blank" rel="noopener">McKinsey, 2026</a></p></div>'
     '</div>', stone=True)}

{sec(prose("Tools and platforms", ["I work with Google Workspace, Microsoft 365, Claude, ChatGPT, GitHub, Cloudflare, WordPress, Substack, Mailchimp, and other commonly used tools.", "If you&rsquo;re already using a particular service, I&rsquo;ll start by looking at what it can do before recommending a replacement."])
     + '<div class="faq" style="margin-top:2rem"><details><summary>Technical capabilities</summary><div class="ans"><p><strong>AI assistants and agents.</strong> Claude and Claude Code, OpenAI Codex, Meta Muse, OpenClaw, NanoClaw.</p><p><strong>Web and infrastructure.</strong> HTML and CSS, static site builds, GitHub, Bash, DigitalOcean cloud servers, Cloudflare DNS and email routing, SSL, OCR text processing, automated content pipelines, automated testing and deployment (CI/CD).</p><p><strong>Platforms.</strong> Google Workspace, Microsoft 365, Salesforce, Mailchimp, WordPress, Substack, Resend, Canva, Basecamp.</p></div></details></div>')}

{sec('<div class="sec-head"><h2>Examples of the work</h2></div>' + cols(recent, 2), stone=True)}

{sec('<div class="sec-head"><h2>Writing about technology</h2><p>I also write about the social, cultural, and ethical questions raised by new technology, including artificial intelligence.</p></div><ul class="articles">' + "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{t}</a><span>{pub}</span></li>' for t, pub, u in arts) + '</ul>'
     '<p class="center-note" style="margin-top:2.5rem">Setting up a vendor record? Business registration details are on the <a href="vendor-information">Vendor Information</a> page.</p>')}

{cta("Need help sorting out your technology?", "Tell me what you&rsquo;re using and where you&rsquo;re running into difficulties. I&rsquo;ll let you know whether I can help and what the work would involve.", "Discuss a Project")}'''
    return page("technology-consulting.html", "Technology and AI Consulting for Small Organizations",
                "Practical help with AI assistants, email, shared files, automation, and technology setup for small businesses and nonprofits.", body, cur="tech")

def vendor():
    rows = [("Legal name", "Likoudis Legacy LLC"), ("Doing business as", "Likoudis Ventures"), ("Brand", "Lickity Split Web Design"),
            ("Business type", "Small business, Maryland limited liability company"), ("Primary NAICS", "541512 Computer Systems Design Services"),
            ("Other NAICS", "541511 Custom Computer Programming Services<br>541519 Other Computer Related Services<br>541613 Marketing Consulting Services<br>611430 Professional and Management Development Training"),
            ("Registrations", "SAM.gov and eMMA registration in progress"), ("Contact", 'Andrew Likoudis, Principal<br><a href="mailto:hello@lickitysplitweb.com">hello@lickitysplitweb.com</a>'),
            ("Capability statement", 'A one-page capability statement is available on request by <a href="mailto:hello@lickitysplitweb.com">email</a>.')]
    body = f'''{hero("Vendor Information", ["For organizations that need business registration details to set up a vendor record, the information is available below."])}

{sec('<dl class="defs">' + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in rows) + '</dl><p class="center-note" style="margin-top:2rem">Codes are from the North American Industry Classification System.</p>')}

{cta("Need help sorting out your technology?", "Tell me what you&rsquo;re using and where you&rsquo;re running into difficulties. I&rsquo;ll let you know whether I can help and what the work would involve.", "Discuss a Project")}'''
    return page("vendor-information.html", "Vendor Information | Lickity Split Web Design", "Business registration details for organizations setting up a vendor record with Lickity Split Web Design.", body, cur="tech")

def website_design():
    kinds = [("Author Websites", ["Book pages, article archives, press kits, and speaking inquiries."], "author-website-design"),
             ("Musician &amp; Composer Websites", ["Recordings, works catalogs, scores, performances, and booking."], "composer-musician-websites"),
             ("Parish &amp; Ministry Websites", ["Schedules, bulletins, programs, publications, and giving."], "parish-ministry-websites"),
             ("Website Migrations", ["Moving an existing site from Wix, Squarespace, or an older blogging platform."], "wix-to-custom-website")]
    kcols = '<div class="cols2">' + "".join(f'<div class="col"><h3>{h}</h3><p>{p[0]}</p><a class="tlink" href="{u}">{h}</a></div>' for h, p, u in kinds) + '</div>'
    tiers = '<div class="cols3"><div class="col"><h3>Starter Site</h3><p class="price-tag">$300&ndash;$500</p><p>A single page or a few simple pages for a professional online presence.</p></div><div class="col"><h3>Custom Website</h3><p class="price-tag">$500&ndash;$1,200</p><p>A more complete website designed around your work. Most projects fall here.</p></div><div class="col"><h3>Full Build</h3><p class="price-tag">$1,200&ndash;$2,500+</p><p>Larger websites with archives, catalogs, event systems, or online stores.</p></div></div><div class="sec-foot"><a class="btn btn-ghost" href="pricing">View Pricing</a></div>'
    body = f'''{hero("Website design", ["New websites for writers, artists, businesses, and organizations. I can handle a straightforward professional site or something larger with publications, archives, or other features.", "I handle the design, development, and launch myself. I also help with the writing, which can be just as important as getting the technical details right."], '<a class="btn btn-primary" href="work">View My Work</a><a class="btn btn-ghost" href="contact">Get an Estimate</a>')}

{sec('<div class="sec-head"><h2>What does a website cost?</h2><p>A simple starter website costs $300 to $500. Most custom websites cost between $500 and $1,200, while larger projects with archives, event systems, or other features start at $1,200 and are priced by scope.</p></div>' + tiers)}

{sec('<div class="sec-head"><h2>Websites for particular kinds of work</h2></div>' + kcols, stone=True)}

{sec(examples([("dcsocial", "Events and Community", "Live ticketing, venue information, and an archive of more than 6,000 photographs from past events."), ("icjf", "Nonprofit and Publishing", "A redesign that brought over 99 pages and 535 news posts."), ("brushsoul", "Art and E-commerce", "A Shopify store for original paintings, prints, and commissions.")], "Recent work"))}

{sec('<div class="sec-head"><h2>How we get started</h2></div>' + steps(), stone=True)}

{cta()}'''
    return page("website-design.html", "Custom Website Design | Lickity Split Web Design",
                "Custom website design for writers, artists, businesses, and organizations, from simple professional sites to larger projects with archives and other features.", body, cur="website-design")

def author():
    body = f'''{hero("Author websites", ["An author website should make it easy to find your books, read your work, and get in touch.", "I build sites for writers who need a professional home for their publications, whether they&rsquo;re launching a first book or bringing years of writing together in one place."])}

{sec('<div class="two">' + prose("What I can build", [], ["Individual book pages with covers, descriptions, and purchase links", "Bibliographies and article archives", "Press kits with biographies, photographs, and media information", "Speaking and interview inquiries", "Newsletter subscriptions", "Blog integrations", "An editor for routine updates"])
     + prose("A website that fits your writing", ["A novelist promoting a new series needs a different website from an academic writer with decades of essays, lectures, and publications.", "I can build book pages, bibliographies, press kits, speaking information, and archives, with a design suited to the author&rsquo;s work.", "Sometimes that means starting with a single book and adding to the site over time. Other projects begin with hundreds or thousands of articles that need to be organized and made searchable."]) + '</div>')}

{sec('<div class="two">' + prose("Have a publication date coming up?", ["If you&rsquo;re preparing for a book launch, I can begin with a simple page containing the cover, description, purchase links, and author information.", "We can add the rest of the website afterward.", "A small launch page can often be completed within about 48 hours once I have the material."])
     + prose("Help with the writing, too", ["I&rsquo;m an editor as well as a web designer, so I can help with biographies, book descriptions, introductions, and the other text that needs to go on the site.", "You don&rsquo;t have to prepare perfectly finished copy before getting in touch."]) + '</div>', stone=True)}

{sec(examples([("roxane", "Writing and Publishing", "An author website with more than 2,300 migrated blog posts."), ("traddyland", "Author and Book Launch", "A memoir website with press coverage, speaking information, and a migrated forum."), ("lapenna", "Author and Young Readers", "An author website featuring the LaRosa Sisters mystery series and visit inquiries.")]))}

{sec(price_block(["Most author websites cost between $500 and $1,200.", "A simple book-launch site may cost less, while larger archives or additional features may cost more.", "I&rsquo;ll give you an estimate after reviewing what you need."]), stone=True)}

{cta()}'''
    return page("author-website-design.html", "Author Website Design from $300 | Lickity Split",
                "Websites for authors, speakers, and writers, including book pages, press kits, article archives, and newsletter integrations.", body, cur="author")

def music():
    body = f'''{hero("Websites for musicians and composers", ["Your website might need a place for recordings and upcoming performances, or it might need a catalog of compositions, scores, and program notes.", "I build both, and I can help with press materials, booking forms, streaming links, and other information that performers, presenters, and listeners need."])}

{sec('<div class="two">' + prose("What your website can include", [], ["Recordings and embedded music players", "A discography", "A searchable works catalog", "Score previews and program notes", "Performances and upcoming events", "Press information", "Booking forms", "Links to streaming and purchasing platforms"])
     + '<div class="stack" style="--s5:2.5rem">' + prose("Organizing the music", ["For composer Frank La Rocca, I built a catalog of 59 compositions with scores, recordings, and individual work pages.", "Other musicians may need a simpler website focused on releases, performances, or booking.", "I&rsquo;ll help determine what belongs on the site and how to make it easy to navigate."])
     + prose("Adding new music", ["Custom Websites and Full Builds include an editor for routine updates, so you can add recordings, change dates, and update your catalog without having to contact me every time."]) + '</div></div>')}

{sec(examples([("larocca", "Composer and Music Publishing", "A catalog of 59 compositions, with scores, recordings, and press information."), ("adan", "Music and Performance", "A bilingual website with recordings, a concert calendar, and an interactive pipe organ."), ("collin", "Music and Publishing", "A musician&rsquo;s website with recordings, a discography, and press materials.")]), stone=True)}

{sec(price_block(["Most musician websites cost between $500 and $1,200.", "Larger composer catalogs and projects with more involved features start at $1,200 and are priced by scope."]))}

{cta()}'''
    return page("composer-musician-websites.html", "Musician and Composer Website Design | Lickity Split",
                "Custom websites for musicians and composers, with recordings, catalogs, scores, performance dates, and press kits.", body, cur="music")

def parish():
    body = f'''{hero("Websites for parishes and Catholic organizations", ["A parish website needs to make the essentials easy to find.", "Mass and confession times, bulletins, office information, sacramental preparation, events, and online giving should all be accessible without having to search through several menus.", "I also build websites for apostolates, Catholic nonprofits, and research organizations that need space for publications, programs, events, or fundraising."])}

{sec('<div class="two">' + prose("What I can include", [], ["Mass, confession, and adoration schedules", "Clergy and staff information", "Ministries and programs", "Bulletins and homily archives", "Giving and registration links", "Publications and newsletters", "Forms and contact information", "An editor for routine updates"])
     + '<div class="stack" style="--s5:2.5rem">' + prose("A website your staff can maintain", ["Parish offices are busy, and the person updating the website may change from one year to the next.", "I provide an editor for routine changes and explain how to use it before the site launches.", "I can also handle updates when the parish would rather have me do them."])
     + prose("For institutes and apostolates", ["Organizations with a larger body of work may need a publication archive, conference registration, a journal, or separate pages for their programs and initiatives.", "I&rsquo;ve built and maintained a nonprofit website of this kind through my own work with the Likoudis Legacy Foundation.", "The structure can be adapted to the organization&rsquo;s needs rather than requiring every ministry to fit into the same standard parish layout."]) + '</div></div>')}

{sec(examples([("llf", "Nonprofit and Publishing", "A nonprofit website with programs, publications, events, and giving options."), ("icjf", "Nonprofit and Research", "A redesign with 99 pages and 535 news posts migrated into a searchable website.")]) + '<p class="center-note" style="margin-top:2rem">For an events-oriented organization that is not a parish or ministry, see <a href="work#dcsocial">DC Social Collective</a>.</p>', stone=True)}

{sec(price_block(["Most parish and ministry websites cost between $500 and $1,200.", "Larger organizational websites with extensive archives, event registration, or more complex requirements are quoted according to scope."]))}

{cta()}'''
    return page("parish-ministry-websites.html", "Catholic Parish and Ministry Website Design | Lickity Split",
                "Affordable websites for parishes, ministries, and Catholic nonprofits, with schedules, bulletins, events, publications, and giving.", body, cur="parish")

def migrate():
    proc = [("Pages and photographs", ["I&rsquo;ll review the existing website and bring over the material you want to keep."]),
            ("Blogs and archives", ["Posts and other material can often be transferred programmatically, which is especially useful for larger archives."]),
            ("Domains and email", ["I&rsquo;ll review the domain and email setup before launch and plan the switch to minimize disruption."]),
            ("Search visibility", ["I&rsquo;ll preserve existing page addresses where possible and set up redirects when pages move.", "These measures help reduce unnecessary disruption, although search rankings can fluctuate after a migration."])]
    faq = [("Will I lose my Google rankings?", ["A migration can affect search rankings, even when it&rsquo;s handled carefully.", "I preserve existing page addresses where possible, set up appropriate redirects, and check the site after launch.", "These steps help reduce avoidable disruption, although no one can guarantee that rankings will remain unchanged."]),
           ("What happens to my domain and email?", ["Your domain remains yours.", "I&rsquo;ll review the existing domain and email records before making changes and plan the transfer to minimize the risk of interruption."]),
           ("Can you move a large blog?", ["Yes. I&rsquo;ve handled archives containing thousands of posts.", "I&rsquo;ll review the current platform and content before giving you an estimate."]),
           ("How long does a migration take?", ["A straightforward migration may take about a week. Larger archives and more complex websites take longer.", "I&rsquo;ll provide a timeline with the estimate."])]
    ex = '<div class="sec-head"><h2>Examples</h2></div><div class="gal-grid">' + "\n".join([
        card("traddyland", "Moved from Wix", "An author website moved from Wix, including press coverage and the existing reader forum."),
        card("dcsocial", "Moved from Squarespace", "An events website moved from Squarespace, bringing together years of photographs, videos, and event information."),
        card("roxane", "Blog archive", "More than 2,300 blog posts moved into a new author website."),
        card("icjf", "Redesign", "A redesign that brought over 99 pages and 535 news posts while preserving the site&rsquo;s accumulated material.")]) + '</div>'
    body = f'''{hero("Ready to move your website?", ["If your current website has become difficult to update, expensive to maintain, or no longer suits what you&rsquo;re doing, I can help you move it.", "I&rsquo;ve rebuilt sites from Wix and Squarespace and migrated large archives from older blogging platforms.", "I can bring over existing text, photographs, articles, and other material while redesigning the site."])}

{sec(prose("Should you move?", ["Not necessarily.", "Wix, Squarespace, and WordPress can be perfectly good choices, especially for people who want to manage a straightforward website themselves.", "But if you&rsquo;re paying for features you don&rsquo;t use, finding the editor difficult to work with, or trying to organize a large amount of material, it may be worth considering another approach.", "I can review your current site and tell you whether I think rebuilding it makes sense."]))}

{sec('<div class="sec-head"><h2>What happens to your existing material?</h2></div>' + cols(proc, 2), stone=True)}

{sec(ex)}

{sec(price_block(["I don&rsquo;t add a separate migration surcharge.", "The work is included in the website estimate, which depends on the size of the existing site and the amount of material that needs to be transferred.", "Most migrations fall within the Custom Website or Full Build ranges."], h="What does a migration cost?"), stone=True)}

{sec('<div class="sec-head"><h2>Common questions</h2></div>' + faq_block(faq, "migration-faq"))}

{cta()}'''
    return page("wix-to-custom-website.html", "Wix and Squarespace Website Migrations | Lickity Split",
                "Move an existing website from Wix, Squarespace, or WordPress, including pages, images, articles, and archives.", body, cur="migrate")

def resources():
    def res(src, title, ps, url):
        return f'<div class="res"><p class="label">{src}</p><h3>{title}</h3>' + "".join(f"<p>{p}</p>" for p in ps) + f'<a class="tlink" href="{url}" target="_blank" rel="noopener">{url.split("//")[1].split("/")[0].replace("www.", "")}</a></div>'
    def group(h, items): return f'<div class="res-group"><h2>{h}</h2><div class="res-list">{"".join(items)}</div></div>'
    G = [
     group("Website performance", [
        res("Portent, 2022", "Site Speed Is (Still) Impacting Your Conversion Rate", ["Portent analyzed more than 100 million page views across 20 websites and found a substantial relationship between loading speed and conversions.", "In its B2B sample, pages loading in one second had three times the conversion rate of pages loading in five seconds.", "That&rsquo;s a useful reason to take performance seriously, although it doesn&rsquo;t mean that speeding up an individual website will automatically triple its sales."], "https://portent.com/blog/analytics/research-site-speed-hurting-everyones-revenue.htm"),
        res("Google", "Core Web Vitals", ["Google&rsquo;s framework for measuring loading performance, responsiveness, and visual stability.", "Its recommended thresholds provide useful benchmarks for testing how a website performs for real visitors."], "https://web.dev/articles/vitals"),
        res("Nielsen Norman Group", "The Need for Speed, 23 Years Later", ["A review of research into response times, loading delays, and the way waiting affects the experience of using a website."], "https://www.nngroup.com/articles/the-need-for-speed/")]),
     group("Accessibility and usability", [
        res("WebAIM, 2026", "The WebAIM Million", ["WebAIM&rsquo;s annual analysis of one million homepages found automatically detectable accessibility failures on 95.9% of them.", "Common problems include insufficient color contrast, missing alternative text, and improperly labeled forms.", "Automated testing cannot establish whether an entire website is accessible, but it is useful for identifying common problems."], "https://webaim.org/projects/million/"),
        res("Stanford", "Guidelines for Web Credibility", ["Stanford&rsquo;s guidelines are older, but much of the advice remains useful, particularly around clear contact information, professional presentation, and making claims that visitors can verify."], "https://credibility.stanford.edu/guidelines/index.html"),
        res("Nielsen Norman Group", "How Users Read on the Web", ["A foundational article about the way visitors scan web pages and use headings and other visual cues to find information."], "https://www.nngroup.com/articles/how-users-read-on-the-web/"),
        res("Nielsen Norman Group", "10 Usability Heuristics for User Interface Design", ["Practical principles for making interfaces understandable, consistent, and easier to use."], "https://www.nngroup.com/articles/ten-usability-heuristics/")]),
     group("Local search", [
        res("Google and Purchased, 2016", "How Mobile Search Connects Consumers to Stores", ["In this 2016 study, 76% of people who searched on a smartphone for something nearby visited a business within a day, and 28% of those searches ended in a purchase.", "The study is now a decade old, so the exact figures are best read as a snapshot of that time."], "https://www.thinkwithgoogle.com/_qs/documents/620/mobile-search-trends-consumers-to-stores.pdf")]),
     group("Websites for authors", [
        res("Jane Friedman", "How to Build an Author Website", ["A practical guide to the pages and information writers may need, including biographies, books, and contact information."], "https://www.janefriedman.com/author-websites/")]),
     group("Useful website tools", [
        res("Google", "PageSpeed Insights", ["Test loading performance and identify technical improvements."], "https://pagespeed.web.dev/"),
        res("Google", "Search Console", ["See how Google indexes your website and which searches bring visitors to it."], "https://search.google.com/search-console/"),
        res("Google Search Central", "SEO Starter Guide", ["Google&rsquo;s introduction to making websites understandable to search engines."], "https://developers.google.com/search/docs/fundamentals/seo-starter-guide"),
        res("Google Chrome Labs", "Squoosh", ["A browser-based tool for optimizing photographs and other images before adding them to a website."], "https://squoosh.app/")]),
     group("Website migrations", [
        res("Google Search Central", "Site Moves and Migrations", ["Guidance on moving websites, preserving useful page addresses, and setting up redirects."], "https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes")]),
     group("AI for small organizations", [
        res("Thryv, 2026", "AI &amp; Small Business Adoption Report", ["A survey of AI adoption among small businesses, including the additional training many business owners say they need."], "https://www.thryv.com/blog/ai-for-small-business-2026-report/"),
        res("McKinsey, 2026", "The State of AI in 2026", ["Research on AI adoption, workflow redesign, management practices, and the challenges of putting AI to work across organizations."], "https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai")]),
    ]
    body = f'''{hero("Resources", ["A selection of studies, guides, and tools I&rsquo;ve found useful in designing and maintaining websites.", "Some are research reports. Others are practical guides for understanding website performance, accessibility, publishing, and search engines."])}

{sec(chr(10).join(G))}

{cta("Need help with any of this?", "If you&rsquo;re planning a website or trying to improve an existing one, feel free to get in touch. I can review what you have and suggest where to start.")}'''
    return page("resources.html", "Website Design and Technology Resources | Lickity Split",
                "Research, tools, and practical guidance on website performance, accessibility, usability, SEO, migrations, and AI.", body, cur="resources")

def build(): return [tech(), vendor(), website_design(), author(), music(), parish(), migrate(), resources()]
