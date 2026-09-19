#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador do site institucional — Julio Bobato Electrician.
Home + 1 pagina SEO por servico + 1 pagina SEO por regiao + sitemap + robots.
SEO em cada pagina (padrao Kevin): title/meta/H1 com keyword+geo, canonical,
schema (Electrician/Service/BreadcrumbList/FAQPage), links internos, breadcrumb.
"""
import os
BASE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://juliobobato.com"
PH_D = "(857) 249-4451"
PH_T = "+18572494451"
EMAIL = "contact@juliobobato.com"

# ---------------------------------------------------------------- data: SERVICES
SERVICES = [
 dict(slug="panel-upgrades", nav="Panel &amp; Service Upgrades", img="service-panel.jpg",
   name="Electrical Panel &amp; Service Upgrades",
   title="Electrical Panel Upgrades on the North Shore, MA | 100A to 200A/400A",
   desc="Licensed electrical panel &amp; service upgrades in Danvers and the North Shore, MA. Upgrade 100-amp to 200-amp or 400-amp service for EVs, heat pumps &amp; modern homes. Free written quotes, permits pulled.",
   h1a="Electrical Panel &amp;", h1b="Service Upgrades",
   intro="Many North Shore homes still run on a 100-amp panel that was never meant for today's electric loads. We upgrade your service to 200 or 400 amps, safely and to code, so your home is ready for EV charging, heat pumps and everything else.",
   included=["100-amp to 200-amp and 400-amp service upgrades","Old fuse box &amp; knob-and-tube panel replacement",
     "Sub-panel installation for additions &amp; garages","Meter and mast repair or replacement",
     "Load calculations for EVs, heat pumps &amp; A/C","Permit pulled and inspection scheduled for you"],
   why="Why upgrade your panel?",
   why_p="Older Essex County homes (many built before 1980) often top out at 100 amps. Add an EV charger or a heat pump and you can trip breakers, or worse. A modern 200/400-amp panel gives you headroom, safety and a home that's easier to sell.",
   faq=[("How much does a 200-amp panel upgrade cost?","Most 100-amp to 200-amp upgrades on the North Shore run in the low thousands, depending on your home, meter location and current wiring. You get a fixed written quote before any work starts."),
        ("Do I need a permit for a panel upgrade?","Yes, and we pull it for you. The upgrade is inspected and signed off so your work is to code and your insurance stays valid."),
        ("How long does a panel upgrade take?","Most residential upgrades are a one-day job. Power is off for part of the day and we coordinate the utility disconnect and reconnect."),
        ("Will a panel upgrade support an EV charger and heat pump?","That's exactly what a 200/400-amp service is for. We size the panel to your current and future loads so you're covered.")]),
 dict(slug="ev-charger-installation", nav="EV Charger Installation", img="service-ev.jpg",
   name="EV Charger Installation",
   title="EV Charger Installation on the North Shore, MA | Level 2 Home Chargers",
   desc="Level 2 home EV charger installation in Danvers and the North Shore, MA. Clean, code-compliant installs, often paired with a panel upgrade and eligible for Massachusetts rebates. Free quotes.",
   h1a="EV Charger", h1b="Installation",
   intro="Charge at home overnight and skip the public stations. We install Level 2 home EV chargers cleanly and to code, size your panel for the load, and handle the permit, so your car is ready every morning.",
   included=["Level 2 (240V) home charger installation","Hardwired or plug-in (NEMA 14-50) setups",
     "Dedicated circuit and breaker sizing","Panel upgrade when your service needs it",
     "Neat cable routing in garages &amp; driveways","Guidance on Massachusetts MOR-EV rebates"],
   why="Why go with a licensed electrician?",
   why_p="A home charger pulls serious current for hours at a time. Done wrong, it's a fire risk and can void your warranty. We install it on a properly sized, permitted circuit so it's safe, fast and covered.",
   faq=[("How much does home EV charger installation cost?","It depends on your panel and how far the charger is from it. A straightforward install is very affordable; if you also need a panel upgrade we quote both together, up front."),
        ("Can you install any brand of charger?","Yes, Tesla, ChargePoint, Wallbox and others. If you haven't bought one yet, we'll point you to a good fit for your car and panel."),
        ("Do I qualify for a Massachusetts EV rebate?","Many MA drivers do through programs like MOR-EV. We'll tell you what's available and make sure the install is done to the standard required."),
        ("Do I need a panel upgrade for an EV charger?","Sometimes. If your panel is full or only 100 amps, we may recommend an upgrade so the charger runs safely. We check before quoting.")]),
 dict(slug="lighting-fixtures", nav="Lighting &amp; Fixtures", img="service-lighting.jpg",
   name="Lighting &amp; Fixture Installation",
   title="Lighting &amp; Fixture Installation on the North Shore, MA | Recessed Lights",
   desc="Recessed lighting, fixtures, dimmers and switches installed in Danvers and the North Shore, MA. Brighten and modernize any room with a licensed electrician. Free estimates.",
   h1a="Lighting &amp; Fixture", h1b="Installation",
   intro="The right lighting changes a whole room. We install recessed LED lighting, fixtures, dimmers and switches cleanly and safely, indoors and out, with a finish you'll be proud of.",
   included=["Recessed &amp; LED can lighting","Chandeliers, pendants &amp; ceiling fixtures",
     "Under-cabinet &amp; accent lighting","Dimmers, switches &amp; smart controls",
     "Outdoor, security &amp; landscape lighting","Bulb and ballast upgrades to efficient LED"],
   why="Why it matters",
   why_p="Beyond looks, dated fixtures and overloaded switches can be a hazard. We make sure every new light is on the right circuit and wired to code, so it looks great and stays safe.",
   faq=[("Can you add recessed lighting to an existing room?","Yes. We add recessed LED lighting to finished ceilings with minimal disruption and clean patching where needed."),
        ("Do you install smart lighting and dimmers?","Absolutely, smart switches, dimmers and app-controlled lighting are some of our most popular upgrades."),
        ("Can you install outdoor and security lighting?","Yes, from motion-sensor security lights to landscape and porch lighting, all weather-rated and to code."),
        ("How many recessed lights do I need?","It depends on room size and use. We'll lay out a plan for even, comfortable light and quote it up front.")]),
 dict(slug="electrical-repairs", nav="Repairs &amp; Troubleshooting", img="service-repairs.jpg",
   name="Electrical Repairs &amp; Troubleshooting",
   title="Electrical Repairs &amp; Troubleshooting on the North Shore, MA | Licensed",
   desc="Fast electrical repairs and troubleshooting in Danvers and the North Shore, MA. Dead outlets, tripping breakers, faulty wiring, fixed right by a licensed electrician. Emergency service available.",
   h1a="Electrical Repairs &amp;", h1b="Troubleshooting",
   intro="Dead outlet? Breaker that keeps tripping? Flickering lights? We track down the real cause, fix it right the first time, and explain what was wrong in plain English.",
   included=["Dead &amp; faulty outlet repair","Tripping breaker diagnosis &amp; repair",
     "Flickering &amp; dimming light fixes","Aluminum &amp; knob-and-tube wiring issues",
     "GFCI &amp; AFCI outlet installation","Whole-home electrical safety inspections"],
   why="Why it matters",
   why_p="Electrical problems are the kind you don't want to guess at. Warm outlets, buzzing panels and repeated trips can point to a real hazard. We diagnose the root cause instead of just resetting the breaker.",
   faq=[("Do you offer emergency electrical service?","Yes. When it's an emergency, especially after a storm, we come right out. Call us and we'll tell you exactly when we can be there."),
        ("Why does my breaker keep tripping?","Usually an overloaded circuit, a short or a failing breaker. We find which one it is and fix the cause, not just the symptom."),
        ("Is a warm or discolored outlet dangerous?","It can be, that's a sign of a loose connection or overload and a real fire risk. Stop using it and call us to inspect it."),
        ("Can you inspect my home's wiring before I buy?","Yes. We do electrical safety inspections and give you a clear written summary of what's safe and what needs work.")]),
 dict(slug="generator-installation", nav="Standby Generators", img="service-panel.jpg",
   name="Standby Generator Installation",
   title="Standby Generator Installation on the North Shore, MA | Licensed Electrician",
   desc="Standby generator installation in Danvers and the North Shore, MA. Keep your heat, lights and sump pump running through the next nor'easter. Properly sized, professionally installed. Free quotes.",
   h1a="Standby Generator", h1b="Installation",
   intro="Nor'easters knock out North Shore power every winter. A standby generator keeps your heat, refrigerator, sump pump and lights running automatically, so your family stays safe and warm.",
   included=["Whole-home &amp; partial standby generators","Correct sizing for your home's real needs",
     "Automatic transfer switch installation","Dedicated circuit &amp; panel integration",
     "Permit, gas coordination &amp; inspection","Testing and a walkthrough of how it works"],
   why="Why it matters",
   why_p="When a storm takes the grid down for days, a properly installed standby generator is the difference between an inconvenience and frozen pipes. We size and wire it so it kicks in on its own.",
   faq=[("What size generator do I need?","It depends on what you want to keep running, just the essentials or the whole house. We do a load calculation and recommend the right size, no overselling."),
        ("Does a standby generator turn on automatically?","Yes. With an automatic transfer switch it senses the outage and starts on its own, usually within seconds."),
        ("Do you handle the permit and gas hookup?","We pull the electrical permit and coordinate the transfer switch and connections. We'll coordinate the gas supply work as needed."),
        ("How often does a standby generator need service?","An annual check keeps it reliable. We'll show you the basics and can point you to a maintenance schedule.")]),
 dict(slug="commercial-electrical", nav="Commercial Electrical", img="service-commercial.jpg",
   name="Commercial Electrical Services",
   title="Commercial Electrician on the North Shore, MA | Shops, Offices &amp; More",
   desc="Commercial electrical services in Danvers and the North Shore, MA. Wiring, lighting, service work and maintenance for shops, offices and small businesses. Licensed, insured, reliable.",
   h1a="Commercial", h1b="Electrical Services",
   intro="Your business can't afford downtime. We handle wiring, lighting, service upgrades and repairs for North Shore shops, offices and small businesses, with maintenance you can count on.",
   included=["Store, office &amp; restaurant wiring","Commercial lighting &amp; LED retrofits",
     "Service upgrades &amp; sub-panels","Dedicated circuits for equipment",
     "Code-compliance &amp; safety corrections","Ongoing maintenance agreements"],
   why="Why local matters for business",
   why_p="Big shops answer to head office. We answer to you, the same person who quotes the job is the one who shows up and stands behind it, so a fast fix stays a fast fix.",
   faq=[("Do you work around business hours?","Yes. We schedule around your customers and staff, including early, late or weekend work when a job can't happen during the day."),
        ("Can you handle a commercial LED lighting retrofit?","Yes, swapping old fixtures for efficient LED is one of the fastest ways to cut a business's electric bill. We quote the savings up front."),
        ("Do you offer maintenance agreements?","We do. A simple maintenance plan keeps your electrical system reliable and catches small problems before they close your doors."),
        ("Are you licensed and insured for commercial work?","Yes, fully licensed and insured in Massachusetts, with the documentation your landlord or inspector may ask for.")]),
]

# ---------------------------------------------------------------- data: CITIES
CITIES = [
 dict(slug="danvers", name="Danvers",
   intro="As our home base, Danvers is where we do the most work, from panel upgrades in older Colonial-era homes near Danvers Square to EV chargers and repairs off Route 1 and Route 114.",
   nearby=["Peabody","Middleton","Topsfield"]),
 dict(slug="peabody", name="Peabody",
   intro="Right next door to Danvers, Peabody keeps us busy with service upgrades, recessed lighting and repairs across its many mid-century homes and busy commercial districts.",
   nearby=["Danvers","Salem","Lynnfield"]),
 dict(slug="beverly", name="Beverly",
   intro="From historic homes near downtown Beverly to newer builds along the water, we handle panel upgrades, EV chargers and everyday electrical repairs, all to code.",
   nearby=["Salem","Danvers","Wenham"]),
 dict(slug="salem", name="Salem",
   intro="Salem's historic housing stock often means older wiring and 100-amp panels. We modernize them safely, with the permit pulled and the work inspected.",
   nearby=["Beverly","Peabody","Marblehead"]),
 dict(slug="middleton", name="Middleton",
   intro="A quick drive from Danvers, Middleton homeowners count on us for panel and service upgrades, generator installs and dependable everyday repairs.",
   nearby=["Danvers","Topsfield","Boxford"]),
 dict(slug="topsfield", name="Topsfield",
   intro="Topsfield's larger and older properties are ideal candidates for 200-amp and 400-amp service upgrades, standby generators and clean EV charging installs.",
   nearby=["Middleton","Boxford","Danvers"]),
 dict(slug="lynnfield", name="Lynnfield",
   intro="Lynnfield homeowners call us for panel upgrades, whole-home lighting and EV chargers, work done neatly and explained in plain English.",
   nearby=["Peabody","Wakefield","Danvers"]),
 dict(slug="wenham", name="Wenham",
   intro="In Wenham we keep classic New England homes safe and up to code, from service upgrades and generators to lighting and repairs.",
   nearby=["Beverly","Hamilton","Topsfield"]),
 dict(slug="hamilton", name="Hamilton",
   intro="Hamilton's established homes often need modern panels and dedicated circuits for today's loads. We upgrade them safely and pull every permit.",
   nearby=["Wenham","Topsfield","Beverly"]),
 dict(slug="boxford", name="Boxford",
   intro="Boxford's larger lots and older houses are a natural fit for 200/400-amp upgrades, standby generators and EV charging, all done to code.",
   nearby=["Topsfield","Middleton","Georgetown"]),
 dict(slug="north-reading", name="North Reading",
   intro="North Reading homeowners rely on us for panel upgrades, lighting, EV chargers and fast, honest electrical repairs.",
   nearby=["Middleton","Lynnfield","Danvers"]),
 dict(slug="marblehead", name="Marblehead",
   intro="Marblehead's historic coastal homes often hide old wiring. We modernize panels and circuits carefully, protecting the character of the house.",
   nearby=["Salem","Swampscott","Beverly"]),
 dict(slug="swampscott", name="Swampscott",
   intro="In Swampscott we handle panel upgrades, EV chargers, lighting and repairs for homes near the shore, safely and to code.",
   nearby=["Marblehead","Salem","Peabody"]),
 dict(slug="georgetown", name="Georgetown",
   intro="Georgetown homeowners count on us for service upgrades, standby generators and dependable repairs, with a written price up front.",
   nearby=["Boxford","Topsfield","Middleton"]),
]

CITY_BY_SLUG = {c["name"]: c["slug"] for c in CITIES}

# ---------------------------------------------------------------- partials
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet">')

def head(title, desc, canon, ld):
    ld_html = "\n".join(f'<script type="application/ld+json">{j}</script>' for j in ld)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="index,follow">
<meta name="theme-color" content="#0d1b2e">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/img/hero-main.jpg">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{ld_html}
</head>
<body>"""

def topbar(sub):
    return (f'<div class="topbar"><div class="wrap">'
      f'<span><strong>Licensed &amp; Insured</strong> · {sub}</span>'
      f'<span>Free estimates · <a href="tel:{PH_T}">{PH_D}</a></span></div></div>')

def header():
    return f"""<header class="site"><div class="wrap">
  <a class="brand" href="index.html" aria-label="Julio Bobato Electrician home"><img src="assets/img/logo-lockup-white.png" alt="Julio Bobato Electrician logo"></a>
  <nav class="main" id="nav">
    <a href="index.html#services">Services</a>
    <a href="index.html#why">Why Us</a>
    <a href="index.html#areas">Service Areas</a>
    <a href="index.html#faq">FAQ</a>
    <a href="index.html#contact">Contact</a>
  </nav>
  <div class="header-cta">
    <a class="phone-link" href="tel:{PH_T}">&#9743; <b>{PH_D}</b></a>
    <a class="btn btn-primary" href="index.html#contact">Free Estimate</a>
    <button class="burger" id="burger" aria-label="Menu"><span></span><span></span><span></span></button>
  </div>
</div></header>"""

def trust():
    return ('<div class="trust"><div class="wrap">'
      '<div class="item">&#9889; Licensed &amp; Insured</div>'
      '<div class="item">&#9201; On Time, Every Time</div>'
      '<div class="item">$ The Price We Quote</div>'
      '<div class="item">&#128203; We Pull the Permit</div></div></div>')

def svc_cards(prefix_city=None):
    """Grid de servicos que linka pras paginas de servico."""
    out = ['<div class="svc-grid">']
    for s in SERVICES:
        loc = f" in {prefix_city}" if prefix_city else ""
        out.append(f"""<article class="svc-card">
  <div class="thumb"><img src="assets/img/{s['img']}" alt="{s['name'].replace('&amp;','and')}{loc} North Shore MA" loading="lazy"></div>
  <div class="body"><h3>{s['nav']}</h3><p>{s['intro'][:118]}...</p>
  <a class="more" href="service-{s['slug']}.html">Learn more &rarr;</a></div>
</article>""")
    out.append('</div>')
    return "\n".join(out)

def area_chips(exclude=None, limit=None):
    out = ['<div class="area-chips">']
    n = 0
    for c in CITIES:
        if exclude and c["name"] == exclude: continue
        out.append(f'<a href="electrician-{c["slug"]}-ma.html">Electrician in <b>{c["name"]}</b></a>')
        n += 1
        if limit and n >= limit: break
    out.append('</div>')
    return "\n".join(out)

def faq_block(items):
    out = ['<div class="faq">']
    for i,(q,a) in enumerate(items):
        op = " open" if i==0 else ""
        out.append(f'<details{op}><summary>{q}</summary><p>{a}</p></details>')
    out.append('</div>')
    return "\n".join(out)

def faq_ld(items):
    q = ",".join('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'
        % (qq.replace('&amp;','and').replace('"','\\"'), aa.replace('&amp;','and').replace('"','\\"'))
        for qq,aa in items)
    return '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[%s]}' % q

def cta_band(headline, sub):
    return f"""<section class="cta-band"><div class="wrap">
  <h2>{headline}</h2><p>{sub}</p>
  <div class="cta-row">
    <a class="btn btn-primary" href="index.html#contact">Get a Free Estimate</a>
    <a class="btn btn-ghost" href="tel:{PH_T}">&#9743; Call {PH_D}</a>
  </div></div></section>"""

def footer():
    svc_li = "\n".join(f'      <li><a href="service-{s["slug"]}.html">{s["nav"]}</a></li>' for s in SERVICES)
    city_li = "\n".join(f'      <li><a href="electrician-{c["slug"]}-ma.html">{c["name"]}, MA</a></li>' for c in CITIES[:8])
    return f"""<footer class="site"><div class="wrap">
  <div class="cols">
    <div><img class="flogo" src="assets/img/logo-lockup-white.png" alt="Julio Bobato Electrician">
      <p>Licensed &amp; insured electrical services for homes and businesses across Danvers and the North Shore of Massachusetts. On time, upfront, done right.</p></div>
    <div><h4>Services</h4><ul>
{svc_li}
    </ul></div>
    <div><h4>Service Areas</h4><ul>
{city_li}
      <li><a href="index.html#areas">All areas &rarr;</a></li>
    </ul></div>
    <div><h4>Contact</h4><ul class="foot-contact">
      <li>&#9743; <a href="tel:{PH_T}">{PH_D}</a></li>
      <li>&#9993; <a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li>&#128205; Danvers &amp; the North Shore, MA</li>
      <li>&#128337; Mon&ndash;Sat, 7 AM &ndash; 7 PM</li>
    </ul></div>
  </div>
  <div class="bottom">
    <span>&copy; 2026 Julio Bobato Electrician · Licensed &amp; Insured in Massachusetts</span>
    <span>Serving Danvers, Peabody, Beverly, Salem &amp; the North Shore</span>
  </div>
</div></footer>
<div class="callbar"><a class="call" href="tel:{PH_T}">&#9743; Call Now</a><a class="quote" href="index.html#contact">Free Estimate</a></div>
<script>
var burger=document.getElementById('burger'),nav=document.getElementById('nav');
burger&&burger.addEventListener('click',function(){{nav.classList.toggle('open')}});
function jbSubmit(e){{e.preventDefault();var f=e.target,n=encodeURIComponent(f.name.value||''),p=encodeURIComponent(f.phone.value||''),s=encodeURIComponent(f.service.value||''),m=encodeURIComponent(f.msg.value||'');window.location.href='mailto:{EMAIL}?subject=Free%20Estimate%20Request%20-%20'+s+'&body=Name:%20'+n+'%0APhone:%20'+p+'%0AService:%20'+s+'%0ADetails:%20'+m;return false;}}
</script>
</body></html>"""

# ---------------------------------------------------------------- LD builders
def business_ld(canon, area=None):
    if area:
        areaj = '"areaServed":{"@type":"City","name":"%s","containedInPlace":{"@type":"AdministrativeArea","name":"Essex County, MA"}},' % area
    else:
        cities = ",".join('{"@type":"City","name":"%s"}' % c["name"] for c in CITIES)
        areaj = '"areaServed":[%s],' % cities
    return ('{"@context":"https://schema.org","@type":"Electrician","@id":"%s#business",'
      '"name":"Julio Bobato Electrician","image":"%s/assets/img/hero-main.jpg","url":"%s",'
      '"telephone":"+1-857-249-4451","email":"%s","priceRange":"$$",'
      '"address":{"@type":"PostalAddress","addressLocality":"Danvers","addressRegion":"MA","postalCode":"01923","addressCountry":"US"},'
      '%s"openingHours":"Mo-Sa 07:00-19:00"}' % (canon, SITE, canon, EMAIL, areaj))

def breadcrumb_ld(name, canon):
    return ('{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
      '{"@type":"ListItem","position":1,"name":"Home","item":"%s/"},'
      '{"@type":"ListItem","position":2,"name":"%s","item":"%s"}]}'
      % (SITE, name.replace('&amp;','and'), canon))

def service_ld(s, canon):
    return ('{"@context":"https://schema.org","@type":"Service","serviceType":"%s",'
      '"provider":{"@type":"Electrician","name":"Julio Bobato Electrician","telephone":"+1-857-249-4451"},'
      '"areaServed":{"@type":"AdministrativeArea","name":"North Shore, Essex County, MA"},"url":"%s"}'
      % (s["name"].replace('&amp;','and'), canon))

# ---------------------------------------------------------------- pages
def build_home():
    canon = f"{SITE}/"
    title = "Licensed Electrician in Danvers &amp; the North Shore, MA | Julio Bobato Electrician"
    desc = ("Julio Bobato Electrician is a licensed &amp; insured electrician serving Danvers and the North Shore, MA. "
      "Panel upgrades, EV chargers, repairs, lighting &amp; commercial work. Upfront pricing, permits pulled. "
      f"Free estimates, call {PH_D}.")
    faq = [("Are you a licensed and insured electrician?","Yes. Julio Bobato Electrician is fully licensed and insured in Massachusetts. We give you our license number up front, before you even ask."),
      ("Do you pull permits for electrical work?","Yes. We pull the required permits so the work is inspected and to code. That keeps your home safe and your homeowner's insurance valid."),
      ("What areas do you serve?","We serve Danvers, Peabody, Beverly, Salem, Middleton, Topsfield and the surrounding North Shore of Massachusetts."),
      ("Do you offer free estimates?","Yes. We provide free, written estimates. The price we quote is the price you pay, no surprises at the end."),
      ("How much does it cost to upgrade to a 200-amp panel?","Most 100-amp to 200-amp panel upgrades on the North Shore run in the low thousands, depending on your home and current wiring. We give you a fixed written quote before any work begins.")]
    ld = [business_ld(canon), faq_ld(faq)]
    html = head(title, desc, canon, ld)
    html += topbar("Serving Danvers &amp; the North Shore, MA")
    html += header()
    html += f"""
<section class="hero-bg"><div class="wrap"><div class="inner">
  <p class="eyebrow" style="color:var(--yellow)">Danvers &amp; North Shore Electrician</p>
  <h1>Powering North Shore Homes <span>You Can Trust</span></h1>
  <p class="sub">Licensed, insured electrical work done right the first time, from panel upgrades and EV chargers to repairs and lighting. On time, upfront pricing, permits always pulled.</p>
  <div class="cta-row">
    <a class="btn btn-primary" href="#contact">Get a Free Estimate</a>
    <a class="btn btn-ghost" href="tel:{PH_T}">&#9743; Call {PH_D}</a>
  </div>
  <div class="hero-badges"><span>&#10003; Licensed &amp; Insured</span><span>&#10003; Upfront Written Quotes</span><span>&#10003; Permits Pulled</span></div>
</div></div></section>
{trust()}
<section id="services"><div class="wrap">
  <div class="sec-head center"><p class="eyebrow">What We Do</p><h2>Residential &amp; Commercial Electrical Services</h2>
  <p class="lead">From a flickering outlet to a full panel and EV charger upgrade, one licensed electrician who does it all and stands behind every job.</p></div>
  {svc_cards()}
</div></section>
<section id="why" class="bg-soft"><div class="wrap"><div class="why">
  <div class="why-img"><img src="assets/img/about-julio.jpg" alt="Julio Bobato, licensed electrician serving the North Shore, MA" loading="lazy"></div>
  <div><p class="eyebrow">Why Homeowners Choose Julio</p><h2>A Local Electrician Who Does What He Says</h2>
  <p class="lead" style="margin-bottom:26px">The big companies answer to investors. We answer to our neighbors. You talk to the same person for years, and the person who quotes the job is the one who stands behind the work.</p>
  <div class="why-list">
    <div class="why-item"><div class="ico">&#9201;</div><div><h4>On Time, Every Time</h4><p>We show up when we say we will. No no-shows, no all-day windows.</p></div></div>
    <div class="why-item"><div class="ico">$</div><div><h4>The Price We Quote Is the Price You Pay</h4><p>A clear written estimate up front. No surprises at the end of the job.</p></div></div>
    <div class="why-item"><div class="ico">&#128203;</div><div><h4>We Pull the Permit</h4><p>Work is inspected and to code, so your home stays safe and your insurance stays valid.</p></div></div>
    <div class="why-item"><div class="ico">&#128172;</div><div><h4>Explained in Plain English</h4><p>We tell you what's wrong, what we'll do and why, no jargon, no pressure.</p></div></div>
  </div></div>
</div></div></section>
<section><div class="wrap"><div class="sec-head center"><p class="eyebrow">Simple &amp; Straightforward</p><h2>How It Works</h2></div>
  <div class="steps">
    <div class="step"><div class="num">1</div><h4>Call or Request a Quote</h4><p>Tell us what's going on. We answer the phone and respond fast.</p></div>
    <div class="step"><div class="num">2</div><h4>Get a Written Estimate</h4><p>A clear, fixed price up front, with the license number and permit plan included.</p></div>
    <div class="step"><div class="num">3</div><h4>Work Done Right</h4><p>On-time, clean, to-code work, and we clean up before we leave.</p></div>
  </div></div></section>
<section id="areas" class="bg-soft"><div class="wrap"><div class="sec-head center"><p class="eyebrow">Proudly Local</p>
  <h2>Serving Danvers &amp; the North Shore</h2>
  <p class="lead">Based in Danvers, we cover Essex County and the surrounding North Shore communities.</p></div>
  {area_chips()}
</div></section>
<section id="faq"><div class="wrap"><div class="sec-head center"><p class="eyebrow">Good to Know</p><h2>Frequently Asked Questions</h2></div>
  {faq_block(faq)}
</div></section>
{cta_band("Need a Licensed Electrician on the North Shore?","Get a free, no-pressure estimate today. On-time service, upfront pricing and work you can trust.")}
<section id="contact"><div class="wrap"><div class="contact">
  <div><p class="eyebrow">Get In Touch</p><h2>Request Your Free Estimate</h2>
    <p class="lead" style="margin-bottom:28px">Call, text or fill out the form, we'll get right back to you with a clear plan and price.</p>
    <div class="contact-info">
      <div class="ci-item"><div class="ico">&#9743;</div><div><b>Phone</b><span><a href="tel:{PH_T}">{PH_D}</a></span></div></div>
      <div class="ci-item"><div class="ico">&#9993;</div><div><b>Email</b><span><a href="mailto:{EMAIL}">{EMAIL}</a></span></div></div>
      <div class="ci-item"><div class="ico">&#128205;</div><div><b>Service Area</b><span>Danvers &amp; the North Shore, Essex County, MA</span></div></div>
      <div class="ci-item"><div class="ico">&#128337;</div><div><b>Hours</b><span>Mon&ndash;Sat, 7:00 AM &ndash; 7:00 PM · Emergency service available</span></div></div>
    </div></div>
  <form class="form" action="#" method="post" onsubmit="return jbSubmit(event)">
    <h3>Free Estimate Request</h3>
    <p style="color:var(--muted);margin-bottom:18px;font-size:.95rem">Tell us about your project, no obligation.</p>
    <div class="fld"><label for="name">Full Name</label><input id="name" name="name" required placeholder="Your name"></div>
    <div class="fld"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" required placeholder="(xxx) xxx-xxxx"></div>
    <div class="fld"><label for="email">Email</label><input id="email" name="email" type="email" placeholder="you@email.com"></div>
    <div class="fld"><label for="service">Service Needed</label><select id="service" name="service">
      <option>Panel / Service Upgrade</option><option>EV Charger Installation</option><option>Lighting &amp; Fixtures</option>
      <option>Electrical Repair / Troubleshooting</option><option>Standby Generator</option><option>Commercial Electrical</option><option>Other</option>
    </select></div>
    <div class="fld"><label for="msg">Details</label><textarea id="msg" name="msg" rows="3" placeholder="Briefly describe the job and your town"></textarea></div>
    <button type="submit" class="btn btn-primary">Send My Request</button>
    <small>Or call us directly at {PH_D}</small>
  </form>
</div></div></section>
"""
    html += footer()
    open(os.path.join(BASE,"index.html"),"w").write(html)
    return "index.html"

def build_service(s):
    fname = f"service-{s['slug']}.html"
    canon = f"{SITE}/{fname}"
    ld = [business_ld(canon), service_ld(s,canon), breadcrumb_ld(s["name"],canon), faq_ld(s["faq"])]
    incl = "\n".join(f'      <li>{i}</li>' for i in s["included"])
    html = head(s["title"], s["desc"], canon, ld)
    html += topbar(f'{s["name"]} · North Shore, MA')
    html += header()
    html += f"""
<div class="crumb"><div class="wrap"><a href="index.html">Home</a> &nbsp;&rsaquo;&nbsp; {s['name']}</div></div>
<section class="hero"><div class="wrap">
  <div class="hero-text">
    <p class="eyebrow" style="color:var(--yellow)">North Shore, MA</p>
    <h1>{s['h1a']} <span>{s['h1b']}</span></h1>
    <p class="sub">{s['intro']}</p>
    <div class="cta-row"><a class="btn btn-primary" href="index.html#contact">Get a Free Estimate</a>
      <a class="btn btn-ghost" href="tel:{PH_T}">&#9743; Call {PH_D}</a></div>
    <div class="hero-badges"><span>&#10003; Licensed &amp; Insured</span><span>&#10003; Permits Pulled</span><span>&#10003; Upfront Pricing</span></div>
  </div>
  <div class="hero-img"><img src="assets/img/{s['img']}" alt="{s['name'].replace('&amp;','and')} on the North Shore, MA" width="1200" height="900"></div>
</div></section>
{trust()}
<section><div class="wrap"><div class="why">
  <div><p class="eyebrow">What's Included</p><h2>{s['name']}</h2>
    <p class="lead" style="margin-bottom:22px">{s['why_p']}</p>
    <ul class="why-list" style="list-style:none">
{incl}
    </ul>
    <div style="margin-top:26px"><a class="btn btn-dark" href="index.html#contact">Request a Free Quote</a></div>
  </div>
  <div class="why-img"><img src="assets/img/{s['img']}" alt="{s['name'].replace('&amp;','and')} service" loading="lazy"></div>
</div></div></section>
<section class="bg-soft"><div class="wrap"><div class="sec-head center"><p class="eyebrow">How It Works</p><h2>Simple, Honest Process</h2></div>
  <div class="steps">
    <div class="step"><div class="num">1</div><h4>Free Assessment</h4><p>We look at your setup and tell you what you actually need, in plain English.</p></div>
    <div class="step"><div class="num">2</div><h4>Written Quote</h4><p>A fixed price up front, with the permit plan included. No surprises.</p></div>
    <div class="step"><div class="num">3</div><h4>Done Right</h4><p>On-time, to-code work, inspected and cleaned up before we leave.</p></div>
  </div></div></section>
<section id="faq"><div class="wrap"><div class="sec-head center"><p class="eyebrow">Good to Know</p><h2>{s['name']} FAQ</h2></div>
  {faq_block(s['faq'])}
</div></section>
<section class="bg-soft"><div class="wrap"><div class="sec-head center"><p class="eyebrow">Where We Work</p><h2>Available Across the North Shore</h2></div>
  {area_chips(limit=10)}
  <p class="center" style="margin-top:16px"><a class="more" href="index.html#areas">See all service areas &rarr;</a></p>
</div></section>
{cta_band(f"Need {s['name']} on the North Shore?","Get a free, no-pressure written quote today. Licensed, insured and always on time.")}
"""
    html += footer()
    open(os.path.join(BASE,fname),"w").write(html)
    return fname

def build_city(c):
    fname = f"electrician-{c['slug']}-ma.html"
    canon = f"{SITE}/{fname}"
    city = c["name"]
    title = f"Electrician in {city}, MA | Licensed &amp; Insured | Julio Bobato Electrician"
    desc = (f"Licensed &amp; insured electrician in {city}, MA. Panel upgrades, EV chargers, lighting, "
      f"repairs &amp; commercial work. Upfront pricing, permits pulled. Free estimates, call {PH_D}.")
    faq = [(f"Are you a licensed electrician in {city}, MA?",
        f"Yes. Julio Bobato Electrician is fully licensed and insured in Massachusetts and serves {city} and the surrounding North Shore. We provide our license number up front."),
      (f"Do you pull electrical permits in {city}?",
        f"Yes. We pull the required permits with the town of {city} so your work is inspected and to code, keeping your home safe and your insurance valid."),
      ("Do you offer free estimates?","Yes. Every estimate is free and in writing. The price we quote is the price you pay."),
      (f"How fast can you get to {city} for a repair?",
        f"Based right in nearby Danvers, we can usually reach {city} quickly, and we offer emergency service when the power's out.")]
    ld = [business_ld(canon, area=city), breadcrumb_ld(f"Electrician in {city}, MA", canon), faq_ld(faq)]
    nearby = "\n".join(
      f'<a href="electrician-{CITY_BY_SLUG[n]}-ma.html">Electrician in <b>{n}</b></a>'
      for n in c["nearby"] if n in CITY_BY_SLUG)
    html = head(title, desc, canon, ld)
    html += topbar(f"Electrician in {city}, MA")
    html += header()
    html += f"""
<div class="crumb"><div class="wrap"><a href="index.html">Home</a> &nbsp;&rsaquo;&nbsp; Electrician in {city}, MA</div></div>
<section class="hero"><div class="wrap">
  <div class="hero-text">
    <p class="eyebrow" style="color:var(--yellow)">Serving {city}, Massachusetts</p>
    <h1>Licensed Electrician in <span>{city}, MA</span></h1>
    <p class="sub">{c['intro']} On time, upfront pricing, permits always pulled, residential and commercial.</p>
    <div class="cta-row"><a class="btn btn-primary" href="index.html#contact">Get a Free Estimate</a>
      <a class="btn btn-ghost" href="tel:{PH_T}">&#9743; Call {PH_D}</a></div>
    <div class="hero-badges"><span>&#10003; Licensed &amp; Insured</span><span>&#10003; Upfront Written Quotes</span><span>&#10003; Permits Pulled</span></div>
  </div>
  <div class="hero-img"><img src="assets/img/hero-main.jpg" alt="Licensed electrician serving {city}, MA" width="1200" height="800">
    <div class="float-badge"><div class="ico">&#9889;</div><div><b>{city}</b><small>&amp; the North Shore</small></div></div>
  </div>
</div></section>
{trust()}
<section><div class="wrap"><div class="sec-head center"><p class="eyebrow">What We Do in {city}</p>
  <h2>Electrical Services in {city}, MA</h2>
  <p class="lead">One licensed electrician for your whole home or business, repairs, upgrades and installs, all done to code.</p></div>
  {svc_cards(prefix_city=city)}
</div></section>
<section id="why" class="bg-soft"><div class="wrap"><div class="why">
  <div class="why-img"><img src="assets/img/about-julio.jpg" alt="Julio Bobato, licensed electrician serving {city}, MA" loading="lazy"></div>
  <div><p class="eyebrow">Why {city} Homeowners Choose Julio</p><h2>A Local Electrician You Can Trust</h2>
    <p class="lead" style="margin-bottom:26px">You talk to the same person for years, and the person who quotes the job is the one who stands behind the work in {city}.</p>
    <div class="why-list">
      <div class="why-item"><div class="ico">&#9201;</div><div><h4>On Time, Every Time</h4><p>We show up when we say we will. No no-shows, no all-day windows.</p></div></div>
      <div class="why-item"><div class="ico">$</div><div><h4>The Price We Quote Is the Price You Pay</h4><p>A clear written estimate up front. No surprises at the end.</p></div></div>
      <div class="why-item"><div class="ico">&#128203;</div><div><h4>We Pull the Permit</h4><p>Work in {city} is inspected and to code, your home stays safe, your insurance stays valid.</p></div></div>
      <div class="why-item"><div class="ico">&#128172;</div><div><h4>Explained in Plain English</h4><p>We tell you what's wrong, what we'll do and why, no jargon, no pressure.</p></div></div>
    </div></div>
</div></div></section>
<section id="faq"><div class="wrap"><div class="sec-head center"><p class="eyebrow">Good to Know</p><h2>{city} Electrician FAQ</h2></div>
  {faq_block(faq)}
</div></section>
<section class="bg-soft"><div class="wrap"><div class="sec-head center"><p class="eyebrow">Nearby</p><h2>We Also Serve</h2></div>
  <div class="area-chips">
{nearby}
    <a href="index.html#areas">All Service Areas</a>
  </div>
</div></section>
{cta_band(f"Need an Electrician in {city}?","Get a free, no-pressure estimate today. On-time service, upfront pricing and work you can trust.")}
"""
    html += footer()
    open(os.path.join(BASE,fname),"w").write(html)
    return fname

# ---------------------------------------------------------------- run
made = [build_home()]
for s in SERVICES: made.append(build_service(s))
for c in CITIES: made.append(build_city(c))

# sitemap + robots
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for m in made:
    u = f"{SITE}/" if m=="index.html" else f"{SITE}/{m}"
    pr = "1.0" if m=="index.html" else ("0.9" if m.startswith("service-") else "0.8")
    sm += f'  <url><loc>{u}</loc><changefreq>weekly</changefreq><priority>{pr}</priority></url>\n'
sm += '</urlset>\n'
open(os.path.join(BASE,"sitemap.xml"),"w").write(sm)
open(os.path.join(BASE,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

print(f"OK: {len(made)} paginas")
print("  home: index.html")
print(f"  servicos ({len(SERVICES)}): " + ", ".join(f"service-{s['slug']}.html" for s in SERVICES))
print(f"  regioes ({len(CITIES)}): " + ", ".join(f"{c['slug']}" for c in CITIES))
print("  + sitemap.xml, robots.txt")
