# -*- coding: utf-8 -*-
"""Generate static product detail pages into ../product/"""
from pathlib import Path
import html

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "product"

SHARED_DELIVERY = """<section class="section-light product-detail-band" id="delivery">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Delivery</span>
          <h2 class="serif">We go where your buildings are.</h2>
          <p>
            Same-day delivery for most Manhattan orders placed before noon. Serving all five boroughs with no big-box runaround —
            <a href="../index.html#delivery">read more about coverage</a>.
          </p>
        </div>
      </div>
    </section>"""

SHARED_PROCESS = """<section class="process product-detail-process" id="process">
      <div class="container">
        <div class="process-top">
          <div>
            <span class="eyebrow">How we work</span>
            <h2 class="serif">Simple, fast, and built around building emergencies.</h2>
          </div>
          <p>
            Call with what you need — we confirm stock, pack for your building, and deliver fast.
          </p>
        </div>
        <div class="steps-grid product-detail-steps">
          <article class="step">
            <div class="step-number">01</div>
            <h4>Call</h4>
            <p>Tell us the building, the timeline, and the part you need.</p>
          </article>
          <article class="step">
            <div class="step-number">02</div>
            <h4>Confirm</h4>
            <p>We verify inventory or source quickly from trusted vendors.</p>
          </article>
          <article class="step">
            <div class="step-number">03</div>
            <h4>Pack</h4>
            <p>Orders are labeled for service entrances, bulk rooms, or job sites.</p>
          </article>
          <article class="step">
            <div class="step-number">04</div>
            <h4>Deliver</h4>
            <p>Same-day options across most of NYC for orders placed early.</p>
          </article>
        </div>
      </div>
    </section>"""

SHARED_CTA = """<section class="shop-cta">
      <div class="container">
        <div class="shop-cta-inner section-head">
          <span class="eyebrow">Questions?</span>
          <h2 class="serif">Call for stock check and delivery windows.</h2>
          <p>(212) 756-1225 · hello@brownstonesupplyco.com</p>
          <a class="button button-primary" href="../index.html#contact">Contact us</a>
        </div>
      </div>
    </section>"""

FOOTER = """<footer class="shop-page-footer" id="contact">
      <div class="container">
        <div class="site-footer">
          <div>
            <a class="brand" href="../index.html#home">
              <div class="brand-mark">B</div>
              <div>
                <p class="brand-title">BROWNSTONE</p>
                <p class="brand-subtitle">Built for the buildings that built New York.</p>
              </div>
            </a>
            <p>
              Hardware, electrical, cleaning supplies, garbage bags, and building essentials delivered fast across Manhattan and the five boroughs.
            </p>
          </div>
          <div>
            <h4>Navigate</h4>
            <ul>
              <li><a href="../index.html#home">Home</a></li>
              <li><a href="../products.html">Products</a></li>
              <li><a href="../index.html#delivery">Delivery</a></li>
              <li><a href="../about-us/">About Us</a></li>
              <li><a href="../index.html#contact">Contact</a></li>
            </ul>
          </div>
          <div>
            <h4>We Carry</h4>
            <ul>
              <li>Hardware &amp; Tools</li>
              <li>Electrical Supplies</li>
              <li>Cleaning Products</li>
              <li>Garbage Bags</li>
              <li>Building Essentials</li>
            </ul>
          </div>
          <div>
            <h4>Contact</h4>
            <ul>
              <li>(212) 756-1225</li>
              <li>hello@brownstonesupplyco.com</li>
              <li>brownstonesupplyco.com</li>
              <li>Manhattan, New York City</li>
            </ul>
          </div>
        </div>
        <div class="footer-bottom">
          <p>© 2026 Brownstone Supply Co. · Manhattan, NYC · All Rights Reserved</p>
          <p>brownstonesupplyco.com</p>
        </div>
      </div>
    </footer>"""

STICKY_NAV = """<div class="sticky-nav" aria-hidden="true">
    <div class="container">
      <a class="brand" href="../index.html#home">
        <div class="brand-mark">B</div>
        <div>
          <p class="brand-title">BROWNSTONE</p>
          
        </div>
      </a>
      <nav class="nav-links">
        <a href="../index.html#home">Home</a>
        <a href="../products.html" aria-current="page">Products</a>
        <a href="../index.html#delivery">Delivery</a>
        <a href="../about-us/">About</a>
        <a href="../contact/" class="button button-primary">Contact</a>
      </nav>
      <button class="mobile-menu-toggle" type="button" data-mobile-menu-toggle aria-label="Open menu" aria-controls="mobile-menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>"""

HERO_NAV = """<div class="hero-nav">
      <div class="container">
        <a class="brand" href="../index.html#home">
          <div class="brand-mark">B</div>
          <div>
            <p class="brand-title">BROWNSTONE</p>
            
          </div>
        </a>
        <nav class="nav-links">
          <a href="../index.html#home">Home</a>
          <a href="../products.html" aria-current="page">Products</a>
          <a href="../index.html#delivery">Delivery</a>
          <a href="../about-us/">About</a>
          <a href="../contact/" class="button button-primary">Contact</a>
        </nav>
        <button class="mobile-menu-toggle" type="button" data-mobile-menu-toggle aria-label="Open menu" aria-controls="mobile-menu" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>"""

MOBILE_MENU = """<div class="mobile-menu" id="mobile-menu" hidden>
    <button class="mobile-menu__backdrop" type="button" data-mobile-menu-close aria-label="Close menu"></button>
    <nav class="mobile-menu__panel" aria-label="Mobile menu">
      <button class="mobile-menu__close" type="button" data-mobile-menu-close aria-label="Close menu">&times;</button>
      <a class="mobile-menu__link" href="../index.html#home">Home</a>
      <a class="mobile-menu__link" href="../products.html">Products</a>
      <a class="mobile-menu__link" href="../index.html#delivery">Delivery</a>
      <a class="mobile-menu__link" href="../about-us/">About</a>
      <a class="mobile-menu__link button button-primary" href="../contact/">Contact</a>
    </nav>
  </div>"""


def page_html(p):
    title_esc = p["title_html"]
    meta = html.escape(p["meta_desc"])
    slug = p["slug"]
    paras = "".join(f"<p>{html.escape(x)}</p>" for x in p["paragraphs"])
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title_esc} | Brownstone Supply Co.</title>
  <meta name="description" content="{meta}">
  <link rel="stylesheet" href="../styles.css">
</head>
<body class="page-products page-product-detail">
  {STICKY_NAV}
  {MOBILE_MENU}

  <header class="hero hero--page product-detail-page-hero" id="top">
    {HERO_NAV}
    <div class="hero-content hero-content--page">
      <div class="container">
        <span class="eyebrow">Product</span>
        <h1 class="serif product-detail-page-title">{title_esc}</h1>
        <p class="product-detail-lead">{html.escape(p["lead"])}</p>
      </div>
    </div>
  </header>

  <main class="shop-page shop-page--light">
    <article class="product-detail-article">
      <div class="container product-detail-layout">
        <div class="product-detail-media">
          <img src="{p["img"]}" alt="{html.escape(p["alt"])}" width="900" height="675" loading="eager">
        </div>
        <div class="product-detail-copy">
          <div class="product-detail-long">
            {paras}
          </div>
          <div class="product-detail-actions">
            <button type="button" class="product-detail-order-btn" aria-label="Order via WhatsApp">Order now</button>
          </div>
        </div>
      </div>
    </article>

    {SHARED_DELIVERY}
    {SHARED_PROCESS}
    {SHARED_CTA}

    {FOOTER}
  </main>

  <a class="whatsapp-float" href="https://wa.me/38345689914" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp">
    <svg class="whatsapp-float__icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
      <path fill="currentColor" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
    </svg>
  </a>
  <a href="#top" class="back-to-top" aria-label="Back to top">↑</a>

  <script>
    document.body.classList.add("js-ready");
    const stickyNav = document.querySelector(".sticky-nav");
    const toggleStickyNav = () => {{
      if (!stickyNav) return;
      const shouldShow = window.scrollY > 110;
      stickyNav.classList.toggle("is-visible", shouldShow);
      stickyNav.setAttribute("aria-hidden", shouldShow ? "false" : "true");
    }};
    window.addEventListener("scroll", toggleStickyNav, {{ passive: true }});
    window.addEventListener("load", toggleStickyNav);
    toggleStickyNav();

    const mobileMenu = document.getElementById("mobile-menu");
    const mobileToggles = Array.from(document.querySelectorAll("[data-mobile-menu-toggle]"));
    const mobileClose = Array.from(document.querySelectorAll("[data-mobile-menu-close], .mobile-menu__link"));
    const setMobileExpanded = (expanded) => {{
      mobileToggles.forEach((btn) => btn.setAttribute("aria-expanded", expanded ? "true" : "false"));
    }};
    const openMobileMenu = () => {{
      if (!mobileMenu) return;
      mobileMenu.hidden = false;
      requestAnimationFrame(() => mobileMenu.classList.add("is-open"));
      document.body.classList.add("mobile-menu-open");
      setMobileExpanded(true);
    }};
    const closeMobileMenu = () => {{
      if (!mobileMenu) return;
      mobileMenu.classList.remove("is-open");
      document.body.classList.remove("mobile-menu-open");
      setMobileExpanded(false);
      setTimeout(() => {{
        if (!mobileMenu.classList.contains("is-open")) mobileMenu.hidden = true;
      }}, 280);
    }};
    mobileToggles.forEach((btn) => btn.addEventListener("click", openMobileMenu));
    mobileClose.forEach((el) => el.addEventListener("click", closeMobileMenu));
    document.addEventListener("keydown", (e) => {{
      if (e.key === "Escape") closeMobileMenu();
    }});

    const orderBtn = document.querySelector(".product-detail-order-btn");
    if (orderBtn) {{
      orderBtn.addEventListener("click", () => {{
        const pageUrl = window.location.href;
        const msg = "Hello, I'm interested in this product: " + pageUrl;
        const waUrl = "https://wa.me/38345689914?text=" + encodeURIComponent(msg);
        window.open(waUrl, "_blank", "noopener,noreferrer");
      }});
    }}
  </script>
</body>
</html>
"""


PRODUCTS = [
    {
        "slug": "screws-nails-anchors",
        "title_html": "Screws, nails &amp; anchors",
        "category": "Hardware &amp; Tools",
        "category_id": "hardware-tools",
        "img": "https://images.unsplash.com/photo-1504148455328-c376907d081c?auto=format&fit=crop&w=1200&q=80",
        "alt": "Screws, nails and anchors on a work surface",
        "lead": "Fasteners for concrete, wood, and metal — stocked so your crew never waits on the right anchor for the substrate.",
        "meta_desc": "Screws, nails and anchors for NYC buildings — tap-to-substrate matching, contractor packs, same-day Manhattan delivery.",
        "paragraphs": [
            "From tapcons and sleeve anchors to finish screws and brads, we stock the fastener lines supers and contractors reach for on occupied buildings. Tell us your substrate and torque requirements — we help you avoid stripped heads, wrong thread pitch, and code surprises on corridor and unit work.",
            "Bulk packs and repeat SKUs are easy to reorder once your building profile is on file. We coordinate drops to service entrances, freight elevators, and job-site staging so your team spends less time chasing parts between floors.",
            "Ask about corrosion-resistant options for wet walls, exterior envelopes, and mechanical rooms where humidity and vibration matter as much as pull-out strength.",
        ],
    },
    {
        "slug": "hand-power-tools",
        "title_html": "Hand &amp; power tools",
        "category": "Hardware &amp; Tools",
        "category_id": "hardware-tools",
        "img": "https://images.unsplash.com/photo-1452860606245-08befc0ff44b?auto=format&fit=crop&w=1200&q=80",
        "alt": "Hand and power tools in a workshop",
        "lead": "Curated drivers, saws, and drills for daily maintenance and quick repairs in occupied buildings.",
        "meta_desc": "Hand and power tools for NYC property maintenance — drivers, drills, saws, and jobsite-ready accessories.",
        "paragraphs": [
            "We focus on tools that fit mechanical closets, tight risers, and punch-list work where noise and footprint matter. Cordless platforms, compact circ saws, and impact sets are chosen for durability under daily use — not big-box hobby kits.",
            "Replacement batteries, blades, and bits ship with the same urgency as the tool itself. Call with your preferred voltage platform and we will confirm what is on the shelf or arriving same day from our vendor network.",
            "Property teams can standardize on a single battery line across porters and handymen to simplify charging rooms and spare inventory.",
        ],
    },
    {
        "slug": "locks-door-hardware",
        "title_html": "Locks &amp; door hardware",
        "category": "Hardware &amp; Tools",
        "category_id": "hardware-tools",
        "img": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?auto=format&fit=crop&w=1200&q=80",
        "alt": "Door lock and hardware",
        "lead": "Cylinders, mortise sets, and exit devices aligned with multifamily and commercial door schedules.",
        "meta_desc": "Locks and door hardware for NYC multifamily — cylinders, mortise locks, exit devices, and schedule-friendly replacements.",
        "paragraphs": [
            "Door hardware is where code, security, and turnover speed meet. We stock common cylinder formats, mortise bodies, and panic hardware patterns that match existing door prep on prewar and modern frames — reducing field modification and rehang time.",
            "Bring your door schedule or a photo of the existing prep — we help match backset, strike, and through-bolt patterns so supers do not burn a day on wrong parts.",
            "Master-keying discussions stay between your locksmith and building security; we supply material to spec and deliver to your lock vendor or on-site team as you prefer.",
        ],
    },
    {
        "slug": "pliers-wrenches-more",
        "title_html": "Pliers, wrenches &amp; more",
        "category": "Hardware &amp; Tools",
        "category_id": "hardware-tools",
        "img": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=1200&q=80",
        "alt": "Pliers and wrenches",
        "lead": "Grip, torque, and cutting tools sized for mechanical closets, risers, and tight service spaces.",
        "meta_desc": "Pliers, wrenches, and hand tools for NYC building maintenance — tight-space sets and contractor-grade quality.",
        "paragraphs": [
            "Channel locks, adjustable wrenches, mini bolt cutters, and insulated pliers are the everyday layer under your power tools. We stock lengths and jaw profiles that fit real NYC closets — not oversized garage sets.",
            "When a riser valve or hose bib needs torque without marring finish, the right wrench saves callbacks. Tell us your typical pipe sizes and we will suggest a compact kit that covers most of your corridor work.",
            "Replacement jaws, grips, and lanyard-ready tools are available for teams working at height or over open shafts.",
        ],
    },
    {
        "slug": "outlets-switches-covers",
        "title_html": "Outlets, switches &amp; covers",
        "category": "Electrical Supplies",
        "category_id": "electrical",
        "img": "https://images.unsplash.com/photo-1431540015161-0bf868a2d407?auto=format&fit=crop&w=1200&q=80",
        "alt": "Electrical outlets and switches",
        "lead": "Commercial-grade receptacles, switches, and wall plates for common corridors and unit refreshes.",
        "meta_desc": "Electrical outlets, switches, and wall plates for NYC buildings — spec-grade devices and fast replenishment.",
        "paragraphs": [
            "Spec-grade receptacles and switches hold up in high-cycle common areas and turnover units where residents plug and unplug constantly. We match decorator and standard profiles so corridor refreshes stay visually consistent floor to floor.",
            "Wall plates in common finishes reduce punch-list friction when supers replace single devices. Bring your existing part numbers or photos and we will align manufacturer and color lines.",
            "GFCI and tamper-resistant requirements evolve by occupancy type — call with your use case and we will steer you toward compliant device families electricians already trust on your jobs.",
        ],
    },
    {
        "slug": "light-bulbs-fixtures",
        "title_html": "Light bulbs &amp; fixtures",
        "category": "Electrical Supplies",
        "category_id": "electrical",
        "img": "https://images.unsplash.com/photo-1513506003901-1e6a229e2d15?auto=format&fit=crop&w=1200&q=80",
        "alt": "Light bulbs and lighting",
        "lead": "LED lamping and retrofit-friendly options that keep halls bright and energy reports predictable.",
        "meta_desc": "LED bulbs and fixtures for NYC multifamily — retrofit lamping, corridor lighting, energy-friendly options.",
        "paragraphs": [
            "Corridor and stair lighting is where energy audits and resident safety intersect. We stock LED A-line, BR, and linear tubes in color temperatures that match existing fixtures so supers can swap without re-bidding the whole building.",
            "Emergency and exit-adjacent lamping has stricter rules — tell us your fixture types and backup strategy so we do not mix consumer-grade lamps into life-safety paths.",
            "Bulk cases and labeled deliveries to electrical closets keep porters from guessing which box belongs to which floor.",
        ],
    },
    {
        "slug": "wire-cable-conduit",
        "title_html": "Wire, cable &amp; conduit",
        "category": "Electrical Supplies",
        "category_id": "electrical",
        "img": "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=1200&q=80",
        "alt": "Electrical wire and cable",
        "lead": "Copper runs, MC cable, and low-voltage supplies for licensed electricians on your approved-vendor list.",
        "meta_desc": "Wire, cable, and conduit for NYC electrical work — copper, MC, low-voltage, and jobsite quantities.",
        "paragraphs": [
            "Romex, THHN, MC, and flexible armored runs are staged for small repairs and fit-out patches — not just full rewires. We cut to length where possible to reduce scrap on congested job sites.",
            "Low-voltage for access control, intercom upgrades, and camera drops moves fast when you standardize on a few jacket colors and pair counts. Ask about fire-rated plenum vs riser when you are above a ceiling line.",
            "Conduit, bushings, and connectors ship with the wire so your electrician is not short one fitting at 4pm.",
        ],
    },
    {
        "slug": "breakers-panels",
        "title_html": "Breakers &amp; panels",
        "category": "Electrical Supplies",
        "category_id": "electrical",
        "img": "https://images.unsplash.com/photo-1484154218962-a197022b5858?auto=format&fit=crop&w=1200&q=80",
        "alt": "Electrical panel and breakers",
        "lead": "Compatible breakers, blanks, and panel accessories for safe service upgrades and troubleshooting.",
        "meta_desc": "Circuit breakers and panel accessories for NYC buildings — matched brands, safe replacements, fast delivery.",
        "paragraphs": [
            "Breaker compatibility is non-negotiable — wrong series trips late or not at all. Send panel model and existing breaker photos; we match manufacturer series and ampacity before anything leaves the shelf.",
            "Blanks, filler plates, and grounding bars keep panels neat and inspectable after changes. We stock the small parts that prevent a half-finished electrical closet.",
            "For larger panel projects, coordinate with your licensed electrician — we supply material to their cut list and delivery window.",
        ],
    },
    {
        "slug": "floor-cleaners-mops",
        "title_html": "Floor cleaners &amp; mops",
        "category": "Cleaning Supplies",
        "category_id": "cleaning",
        "img": "https://images.unsplash.com/photo-1581578731548-c64695cc6952?auto=format&fit=crop&w=1200&q=80",
        "alt": "Floor cleaning and mops",
        "lead": "PH-balanced solutions and commercial mop systems for stone, tile, and resilient surfaces.",
        "meta_desc": "Floor cleaners and mops for NYC buildings — commercial formulas, stone-safe options, janitor closet refills.",
        "paragraphs": [
            "Lobby stone, corridor VCT, and unit LVT all punish the wrong chemistry. We stock neutral cleaners, degreasers, and finish strippers sized for janitor closets that do not have room for a dozen half-used jugs.",
            "Flat mops, loop-end wet mops, and microfiber systems reduce streaking in high-gloss lobbies where residents notice every footprint.",
            "Dilution charts and SDS sheets ship with first orders so new porters train consistently building to building.",
        ],
    },
    {
        "slug": "disinfectants-sprays",
        "title_html": "Disinfectants &amp; sprays",
        "category": "Cleaning Supplies",
        "category_id": "cleaning",
        "img": "https://images.unsplash.com/photo-1460317442991-0ec209397118?auto=format&fit=crop&w=1200&q=80",
        "alt": "Disinfectant sprays and bottles",
        "lead": "Hospital-grade and EPA-listed options for elevators, mailrooms, and high-touch fixtures.",
        "meta_desc": "Disinfectants and sprays for NYC multifamily — EPA-listed products for high-touch and back-of-house use.",
        "paragraphs": [
            "Elevator panels, door pulls, and mail slots see thousands of touches a week. We carry concentrates and ready-to-use bottles that fit your porters’ carts and your building’s safety data requirements.",
            "Fragrance-sensitive residents matter — ask about low-odor formulations for interior corridors.",
            "Refill sizes reduce plastic waste when your team is trained on consistent dilution and labeling.",
        ],
    },
    {
        "slug": "paper-towels-dispensers",
        "title_html": "Paper towels &amp; dispensers",
        "category": "Cleaning Supplies",
        "category_id": "cleaning",
        "img": "https://images.unsplash.com/photo-1628177142898-93e36e4e3a50?auto=format&fit=crop&w=1200&q=80",
        "alt": "Paper towels and dispensers",
        "lead": "Jumbo rolls, folded towels, and compatible dispensers for supers’ closets and amenity restrooms.",
        "meta_desc": "Paper towels and dispensers for NYC buildings — jumbo rolls, folded towels, key-compatible refills.",
        "paragraphs": [
            "Nothing burns a super’s budget faster than the wrong roll for the installed dispenser. Send a photo of the cabinet — we match core size, sheet length, and adapter needs so refills slide in without jamming.",
            "Amenity restrooms and service corridors have different traffic — we split case packs so you are not storing six months of towels in a closet built for two.",
            "Touchless upgrade paths exist for many standard cabinets; ask when you are refreshing restrooms on a floor-by-floor schedule.",
        ],
    },
    {
        "slug": "gloves-ppe",
        "title_html": "Gloves &amp; PPE",
        "category": "Cleaning Supplies",
        "category_id": "cleaning",
        "img": "https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?auto=format&fit=crop&w=1200&q=80",
        "alt": "Protective gloves",
        "lead": "Nitrile and latex-alternative gloves plus basic PPE for porters, maintenance, and turnover crews.",
        "meta_desc": "Gloves and PPE for NYC building staff — nitrile, latex-free, and basic protection for maintenance work.",
        "paragraphs": [
            "Glove sizing and cuff length matter when staff work drains, compactors, and paint touch-ups all in one shift. We stock cases in common sizes so closets are not empty on the day a bigger job lands.",
            "Basic eye protection, dust masks, and disposable coveralls rotate fast during turnovers — bundle sizes match typical unit counts per month.",
            "Latex sensitivity is common — we default to nitrile unless you specify otherwise.",
        ],
    },
    {
        "slug": "heavy-duty-contractor-bags",
        "title_html": "Heavy-duty contractor bags",
        "category": "Garbage &amp; bags",
        "category_id": "garbage-essentials",
        "img": "https://images.unsplash.com/photo-1604187351574-c75ca79f5807?auto=format&fit=crop&w=1200&q=80",
        "alt": "Heavy garbage bags",
        "lead": "High-mil black bags for construction debris, metal scrap, and loads that would tear standard liners.",
        "meta_desc": "Heavy-duty contractor bags for NYC jobsites and buildings — high-mil strength, bulk cases, delivery to service entrances.",
        "paragraphs": [
            "Renovation floors and punch-list days generate sharp debris and dense loads. Our contractor bags are rated for puncture resistance you will not get from kitchen liners — fewer split bags in elevators and compactor rooms.",
            "Fluorescent sizing labels help porters grab the right roll without opening three cases in a crowded closet.",
            "Same-day restock matters when a Friday job runs long — call before noon when Manhattan traffic still allows a second drop.",
        ],
    },
    {
        "slug": "kitchen-desk-recycling-compost-liners",
        "title_html": "Kitchen, desk, recycling, and compost liners",
        "category": "Garbage &amp; bags",
        "category_id": "garbage-essentials",
        "img": "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?auto=format&fit=crop&w=1200&q=80",
        "alt": "Trash liners and recycling",
        "lead": "Sized rolls for chutes, desk-side bins, and sorting programs that keep waste rooms organized.",
        "meta_desc": "Trash and recycling liners for NYC multifamily — chute bags, desk liners, compost-compatible options.",
        "paragraphs": [
            "Chute lines need consistent sizing — too small and bags fall; too large and they jam. We map your chute door dimensions to the right gallon rating and thickness so supers are not guessing at the big-box aisle.",
            "Desk-side and recycling totes for management offices rotate on a different cadence than tenant trash — split SKUs keep accounting clean.",
            "Pilot compost programs need liners that breathe right for organics pickup — ask what your hauler accepts before you standardize.",
        ],
    },
    {
        "slug": "caulk-tape-patching-supplies",
        "title_html": "Caulk, tape, patching supplies",
        "category": "Garbage &amp; bags",
        "category_id": "garbage-essentials",
        "img": "https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=1200&q=80",
        "alt": "Caulk and tape supplies",
        "lead": "Sealants, painter’s tape, and patch kits for quick turnovers between tenants.",
        "meta_desc": "Caulk, tape, and patching supplies for NYC turnovers — sealants, tapes, spackle kits for fast unit prep.",
        "paragraphs": [
            "Turnover week is a race between paint, patch, and punch list. We bundle painter’s tape, lightweight spackle, and sandpaper grits that match your supers’ usual workflow — fewer trips to the closet mid-unit.",
            "Silicone and latex sealants are not interchangeable at tubs and perimeter gaps — tell us moisture level and paint schedule so we steer you right.",
            "Small-batch orders are normal — you should not buy a case of caulk for one bathroom refresh.",
        ],
    },
    {
        "slug": "plumbing-fittings-safety-signage",
        "title_html": "Plumbing fittings, safety, and signage",
        "category": "Garbage &amp; bags",
        "category_id": "garbage-essentials",
        "img": "https://images.unsplash.com/photo-1514565131-fce0801e5785?auto=format&fit=crop&w=1200&q=80",
        "alt": "Plumbing fittings and tools",
        "lead": "Common brass and PVC fittings plus safety markers and code-friendly signage for service routes.",
        "meta_desc": "Plumbing fittings, safety items, and signage for NYC buildings — service-route essentials in one call.",
        "paragraphs": [
            "Mixed-material buildings need mixed fittings — compression for quick stops, PVC for drain repairs, and brass for older risers. We stock the intersection parts supers grab before the licensed plumber arrives for the final joint.",
            "Temporary signage keeps residents out of active work zones; photoluminescent and reflective options match DOB-visible paths where required.",
            "Bundling signage with your fittings order saves a second truck when Friday service windows are tight.",
        ],
    },
    {
        "slug": "caulk-sealants-tape",
        "title_html": "Caulk, sealants &amp; tape",
        "category": "Building Essentials",
        "category_id": "building-essentials",
        "img": "https://images.unsplash.com/photo-1448630360428-65456885c650?auto=format&fit=crop&w=1200&q=80",
        "alt": "Maintenance supplies and tools",
        "lead": "Interior and exterior sealants plus tapes for drafts, perimeter gaps, and finish transitions.",
        "meta_desc": "Caulk, sealants, and tape for NYC buildings — weather sealing, interior finishes, bulk and small orders.",
        "paragraphs": [
            "Perimeter air sealing pays back in HVAC load and resident comfort. We stock low-VOC interior caulks and durable exterior formulas that survive freeze-thaw on brick and stone facades common in brownstone stock.",
            "Foam, butyl, and foil tapes each have a place — window bucks, curtain-wall transitions, and mechanical penetrations. Photos of your gap profile help us narrow the line before you buy three wrong rolls.",
            "Color-matched caulks reduce punch lists on millwork-heavy units.",
        ],
    },
    {
        "slug": "paint-patching-supplies",
        "title_html": "Paint &amp; patching supplies",
        "category": "Building Essentials",
        "category_id": "building-essentials",
        "img": "https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&w=1200&q=80",
        "alt": "Paint cans and supplies",
        "lead": "Touch-up gallons, spackle, sandpaper, and mini-rollers for fast cosmetic work between leases.",
        "meta_desc": "Paint and patching supplies for NYC unit turnovers — touch-up paint, spackle, rollers, same-day delivery.",
        "paragraphs": [
            "Carrying every wall color on site is impossible — we help you standardize a building palette and keep touch-up quarts labeled by floor and line. When a tenant leaves scuffs, porters match faster.",
            "Spackle drying time drives whether you paint same-day — lightweight vs setting-type matters on deep nail pops.",
            "Mini-rollers and angled brushes in contractor packs reduce waste when three units turn in one week.",
        ],
    },
    {
        "slug": "plumbing-fittings",
        "title_html": "Plumbing fittings",
        "category": "Building Essentials",
        "category_id": "building-essentials",
        "img": "https://images.unsplash.com/photo-1581244277943-fe4a9c777189?auto=format&fit=crop&w=1200&q=80",
        "alt": "Plumbing pipes and fittings",
        "lead": "Compression, push-fit, and threaded fittings for leak repairs without a full material order.",
        "meta_desc": "Plumbing fittings for NYC repairs — compression, push-fit, threaded, and emergency stock.",
        "paragraphs": [
            "Stop leaks before they hit the unit below — we stock the fittings supers can legally install on shut-off repairs while your plumber schedules the permanent fix.",
            "Push-fit speeds work in tight cabinets; compression fits older chrome stops — bring photos so we do not mix threads.",
            "Teflon, pipe dope, and thread sealant ship in small quantities so nothing expires on the shelf.",
        ],
    },
    {
        "slug": "safety-signage",
        "title_html": "Safety &amp; signage",
        "category": "Building Essentials",
        "category_id": "building-essentials",
        "img": "https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=1200&q=80",
        "alt": "Building hallway and safety lighting",
        "lead": "Exit signs, floor marking tape, and directional plaques to keep paths legible during work.",
        "meta_desc": "Safety and signage for NYC buildings — exit signs, floor tape, directional markers for corridors and work zones.",
        "paragraphs": [
            "During façade or boiler work, residents still need clear egress. Battery exit signs, A-frame warnings, and photoluminescent tape bridge the gap between code drawings and real-world foot traffic.",
            "Floor marking tape survives rolling loads in service corridors better than consumer tape — we stock widths that match typical stripe guns.",
            "Custom plaques take longer — call early if your lobby refresh includes suite renumbering.",
        ],
    },
]


def main():
    OUT.mkdir(exist_ok=True)
    for p in PRODUCTS:
        p = {**p, "title": p["title_html"].replace("&amp;", "&").replace("&#39;", "'")}
        out_path = OUT / f"{p['slug']}.html"
        out_path.write_text(page_html(p), encoding="utf-8")
        print("Wrote", out_path.relative_to(ROOT))


if __name__ == "__main__":
    main()
