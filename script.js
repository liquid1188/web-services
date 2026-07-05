/* ── Sticky nav ── */
window.addEventListener('scroll',()=>{
  document.getElementById('main-nav').classList.toggle('scrolled',window.scrollY>40);
});

/* ── Reduced-motion preference ── */
const prefersReduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ── Mobile menu ── */
(function(){
  const nav=document.getElementById('main-nav');
  const toggle=nav.querySelector('.nav-toggle');
  const menu=document.getElementById('nav-items');
  if(!toggle) return;
  function setOpen(open){
    nav.classList.toggle('open',open);
    toggle.setAttribute('aria-expanded',open?'true':'false');
    toggle.setAttribute('aria-label',open?'Close menu':'Open menu');
  }
  toggle.addEventListener('click',()=>setOpen(!nav.classList.contains('open')));
  menu.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>setOpen(false)));
  document.addEventListener('keydown',e=>{if(e.key==='Escape')setOpen(false);});
  window.addEventListener('resize',()=>{if(window.innerWidth>700)setOpen(false);});
})();

/* ── Scroll-reveal (pricing cards + case studies / work) ── */
const revealObserver=new IntersectionObserver(entries=>{
  entries.forEach(e=>{
    if(e.isIntersecting){
      e.target.classList.add(e.target.hasAttribute('data-reveal')?'revealed':'in');
      revealObserver.unobserve(e.target);
    }
  });
},{threshold:0.12,rootMargin:'0px 0px -40px 0px'});
document.querySelectorAll('[data-reveal],.reveal').forEach(el=>revealObserver.observe(el));

/* ── Counter animation ── */
function animateCounter(el){
  const target=parseFloat(el.dataset.counter);
  const suffix=el.dataset.suffix||'';
  const isDecimal=target<10;
  if(prefersReduce){el.textContent=(isDecimal?target.toFixed(1):Math.round(target))+suffix;return;}
  const duration=1600;
  const start=performance.now();
  const update=now=>{
    const progress=Math.min((now-start)/duration,1);
    const ease=1-Math.pow(1-progress,3);
    const val=isDecimal?(ease*target).toFixed(1):(Math.round(ease*target));
    el.textContent=val+suffix;
    if(progress<1)requestAnimationFrame(update);
  };
  requestAnimationFrame(update);
}
const counterObserver=new IntersectionObserver(entries=>{
  entries.forEach(e=>{
    if(e.isIntersecting){
      e.target.querySelectorAll('[data-counter]').forEach(animateCounter);
      counterObserver.unobserve(e.target);
    }
  });
},{threshold:0.3});
document.querySelectorAll('.stats-grid,.perf-inner').forEach(el=>counterObserver.observe(el));

/* ── Perf bar special counters ── */
document.querySelectorAll('.perf-score[data-count]').forEach(el=>{
  const target=parseFloat(el.dataset.count);
  const obs=new IntersectionObserver(entries=>{
    entries.forEach(e=>{
      if(e.isIntersecting){
        if(prefersReduce){el.textContent=(target<10?target.toFixed(1):Math.round(target));obs.unobserve(e.target);return;}
        const isDecimal=target<10;
        const duration=1400;
        const start=performance.now();
        const update=now=>{
          const p=Math.min((now-start)/duration,1);
          const ease=1-Math.pow(1-p,3);
          const val=isDecimal?(ease*target).toFixed(1):Math.round(ease*target);
          el.textContent=val;
          if(p<1)requestAnimationFrame(update);
        };
        requestAnimationFrame(update);
        obs.unobserve(e.target);
      }
    });
  },{threshold:0.5});
  obs.observe(el);
});

/* ── FAQ ── */
function toggleFaq(btn){
  const item=btn.closest('.faq-item');
  const isOpen=item.classList.contains('open');
  document.querySelectorAll('.faq-item.open').forEach(i=>i.classList.remove('open'));
  if(!isOpen)item.classList.add('open');
}

/* ── Quote form ── */
function handleSubmit(e){
  e.preventDefault();
  const v=id=>document.getElementById(id).value;
  const body=`New quote request from ${v('fname')} ${v('lname')}\n\nEmail: ${v('email')}\nPhone: ${v('phone')||'Not provided'}\nBusiness: ${v('bizname')}\nType: ${v('biztype')}\nBudget: ${v('budget')||'Not specified'}\nCurrent URL: ${v('currenturl')||'None'}\n\nMessage:\n${v('message')||'None'}`;
  window.location.href=`mailto:andrewlikoudis@gmail.com?subject=Quote Request — ${v('bizname')}&body=${encodeURIComponent(body)}`;
  document.getElementById('quote-form').style.display='none';
  document.getElementById('form-success').style.display='block';
}

/* ── Lead magnet ── */
/* ---- Website Health Check: live PageSpeed-powered audit ---- */
(function(){
  var PSI_KEY=""; /* optional: paste a Google PageSpeed Insights API key here for higher rate limits */
  var runBtn=document.getElementById('hc-run');
  if(!runBtn) return;
  var urlInput=document.getElementById('hc-url'),
      results=document.getElementById('hc-results');

  function normUrl(v){
    v=(v||'').trim();
    if(!v) return '';
    if(!/^https?:\/\//i.test(v)) v='https://'+v;
    try{ var u=new URL(v); if(u.hostname.indexOf('.')<0) return ''; return u.href; }catch(e){ return ''; }
  }
  function band(s){ return s>=90?'hc-good':s>=50?'hc-mid':'hc-bad'; }
  function pct(x){ return (x==null)?null:Math.round(x*100); }
  function fetchTimeout(u,ms){ return Promise.race([ fetch(u), new Promise(function(_,rej){ setTimeout(function(){rej(new Error('timeout'));},ms); }) ]); }

  function callPSI(api){
    return fetchTimeout(api,38000).then(function(r){
      if(r.status===429||r.status===403){ var e=new Error('quota'); e.code=r.status; throw e; }
      return r.json();
    }).then(function(d){
      if(!d||!d.lighthouseResult||!d.lighthouseResult.categories){
        var e=new Error('nodata'); if(d&&d.error&&d.error.code) e.code=d.error.code; throw e;
      }
      return d;
    });
  }

  function run(){
    var url=normUrl(urlInput.value);
    if(!url){ urlInput.focus(); urlInput.style.borderColor='#ff5a4d'; return; }
    urlInput.style.borderColor='';
    runBtn.disabled=true; runBtn.textContent='Scanning…';
    results.hidden=false;
    var host; try{ host=new URL(url).hostname.replace(/^www\./,''); }catch(e){ host=url; }
    results.innerHTML='<div class="hc-loading"><div class="hc-spin"></div><div>Scanning <strong>'+host+'</strong> — speed, mobile, SEO…</div></div>';
    var api='https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url='+encodeURIComponent(url)
      +'&strategy=mobile&category=performance&category=seo&category=accessibility&category=best-practices'
      +(PSI_KEY?('&key='+PSI_KEY):'');
    callPSI(api).then(function(d){ render(d, host); }).catch(function(){
      // one retry after a short delay (clears transient rate limits)
      results.innerHTML='<div class="hc-loading"><div class="hc-spin"></div><div>Still scanning <strong>'+host+'</strong>…</div></div>';
      setTimeout(function(){
        callPSI(api).then(function(d){ render(d, host); }).catch(function(){ showError(host); });
      }, 2200);
    });
  }

  function render(d, host){
    var c=d.lighthouseResult.categories, a=d.lighthouseResult.audits||{};
    var perf=pct(c.performance&&c.performance.score),
        seo=pct(c.seo&&c.seo.score),
        acc=pct(c.accessibility&&c.accessibility.score),
        bp=pct(c['best-practices']&&c['best-practices'].score);
    var lcp=(a['largest-contentful-paint']||{}).displayValue||null;
    var weight=(a['total-byte-weight']||{}).displayValue||null;
    function cell(n,lbl){ return n==null?'':'<div class="hc-score"><div class="hc-score-num '+band(n)+'">'+n+'</div><div class="hc-score-lbl">'+lbl+'</div></div>'; }
    var f=[];
    if(perf!=null&&perf<90) f.push(['warn','Your site loads slowly on phones. Most visitors leave a page that takes over 3 seconds — and most local searches happen on mobile.']);
    if(lcp) f.push([(perf!=null&&perf>=90)?'ok':'warn','Largest content paints in '+lcp+'. Under 2.5s is what keeps visitors from bouncing.']);
    if(seo!=null&&seo<90) f.push(['warn','Search engines aren\u2019t reading your site cleanly — lost Google visibility when customers look for you.']);
    if(acc!=null&&acc<90) f.push(['warn','Parts of the site are hard to read or use, quietly turning customers away.']);
    if(bp!=null&&bp<90) f.push(['warn','It\u2019s missing modern best practices — security, mobile, code health — that Google rewards.']);
    if(weight) f.push([(perf!=null&&perf>=90)?'ok':'warn','The page weighs '+weight+'. My hand-built sites ship under 1MB and load almost instantly.']);
    if(!f.length) f.push(['ok','Strong scores across the board. A few tweaks could still squeeze out more speed and conversions.']);
    f=f.slice(0,4);
    var ico={warn:'<svg viewBox="0 0 24 24"><path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
             ok:'<svg viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>'};
    var findHtml=f.map(function(x){ return '<li class="hc-finding '+x[0]+'">'+ico[x[0]]+'<span>'+x[1]+'</span></li>'; }).join('');
    var weak=[perf,seo,acc,bp].filter(function(v){return v!=null&&v<90;});
    var ctaLine=weak.length?'Want these fixed? I rebuild sites to score 90+ across the board — fast, mobile, and built to bring in customers.':'Even a strong site can convert better. Let\u2019s turn those scores into more calls and bookings.';
    results.innerHTML=
      '<div class="hc-target">Results for <strong>'+host+'</strong> · via Google PageSpeed</div>'
      +'<div class="hc-scoregrid">'+cell(perf,'Speed')+cell(seo,'SEO')+cell(acc,'Accessibility')+cell(bp,'Best Practices')+'</div>'
      +(lcp?'<div class="hc-metric">Loads its main content in <strong>'+lcp+'</strong></div>':'')
      +'<ul class="hc-findings">'+findHtml+'</ul>'
      +'<div class="hc-cta-wrap"><div class="hc-cta-line">'+ctaLine+'</div>'
      +'<button type="button" class="magnet-btn" id="hc-fix">Get My Free Fix Quote</button>'
      +'<button type="button" class="hc-again" id="hc-again">Check another site</button></div>';
    document.getElementById('hc-fix').addEventListener('click',function(){ toQuote(host,{perf:perf,seo:seo,acc:acc,bp:bp}); });
    document.getElementById('hc-again').addEventListener('click',reset);
    runBtn.disabled=false; runBtn.textContent='Run My Free Health Check';
  }

  function showError(host){
    results.innerHTML='<div class="hc-error">I couldn\u2019t pull an automated score for <strong style="color:rgba(255,255,255,.85)">'+host+'</strong> just now \u2014 the scan service is busy or the address may be off. Send it over and I\u2019ll run a full check by hand and get back to you, free.<br><br>'
      +'<button type="button" class="magnet-btn" id="hc-fix">Get a Free Review</button>'
      +'<button type="button" class="hc-again" id="hc-again">Try another address</button></div>';
    document.getElementById('hc-fix').addEventListener('click',function(){ toQuote(host,null); });
    document.getElementById('hc-again').addEventListener('click',reset);
    runBtn.disabled=false; runBtn.textContent='Run My Free Health Check';
  }

  function toQuote(host,scores){
    var cu=document.getElementById('currenturl'), msg=document.getElementById('message');
    if(cu) cu.value=host;
    if(msg){
      var s=scores?(' My free health check scored it — Speed '+(scores.perf!=null?scores.perf:'?')+', SEO '+(scores.seo!=null?scores.seo:'?')+', Accessibility '+(scores.acc!=null?scores.acc:'?')+', Best Practices '+(scores.bp!=null?scores.bp:'?')+'.'):'';
      msg.value='I ran the free health check on '+host+'.'+s+' I\u2019d like a quote to fix these and bring in more customers.';
    }
    var contact=document.getElementById('contact');
    if(contact&&contact.scrollIntoView) contact.scrollIntoView({behavior:'smooth'});
    setTimeout(function(){ var fn=document.getElementById('fname'); if(fn) fn.focus(); },650);
  }

  function reset(){ results.hidden=true; results.innerHTML=''; urlInput.value=''; urlInput.focus(); }

  runBtn.addEventListener('click',run);
  urlInput.addEventListener('keydown',function(e){ if(e.key==='Enter'){ e.preventDefault(); run(); } });
})();

/* ---- hero: live cycling browser of real client sites ---- */
(function(){
  var shots=document.getElementById('liveShots');
  if(!shots) return;
  var link=document.getElementById('liveBrowser'),
      urlEl=document.getElementById('b-url'),
      dotsWrap=document.getElementById('liveDots'),
      imgs=[].slice.call(shots.querySelectorAll('img'));
  var data=[
    ['https://liquid1188.github.io/christa-dalmazio/','liquid1188.github.io/christa-dalmazio'],
    ['https://liquid1188.github.io/collin-westerlund-site/','liquid1188.github.io/collin-westerlund-site'],
    ['https://brushandsoulstudio.com/','brushandsoulstudio.com'],
    ['https://liquid1188.github.io/roxane-salonen/','liquid1188.github.io/roxane-salonen'],
    ['https://liquid1188.github.io/likoudis-ventures/','liquid1188.github.io/likoudis-ventures'],
    ['https://likoudislegacy.com/','likoudislegacy.com'],
    ['https://andrewlikoudis.com/','andrewlikoudis.com'],
    ['https://liquid1188.github.io/ana-restaurant/','liquid1188.github.io/ana-restaurant']
  ];
  if(data.length>1) data.forEach(function(_,k){var s=document.createElement('span');if(k===0)s.className='on';dotsWrap.appendChild(s);});
  var dots=[].slice.call(dotsWrap.children);
  var i=0, paused=false, typeTimer, holdTimer;
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(link) link.href=data[0][0];
  if(reduce){ urlEl.textContent=data[0][1]; return; }
  function typeUrl(str){
    urlEl.textContent=''; var j=0; clearInterval(typeTimer);
    typeTimer=setInterval(function(){ urlEl.textContent=str.slice(0,++j); if(j>=str.length) clearInterval(typeTimer); }, 26);
  }
  function show(next){
    imgs[i].classList.remove('on'); dots[i].classList.remove('on');
    i=next;
    imgs[i].classList.add('on'); dots[i].classList.add('on');
    if(link) link.href=data[i][0];
    typeUrl(data[i][1]);
  }
  function tick(){ if(!paused) show((i+1)%imgs.length); holdTimer=setTimeout(tick,3400); }
  if(link){ link.addEventListener('mouseenter',function(){paused=true;}); link.addEventListener('mouseleave',function(){paused=false;}); }
  document.addEventListener('visibilitychange',function(){ paused=document.hidden; });
  typeUrl(data[0][1]);
  if(data.length>1) holdTimer=setTimeout(tick,3400);
})();
