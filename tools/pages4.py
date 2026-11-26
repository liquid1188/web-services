"""Case study pages (projects/*) and the publisher and nonprofit service pages."""
from core import *
from pages3 import sec, prose, examples, price_block

CASE = {
 "dcsocial": dict(
   slug="dc-social-collective", kind="Events, ticketing, and community",
   title="DC Social Collective Website Case Study",
   lede="A website for a young-adult events company in Washington, DC, built to sell the next night and keep every night before it.",
   facts=["Moved from Squarespace", "43 photo albums", "More than 6,000 photographs", "Live ticketing", "Self-serve uploads"],
   brief=["DC Social Collective hosts nights out for young adults around Washington, DC, with dance lessons, live bands, and a few hundred guests. The website has two jobs. It has to sell tickets for the next event, and it has to hold years of photographs and videos from the events before it.",
          "Chris Byrne, the founder, also needed to run it himself, adding a new night with its photos and video without calling anyone for help."],
   built=[("Event pages that sell the night", "Each event gets its own page with the flyer shown whole, the venue, directions, and a ticket link. Upcoming nights lead the homepage."),
          ("An archive kept at full quality", "All 43 photo albums are hosted on the new site. Pages load fast web copies, and each photograph can be downloaded one at a time at the photographer&rsquo;s original quality. Whole albums can&rsquo;t be downloaded, by design."),
          ("Video in high resolution", "Recap videos from past nights play on the site from the highest-quality files available, up to 4K."),
          ("The mailing list stayed in one place", "The signup form on the new site feeds the email list Chris already used, so nothing had to be moved or kept in two places.")],
   editor=["Chris adds a night from a single upload page. He enters the name, date, and venue, drops in the photographer&rsquo;s folder and the video, and the site builds the album, the web copies, and the download links.",
           "Events and albums can be saved as drafts. The homepage, sponsors, partners, and team are all editable from the same login."],
   test="Christopher Byrne", next="larocca"),
 "larocca": dict(
   slug="frank-la-rocca", kind="Composer and music publishing",
   title="Frank La Rocca Composer Website Case Study",
   lede="A website for a composer of sacred music, organized around a catalog of 59 works, and simple enough for him to keep up himself.",
   facts=["59 works", "Recordings and scores", "Discography", "Press kit", "Moved from Wix"],
   brief=["Frank La Rocca is Composer-in-Residence at the Benedict XVI Institute. He had always built his own websites, and one of his first questions was whether he could maintain the new one without learning complicated software.",
          "The site also had to present a large body of sacred music to conductors, presenters, and listeners."],
   built=[("A catalog, one page per work", "All 59 compositions have their own page, with recordings, score information, and program notes. A discography and a press section sit alongside them."),
          ("A design that suits the music", "A dark, quiet palette and a large portrait set the tone of sacred music before a word is read."),
          ("A mark drawn from chant", "At Frank&rsquo;s request, the site&rsquo;s small musical mark is the opening of the Miserere, Psalm 50 in the first psalm tone."),
          ("Scores by request", "Frank prefers to handle score orders personally, so his imprint, Lumen Verum Music, takes requests by email rather than through an automated store."),
          ("Kept in his name", "The domain stays registered to Frank. Images ship in modern formats with the originals kept untouched, and the fonts are hosted on the site itself.")],
   editor=["Frank signs in to an editor on his own site to update his works, recordings, and news. Each kind of content has its own form, so adding a new piece is a matter of filling in its details."],
   test="Frank La Rocca", next="icjf"),
 "icjf": dict(
   slug="international-catholic-jurists-forum", kind="Nonprofit and research",
   title="International Catholic Jurists Forum Website Case Study",
   lede="A redesign for an international forum of jurists, carrying over 99 pages and 535 news posts word for word into a site built around its books, conferences, and projects.",
   facts=["99 pages migrated", "535 news posts", "Documents hosted on the site", "Embedded video", "Site search"],
   brief=["The International Catholic Jurists Forum had years of publications, conference material, documents, and news. The forum wanted a site that looked as serious as its work, without losing anything it had already published.",
          "Every page and post was carried over with its original wording."],
   built=[("Nothing rewritten, nothing lost", "All 99 pages and 535 news posts moved over word for word. Documents that used to live elsewhere are now hosted on the site itself."),
          ("Organized by the work", "Each book, conference, and project has its own page, and the media connected to it lives there. Interviews and coverage that stand on their own go to a Press page."),
          ("Video in place", "Talks and interviews play in embedded players on the page, so visitors don&rsquo;t have to leave the site."),
          ("Search and giving", "A site search covers the full archive, and donation information sits where supporters expect to find it.")],
   editor=["The forum&rsquo;s editor is set up with presets for its own kinds of content, so staff can add news, documents, and events without touching the layout."],
   test="Jane Adolphe", attrib="Jane Adolphe &middot; Executive Director, International Catholic Jurists Forum", next="roxane"),
 "roxane": dict(
   slug="roxane-salonen", kind="Author website and archive",
   title="Roxane Salonen Author Website Case Study",
   lede="An author website that gathers a long-running blog, newspaper columns, books, and a Substack into one place, with more than 2,300 posts carried over.",
   facts=["2,300+ posts migrated", "Books and speaking", "Substack feed", "Content editor", "Built over a weekend"],
   brief=["Roxane B. Salonen is an author, speaker, and podcast host in Fargo, North Dakota. Her writing was spread across a blog she had kept for years, newspaper columns, and Substack.",
          "She wanted one home for all of it, without losing the archive, and she had been putting the project off because she expected it to take weeks."],
   built=[("The whole archive, carried over", "More than 2,300 blog posts moved into the new site, each with its own page."),
          ("An editorial design", "The design follows the warmth of her writing, with clear pages for her books, speaking, awards, and press."),
          ("New writing arrives on its own", "Recent Substack posts appear on the site automatically, so she publishes in one place and the website keeps up."),
          ("Search basics on every page", "Each page has its own title and description, so her older writing can still be found.")],
   editor=["Roxane has an editor for new content, so she can update the site herself whenever she likes, while new Substack posts keep arriving on their own."],
   test="Roxane B. Salonen", next="dcsocial"),
}

def phone(k):
    return f'<div class="phone"><img src="screenshots/mobile-{k}.webp" alt="{P[k]["alt"]} on a phone" width="780" height="1688" decoding="async"></div>'

def ba(k):
    p = P[k]; plain = html.escape(html.unescape(p["name"]))
    after = f"screenshots/case-{k}.webp"
    if not p["before"]:
        return f'<div class="shot"><img src="{after}" alt="{p["alt"]}" width="2880" height="1920" loading="lazy" decoding="async"></div>'
    return f'''<div class="shot" data-ba style="--p:50%">
        <div class="ba-stage">
          <img src="{after}" alt="{p["alt"]}, the new site" width="2880" height="1920" loading="lazy" decoding="async">
          <div class="ba-before"><img src="screenshots/{p["before"]}" alt="{p["alt"]}, the previous site" width="2560" height="1706" loading="lazy" decoding="async"></div>
          <span class="ba-tag ba-tag-b" aria-hidden="true">Before</span><span class="ba-tag ba-tag-a" aria-hidden="true">After</span>
          <div class="ba-handle" aria-hidden="true"><span></span></div>
          <input class="ba-range" type="range" min="0" max="100" value="50" step="1" aria-label="Compare the previous and new {plain} websites. Use the arrow keys or drag.">
        </div>
      </div>
      <p class="ba-help">Drag the handle, or use the arrow keys, to compare the previous site with the new one.</p>'''

def case(k):
    c = CASE[k]; p = P[k]
    T = {t["name"]: t for t in SRC["tests"]}
    if c["test"] in T:
        t = T[c["test"]]
        q = f'<figure class="case-quote"><blockquote>{t["quote"]}</blockquote><figcaption><img src="{t["img"]}" alt="" width="96" height="96" loading="lazy"><div class="who">{t["name"]}<span>{t["role"]}</span></div></figcaption></figure>'
    else:
        q = f'<figure class="case-quote"><blockquote>{p["quote"]}</blockquote><figcaption><div class="who">{c.get("attrib", p["attrib"]).replace(" &middot; ", "<span>", 1)}</span></div></figcaption></figure>'
    nk = c["next"]
    built = "".join(f'<li><h3>{h}</h3><p>{d}</p></li>' for h, d in c["built"])
    body = f'''  <section class="case-hero">
    <div class="wrap case-hero-in">
      <div>
        <p class="crumbs"><a href="work">Portfolio</a> <span aria-hidden="true">/</span> Case study</p>
        <p class="label">{c["kind"]}</p>
        <h1>{p["name"]}</h1>
        <p class="lead">{c["lede"]}</p>
        <ul class="facts-row">{"".join(f"<li>{x}</li>" for x in c["facts"])}</ul>
        <div class="hero-actions"><a class="btn btn-primary" href="{p["url"]}" target="_blank" rel="noopener">Visit the Website</a><a class="btn btn-ghost" href="contact">Start a Project Like This</a></div>
      </div>
      {phone(k)}
    </div>
  </section>

  <section class="sec case-shot">
    <div class="wrap">
      {ba(k)}
    </div>
  </section>

  <section class="sec sec-stone">
    <div class="wrap case-cols">
      <div class="prose"><h2>The brief</h2>{"".join(f"<p>{x}</p>" for x in c["brief"])}</div>
      <div><h2 class="case-h">What I built</h2><ol class="decisions">{built}</ol></div>
    </div>
  </section>

  <section class="sec">
    <div class="wrap case-cols">
      <div class="prose"><h2>Keeping it up to date</h2>{"".join(f"<p>{x}</p>" for x in c["editor"])}<p><a class="tlink" href="./#editor">How the editor works</a></p></div>
      <div>{q}</div>
    </div>
  </section>

  <section class="sec sec-stone case-next">
    <div class="wrap case-next-in">
      <p class="label">Next case study</p>
      <a class="case-next-link" href="{CASEURL[nk]}">{P[nk]["name"]}</a>
      <a class="tlink" href="work">Back to the Portfolio</a>
    </div>
  </section>

{cta("Have a project like this in mind?", "Tell me what you&rsquo;re working on and what the site needs to do. I&rsquo;ll let you know what I recommend and what it would cost.")}'''
    plain = html.unescape(p["name"])
    ld = '<script type="application/ld+json">\n' + json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Portfolio", "item": SITE + "work"},
        {"@type": "ListItem", "position": 2, "name": plain, "item": SITE + CASEURL[k]}]}, ensure_ascii=False) + '\n</script>\n'
    desc = html.unescape(c["lede"]).replace('"', "&quot;")
    return page(CASEURL[k] + ".html", f'{c["title"]} | Lickity Split', desc, body, cur="work", ld=ld, scripts=BAJS, base="../")

def publisher():
    body = f'''{hero("Websites for publishers, imprints, and journals", ["A small press or journal needs a website that works like a catalog. Readers should find a title, see what it is, and buy it. Authors should find your submission guidelines. Booksellers and reviewers should find what they need without writing to ask.", "I edit books myself, so I know what a publisher&rsquo;s site has to carry."])}

{sec('<div class="two">' + prose("What I can build", [], ["A title catalog with a page for every book, including cover, description, author, ISBN, and where to buy", "Author pages that link to each author&rsquo;s books", "Journal issues and article archives", "Submission guidelines and forms", "Series, imprints, and new-release pages", "Review copy and media request forms", "Newsletter signup", "An editor with presets for new titles and issues"])
     + '<div class="stack">' + prose("Built for a growing list", ["Adding a title should be a short form, not a design job. Each new book or issue fills in its own fields, and the site puts it in the catalog, on the author&rsquo;s page, and in the right series.", "If your list already lives in a spreadsheet or on an older site, I can bring it over in one pass."])
     + prose("Selling", ["Most small publishers already sell through a distributor, a bookstore, or a platform such as Shopify. I&rsquo;ll link to where your books are sold, or set up a store when selling directly makes sense."]) + '</div></div>')}

{sec(examples([("larocca", "Music publishing", "A composer&rsquo;s catalog of 59 works, with scores available by request through his own imprint."), ("icjf", "Publications and research", "Books, conference proceedings, and 535 news posts in one searchable site."), ("roxane", "Writing archive", "More than 2,300 posts moved into an author&rsquo;s new home.")], "Related work"), stone=True)}

{sec(price_block(["Most publisher and journal websites cost between $500 and $1,200.", "Larger catalogs, back issues to migrate, or a direct store start at $1,200 and are priced by scope.", "I&rsquo;ll give you an estimate after looking at your list."]))}

{cta()}'''
    return page("publisher-website-design.html", "Publisher and Journal Website Design | Lickity Split",
                "Websites for small presses, imprints, and journals, with title catalogs, author pages, issue archives, and submission guidelines.", body, cur="publisher")

def nonprofit():
    body = f'''{hero("Websites for nonprofits", ["A nonprofit&rsquo;s website has to explain the mission quickly, show the work, and make it easy to give, volunteer, or get in touch.", "I founded a nonprofit and built its website, so I&rsquo;ve seen the job from the inside. I also help small organizations with the technology behind the site, from shared email to simple automation."])}

{sec('<div class="two">' + prose("What I can include", [], ["A clear statement of the mission and programs", "Events with registration or ticket links", "Donation pages connected to your existing giving platform", "Volunteer and partner forms", "News, reports, and publications", "Board and staff pages", "Newsletter signup", "An editor your staff can use, with presets for news and events"])
     + '<div class="stack">' + prose("A site your team can keep current", ["Small organizations change staff and volunteers often. The editor is set up so whoever has the job next year can post an event or a news item by filling in a short form.", "If you&rsquo;d rather hand updates to me, there are simple monthly plans."])
     + prose("Help beyond the website", ["Many nonprofits also need help with shared email, files, donor lists, and the tools that connect them. That is part of my <a href=technology-consulting>technology consulting</a> work."]) + '</div></div>')}

{sec(examples([("icjf", "International forum", "A redesign with 99 pages and 535 news posts carried over word for word."), ("dcsocial", "Events and community", "Event pages, volunteer forms, and an archive of more than 6,000 photographs."), ("llf", "Research foundation", "Programs, publications, events, and giving, for a foundation I run myself.")], "Related work") + '<p class="center-note" style="margin-top:2rem">For parishes and ministries, see <a href="parish-ministry-websites">Parish and Ministry Websites</a>.</p>', stone=True)}

{sec(price_block(["Most nonprofit websites cost between $500 and $1,200.", "Larger sites with archives, event systems, or migrations start at $1,200 and are priced by scope.", "If your budget is tight, tell me. I can often suggest a simpler way to start."]))}

{cta()}'''
    return page("nonprofit-website-design.html", "Nonprofit Website Design | Lickity Split Web Design",
                "Websites for small nonprofits, with programs, events, donations, volunteer forms, and an editor your staff can use.", body, cur="nonprofit")

def build():
    return [case(k) for k in CASE] + [publisher(), nonprofit()]
