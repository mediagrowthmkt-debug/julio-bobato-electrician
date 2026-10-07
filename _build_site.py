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
SITE = "https://juliobobatoelectrician.com"
PH_D = "(857) 249-4451"
PH_T = "+18572494451"
EMAIL = "contact@juliobobato.com"

# ---------------------------------------------------------------- Kevin preenche (analytics)
# GA4: ID da propriedade (ex.: "G-AB12CD34EF"). Enquanto tiver "XXXX", o build NAO injeta a tag.
GA4_ID = "G-8VNZTT31N2"   # Kevin 06-10-26 (property 557720474)
# Search Console: valor do content da meta google-site-verification (so o codigo). Vazio = nao injeta.
# Obs.: o DNS do dominio ja tem 2 TXT google-site-verification (propriedade de dominio pode ja estar verificada).
GSC_VERIFICATION = ""

# ---------------------------------------------------------------- formulario
# Endpoint do form. "contact.php" = mesmo servidor (Hostinger com PHP).
# Se o site ficar no GitHub Pages (sem PHP), trocar pela URL absoluta do contact.php hospedado com PHP
# (ex.: "https://mediagrowth.com.br/julio-contact/contact.php") e liberar a origem em ALLOWED_ORIGINS no PHP.
FORM_ENDPOINT = "https://mediagrowth.com.br/julio-contact/contact.php"

ASSET_V = "20261006f"   # trocar a cada mudanca de CSS/JS (cache-busting)
FEATURED = ["panel-upgrades", "ev-charger-installation", "commercial-electrical"]

# ---------------------------------------------------------------- data: SERVICES
SERVICES = [
 dict(slug="panel-upgrades", nav="Panel &amp; Service Upgrades", img="service-panel.jpg",
   name="Electrical Panel &amp; Service Upgrades",
   title="Electrical Panel Upgrade &amp; Replacement | Danvers, MA",
   desc="Licensed electrical panel &amp; service upgrades in Danvers and the North Shore, MA. Upgrade 100-amp to 200-amp or 400-amp service for EVs, heat pumps &amp; modern homes. Free estimates, permits pulled.",
   h1a="Electrical Panel &amp;", h1b="Service Upgrades",
   intro="Many North Shore homes still run on a 100-amp panel that was never meant for today's electric loads. We upgrade your service to 200 or 400 amps, safely and to code, so your home is ready for EV charging, heat pumps and everything else.",
   included=["100-amp to 200-amp and 400-amp service upgrades","Old fuse box &amp; knob-and-tube panel replacement",
     "Sub-panel installation for additions &amp; garages","Meter and mast repair or replacement",
     "Load calculations for EVs, heat pumps &amp; A/C","Permit pulled and inspection scheduled for you"],
   why="Why upgrade your panel?",
   why_p="Older Essex County homes (many built before 1980) often top out at 100 amps. Add an EV charger or a heat pump and you can trip breakers, or worse. A modern 200/400-amp panel gives you headroom, safety and a home that's easier to sell.",
   faq=[("Can I get a free estimate for a panel upgrade?","Yes. Every home is different, so we never guess over the phone. We come out, look at your panel, meter and wiring, and hand you a free written estimate before any work starts."),
        ("Do I need a permit for a panel upgrade?","Yes, and we pull it for you. The upgrade is inspected and signed off so your work is to code and your insurance stays valid."),
        ("How long does a panel upgrade take?","Most residential upgrades are a one-day job. Power is off for part of the day and we coordinate the utility disconnect and reconnect."),
        ("Will a panel upgrade support an EV charger and heat pump?","That's exactly what a 200/400-amp service is for. We size the panel to your current and future loads so you're covered.")]),
 dict(slug="ev-charger-installation", nav="EV Charger Installation", img="service-ev-nopeople.jpg",
   name="EV Charger Installation",
   title="EV Charger Installation in Danvers, MA | Level 2 &amp; Tesla",
   desc="Level 2 home EV charger installation in Danvers and the North Shore, MA. Clean, code-compliant installs, sized to your panel, with guidance on Massachusetts incentives. Free estimates.",
   h1a="EV Charger", h1b="Installation",
   intro="Charge at home overnight and skip the public stations. We install Level 2 home EV chargers cleanly and to code, size your panel for the load, and handle the permit, so your car is ready every morning.",
   included=["Level 2 (240V) home charger installation","Hardwired or plug-in (NEMA 14-50) setups",
     "Dedicated circuit and breaker sizing","Panel upgrade when your service needs it",
     "Neat cable routing in garages &amp; driveways","Guidance on Massachusetts EV charging incentives"],
   why="Why go with a licensed electrician?",
   why_p="A home charger pulls serious current for hours at a time. Done wrong, it's a fire risk and can void your warranty. We install it on a properly sized, permitted circuit so it's safe, fast and covered.",
   faq=[("Can I get a free estimate for an EV charger install?","Yes. We check your panel and the distance to where the charger will go, then give you a free written estimate. If you also need a panel upgrade, both are in the same estimate."),
        ("Can you install any brand of charger?","Yes, Tesla, ChargePoint, Wallbox and others. If you haven't bought one yet, we'll point you to a good fit for your car and panel."),
        ("Are there Massachusetts incentives for home EV chargers?","Often, yes. Programs through Mass Save and your electric company change over time, so we'll point you to what's currently available and make sure the install meets the standard they require."),
        ("Do I need a panel upgrade for an EV charger?","Sometimes. If your panel is full or only 100 amps, we may recommend an upgrade so the charger runs safely. We check before quoting.")]),
 dict(slug="lighting-fixtures", nav="Lighting &amp; Fixtures", img="service-fixtures.jpg",
   name="Lighting &amp; Fixture Installation",
   title="Light Fixture Installation in Danvers, MA | Julio Bobato",
   desc="Chandeliers, pendants, ceiling fixtures, under-cabinet lights, dimmers and switches installed in Danvers and the North Shore, MA by a licensed electrician. Free estimates.",
   h1a="Lighting &amp; Fixture", h1b="Installation",
   intro="The right fixture changes a whole room. We hang chandeliers and pendants, swap dated ceiling lights and add dimmers and smart switches, cleanly and safely, with a finish you'll be proud of.",
   included=["Chandeliers, pendants &amp; ceiling fixtures","Kitchen island &amp; dining room lighting",
     "Under-cabinet &amp; accent lighting","Dimmers, switches &amp; smart controls",
     "Bathroom, vanity &amp; closet lighting","Bulb and ballast upgrades to efficient LED"],
   why="Why it matters",
   why_p="Beyond looks, dated fixtures and overloaded switches can be a hazard. We make sure every new light is on the right circuit, mounted on a box rated for its weight and wired to code, so it looks great and stays safe. Looking for <a href=\"service-recessed-lighting.html\">recessed lighting installation</a> instead? It has its own page.",
   faq=[("Can you hang a heavy chandelier or a fixture on a high ceiling?","Yes. We check that the ceiling box is rated for the weight, add proper support where needed and bring the right equipment for tall foyers and stairwells."),
        ("Do you install smart lighting and dimmers?","Absolutely, smart switches, dimmers and app-controlled lighting are some of our most popular upgrades."),
        ("Can you install a fixture I bought myself?","Yes. Send us a link or a photo and we'll confirm it fits your ceiling box and circuit before we install it."),
        ("Do you also do recessed and outdoor lighting?","Yes. Recessed lighting and outdoor and landscape lighting each have their own page on this site, and we're happy to plan everything in one free estimate.")]),
 dict(slug="recessed-lighting", nav="Recessed Lighting", img="service-lighting.jpg",
   name="Recessed Lighting Installation",
   service_type="Recessed Lighting Installation",
   title="Recessed Lighting Installation Danvers, MA | Julio Bobato",
   desc="Licensed electrician for recessed and can light installation in Danvers and the North Shore. LED retrofits, existing ceilings, clean work. Free estimate.",
   h1a="Recessed Lighting Installation<br>", h1b="Danvers, MA",
   intro="Bright, even light without a single fixture hanging in the way. We plan and install recessed and can lights in kitchens, living rooms, basements and bedrooms across Danvers and the North Shore, in new and existing ceilings, with the right dimmer for every room.",
   h2_included="Recessed and Can Light Installation by a Licensed Massachusetts Electrician",
   included=["Recessed and can lights in new and existing ceilings","Canless LED wafer lights for tight ceiling spaces",
     "A layout plan for even, glare-free light","Dimmer &amp; smart switch installation",
     "Kitchen, basement, bathroom &amp; living room lighting","Old can lights upgraded to LED retrofits"],
   why_p="One ceiling light in the middle of a room leaves the corners dark and throws shadows right where you work. A planned layout of recessed lights spreads the light evenly, makes low ceilings feel taller and gives an older home a clean, modern look. Every job is done by a licensed Massachusetts electrician, on the right circuit and to code.",
   body=[("How Much Does Recessed Lighting Installation Cost?",[
       "It's the first question almost everyone asks, and the honest answer is that it depends on what's above your ceiling. Two rooms that look the same from below can be very different jobs once you account for the framing, the insulation and how far the nearest circuit is.",
       "The things that move the price the most are the number of lights, the type of ceiling (drywall, plaster or a drop ceiling), whether there is attic access above the room, whether the existing circuit can carry the new lights or a new circuit is needed, the type of fixture you choose and any dimmers or smart switches you want.",
       "That's why we don't publish a one size fits all number. We come out, look at the room and hand you a <strong>free written estimate</strong> with the exact layout and the exact price before any work starts. No guesswork over the phone, no surprises at the end."]),
     ("Installing Recessed Lights in an Existing Ceiling (No Attic Access)",[
       "Most of our recessed lighting jobs are in finished rooms, not new construction. Under a second floor or in a ranch without attic space, there is no way to work from above, so we work from below: we cut each opening to the exact size of the fixture and fish new wiring through the joist bays with as few extra openings as possible.",
       "Older North Shore homes often have plaster and lath ceilings, tight framing and wiring from another era. We pick fixtures and routes that respect the ceiling you have, and if we need an access hole to get a wire across a joist, we leave the patch clean and ready for paint.",
       "Before we cut anything, we check the existing circuit. If it's already loaded with other lights and outlets, we tell you and plan a new circuit so the lights never trip a breaker. When a bigger job is involved, it can be handled together with a <a href=\"service-panel-upgrades.html\">panel or service upgrade</a>."]),
     ("Canless LED Wafer Lights vs Traditional Can Lights",[
       "Traditional can lights use a metal housing that sits above the ceiling, with a trim and a bulb or LED module below. They're a great choice in new construction or when there's plenty of space above the ceiling, and they make it easy to change trims later.",
       "Canless LED wafer lights are thin, flat fixtures with a small junction box that sits beside them. They need very little depth, which makes them ideal under floors, in basements full of ductwork and anywhere framing is tight. Many models let you pick the color of the light with a small switch, from warm white to a cooler daylight, and versions rated for contact with insulation are available where the location requires it.",
       "There is no single right answer. During the estimate we look at your ceiling and recommend the option that fits it best, and we explain why."]),
     ("Where Recessed Lighting Works Best: Kitchens, Basements and Living Rooms",[
       "<strong>Kitchens.</strong> Light the work surfaces, not just the middle of the room. We place recessed lights over the counters so you don't stand in your own shadow while you cook, and we can pair them with under-cabinet lights for a finished look. A common starting point is to space lights about half the ceiling height apart, then adjust for cabinets, the island and the range hood.",
       "<strong>Basements.</strong> Low ceilings and ductwork make basements feel dark. More lights at a lower output, often canless wafers, make the space feel bright and usable. If your basement has a drop ceiling, we use fixtures made for suspended ceiling tiles so nothing sags or overheats.",
       "<strong>Living rooms and bedrooms.</strong> Here the goal is comfort. We keep the light warm and add a dimmer, so the same room works for movie night and for cleaning day. We also keep lights out of your direct line of sight from the couch and the bed, so there's no glare."]),
     ("Replacing Old Can Lights with LED Retrofits",[
       "If you already have can lights with old incandescent or halogen bulbs, you don't need to tear out the ceiling. In many cases we can install an LED retrofit trim right into the existing housing: it screws into the old socket or connects to the fixture, uses a fraction of the energy, runs cooler and lasts for many years.",
       "If the old housings are damaged, rusted or not rated for the location, we replace them with new LED fixtures instead. Either way, we check the connections and the dimmer, because old dimmers often flicker or buzz with LED lights. Pairing the new lights with a compatible LED dimmer fixes that.",
       "Switching to LED is also a good moment to rethink the layout. If a room has always felt dark in one corner, we can add a light or two on the same circuit while we're there, so you get the upgrade and the better light in one visit."])],
   h2_process="Our Recessed Lighting Installation Process",
   h2_areas="Recessed Lighting Across the North Shore",
   areas_p="We install recessed lighting all over the North Shore, from homes near downtown <a href=\"electrician-danvers-ma.html\">Danvers</a> to mid-century houses in <a href=\"electrician-peabody-ma.html\">Peabody</a> and historic homes in <a href=\"electrician-beverly-ma.html\">Beverly</a>. Prefer a decorative fixture instead? See our <a href=\"service-lighting-fixtures.html\">light fixture installation</a> page.",
   h2_faq="Recessed Lighting FAQ",
   faq=[("How much does it cost to install recessed lighting in Massachusetts?","It depends on the number of lights, the ceiling type, attic access and whether a new circuit is needed. Instead of guessing over the phone, we come out and give you a free written estimate with the exact layout and price before any work starts."),
        ("Can you install recessed lighting without attic access?","Yes. Most of our jobs are in finished ceilings with no attic above. We work from below through the fixture openings and keep any extra access holes small, then leave the patches clean and ready for paint."),
        ("Do I need a licensed electrician and a permit to add recessed lights in Massachusetts?","Electrical work in Massachusetts is required to be done by a licensed electrician, and new wiring and circuits generally need an electrical permit from your town. We pull the permit when the job requires one and have the work inspected."),
        ("Can I replace my old can lights with LED lights?","Yes. In many cases an LED retrofit trim fits right into the existing can. If the old housings are damaged or not rated for the location, we replace them with new LED fixtures."),
        ("How many recessed lights do I need in a kitchen, and how far apart?","A common starting point is spacing the lights about half the ceiling height apart and focusing them over the counters. The right number depends on your layout, so we sketch a plan during your free estimate."),
        ("Can recessed lights go in a drop ceiling or a finished basement?","Yes. Drop ceilings use fixtures made for suspended tiles, and finished basements are a great fit for thin canless LED wafers that need very little space above the ceiling.")]),
 dict(slug="outdoor-landscape-lighting", nav="Outdoor &amp; Landscape Lighting", img="service-outdoor.jpg",
   name="Outdoor &amp; Landscape Lighting",
   service_type="Landscape Lighting Installation",
   title="Landscape Lighting Installation Danvers, MA | Julio Bobato",
   desc="Licensed electrician for landscape and outdoor lighting in Danvers and the North Shore. Path lights, uplighting, patio and security lights. Free estimate.",
   h1a="Landscape Lighting Installation<br>", h1b="Danvers, MA",
   intro="New England nights start early in the fall. We install landscape and outdoor lighting that makes your home safer to come home to, easy to find and great looking after dark, from path and patio lights to uplighting and security floodlights.",
   h2_included="Outdoor Lighting Installed by a Licensed Electrician, Not Just a Landscaper",
   included=["Landscape &amp; garden uplighting","Path, step &amp; walkway lights",
     "Patio, deck &amp; porch lighting","Motion sensor security &amp; flood lights",
     "Transformers, timers, photocells &amp; smart controls","Weatherproof GFCI outlets &amp; outdoor circuits"],
   why_p="Many outdoor lighting projects on the North Shore are sold by landscaping companies that hand off the electrical side. With us, the person who designs the lighting is a licensed electrician: we plan the circuit, the GFCI protection, the transformer and the timer, pull the permit when it's needed, and stand behind the whole system.",
   body=[("Landscape Lighting Services: Path, Uplighting, Patio, Deck and Security Lights",[
       "<strong>Path and step lights.</strong> Good outdoor lighting starts with the routes you walk every day: the driveway, the front steps, the walkway to the door and the stairs to the deck. We light them so you can see every step in the winter dark, in rain or in snow.",
       "<strong>Uplighting and accent lighting.</strong> Lights aimed up into a tree, across a stone wall or along the front of the house give your property depth and curb appeal. We place each fixture to highlight what makes your home stand out and aim it to keep glare out of your neighbors' windows.",
       "<strong>Patio, deck and porch lighting.</strong> Step lights, rail lights and soft overhead lighting turn the deck or patio into a space you actually use after sunset.",
       "<strong>Security lighting.</strong> Motion sensor floodlights over the driveway, the garage and the side yard add security without leaving lights burning all night.",
       "<strong>Driveway, entry and garage lighting.</strong> The light by your front door and over the garage is the first thing guests and delivery drivers look for. We replace tired fixtures with brighter, efficient LED lights, add a second light where one side of the driveway stays dark and put them on a photocell so they're always on when you pull in.",
       "<strong>Lighting the house itself.</strong> Soft light washed across the front of the house, the columns of a porch or the texture of a stone chimney makes a classic New England home look its best at night. We keep it subtle: the goal is a warm, welcoming glow, not a stadium."]),
     ("Low Voltage Landscape Lighting: Transformers, Wiring and Smart Timers",[
       "Most landscape lighting runs on a low voltage system. A transformer, plugged into or wired to a weatherproof outdoor circuit, steps the power down to a safe low voltage that runs through buried cable to each fixture. It's safe around gardens and easy to adjust or expand as your plants grow.",
       "The details make the difference: the transformer has to be sized for the total load, the cable has to be the right gauge for the distance so the last light isn't dimmer than the first, and every connection has to be sealed against water. That's electrical work, and it's where many outdoor systems fail.",
       "Security floodlights, post lights and outdoor outlets usually run on a standard line voltage circuit instead. We tell you which one fits each spot, and we add photocells, timers or smart controls so the lights come on at dusk and turn off on their own."]),
     ("How Much Does Landscape Lighting Installation Cost?",[
       "The price depends on how many fixtures you want, the type and quality of the fixtures, the size of the transformer, how far the cable has to run, whether a new outdoor circuit or GFCI outlet is needed and the kind of controls you choose.",
       "Instead of a generic number, we walk the property with you, ideally late in the afternoon, mark where each light goes and give you a <strong>free written estimate</strong> before any work begins. You can also start small, with the front walk and the entry, and add more lights later on the same system.",
       "We'll also be straight with you about where to spend and where to save. A good transformer and solid fixtures in the spots that matter most will outlast a big kit of cheap lights, and a system planned with room to grow means adding lights next year is quick and simple."]),
     ("Built for New England Weather: GFCI Outlets, Weatherproof Fixtures and Buried Cable",[
       "Outdoor lighting on the North Shore has to handle salt air near the coast, freezing winters, heavy snow and spring thaws. We use weather rated fixtures, in-use covers on outdoor outlets and GFCI protection where it's required, and we bury and protect the cable so it doesn't get cut by the next round of yard work.",
       "We also think about winter: fixtures placed where the plow and the snow blower won't hit them, and timers that keep the driveway and steps lit during the longest nights of the year. When an outdoor circuit gives you trouble, our <a href=\"service-electrical-repairs.html\">electrical repair</a> service can track down the cause."]),
     ("Smart Controls That Run the Lights for You",[
       "Outdoor lighting should take care of itself. A photocell turns the lights on at dusk and off at dawn, so they follow the seasons without anyone touching a switch. An astronomical timer does the same and can also shut the garden lights off at a set time, while the path and entry lights stay on all night.",
       "If you like to control things from your phone, smart transformers and smart switches let you set scenes, change schedules and turn on the backyard lights from the couch. We set it all up, show you how it works and leave the system simple enough that anyone in the family can use it."])],
   h2_process="Our Outdoor Lighting Installation Process",
   h2_areas="Outdoor Lighting Across the North Shore",
   areas_p="We install landscape and outdoor lighting across the North Shore, including larger properties in <a href=\"electrician-topsfield-ma.html\">Topsfield</a>, <a href=\"electrician-boxford-ma.html\">Boxford</a> and <a href=\"electrician-lynnfield-ma.html\">Lynnfield</a> and coastal homes in <a href=\"electrician-marblehead-ma.html\">Marblehead</a> and <a href=\"electrician-swampscott-ma.html\">Swampscott</a>. Planning an outdoor <a href=\"service-ev-charger-installation.html\">EV charger</a> or need more capacity first? See our <a href=\"service-panel-upgrades.html\">panel upgrades</a>. For indoor light, see <a href=\"service-recessed-lighting.html\">recessed lighting installation</a>.",
   h2_faq="Landscape Lighting FAQ",
   faq=[("What is the average cost to install landscape lighting?","It depends on the number and quality of the fixtures, the transformer, the cable runs and whether a new outdoor circuit is needed. We walk the property with you and give you a free written estimate before any work begins."),
        ("Can you install landscape lighting yourself?","Plug-in low voltage kits are sold for do it yourself projects, but anything that involves a new outdoor outlet, a new circuit or line voltage fixtures should be done by a licensed electrician. A professional install also avoids the most common problems: undersized transformers, dim lights at the end of the run and failing connections."),
        ("What are some common problems with landscape lighting?","The most common are corroded or loose connections, cable cut by yard work, transformers that are too small for the number of lights, lights that get dimmer along a long cable run and water getting into cheap fixtures. Proper sizing, sealed connections and buried cable prevent most of them."),
        ("What is the best quality landscape lighting?","Look for solid brass or copper fixtures, sealed integrated LED or quality LED lamps, and a properly sized transformer with a timer or photocell. They cost more up front than plastic kits but hold up to New England weather for many years."),
        ("Do I need a dedicated outdoor GFCI outlet for landscape lighting?","A low voltage transformer needs a weatherproof, GFCI protected outdoor outlet or circuit. If you don't have one in the right place, we install it as part of the job."),
        ("What is the difference between low voltage and line voltage outdoor lighting?","Low voltage systems use a transformer and are ideal for path, garden and accent lights. Line voltage runs at standard household voltage and is used for floodlights, post lights and outlets. Most homes use a mix of both.")]),
 dict(slug="electrical-repairs", nav="Repairs &amp; Troubleshooting", img="service-repairs.jpg",
   name="Electrical Repairs &amp; Troubleshooting",
   title="Electrical Repairs &amp; Emergency Electrician | Danvers, MA",
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
 dict(slug="commercial-electrical", nav="Commercial Electrical", img="service-commercial.jpg",
   name="Commercial Electrical Services",
   title="Commercial Electrician North Shore, MA | Shops &amp; Offices",
   desc="Commercial electrical services in Danvers and the North Shore, MA. Wiring, lighting, service work and maintenance for shops, offices and small businesses. Free estimates.",
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
   intro="A quick drive from Danvers, Middleton homeowners count on us for panel and service upgrades, EV chargers, recessed lighting and dependable everyday repairs.",
   nearby=["Danvers","Topsfield","Boxford"]),
 dict(slug="topsfield", name="Topsfield",
   intro="Topsfield's larger and older properties are ideal candidates for 200-amp and 400-amp service upgrades, outdoor and landscape lighting and clean EV charging installs.",
   nearby=["Middleton","Boxford","Danvers"]),
 dict(slug="lynnfield", name="Lynnfield",
   intro="Lynnfield homeowners call us for panel upgrades, whole-home lighting and EV chargers, work done neatly and explained in plain English.",
   nearby=["Peabody","Wakefield","Danvers"]),
 dict(slug="wenham", name="Wenham",
   intro="In Wenham we keep classic New England homes safe and up to code, from service upgrades and EV chargers to recessed lighting, outdoor lighting and repairs.",
   nearby=["Beverly","Hamilton","Topsfield"]),
 dict(slug="hamilton", name="Hamilton",
   intro="Hamilton's established homes often need modern panels and dedicated circuits for today's loads. We upgrade them safely and pull every permit.",
   nearby=["Wenham","Topsfield","Beverly"]),
 dict(slug="boxford", name="Boxford",
   intro="Boxford's larger lots and older houses are a natural fit for 200/400-amp upgrades, landscape lighting and EV charging, all done to code.",
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
   intro="Georgetown homeowners count on us for service upgrades, recessed lighting and dependable repairs, with a free written estimate up front.",
   nearby=["Boxford","Topsfield","Middleton"]),
]

CITY_BY_SLUG = {c["name"]: c["slug"] for c in CITIES}

# servicos em destaque primeiro (menu, home, cidades, footer)
SERVICES = [s for f in FEATURED for s in SERVICES if s["slug"] == f] + [s for s in SERVICES if s["slug"] not in FEATURED]
for _s in SERVICES:
    _s.setdefault("body", [])

# ---------------------------------------------------------------- fotos REAIS (Drive "Servicos fotos", 06-10-26)
# key: (arquivo, w, h, alt, legenda). Sem cidade/cliente inventado.
PHOTOS = {
  "panel_meter":   ("g-panel-meter.jpg",900,675,"New electrical meter and service disconnect installed on a home","New meter and service disconnect"),
  "panel_socket":  ("g-panel-socket.jpg",900,675,"Electrical service upgrade in progress with new meter socket wiring","Service upgrade, meter socket wiring"),
  "sign_day":      ("g-sign-day.jpg",900,675,"Illuminated LED storefront sign installed by a commercial electrician","Commercial LED sign installation"),
  "sign_night":    ("g-sign-night.jpg",900,675,"Commercial LED building sign lit up at night","Storefront sign, lit at night"),
  "com_pendants":  ("g-commercial-pendants.jpg",900,675,"Commercial pendant lighting installed in a warehouse space","Commercial pendant lighting"),
  "deck_house":    ("g-deck-house.jpg",720,540,"Deck post cap lights installed on a home railing at dusk","Deck railing post lights"),
  "deck_steps":    ("g-deck-steps.jpg",720,540,"Outdoor deck step and post lighting at dusk","Deck step and post lighting"),
  "chandelier":    ("g-chandelier-crystal.jpg",900,675,"Large crystal chandelier installed in a two-story foyer","Crystal foyer chandelier"),
  "chandelier_mod":("g-chandelier-modern.jpg",900,675,"Modern chandelier light fixture installed in a dining room","Modern dining room fixture"),
  "stairs":        ("g-stair-lights.jpg",900,675,"LED stair lighting installed under each stair tread","LED stair tread lighting"),
  "vanity":        ("g-vanity.jpg",900,675,"Bathroom vanity light fixture installed above a backlit LED mirror","Vanity light and LED mirror"),
  "bath_fan":      ("g-bathroom-fan.jpg",900,675,"Bathroom lighting with LED exhaust fan light and vanity fixture","Bathroom fan light and vanity"),
  "led_mirror":    ("g-led-mirror.jpg",900,675,"Large backlit LED bathroom mirror wired and installed","Backlit LED mirror install"),
  "kitchen":       ("g-kitchen.jpg",900,675,"Kitchen recessed lighting and island pendant lights installed","Kitchen recessed and pendant lights"),
}
REAL = {
  "panel-upgrades": dict(img="real-panel-upgrade.jpg", img_alt="Panel and service upgrade with new meter and conduit on a North Shore MA home",
      img2="real-panel-meter-disconnect.jpg", img2_alt="New electrical meter and emergency service disconnect after a service upgrade",
      gallery=["panel_meter","panel_socket"]),
  "commercial-electrical": dict(img="real-commercial-sign.jpg", img_alt="Commercial electrical work, illuminated LED building sign installation on the North Shore MA",
      img2="real-commercial-pendant-lighting.jpg", img2_alt="Commercial pendant lighting installed by a licensed commercial electrician",
      gallery=["sign_day","sign_night","com_pendants"]),
  "outdoor-landscape-lighting": dict(img="real-outdoor-deck-lights.jpg", img_alt="Outdoor deck lighting with lit railing post caps on a North Shore MA home",
      img2="real-deck-step-lights.jpg", img2_alt="Outdoor deck step and post lighting installed at dusk",
      gallery=["deck_house","deck_steps","stairs"]),
  "lighting-fixtures": dict(img="real-chandelier-install.jpg", img_alt="Lighting fixture installation, crystal chandelier hung in a two-story foyer",
      img2="real-vanity-light-mirror.jpg", img2_alt="Bathroom vanity light fixture and backlit LED mirror installation",
      gallery=["chandelier","chandelier_mod","vanity","stairs","led_mirror","bath_fan"]),
  "recessed-lighting": dict(img="real-recessed-kitchen.jpg", img_alt="Kitchen recessed lighting and island pendant lights installed on the North Shore MA",
      gallery=["kitchen","bath_fan"]),
}
IMG_WH = {"real-panel-upgrade.jpg":(1400,1400),"real-commercial-sign.jpg":(1400,1400),"real-outdoor-deck-lights.jpg":(720,720),
  "real-chandelier-install.jpg":(1400,1400),"real-recessed-kitchen.jpg":(1125,1125),"real-panel-meter-disconnect.jpg":(1200,1500),
  "real-commercial-pendant-lighting.jpg":(1200,1500),"real-deck-step-lights.jpg":(720,900),"real-vanity-light-mirror.jpg":(1200,1500)}
for _s in SERVICES:
    _s.update(REAL.get(_s["slug"], {}))
CITY_HERO = ["real-chandelier-install.jpg","real-panel-upgrade.jpg","real-recessed-kitchen.jpg","real-commercial-sign.jpg"]
CITY_WORK = [["panel_meter","sign_day","chandelier","deck_house"],["kitchen","stairs","panel_socket","com_pendants"],
  ["vanity","sign_night","deck_steps","chandelier_mod"]]
HOME_WORK = ["panel_meter","sign_day","chandelier","deck_house","kitchen","stairs","vanity","com_pendants"]

def work_gallery(keys, cols=""):
    figs = "\n".join(
      f'  <figure><img src="assets/img/{PHOTOS[k][0]}" alt="{PHOTOS[k][3]}" width="{PHOTOS[k][1]}" height="{PHOTOS[k][2]}" loading="lazy" decoding="async"><figcaption>{PHOTOS[k][4]}</figcaption></figure>'
      for k in keys)
    return f'<div class="work-grid{(" " + cols) if cols else ""}">\n{figs}\n</div>'

def _wh(f, d=(1200,900)):
    w, h = IMG_WH.get(f, d)
    return f'width="{w}" height="{h}"'

# ---------------------------------------------------------------- partials
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet">')

def analytics_head():
    out = []
    if GSC_VERIFICATION:
        out.append(f'<meta name="google-site-verification" content="{GSC_VERIFICATION}">')
    if GA4_ID and "XXXX" not in GA4_ID:
        out.append(f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>'
                   f"<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA4_ID}');</script>")
    return "\n".join(out)

def head(title, desc, canon, ld, robots="index,follow", og_img="hero-real-chandelier.jpg"):
    ld_html = "\n".join(f'<script type="application/ld+json">{j}</script>' for j in ld)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#0d1b2e">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/img/{og_img}">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
{analytics_head()}
{FONTS}
<link rel="stylesheet" href="assets/css/style.css?v={ASSET_V}">
{ld_html}
</head>
<body>"""

def topbar(sub):
    return (f'<div class="topbar"><div class="wrap">'
      f'<span><strong>Licensed &amp; Insured</strong> · {sub}</span>'
      f'<span><strong>FREE Estimates</strong> · <a href="tel:{PH_T}">{PH_D}</a></span></div></div>')

def header():
    sub = "\n".join(f'        <a href="service-{s["slug"]}.html">{s["nav"]}</a>' for s in SERVICES)
    return f"""<header class="site"><div class="wrap">
  <a class="brand" href="index.html" aria-label="Julio Bobato Electrician home">
    <img class="brand-ico" src="assets/img/logo-icon.png" alt="Julio Bobato Electrician logo" width="64" height="100">
    <span class="brand-txt"><span class="bn">Julio Bobato</span><span class="bt">Electrician</span></span>
  </a>
  <nav class="main" id="nav">
    <div class="has-sub"><a href="index.html#services">Services <span class="caret">&#9662;</span></a>
      <div class="sub">
{sub}
      </div></div>
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
      '<div class="item">&#10003; 100% Free Estimates</div>'
      '<div class="item">&#128203; We Pull the Permit</div></div></div>')

def _short(t, n=118):
    if len(t) <= n: return t
    return t[:n].rsplit(" ", 1)[0].rstrip(",.;:") + "..."

def _card(s, loc, feat):
    badge = '<span class="badge">Most Requested</span>' if feat else ""
    cls = "svc-card featured" if feat else "svc-card"
    return f"""<article class="{cls}">
  <div class="thumb">{badge}<img src="assets/img/{s['img']}" alt="{s['name'].replace('&amp;','and')}{loc} North Shore MA" loading="lazy"></div>
  <div class="body"><h3>{s['nav']}</h3><p>{_short(s['intro'])}</p>
  <a class="more" href="service-{s['slug']}.html">Learn more &rarr;</a></div>
</article>"""

def svc_cards(prefix_city=None):
    """Grid de servicos: destaques (3) em cima, demais (4) embaixo."""
    loc = f" in {prefix_city}" if prefix_city else ""
    feat = [s for s in SERVICES if s["slug"] in FEATURED]
    rest = [s for s in SERVICES if s["slug"] not in FEATURED]
    out = ['<div class="svc-grid">'] + [_card(s, loc, True) for s in feat] + ['</div>']
    out += ['<div class="svc-grid svc-grid-4">'] + [_card(s, loc, False) for s in rest] + ['</div>']
    return "\n".join(out)

def related_services(cur_slug):
    out = ['<div class="area-chips">']
    for s in SERVICES:
        if s["slug"] == cur_slug: continue
        out.append(f'<a href="service-{s["slug"]}.html">{s["nav"]}</a>')
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
    <a class="btn btn-primary" href="index.html#contact">Get My Free Estimate</a>
    <a class="btn btn-ghost" href="tel:{PH_T}">&#9743; Call {PH_D}</a>
  </div></div></section>"""

def footer():
    svc_li = "\n".join(f'      <li><a href="service-{s["slug"]}.html">{s["nav"]}</a></li>' for s in SERVICES)
    city_li = "\n".join(f'      <li><a href="electrician-{c["slug"]}-ma.html">{c["name"]}, MA</a></li>' for c in CITIES[:8])
    return f"""<footer class="site"><div class="wrap">
  <div class="cols">
    <div><img class="flogo" src="assets/img/logo-lockup.png" alt="Julio Bobato Electrician logo" width="800" height="350">
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
      <li>&#128337; Mon to Sat, 7 AM to 7 PM</li>
      <li>&#10003; <a href="index.html#contact">Free estimates</a></li>
    </ul></div>
  </div>
  <div class="bottom">
    <span>&copy; 2026 Julio Bobato Electrician · Licensed &amp; Insured in Massachusetts</span>
    <span>Serving Danvers, Peabody, Beverly, Salem &amp; the North Shore</span>
  </div>
</div></footer>
<div class="callbar"><a class="call" href="tel:{PH_T}">&#9743; Call Now</a><a class="quote" href="index.html#contact">Free Estimate</a></div>
<script src="assets/js/site.js?v={ASSET_V}" defer></script>
</body></html>"""

# ---------------------------------------------------------------- LD builders
def business_ld(canon, area=None):
    if area:
        areaj = '"areaServed":{"@type":"City","name":"%s","containedInPlace":{"@type":"AdministrativeArea","name":"Essex County, MA"}},' % area
    else:
        cities = ",".join('{"@type":"City","name":"%s"}' % c["name"] for c in CITIES)
        areaj = '"areaServed":[%s],' % cities
    return ('{"@context":"https://schema.org","@type":"Electrician","@id":"%s#business",'
      '"name":"Julio Bobato Electrician","image":"%s/assets/img/hero-real-chandelier.jpg","logo":"%s/assets/img/logo-lockup.png","url":"%s/",'
      '"telephone":"+1-857-249-4451","email":"%s","priceRange":"$$",'
      '"address":{"@type":"PostalAddress","addressLocality":"Danvers","addressRegion":"MA","postalCode":"01923","addressCountry":"US"},'
      '%s"openingHours":"Mo-Sa 07:00-19:00"}' % (SITE + "/", SITE, SITE, SITE, EMAIL, areaj))

def breadcrumb_ld(name, canon):
    return ('{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
      '{"@type":"ListItem","position":1,"name":"Home","item":"%s/"},'
      '{"@type":"ListItem","position":2,"name":"%s","item":"%s"}]}'
      % (SITE, name.replace('&amp;','and'), canon))

def service_ld(s, canon):
    cities = ",".join('{"@type":"City","name":"%s, MA"}' % c["name"] for c in CITIES)
    stype = s.get("service_type", s["name"]).replace('&amp;','and')
    return ('{"@context":"https://schema.org","@type":"Service","serviceType":"%s","name":"%s",'
      '"provider":{"@id":"%s/#business"},'
      '"areaServed":[%s],"url":"%s"}'
      % (stype, stype, SITE, cities, canon))

# ---------------------------------------------------------------- pages
def build_home():
    canon = f"{SITE}/"
    title = "Licensed Electrician North Shore, MA | Julio Bobato"
    desc = ("Julio Bobato Electrician is a licensed &amp; insured electrician serving Danvers and the North Shore, MA. "
      "Panel upgrades, EV chargers, commercial work, recessed &amp; outdoor lighting and repairs. Permits pulled. "
      f"Free estimates, call {PH_D}.")
    faq = [("Are you a licensed and insured electrician?","Yes. Julio Bobato Electrician is fully licensed and insured in Massachusetts. We give you our license number up front, before you even ask."),
      ("Do you pull permits for electrical work?","Yes. We pull the required permits so the work is inspected and to code. That keeps your home safe and your homeowner's insurance valid."),
      ("What areas do you serve?","We serve Danvers, Peabody, Beverly, Salem, Middleton, Topsfield and the surrounding North Shore of Massachusetts."),
      ("Do you offer free estimates?","Yes. We provide free, written estimates. The price we quote is the price you pay, no surprises at the end."),
      ("Can I get a free estimate for a panel upgrade?","Yes. Every home is different, so we come out, look at your panel, meter and wiring, and give you a free written estimate before any work begins. No guesswork over the phone and no obligation.")]
    ld = [business_ld(canon), faq_ld(faq)]
    svc_opts = "\n".join(f'      <option value="{x["nav"]}" data-slug="{x["slug"]}">{x["nav"]}</option>' for x in SERVICES)
    town_opts = "".join(f'<option value="{c["name"]}">' for c in CITIES)
    html = head(title, desc, canon, ld)
    html += topbar("Serving Danvers &amp; the North Shore, MA")
    html += header()
    html += f"""
<section class="hero-bg"><div class="wrap"><div class="inner">
  <p class="eyebrow" style="color:var(--yellow)">Danvers &amp; North Shore Electrician</p>
  <h1>Licensed Electrician on the <span>North Shore, MA</span></h1>
  <p class="sub">Powering North Shore homes you can trust. Licensed, insured electrical work done right the first time, from panel upgrades and EV chargers to commercial work and lighting. On time, permits always pulled, and every estimate is free.</p>
  <div class="cta-row">
    <a class="btn btn-primary" href="#contact">Get My Free Estimate</a>
    <a class="btn btn-ghost" href="tel:{PH_T}">&#9743; Call {PH_D}</a>
  </div>
  <div class="hero-badges"><span>&#10003; Licensed &amp; Insured</span><span>&#10003; 100% Free Estimates</span><span>&#10003; Permits Pulled</span></div>
</div></div></section>
{trust()}
<section id="services"><div class="wrap">
  <div class="sec-head center"><p class="eyebrow">What We Do</p><h2>Residential &amp; Commercial Electrical Services</h2>
  <p class="lead">From a flickering outlet to a full panel and EV charger upgrade, one licensed electrician who does it all and stands behind every job.</p></div>
  {svc_cards()}
</div></section>
<section id="recent-work" class="bg-soft"><div class="wrap">
  <div class="sec-head center"><p class="eyebrow">Real Jobs, Real Photos</p><h2>Recent Electrical Work</h2>
  <p class="lead">A look at panel upgrades, lighting and commercial installs we have completed for homeowners and businesses.</p></div>
  {work_gallery(HOME_WORK)}
</div></section>
<section id="why"><div class="wrap"><div class="why">
  <div class="why-img"><img src="assets/img/real-panel-meter-square.jpg" alt="New meter and service disconnect installed by Julio Bobato Electrician on the North Shore, MA" width="1000" height="1000" loading="lazy"></div>
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
    <div class="step"><div class="num">1</div><h4>Call or Request a Free Estimate</h4><p>Tell us what's going on. We answer the phone and respond fast.</p></div>
    <div class="step"><div class="num">2</div><h4>Get Your Free Written Estimate</h4><p>A clear, fixed price up front, with the license number and permit plan included. Free, no obligation.</p></div>
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
    <p class="lead" style="margin-bottom:28px">Every estimate is 100% free with no obligation. Call, text or fill out the form and we'll get right back to you with a clear plan.</p>
    <div class="contact-info">
      <div class="ci-item"><div class="ico">&#9743;</div><div><b>Phone</b><span><a href="tel:{PH_T}">{PH_D}</a></span></div></div>
      <div class="ci-item"><div class="ico">&#9993;</div><div><b>Email</b><span><a href="mailto:{EMAIL}">{EMAIL}</a></span></div></div>
      <div class="ci-item"><div class="ico">&#128205;</div><div><b>Service Area</b><span>Danvers &amp; the North Shore, Essex County, MA</span></div></div>
      <div class="ci-item"><div class="ico">&#128337;</div><div><b>Hours</b><span>Mon to Sat, 7:00 AM to 7:00 PM · Emergency service available</span></div></div>
    </div></div>
  <form class="form" id="estimate-form" action="{FORM_ENDPOINT}" method="post" data-phone="{PH_D}" data-tel="{PH_T}" data-email="{EMAIL}">
    <h3>Get Your <span class="hl">FREE</span> Estimate</h3>
    <p style="color:var(--muted);margin-bottom:18px;font-size:.95rem">Free and no obligation. Tell us about the job and we'll get right back to you.</p>
    <div class="fld"><label for="name">Full Name</label><input id="name" name="name" required maxlength="80" autocomplete="name" placeholder="Your name"></div>
    <div class="fld"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" required maxlength="25" autocomplete="tel" placeholder="Best number to reach you"></div>
    <div class="fld"><label for="email">Email</label><input id="email" name="email" type="email" maxlength="120" autocomplete="email" placeholder="you@email.com"></div>
    <div class="fld"><label for="service">Service Needed</label><select id="service" name="service">
{svc_opts}
      <option value="Other">Other</option>
    </select></div>
    <div class="fld"><label for="city">Town</label><input id="city" name="city" maxlength="60" list="towns" autocomplete="address-level2" placeholder="e.g. Danvers"><datalist id="towns">{town_opts}</datalist></div>
    <div class="fld"><label for="msg">Details</label><textarea id="msg" name="msg" rows="3" maxlength="2000" placeholder="Briefly describe the job"></textarea></div>
    <div class="hp" aria-hidden="true"><label for="website">Leave this empty</label><input id="website" name="website" tabindex="-1" autocomplete="off"></div>
    <input type="hidden" name="page" value="">
    <button type="submit" class="btn btn-primary">Get My Free Estimate</button>
    <p class="form-status" id="form-status" role="status" aria-live="polite"></p>
    <small>100% free, no obligation. Or call us directly at <a href="tel:{PH_T}">{PH_D}</a></small>
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
    est = f"index.html?service={s['slug']}#contact"
    areas_p = f'<p class="lead">{s["areas_p"]}</p>' if s.get("areas_p") else ""
    body = ""
    if s["body"]:
        blocks = "\n".join(f'  <h2>{h}</h2>\n' + "\n".join(f"  <p>{pp}</p>" for pp in ps) for h, ps in s["body"])
        body = f'<section class="article-sec"><div class="wrap"><div class="article">\n{blocks}\n  <p class="article-cta"><a class="btn btn-primary" href="{est}">Get My Free Estimate</a></p>\n</div></div></section>'
    gallery = ""
    if s.get("gallery"):
        gallery = (f'<section class="bg-soft"><div class="wrap"><div class="sec-head center"><p class="eyebrow">Real Jobs, Real Photos</p>'
          f'<h2>Recent {s["nav"]} Work</h2></div>\n  {work_gallery(s["gallery"], "cols-3" if len(s["gallery"]) in (3,6) else "")}\n</div></section>')
    html = head(s["title"], s["desc"], canon, ld, og_img=s["img"])
    html += topbar(f'{s["name"]} · North Shore, MA')
    html += header()
    html += f"""
<div class="crumb"><div class="wrap"><a href="index.html">Home</a> &nbsp;&rsaquo;&nbsp; {s['name']}</div></div>
<section class="hero"><div class="wrap">
  <div class="hero-text">
    <p class="eyebrow" style="color:var(--yellow)">North Shore, MA</p>
    <h1>{s['h1a']} <span>{s['h1b']}</span></h1>
    <p class="sub">{s['intro']}</p>
    <div class="cta-row"><a class="btn btn-primary" href="{est}">Get My Free Estimate</a>
      <a class="btn btn-ghost" href="tel:{PH_T}">&#9743; Call {PH_D}</a></div>
    <div class="hero-badges"><span>&#10003; Licensed &amp; Insured</span><span>&#10003; Permits Pulled</span><span>&#10003; 100% Free Estimates</span></div>
  </div>
  <div class="hero-img"><img src="assets/img/{s['img']}" alt="{s.get('img_alt', s['name'].replace('&amp;','and') + ' on the North Shore, MA')}" {_wh(s['img'])} fetchpriority="high"></div>
</div></section>
{trust()}
<section><div class="wrap"><div class="why">
  <div><p class="eyebrow">What's Included</p><h2>{s.get('h2_included', s['name'])}</h2>
    <p class="lead" style="margin-bottom:22px">{s['why_p']}</p>
    <ul class="why-list" style="list-style:none">
{incl}
    </ul>
    <div style="margin-top:26px"><a class="btn btn-dark" href="{est}">Get My Free Estimate</a></div>
  </div>
  <div class="why-img"><img src="assets/img/{s.get('img2', s['img'])}" alt="{s.get('img2_alt', s['name'].replace('&amp;','and') + ' service')}" {_wh(s.get('img2', s['img']))} loading="lazy"></div>
</div></div></section>
{gallery}
{body}
<section class="bg-soft"><div class="wrap"><div class="sec-head center"><p class="eyebrow">How It Works</p><h2>{s.get('h2_process', 'Simple, Honest Process')}</h2></div>
  <div class="steps">
    <div class="step"><div class="num">1</div><h4>Free Estimate</h4><p>We look at your setup and tell you what you actually need, in plain English. Always free.</p></div>
    <div class="step"><div class="num">2</div><h4>Clear Written Price</h4><p>A fixed price in writing before any work, with the permit plan included. No surprises.</p></div>
    <div class="step"><div class="num">3</div><h4>Done Right</h4><p>On-time, to-code work, inspected and cleaned up before we leave.</p></div>
  </div></div></section>
<section id="faq"><div class="wrap"><div class="sec-head center"><p class="eyebrow">Good to Know</p><h2>{s.get('h2_faq', s['name'] + ' FAQ')}</h2></div>
  {faq_block(s['faq'])}
</div></section>
<section class="bg-soft"><div class="wrap"><div class="sec-head center"><p class="eyebrow">Where We Work</p><h2>{s.get('h2_areas', 'Available Across the North Shore')}</h2>{areas_p}</div>
  {area_chips(limit=10)}
  <p class="center" style="margin-top:16px"><a class="more" href="index.html#areas">See all service areas &rarr;</a></p>
</div></section>
<section><div class="wrap"><div class="sec-head center"><p class="eyebrow">More From Julio</p><h2>Related Electrical Services</h2></div>
  {related_services(s['slug'])}
</div></section>
{cta_band(f"Need {s['name']} on the North Shore?","Get a free, no-pressure estimate today. Licensed, insured and always on time.")}
"""
    html += footer()
    open(os.path.join(BASE,fname),"w").write(html)
    return fname

def build_city(c):
    fname = f"electrician-{c['slug']}-ma.html"
    canon = f"{SITE}/{fname}"
    city = c["name"]
    title = f"Electrician in {city}, MA | Julio Bobato Electrician"
    desc = (f"Licensed &amp; insured electrician in {city}, MA. Panel upgrades, EV chargers, lighting, "
      f"repairs &amp; commercial work. Permits pulled. 100% free estimates, call {PH_D}.")
    faq = [(f"Are you a licensed electrician in {city}, MA?",
        f"Yes. Julio Bobato Electrician is fully licensed and insured in Massachusetts and serves {city} and the surrounding North Shore. We provide our license number up front."),
      (f"Do you pull electrical permits in {city}?",
        f"Yes. We pull the required permits with the town of {city} so your work is inspected and to code, keeping your home safe and your insurance valid."),
      ("Do you offer free estimates?","Yes. Every estimate is 100% free, in writing and with no obligation. The price we quote is the price you pay."),
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
    <p class="sub">{c['intro']} On time, permits always pulled and every estimate is free, residential and commercial.</p>
    <div class="cta-row"><a class="btn btn-primary" href="index.html#contact">Get My Free Estimate</a>
      <a class="btn btn-ghost" href="tel:{PH_T}">&#9743; Call {PH_D}</a></div>
    <div class="hero-badges"><span>&#10003; Licensed &amp; Insured</span><span>&#10003; 100% Free Estimates</span><span>&#10003; Permits Pulled</span></div>
  </div>
  <div class="hero-img"><img src="assets/img/{CITY_HERO[CITIES.index(c) % len(CITY_HERO)]}" alt="Electrical work by a licensed electrician serving {city}, MA" {_wh(CITY_HERO[CITIES.index(c) % len(CITY_HERO)])}>
    <div class="float-badge"><div class="ico">&#9889;</div><div><b>{city}</b><small>&amp; the North Shore</small></div></div>
  </div>
</div></section>
{trust()}
<section><div class="wrap"><div class="sec-head center"><p class="eyebrow">What We Do in {city}</p>
  <h2>Electrical Services in {city}, MA</h2>
  <p class="lead">One licensed electrician for your whole home or business, repairs, upgrades and installs, all done to code.</p></div>
  {svc_cards(prefix_city=city)}
</div></section>
<section><div class="wrap"><div class="sec-head center"><p class="eyebrow">Real Jobs, Real Photos</p><h2>Recent Work on the North Shore</h2></div>
  {work_gallery(CITY_WORK[CITIES.index(c) % len(CITY_WORK)])}
</div></section>
<section id="why" class="bg-soft"><div class="wrap"><div class="why">
  <div class="why-img"><img src="assets/img/real-panel-meter-square.jpg" alt="Service upgrade by Julio Bobato Electrician, serving {city}, MA" width="1000" height="1000" loading="lazy"></div>
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

def build_thankyou():
    fname = "thank-you.html"
    canon = f"{SITE}/{fname}"
    html = head("Thank You | Julio Bobato Electrician", "Your free estimate request was received.", canon, [], robots="noindex, follow")
    html += topbar("Serving Danvers &amp; the North Shore, MA")
    html += header()
    html += f"""
<section class="hero thanks" data-lead="1"><div class="wrap"><div class="hero-text">
  <p class="eyebrow" style="color:var(--yellow)">Request Received</p>
  <h1>Thank You! <span>Your Free Estimate Request Is In</span></h1>
  <p class="sub">Julio will review the details and get back to you shortly, usually the same business day. If it's urgent, call or text now and we'll pick up.</p>
  <div class="cta-row"><a class="btn btn-primary" href="tel:{PH_T}">&#9743; Call {PH_D}</a>
    <a class="btn btn-ghost" href="index.html">Back to Home</a></div>
</div></div></section>
<section><div class="wrap"><div class="sec-head center"><p class="eyebrow">What Happens Next</p><h2>Simple, Honest Process</h2></div>
  <div class="steps">
    <div class="step"><div class="num">1</div><h4>We Reach Out</h4><p>We call or text you to understand the job and set a time that works for you.</p></div>
    <div class="step"><div class="num">2</div><h4>Free Estimate</h4><p>We look at your setup and give you a clear written price. Free, no obligation.</p></div>
    <div class="step"><div class="num">3</div><h4>Done Right</h4><p>On-time, to-code work, permit pulled, cleaned up before we leave.</p></div>
  </div></div></section>
"""
    html += footer()
    open(os.path.join(BASE,fname),"w",encoding="utf-8").write(html)
    return fname

# ---------------------------------------------------------------- run
import datetime, shutil
for _old in ["service-generator-installation.html"]:          # servico removido (reuniao 19/09)
    if os.path.exists(os.path.join(BASE,_old)): os.remove(os.path.join(BASE,_old))

made = [build_home()]
for s in SERVICES: made.append(build_service(s))
for c in CITIES: made.append(build_city(c))
build_thankyou()   # fora do sitemap (noindex)

# WebP: gera .webp ao lado de cada jpg/png e serve WebP nas <img> e no CSS (og:image/schema seguem em jpg)
import re as _re, subprocess as _sp
IMG_DIR = os.path.join(BASE,"assets","img")
for f in os.listdir(IMG_DIR):
    if not _re.search(r"\.(jpe?g|png)$", f, _re.I) or f == "favicon.png": continue
    src = os.path.join(IMG_DIR,f); dst = _re.sub(r"\.(jpe?g|png)$", ".webp", src, flags=_re.I)
    if not os.path.exists(dst) or os.path.getmtime(dst) < os.path.getmtime(src):
        _sp.run(["cwebp","-quiet","-q","80","-m","6","-mt",src,"-o",dst], check=True)
def _to_webp(m):
    w = _re.sub(r"\.(jpe?g|png)$", ".webp", m.group(2), flags=_re.I)
    return m.group(1) + (w if os.path.exists(os.path.join(BASE,w)) else m.group(2)) + m.group(3)
for f in os.listdir(BASE):
    if f.endswith(".html"):
        fp = os.path.join(BASE,f); h = open(fp,encoding="utf-8").read()
        h2 = _re.sub(r'(<img\b[^>]*?\bsrc=")(assets/img/[^"]+\.(?:jpe?g|png))(")', _to_webp, h)
        if h2 != h: open(fp,"w",encoding="utf-8").write(h2)
_css = os.path.join(BASE,"assets","css","style.css"); _c = open(_css,encoding="utf-8").read()
_c2 = _re.sub(r"(url\('\.\./img/)([^']+)\.(?:jpe?g|png)('\))", r"\1\2.webp\3", _c)
if _c2 != _c: open(_css,"w",encoding="utf-8").write(_c2)

# titulos <= 60 caracteres (entidades contam 1)
import html as _h
for s in SERVICES:
    if len(_h.unescape(s["title"])) > 60: print("  AVISO title > 60:", _h.unescape(s["title"]))

# sitemap + robots
today = datetime.date.today().isoformat()
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for m in made:
    u = f"{SITE}/" if m=="index.html" else f"{SITE}/{m}"
    pr = "1.0" if m=="index.html" else ("0.9" if m.startswith("service-") else "0.8")
    sm += f'  <url><loc>{u}</loc><lastmod>{today}</lastmod><changefreq>weekly</changefreq><priority>{pr}</priority></url>\n'
sm += '</urlset>\n'
open(os.path.join(BASE,"sitemap.xml"),"w").write(sm)
open(os.path.join(BASE,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nDisallow: /contact.php\n\nSitemap: {SITE}/sitemap.xml\n")

# _dist = pasta final pronta pra public_html (so o que e publicavel)
DIST = os.path.join(BASE, "_dist")
if os.path.isdir(DIST): shutil.rmtree(DIST)
os.makedirs(DIST)
for f in sorted(os.listdir(BASE)):
    if f.endswith(".html") or f in ("sitemap.xml","robots.txt","contact.php",".htaccess"):
        shutil.copy2(os.path.join(BASE,f), os.path.join(DIST,f))
shutil.copytree(os.path.join(BASE,"assets"), os.path.join(DIST,"assets"),
    ignore=shutil.ignore_patterns(".DS_Store","*.ceu.json","logo-lockup-white.png","logo-bulb.png"))
EMAIL_SRC = os.path.normpath(os.path.join(BASE,"..","design","assinatura-email"))
os.makedirs(os.path.join(DIST,"email"))
for f in ("logo-julio.png","banner-julio.jpg"):
    shutil.copy2(os.path.join(EMAIL_SRC,f), os.path.join(DIST,"email",f))

print(f"OK: {len(made)} paginas no sitemap + thank-you.html (noindex)")
print("  home: index.html")
print(f"  servicos ({len(SERVICES)}): " + ", ".join(f"service-{s['slug']}.html" for s in SERVICES))
print(f"  regioes ({len(CITIES)}): " + ", ".join(f"{c['slug']}" for c in CITIES))
print("  + sitemap.xml, robots.txt, _dist/ (public_html + email/)")
