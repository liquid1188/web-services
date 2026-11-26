from core import *

def faq_block(items, ident="faq"):
    return f'<div class="faq" id="{ident}">' + "".join(
        f'<details><summary>{q}</summary><div class="ans">{"".join(f"<p>{p}</p>" for p in a)}</div></details>' for q, a in items) + "</div>"

def pcard(name, price, paras, feats, timeline, btn):
    return f'''        <div class="pcard">
          <h3>{name}</h3>
          <p class="price-tag">{price}</p>
          {"".join(f"<p>{p}</p>" for p in paras)}
          <details class="feat" open><summary>Typical features</summary>{ul(feats)}</details>
          <h4>Timeline</h4>
          <p class="pcard-note">{timeline}</p>
          <a class="btn btn-primary" href="contact">{btn}</a>
        </div>'''

CALC_JS = '''<script>
/* Website cost estimate. Each item has one price and the total is the sum.
   To change a price, edit the number next to the item below. */
(function(){
  var FULL_MAX=2500, CUSTOM_MIN=500, FULL_MIN=1200;
  var ITEMS=[
    {id:'setup',   name:'Starter site: homepage plus two pages, mobile ready', price:300, fixed:true, note:'Every site starts here'},
    {id:'pages',   name:'Extra pages', price:25, qty:true, max:30, note:'Books, Events, Press, and so on'},
    {id:'editor',  name:'Edit it yourself (content editor)', price:100},
    {id:'seo',     name:'Search engine setup', price:50},
    {id:'gallery', name:'Gallery or portfolio of your work', price:75},
    {id:'store',   name:'Sell books, prints, or products', price:150},
    {id:'press',   name:'Press kit page', price:75},
    {id:'events',  name:'Events calendar or ticket links', price:150},
    {id:'news',    name:'Newsletter signup', price:25},
    {id:'donate',  name:'Donations', price:50},
    {id:'catalog', name:'Works catalog with audio or scores', price:500},
    {id:'auto',    name:'Pages that update when you publish (Substack, podcast, YouTube)', price:300},
    {id:'arch1',   name:'Bring over a blog, under 100 posts', price:100, group:'arch'},
    {id:'arch2',   name:'Bring over a blog, 100 to 1,000 posts', price:300, group:'arch'},
    {id:'arch3',   name:'Bring over a blog, over 1,000 posts', price:600, group:'arch'}
  ];
  var list=document.getElementById('est-list'); if(!list) return;
  function fmt(n){return '$'+n.toLocaleString('en-US');}
  list.innerHTML=ITEMS.map(function(it){
    var price='<span class="est-price">'+fmt(it.price)+(it.qty?' each':'')+'</span>';
    var note=it.note?'<em>'+it.note+'</em>':'';
    if(it.fixed) return '<div class="est-item"><span class="est-name">'+it.name+note+'</span>'+price+'</div>';
    if(it.qty) return '<div class="est-item"><span class="est-name" id="est-pages-lbl">'+it.name+note+'</span><span class="est-qty" role="group" aria-labelledby="est-pages-lbl"><button type="button" data-step="-1" aria-label="Fewer pages">&minus;</button><output id="est-pages" aria-live="polite">0</output><button type="button" data-step="1" aria-label="More pages">+</button></span>'+price+'</div>';
    return '<label class="est-item est-check"><input type="checkbox" data-id="'+it.id+'"'+(it.group?' data-group="'+it.group+'"':'')+'><span class="est-name">'+it.name+'</span>'+price+'</label>';
  }).join('');
  var pages=0, pagesItem=ITEMS.filter(function(x){return x.qty;})[0];
  list.addEventListener('click',function(e){var b=e.target.closest('[data-step]');if(!b)return;
    pages=Math.max(0,Math.min(pagesItem.max,pages+Number(b.getAttribute('data-step'))));document.getElementById('est-pages').textContent=pages;calc();});
  list.addEventListener('change',function(e){var c=e.target;if(c.checked&&c.dataset.group){
    list.querySelectorAll('input[data-group="'+c.dataset.group+'"]').forEach(function(o){if(o!==c)o.checked=false;});}calc();});
  function calc(){
    var total=0, picked=[];
    ITEMS.forEach(function(it){
      if(it.fixed){total+=it.price;picked.push(it.name+' '+fmt(it.price));}
      else if(it.qty){if(pages>0){total+=it.price*pages;picked.push(pages+' extra pages '+fmt(it.price*pages));}}
      else{var c=list.querySelector('input[data-id="'+it.id+'"]');if(c&&c.checked){total+=it.price;picked.push(it.name+' '+fmt(it.price));}}
    });
    var over=total>FULL_MAX;
    var kind=over?'Custom estimate required':(total>=FULL_MIN?'Full Build':(total>=CUSTOM_MIN?'Custom Website':'Starter Site'));
    document.getElementById('est-total').textContent=over?'Custom estimate required':fmt(total);
    document.getElementById('est-kind').textContent=over?'':kind;
    document.getElementById('est-over').hidden=!over;
    var summary=(over?'Custom estimate required (items add up to '+fmt(total)+')':fmt(total)+' ('+kind+')')+': '+picked.join(', ');
    document.getElementById('est-send').href='contact?estimate='+encodeURIComponent(summary);
  }
  calc();
})();
if(window.matchMedia('(max-width: 760px)').matches){document.querySelectorAll('details.feat').forEach(function(d){d.open=false})}
</script>'''

def pricing():
    cards = "\n".join([
        pcard("Starter Site", "$300&ndash;$500",
              ["A straightforward website for someone who needs a professional online presence without a large investment.",
               "This can be a single-page website or a few simple pages, with your basic information, photographs, contact details, and links.",
               "A good option for book launches, new businesses, independent professionals, and small organizations."],
              ["Mobile-friendly design", "Basic information and contact details", "Contact form", "Social links", "Basic search engine setup", "Domain configuration"],
              "A small starter site can often be completed in about 48 hours once the material is ready.", "Get an Estimate"),
        pcard("Custom Website", "$500&ndash;$1,200",
              ["A more complete website designed around your work, with separate pages for services, books, publications, galleries, or other material.",
               "I can help organize your content, set up forms and integrations, and give you a way to make routine updates.",
               "Most of my projects fall into this category."],
              ["Custom design", "Multiple pages", "Publications, books, or portfolio listings", "Galleries", "Contact and inquiry forms", "Newsletter and other integrations", "Content editor", "One consolidated revision round", "30 days of post-launch support"],
              "Usually around a week, depending on the project.", "Discuss a Website"),
        pcard("Full Build", "$1,200&ndash;$2,500+",
              ["For larger websites that need a more involved structure or additional features.",
               "This might include a substantial archive, searchable catalog, event system, online store, or content migration.",
               "The price depends on what needs to be built and how much existing material needs to be transferred."],
              ["Everything relevant from the Custom Website tier", "Large archives", "Searchable catalogs", "E-commerce or donation integrations", "Event registration or ticketing", "More complex content management", "Custom interactive features", "Two consolidated revision rounds", "30 days of post-launch support"],
              "Determined by scope, often around two weeks for projects in this range.", "Discuss a Larger Project"),
    ])
    body = f'''{hero("A website doesn&rsquo;t have to cost thousands.", ["Most of the websites I build cost between $500 and $1,200. That includes custom design, the pages you need, and help getting everything online.", "If you only need something simple, I offer starter websites for $300 to $500. Larger projects, particularly those involving archives, online stores, or custom features, start at $1,200 and are priced by scope. Most of them land under $2,500.", "I&rsquo;ll give you a written estimate before any work begins."])}

  <section class="sec">
    <div class="wrap">
      <div class="price-cards">
{cards}
      </div>
      <div class="prose" style="margin-top:2.5rem">
        <p>Most projects fit within these ranges. Larger websites or projects requiring more specialized features are quoted individually.</p>
        <p>If you&rsquo;re working with a smaller budget, let me know. I can often suggest a simpler way to get started.</p>
      </div>
    </div>
  </section>

  <section class="sec sec-stone">
    <div class="wrap two">
      <div class="prose">
        <h2>Why I build websites this way</h2>
        <p>I generally prefer custom development because it gives me more control over the design and lets me build around what a client actually needs.</p>
        <p>It can also make a straightforward website easier to maintain without depending on an elaborate page builder or a long list of plugins.</p>
        <p>I still use established platforms when they&rsquo;re the better fit. For an online store, for example, Shopify may make more sense than building a shopping system from scratch.</p>
        <p>I&rsquo;m interested in what works for the project, not defending one way of building websites against every other.</p>
      </div>
      <div class="prose">
        <h2>What happens after launch?</h2>
        <p>Before a website goes live, I check the pages, forms, links, and layout across different screen sizes.</p>
        <p>Custom Websites and Full Builds include 30 days of post-launch support. If something isn&rsquo;t working because of a problem with the build, I&rsquo;ll correct it.</p>
        <p>You can also make routine changes yourself using the editor, or ask me to handle them.</p>
      </div>
    </div>
  </section>

  <section class="sec" id="maintenance">
    <div class="wrap">
      <div class="sec-head">
        <h2>Help after launch</h2>
        <p>Some clients prefer to update their own websites. Others would rather send me the changes.</p>
        <p>You can request an individual update or choose a monthly plan if you expect regular work. There&rsquo;s no requirement to sign up for ongoing maintenance.</p>
      </div>
      <h3 style="margin-bottom:1.2rem">One-time edits</h3>
      <div class="plan-list">
        <div class="col"><h3>Quick Fix</h3><p class="price-tag">$25</p><p>One small change, such as replacing a photograph, updating a date, or changing a short passage.</p></div>
        <div class="col"><h3>Edit Session</h3><p class="price-tag">$75</p><p>A collection of routine changes handled together, generally requiring up to one hour of work.</p></div>
        <div class="col"><h3>Larger Revision Session</h3><p class="price-tag">$150</p><p>A larger collection of routine updates or minor layout revisions, generally requiring two to three hours.</p></div>
      </div>
      <h3 style="margin:3rem 0 1.2rem">Monthly plans</h3>
      <div class="plan-list two-up">
        <div class="col"><h3>Edits Plan</h3><p class="price-tag">$19.99/month</p><p>One batch of routine changes each month, up to about 20 minutes of work.</p><p>Suitable for clients who occasionally need a date, photograph, announcement, or short passage updated.</p></div>
        <div class="col"><h3>Care Plan</h3><p class="price-tag">$49.99/month</p><p>Up to three batches of routine updates each month, together requiring no more than approximately 45 minutes of work.</p><p>Includes basic uptime monitoring and priority scheduling.</p></div>
      </div>
      <p class="center-note" style="margin-top:2rem">New pages, major redesigns, custom features, and extensive content entry are quoted separately.</p>
    </div>
  </section>

  <section class="sec sec-stone">
    <div class="wrap two">
      <div class="prose">
        <h2>Payment and scheduling</h2>
        <p>Once we&rsquo;ve agreed on the scope and price, I&rsquo;ll send a payment link.</p>
        <p>Custom Websites and Full Builds begin with a $500 deposit, which counts toward the total and holds your place on my calendar.</p>
        <p>No payment is required before you approve the estimate.</p>
      </div>
      <div class="prose">
        <h2>Hosting and ongoing costs</h2>
        <p>Hosting is included for the custom websites I build, with no platform fees.</p>
        <p>You&rsquo;ll still need a domain name. Third-party services carry their own costs, such as a Shopify store, paid email, a premium domain, booking software, a newsletter platform, or certain integrations.</p>
        <p>I&rsquo;ll identify those costs before we begin.</p>
      </div>
    </div>
  </section>

  <section class="sec" id="estimate">
    <div class="wrap">
      <div class="sec-head">
        <h2>Estimate your website cost</h2>
        <p>Choose the features you think you&rsquo;ll need to get an approximate starting price. I&rsquo;ll confirm the final amount after reviewing the project.</p>
      </div>
      <div class="calc">
        <div id="est-list"></div>
        <div class="est-total"><span>Approximate starting price <span class="est-kind" id="est-kind"></span></span><strong id="est-total" aria-live="polite">$300</strong></div>
        <p class="est-over" id="est-over" hidden>This project may need a more detailed estimate. Send me the requirements and I&rsquo;ll review the scope before providing a price.</p>
        <a class="btn btn-primary" id="est-send" href="contact">Send This With My Inquiry</a>
        <p class="small" style="margin-top:1rem">This is a preliminary estimate, not a binding quote. The final price depends on the scope of work.</p>
      </div>
    </div>
  </section>

{cta()}'''
    return page("pricing.html", "Website Design Pricing from $300 | Lickity Split",
                "Affordable custom website design. Starter sites from $300, custom websites from $500, and larger projects quoted by scope.", body, cur="pricing", scripts=CALC_JS)

FAQ = [
 ("Who owns the website?", ["You do. Once the project is complete, the website files are yours. I can continue hosting the site, or help you move it elsewhere.", "Some features may depend on third-party services with their own accounts or terms. I&rsquo;ll identify those before we begin."]),
 ("Can I update it myself?", ["Yes. Custom Websites and Full Builds include an editor set up for your site, with presets for the things you add most, such as an event, a book, or a post. You fill in a short form and the site handles the layout.", "You can also change text, replace photographs, and save drafts. I&rsquo;ll show you how to use it before launch."]),
 ("How long does a website take?", ["A small starter site can sometimes be ready in about 48 hours once I have the material. Custom websites usually take about a week, while larger projects take longer.", "I&rsquo;ll give you an expected timeline with the estimate."]),
 ("What does it cost to maintain?", ["Hosting is currently included for the straightforward websites I build.", "You&rsquo;ll still need a domain name, and some projects may involve separate costs for email, e-commerce, newsletters, booking services, or other integrations.", "I&rsquo;ll explain any recurring costs in advance."]),
 ("Can you move an existing website?", ["Yes. I&rsquo;ve moved websites from Wix, Squarespace, and older blogging platforms, including archives with thousands of posts.", "I&rsquo;ll review the existing site before giving you an estimate."]),
 ("What if something needs fixing?", ["Custom Websites and Full Builds include 30 days of post-launch support. If there&rsquo;s a problem caused by my work, I&rsquo;ll correct it.", "Additional changes and new features can be quoted separately."]),
 ("Do you use AI in your development process?", ["Yes. I use AI-assisted development tools to help with coding and other technical work, which allows me to complete projects more efficiently and keep my prices affordable. I remain responsible for the design, testing, and finished website."]),
]

def about():
    import json as _j, re as _r, html as _h
    strip = lambda s: _h.unescape(_r.sub(r"<[^>]+>", "", s))
    ld = '<script type="application/ld+json">\n' + _j.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": " ".join(strip(p) for p in a)}} for q, a in FAQ]}, ensure_ascii=False) + '\n</script>\n'
    logos = [("logos/edu-ccbc.svg", "Community College of Baltimore County", "https://www.ccbcmd.edu/"),
             ("logos/edu-towson.png", "Towson University", "https://www.towson.edu/"),
             ("logos/edu-franciscan.png", "Franciscan University of Steubenville", "https://franciscan.edu/"),
             ("logos/cred-goldman-sachs.svg", "Goldman Sachs 10,000 Small Businesses", "gs-10ksb-certificate.jpg"),
             ("logos/cred-johns-hopkins.png", "Johns Hopkins University", "https://www.jhu.edu/"),
             ("logos/cred-mckinsey.png", "McKinsey Forward", "https://www.credly.com/badges/9d5022d2-4f02-49e2-9d51-d56439b8ff34")]
    lg = "".join(f'<a href="{u}" target="_blank" rel="noopener"><img src="{s}" alt="{a}" loading="lazy"></a>' for s, a, u in logos)
    body = f'''  <section class="page-hero">
    <div class="wrap hero-split">
      <div>
        <h1>I&rsquo;m Andrew, and you&rsquo;ll work directly with me.</h1>
        <p class="lead">Lickity Split is my web design business, based in Baltimore. I work directly with clients on everything from the first conversation to the finished website, including the design, writing, and technical setup.</p>
        <p class="lead">My background is in business, communications, and publishing. I&rsquo;ve founded a nonprofit, edited books, and written for national publications. That experience shapes how I approach websites, particularly for people and organizations with a large body of work to present.</p>
        <p class="lead">I care about how a site looks, and just as much about how the information is organized, whether the writing is clear, and how easy it is to keep up to date.</p>
      </div>
      <img src="andrew-about.webp?v=3" alt="Andrew Likoudis" width="880" height="1100" decoding="async">
    </div>
  </section>

  <section class="sec">
    <div class="wrap">
      <div class="prose">
        <h2>A little about my background</h2>
        <p>I studied business administration at the Community College of Baltimore County, communication studies at Towson University, and Catholic studies at Franciscan University of Steubenville.</p>
        <p>My work has included journalism, publishing, communications, and nonprofit administration. I&rsquo;ve also completed professional development programs through Goldman Sachs 10,000 Small Businesses, Johns Hopkins University, and McKinsey Forward.</p>
        <p>I founded the Likoudis Legacy Foundation, whose website I built and continue to maintain.</p>
        <p>These experiences have given me a useful perspective on what small organizations, writers, and independent professionals need from a website, particularly when they don&rsquo;t have a technical staff or marketing department.</p>
      </div>
      <div class="logos" aria-label="Education and training">{lg}</div>
    </div>
  </section>

  <section class="sec sec-stone">
    <div class="wrap">
      <div class="prose">
        <h2>Based in Baltimore</h2>
        <p>I live and work in Baltimore, although many of my clients are elsewhere. Most projects can be handled remotely, and I&rsquo;m happy to meet locally when it makes sense.</p>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="wrap">
      <div class="sec-head"><h2>How we get started</h2></div>
      {steps()}
    </div>
  </section>

  <section class="sec sec-stone">
    <div class="wrap">
      <div class="sec-head"><h2>Common questions</h2></div>
      {faq_block(FAQ)}
    </div>
  </section>

{cta()}'''
    return page("about.html", "About Andrew Likoudis | Lickity Split Web Design",
                "Meet the Baltimore-based web designer behind Lickity Split, building websites for authors, artists, organizations, and small businesses.", body, cur="about", ld=ld)

FORM_JS = '''<script>
window.W3F_KEY="1c22e611-8b13-43bf-ab24-5af6f472a676";
(function(){
  var f=document.getElementById('inquiry'); if(!f) return;
  var est=new URLSearchParams(location.search).get('estimate');
  if(est){document.getElementById('estimate').value=est;var n=document.getElementById('est-note');n.hidden=false;n.querySelector('span').textContent=est;}
  function bad(id,on){document.getElementById(id).closest('.field').classList.toggle('bad',on);document.getElementById(id).setAttribute('aria-invalid',on?'true':'false')}
  f.addEventListener('submit',function(e){
    e.preventDefault();
    var v=function(id){return document.getElementById(id).value.trim()};
    var okN=!!v('name'), okE=/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(v('email')), okP=!!v('project');
    bad('name',!okN);bad('email',!okE);bad('project',!okP);
    var msg=document.getElementById('form-msg');msg.textContent='';
    if(!(okN&&okE&&okP)){(f.querySelector('.bad input, .bad textarea')||f).focus();return}
    var btn=f.querySelector('button[type=submit]'),orig=btn.textContent;btn.textContent='Sending\\u2026';btn.disabled=true;
    var body={access_key:window.W3F_KEY,subject:'Website inquiry from '+v('name'),from_name:'Lickity Split website',replyto:v('email'),
      Name:v('name'),Email:v('email'),'Help with':v('help')||'Not specified',Project:v('project'),'Existing website':v('site')||'None',Deadline:v('deadline')||'None',
      'Estimate from calculator':v('estimate')||'Not used'};
    if(document.getElementById('botcheck').checked) body.botcheck=true;
    fetch('https://api.web3forms.com/submit',{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(body)})
    .then(function(r){return r.json().then(function(d){if(!r.ok||!(d.success===true||d.success==='true'))throw new Error('send');})})
    .then(function(){if(typeof gtag==='function'){gtag('event','generate_lead',{help_with:v('help')||'unspecified',has_existing_site:v('site')?'yes':'no'})}
      setTimeout(function(){location.href='thank-you'},300)})
    .catch(function(){btn.textContent=orig;btn.disabled=false;msg.textContent='Sorry, the form could not send. Please email hello@lickitysplitweb.com instead.'});
  });
})();
/* Website performance check, using Google PageSpeed Insights */
(function(){
  var PSI_KEY="AIzaSyCyzk0dHSfZ040q6KmyP3Fb-Im_N8IyK-w"; /* referrer-locked to lickitysplitweb.com; PSI API only */
  var run=document.getElementById('hc-run'); if(!run) return;
  var input=document.getElementById('hc-url'),out=document.getElementById('hc-results');
  function norm(v){v=(v||'').trim();if(!v)return'';if(!/^https?:\\/\\//i.test(v))v='https://'+v;try{var u=new URL(v);return u.hostname.indexOf('.')<0?'':u.href}catch(e){return''}}
  function band(s){return s>=90?'hc-good':s>=50?'hc-mid':'hc-bad'}
  function pct(x){return x==null?null:Math.round(x*100)}
  function call(api){return Promise.race([fetch(api),new Promise(function(_,rej){setTimeout(function(){rej(new Error('timeout'))},40000)})]).then(function(r){return r.json()}).then(function(d){if(!d||!d.lighthouseResult||!d.lighthouseResult.categories)throw new Error('nodata');return d})}
  function go(){
    var url=norm(input.value);
    if(!url){input.focus();out.hidden=false;out.textContent='Enter a website address, such as example.com.';return}
    var host=new URL(url).hostname.replace(/^www\\./,'');
    run.disabled=true;run.textContent='Checking\\u2026';out.hidden=false;out.textContent='Checking '+host+'. This can take up to half a minute.';
    var base='https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url='+encodeURIComponent(url)+'&strategy=mobile&category=performance&category=seo&category=accessibility&category=best-practices';
    var keyed=/(^|\\.)lickitysplitweb\\.com$/.test(location.hostname)?base+'&key='+PSI_KEY:base;
    call(keyed).catch(function(){return new Promise(function(res){setTimeout(res,2200)}).then(function(){return call(base)})}).then(function(d){
      var c=d.lighthouseResult.categories,a=d.lighthouseResult.audits||{};
      var rows=[['Performance',pct(c.performance&&c.performance.score)],['Search basics',pct(c.seo&&c.seo.score)],['Accessibility',pct(c.accessibility&&c.accessibility.score)],['Best practices',pct(c['best-practices']&&c['best-practices'].score)]];
      var lcp=(a['largest-contentful-paint']||{}).displayValue,w=(a['total-byte-weight']||{}).displayValue;
      var h='<p>Results for <strong>'+host+'</strong> on a phone, from Google PageSpeed Insights.</p><div class="hc-grid">'+rows.map(function(r){return r[1]==null?'':'<div class="hc-score"><b class="'+band(r[1])+'">'+r[1]+'</b><span>'+r[0]+'</span></div>'}).join('')+'</div><ul class="hc-list">';
      if(lcp)h+='<li>Main content appears in '+lcp+'. Google&rsquo;s benchmark is 2.5 seconds or less.</li>';
      if(w)h+='<li>'+String(w).replace(/^Total size was\\s*/i,'The page weighs ')+'.</li>';
      h+='</ul><p class="small" style="margin-top:.8rem">Scores are out of 100. They&rsquo;re a useful starting point, although they won&rsquo;t tell you everything about a site&rsquo;s design, accessibility, or search visibility.</p>';
      out.innerHTML=h;
    }).catch(function(){out.textContent='The check could not be completed for '+host+'. You can run it directly at pagespeed.web.dev.'}).then(function(){run.disabled=false;run.textContent='Check My Website'});
  }
  run.addEventListener('click',go);input.addEventListener('keydown',function(e){if(e.key==='Enter'){e.preventDefault();go()}});
})();
</script>'''

def contact():
    body = f'''{hero("Tell me what you have in mind.", ["Tell me a little about your project, whether you&rsquo;re starting a new website, replacing an old one, or looking for help with technology.", "You don&rsquo;t need to have everything figured out before getting in touch.", "I&rsquo;ll review your inquiry and let you know what I recommend and what it would cost."])}

  <section class="sec">
    <div class="wrap two">
      <form class="form" id="inquiry" novalidate>
        <div class="field"><label for="name">Your name</label><input type="text" id="name" name="name" autocomplete="name" placeholder="Your name" required><p class="err">Please enter your name.</p></div>
        <div class="field"><label for="email">Email address</label><input type="email" id="email" name="email" autocomplete="email" placeholder="you@example.com" required><p class="err">Please enter a valid email address.</p></div>
        <div class="field"><label for="help">What do you need help with?</label><select id="help" name="help"><option value="">Choose one</option><option>New website</option><option>Website redesign or migration</option><option>Technology consulting</option><option>AI setup or training</option><option>Something else</option></select></div>
        <div class="field"><label for="project">Tell me about your project</label><textarea id="project" name="project" placeholder="What do you do, and what would you like help with?" required></textarea><p class="err">Please add a sentence or two about your project.</p></div>
        <div class="field"><label for="site">Existing website <span class="hint">(if you have one)</span></label><input type="url" id="site" name="site" inputmode="url" placeholder="https://"></div>
        <div class="field"><label for="deadline">Deadline <span class="hint">(if any)</span></label><input type="text" id="deadline" name="deadline" placeholder="Is there a date you&rsquo;re working toward?"></div>
        <p class="est-note" id="est-note" hidden>Your estimate from the calculator will be sent with this inquiry: <span></span></p>
        <input type="hidden" id="estimate" name="estimate" value="">
        <div class="hp" aria-hidden="true"><label>Leave this box unchecked <input type="checkbox" id="botcheck" name="botcheck" tabindex="-1" autocomplete="off"></label></div>
        <p class="form-msg" id="form-msg" role="alert"></p>
        <div><button class="btn btn-primary" type="submit">Send My Inquiry</button></div>
        <p class="form-note">I usually reply within 24 to 48 hours. You can also <a href="{CALL}" target="_blank" rel="noopener">book a call</a> or write to <a href="mailto:hello@lickitysplitweb.com">hello@lickitysplitweb.com</a>.</p>
      </form>
      <div class="prose">
        <h2>What should I send?</h2>
        <p>A few sentences are enough to start.</p>
        <p>If you already have a website, include the address. You can send photographs, writing, and other material after we&rsquo;ve discussed the project.</p>
        <p>If you&rsquo;d like a rough number first, the <a href="pricing#estimate">cost estimate on the Pricing page</a> lets you choose features and see an approximate starting price.</p>
      </div>
    </div>
  </section>

  <section class="sec sec-stone" id="healthcheck">
    <div class="wrap">
      <div class="prose">
        <h2>Check your website&rsquo;s performance</h2>
        <p>Already have a website? Enter its address to see how it performs in Google&rsquo;s PageSpeed tools.</p>
        <p>The report can help identify slow-loading elements and other technical issues.</p>
        <p>It&rsquo;s a useful starting point, although it won&rsquo;t tell you everything about your site&rsquo;s design, accessibility, or search visibility.</p>
      </div>
      <div class="hc-row"><label class="hp" for="hc-url">Website address</label><input type="url" id="hc-url" inputmode="url" placeholder="yourwebsite.com" autocomplete="url"><button class="btn btn-primary" type="button" id="hc-run">Check My Website</button></div>
      <div class="hc-results" id="hc-results" aria-live="polite" hidden></div>
    </div>
  </section>'''
    return page("contact.html", "Get a Website Estimate | Lickity Split Web Design",
                "Tell me about your website or technology project and get a clear estimate. Based in Baltimore, serving clients nationwide.", body, cur="contact", scripts=FORM_JS)

def thanks():
    body = f'''{hero("Thanks for getting in touch.", ["I&rsquo;ve received your inquiry and will review the details before replying.", "I usually reply within 24 to 48 hours."], '<a class="btn btn-primary" href="work">View My Work</a><a class="btn btn-ghost" href="./">Back to the Homepage</a>')}'''
    return page("thank-you.html", "Thanks for Getting in Touch | Lickity Split Web Design", "Your inquiry has been received.", body, noindex=True)

def build(): return [pricing(), about(), contact(), thanks()]
