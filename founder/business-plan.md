# Turbolux Home Finish (working name): the paint + painter package · Business plan

**Verdict: Not yet**

> **How to read the numbers in this plan:** every amount is **Indian rupees (₹)**, even where the tools print `$`. Volumes are **per month**: every "a day" from the tools means "a month", because `days_per_month` is 1. The price per job is **before 18% GST**: ₹75,423.73 = ₹89,000 to the buyer. The idea section below is the original pitch at ₹78,000; the current offer and prices are in the Offer and Pricing sections. Most costs are estimates (`cfo-sources.md`). The buyer panel is simulated.

- ✓ Each job earns $14308.73 before fixed costs (19% contribution).
- ✗ Year 1 operating LOSS: $905,057.
- ✓ Break-even is 15 jobs a day against a capacity of 20.
- ✗ 4 of 20 simulated buyers buy (20%, the bar is 25%).

| key number | |
| --- | ---: |
| Price | $75423.73 a job |
| Profit margin at plan | 5% per job |
| Break-even | 15 jobs a day |
| Year 1 operating profit | $-905,057 |
| Startup spend | $800,000 |
| Cash needed before it pays for itself | $1,840,389 |
| Startup money earned back | not in year 1 |
| Buyer panel | 4 buy · 16 pass |

## The idea

- What it is: Turbolux Paints sells a complete 2BHK repaint as one fixed-price package, with Turbolux paint plus a vetted, Turbolux-trained painter crew booked in one order, a fixed finish date and a workmanship guarantee against bubbling and peeling.
- Who it is for: homeowners in Kochi with a 2BHK house or flat who want to repaint after the monsoon (Sept to Jan season) and don't want to find, manage and check a contractor themselves.
- What it sells, at what price: a premium 2BHK full repaint (interior + exterior, premium finish). Working price ₹78,000 per 2BHK, including paint, labour, surface preparation and the guarantee. The founder chose the "over ₹70,000" bracket; ₹78,000 is a working number that `/founder-pricing` will test.
- Where and how: pilot in Kochi only. Sold on turboluxpaints.com (booking + site visit) and through Turbolux dealers in Kochi. A site visit confirms scope, then a crew does the job on a fixed schedule.
- Budget and constraints: launch budget not set yet; the CFO uses clearly labelled estimates until real figures are in. Turbolux is an existing paint brand with its own products, dealers and a website with SEO blog content (e.g. on paint bubbling, how much paint a 2BHK needs, the best time to paint in Kerala). The season is fixed: post-monsoon, Sept to Jan.

## Summary

**Verdict: NOT YET.** It is computed by `compile.py` from the numbers, not written by hand. Two of four checks fail:
- **Year 1 operating loss of ₹9.05 lakh.**
- **20% of simulated buyers buy**, against a 25% bar.

The unit works: each job earns ₹14,309 before fixed costs, and break-even (14.3 jobs a month) fits inside capacity (20).

### What has to change first

1. **The year 1 loss: fix the cost of a job, not the volume.** On the CFO's tool, three changes together turn year 1 to an operating profit of **+₹3.25 lakh** with a 19% margin at plan:
   - **Test the price at ₹95,000** (`pricing.md`).
   - **Agree a crew piece rate about 10% lower** in exchange for guaranteed volume to certified crews.
   - **Confirm Turbolux's real paint cost.** The estimate assumes 50% of retail; at 40% it adds ₹2,675 per job.

   None of the three works alone (`cfo.md`). Skills: `/founder-pricing`, `/founder-ops`, `/founder-cfo`.
2. **The buy rate: proof, not more bonuses.** The new offer lifted simulated buyers from 5% to 20% (`offer.md` §5). What still blocks the rest:
   - **The family painter** (6 of 16 no's). Answer: certify local painters as Turbolux crews.
   - **No finished homes in Kochi** (5). Answer: the founding homes.
   - **The guarantee doesn't cover damp** (5). Answer: price Damp Shield.
   - **Only some walls needed** (2). Answer: a partial-job option.

   Skills: `/founder-offer`, `/founder-ops`.

### What the business is

A fixed-price repaint of a Kochi 2BHK by a Turbolux-certified crew with Turbolux paint:
- **₹89,000** for an independent house, inside and out.
- **₹59,000** for a flat, inside only.

It comes with a written final price, a signed finish date with ₹2,000 off per late day, 70% paid only after the owner checks the work, one coordinator with daily WhatsApp photos, and a 3-year guarantee against bubbling and peeling.

It is for families with a **deadline** (a wedding or function) or a **distance** (the owner works in the Gulf and the parents live in the house).

### The three numbers

| | Value |
| --- | --- |
| Earned per job before fixed costs | ₹14,309 (19% of the ₹75,424 pre-GST price); 5% profit margin at the plan of 20 jobs a month |
| Break-even | 14.3 jobs a month, with capacity 20 (10 crews; a house takes ~13 working days) |
| Year 1 operating result | **−₹9.05 lakh** (−₹17.05 lakh after the ₹8 lakh startup); cash needed ₹18.4 lakh |

### Where the board, the buyers and the market agree, and where they don't

**They agree:**
- The crews are the business. All three board members, the ops plan and the buyers' top fear ("crews stop turning up halfway") point the same way.
- Proof matters more than promises. The board says likelihood is weakest; the buyers ask to see a finished home; the competitor complaints show promises slipping.
- Flats need their own product. The board predicted it, and four flat-owning buyers said so.

**They disagree:**
- The board's Offers and Product lenses called "the paint maker owns the result" the core strength. The Monopoly lens called it a copyable business model.
- The competitor scan sides with Monopoly: Asian Paints could match a published price plus a late-day credit within a season.
- The buyers mostly didn't mention who makes the paint. They cared about the date, the final price and paying after checking.

### The biggest risk and what will be done

**Crew reliability and capacity.** A no-show, or a job that runs past 13 days, breaks the one promise the brand is built on, and the damage lands on Turbolux paint as well.

What will be done (`ops.md` risks 1–2):
- a standby crew;
- part of the piece rate held back until handover;
- January's jobs timed room by room before any later date is signed;
- more crews certified than needed;
- dealers' own painters certified first.

### What is needed to start

- **Now:** about **₹60,000** for the founding-homes pre-sale test, 23 Nov – 13 Dec 2026 (`launch.md` §1). That buys 10 real bookings with 30% deposits, refundable.
- **If the test passes (≥ 6 paid bookings from ≥ 40 site visits):** cash of about **₹18.4 lakh** on today's estimates, or about **₹12 lakh** if the three changes above hold.

### The one thing to do this week

**Decide painter status (employee or independent crew) with the accountant, and set Turbolux's transfer price for paint, by Fri 20 Nov.** Both are on the critical path to job 1 on 4 January. They also replace the two biggest guesses in the numbers: the crew cost and the paint cost.

---

*The buyer panel is simulated and the numbers are projections built mostly on estimates. Real buyers (the founding-homes test) and real quotes confirm them. Not financial, legal or tax advice.*

## What the board said

**Vote: 3 FUND IF, 0 FUND, 0 PASS. Average score 5.7 / 10** (Offers 6, Monopoly 5, Product 6).

None of the three backed the idea as pitched, and none rejected it. All three would fund it once the crews, the fixed price and the dealer question are settled. The memos are in `founder/board/offers.md`, `monopoly.md` and `product.md`.

### Risks raised by more than one member (most dangerous first)

1. **The crews are the product, and they don't exist yet** (all three). The promise of a fixed date, no bubbling and a trained crew depends on painters who haven't been hired, trained or tested. Surface preparation is the first corner a rushed crew cuts in a short season. When it fails, it shows up months later as bubbling, under the Turbolux name, so the damage lands on the paint brand as well. Monopoly adds: trained crews can leave and do the same job cheaper themselves, and a Sept to Jan season leaves them idle the rest of the year.
2. **"A 2BHK" is not one fixed product, so the fixed price may break** (Offers, Product). Floor area, damp, cracks and access vary a lot. A flat owner usually doesn't control the exterior. Either margin leaks on the bad jobs, or the site visit re-quotes and "fixed price" stops being true.
3. **Conflict with dealers and contractors** (all three). Dealers sell paint to the contractors this package replaces. Those contractors influence which paint brand homeowners buy, so a hostile trade puts the core paint business at risk, not just the pilot.
4. **No proof yet, and easy to copy** (Offers, Monopoly). The weakest part of the offer is the buyer's belief that it will actually turn out well (Offers lens: likelihood 4/10). Any paint brand with dealers can copy the bundle, and another brand may already sell it in Kochi.

### Where they disagreed

- **Is the bundle an advantage?** Offers and Product see "one party owns the result" as the core strength: only the paint maker can credibly guarantee both the paint and the work. Monopoly calls it a business model, not a breakthrough, and wants evidence that Turbolux is *far* better on one dimension, not slightly better.
- **Scope.** Offers wants separate interior-only (flats) and interior + exterior (houses) packages. Product would go further and cut to one of them if prices keep changing at site visits. Monopoly is relaxed about scope, as long as the target share of the Kochi market can be measured.

### Conditions: the checklist for the rest of the pack

- [ ] **Price rule is written down.** Fixed price bands by size and condition, with interior-only (flats) separate from interior + exterior (houses). The site visit confirms the band and never raises it. Track how often a visit changes the band. *(/founder-offer, /founder-pricing)*
- [ ] **Margin at the price.** The package earns money after crew wages, paint at Turbolux's cost, the dealer's share and a guarantee reserve, in every band. *(/founder-cfo)*
- [ ] **A guarantee that can be paid out.** Plain terms: what it covers, how long, the remedy, response time. Costed at a realistic claim rate. Add a finish-date guarantee only if the numbers allow. *(/founder-offer, /founder-cfo)*
- [ ] **Buyers pay for certainty.** Kochi 2BHK owners value the fixed price, date and guarantee enough not to compare on price per square foot alone. *(/founder-consumer, /founder-pricing)*
- [ ] **A clear gap against competitors.** No other brand already owns this bundle in Kochi, or Turbolux is clearly far better on one named dimension. *(/founder-competitors)*
- [ ] **Dealers and painters as partners.** Dealers earn on each package. Good local painters can become certified Turbolux crews. *(/founder-ops, /founder-cfo)*
- [ ] **A crew model that keeps people.** Training, a written prep standard, a Turbolux check before paint goes on, photo records, and work beyond the season (e.g. interior-only jobs off-season). Costs go into the CFO's numbers. *(/founder-ops, /founder-cfo)*
- [ ] **One owner per customer**, from booking to guarantee claim. *(/founder-ops)*
- [ ] **Pilot before scale.** A small batch of real Kochi jobs, recording whether each finished on date, prep photos and reviews, before booking opens wider. *(/founder-launch)*
- [ ] **A target share** of the Kochi season, set once the market size is known. *(/founder-plan; market size needs outside data)*

### The strongest version the board can see

The pitch sells one "2BHK interior + exterior" package to everyone. The board sees a stronger business in two clearly priced products. The first is an **interior + exterior package for independent houses**, where the owner controls the walls and the post-monsoon damp is worst. The second is an **interior-only package for flats**. Both use published size and condition bands, so the price really is fixed. The jobs are done by **existing local painters certified and checked by Turbolux** rather than new hires, and the dealers who sell to them **earn on each package**. That turns the trade from a threat into a channel. The pitch to the buyer is certainty, not cheapness: one price, one date, one name behind the paint and the work. It starts with a small pilot batch and booking opens wider only after it delivers. That is narrower than what was pitched, and the board thinks the narrowing is the point.

## The competition

Researched 2026-11-11 from public sources only. Every row links to its source; the full data is in `founder/competitors.csv`.

**Read this first: limits of this research.**
- From this session, the pages on asianpaints.com and hometriangle.com could not be opened (blocked by the session's network settings), and reddit.com was not reachable. So I stopped opening pages and read every linked page through its search-engine index entry instead. Prices, ratings and quotes below are as that index shows them. Open the links to check them before quoting them in public.
- Google Maps reviews of Kochi contractors were not read.
- No Kochi-specific 1–3 star review of any branded painting service was found. The complaints below come from customers across India, and some are several years old.

### 1. The table (sorted by how directly each competes)

Direct means a paint brand or platform sells paint plus a crew in one order to a homeowner. Indirect means a local contractor you hire yourself. A substitute means no painting business is involved.

| # | Name | Type | Where | Comparable price (2BHK repaint) | Rating (count) | Source |
|---|---|---|---|---|---|---|
| 1 | Asian Paints Beautiful Homes Painting Service | direct | National (90+ locations). Kochi customer testimonials on its pages. | **Price not published.** Quote after a site visit (₹250 refundable fee). Claims a 4-day 2BHK repaint ([quick makeover page](https://www.asianpaints.com/campaign/quick-home-makeover.html)) | 2/5 Trustpilot, for all of asianpaints.com (7–12 reviews) | [service page](https://www.asianpaints.com/services/asian-paints-safe-painting-service.html), [Trustpilot](https://www.trustpilot.com/review/asianpaints.com) |
| 2 | HomeTriangle (Kochi) | direct (platform) | Kochi city page | **₹17,055** for an unfurnished 2BHK, ₹19,499 furnished. Includes materials, labour and cleanup. Interior/exterior scope not stated. | 4.7 (324) | [Kochi page](https://hometriangle.com/kochi/house-painting) |
| 3 | Birla Opus PaintCraft | direct | National, booked online. Kochi coverage not confirmed. | **Price not published** (instant online quote) | not found | [PaintCraft page](https://www.birlaopus.com/paintcraft-painting-services) |
| 4 | Berger Express Painting | direct | National. Kochi coverage not confirmed. | **Price not published.** One customer reported about ₹28/sq ft in peak season, city not stated ([NoBroker forum](https://www.nobroker.in/forum/how-much-does-berger-express-painting-cost)) | not found | [Express Painting page](https://www.bergerpaints.com/express-painting) |
| 5 | Urban Company painting | direct (platform) | App. Kochi appears in its list of served cities. | **Kochi price not published.** A Hyderabad 2BHK starts at ₹10,999 ([other city](https://urbancompany.com/hyderabad-painting-shp-sku)). | not found for Kochi | [painting page listing Kochi](https://www.urbancompany.com/bangalore-painting-shp-fulfilment) |
| 6 | Nerolac NXTGEN painting service | direct (referral) | National. Kochi not confirmed, but Kochi dealers are listed. | **Price not published** (free site evaluation) | not found | [service page](https://www.nerolac.com/node/18882) |
| 7 | Magic Brush Painting Solutions | indirect | Panampilly Nagar, Kochi | **₹25/sq ft** for the full system (putty, primer, 2 coats of premium emulsion, interior and exterior). **₹10/sq ft** for painting only. | not found | [Kolo listing](https://koloapp.in/kerala/painters/magicbrush-paintingsolutions--ernakulam) |
| 8 | Xpress Painters | indirect | Palarivattom, Kochi | price not published | 4.8 Justdial (179–199) | [Justdial Ernakulam](https://www.justdial.com/Ernakulam/Painting-Contractors-For-Residential/nct-10350836) |
| 9 | Paint House | indirect | Kakkanad, Kochi | price not published | 4.8 Justdial (145) | [Justdial Ernakulam](https://www.justdial.com/Ernakulam/Painting-Contractors-For-Residential/nct-10350836) |
| 10 | Elements Painting Contractors | indirect | Thevara, Kochi | price not published | 4.9 Justdial (41) | [Justdial Ernakulam](https://www.justdial.com/Ernakulam/Painting-Contractors-For-Residential/nct-10350836) |
| 11 | The Painting Company | indirect | Judgemukku, Kochi | price not published | 4.7 Justdial (41–43) | [Justdial Ernakulam](https://www.justdial.com/Ernakulam/Painting-Contractors-For-Residential/nct-10350836) |
| 12 | Dealer paint + a daily-wage painter you manage | substitute | Kochi paint dealers | Labour only: ₹7–12/sq ft interior and ₹9–15/sq ft exterior ([Kerala 2026 guide](https://aapkapainter.com/blog/house-painting-cost-in-kerala-rates-for-interior-exterior-work-2026/)), plus paint at ₹195–378/L ([InfraLens Kochi](https://infralens.in/prices/paint/kochi)). Kerala's legal minimum for a semi-skilled painter is ₹820/day ([WageIndicator](https://wageindicator.org/en-in/work-in-india/minimum-wage/18414-kerala/41870-stone-crushing-construction-sector)). | n/a | see links |
| 13 | DIY | substitute | Dealer or online | Paint only: ₹195–378/L interior, about ₹335/L exterior ([InfraLens Kochi](https://infralens.in/prices/paint/kochi)) | n/a | [Birla Opus DIY vs pro guide](https://www.birlaopus.com/blog/diy-painting-vs-professional-services) |

What the brands promise, in their own words or page titles:
- **Asian Paints:** "Beautiful Homes Painting Service for Your Home Walls". Supervised painting, trained painters, masking and digital site updates. A 1-year service warranty comes only with the Platinum tier.
- **Birla Opus PaintCraft:** "Your 360-degree painting solutions partner". A free repaint if the surface develops issues within a year.
- **Berger:** "Professional & Safe Home Painting & Waterproofing Services".
- **Nerolac:** a product warranty only. It requires more than 60 L of paint for an exterior job and 40 L for an interior job, with a separate grid for coastal Kerala ([terms](https://www.nerolac.com/nerolac-warranty/terms-and-conditions.php)). Workmanship cover is not stated.

### 2. Price range for a comparable 2BHK repaint

Only one Kochi business publishes a 2BHK package price: HomeTriangle. Everything else is a per-sq-ft rate or not published.

**Area assumption (stated, not sourced):**
- The 2BHK has about **800 sq ft** of carpet area.
- Interior paintable area (walls plus ceilings) is **800 × 3.2 = 2,560 sq ft**. The 3.2 multiplier is the one a published Indian painting-cost calculator uses.
- Exterior wall area is **1,000 sq ft**, my assumption for a single-storey independent 2BHK house.
- Total: **3,560 sq ft.** For a flat, the exterior is usually building-level work, so the comparison should be redone interior-only. Turbolux should confirm what "exterior" means for flat buyers.

| Price point | Basis | 2BHK interior + exterior |
|---|---|---|
| HomeTriangle unfurnished 2BHK | published package (not converted; scope unclear, likely basic) | ₹17,055 |
| Magic Brush, painting only (no putty) | ₹10/sq ft × 3,560 | ₹35,600 |
| Magic Brush, full system (putty + primer + 2 coats premium) | ₹25/sq ft × 3,560 | ₹89,000 |
| Independent contractor at Kochi guide rates, low | interior ₹26/sq ft × 2,560 plus exterior ₹25/sq ft × 1,000 ([guide](https://aapkapainter.com/blog/house-painting-cost-in-kerala-rates-for-interior-exterior-work-2026/)) | ₹91,560 |
| Berger Express Painting (one customer's report, city not stated) | ₹28/sq ft × 3,560 | ₹99,680 |
| Independent contractor at Kochi guide rates, high | interior ₹36 × 2,560 plus exterior ₹40 × 1,000 | ₹1,32,160 |

- **All six points:** lowest **₹17,055**, median **₹90,280**, highest **₹1,32,160**.
- **Like-for-like only** (surface prep plus interior and exterior; the HomeTriangle package and the no-putty rate are dropped): lowest **₹89,000**, median **₹95,620**, highest **₹1,32,160**.
- **Labour-only substitute** (you buy the paint): ₹26,920–₹45,720 for labour, plus paint.
- **Turbolux at ₹78,000** sits about 18% below the like-for-like median. It is about 4.6× HomeTriangle's 2BHK package.

**Caveats:**
- The answer swings with the area assumption. The same Kerala guide quotes a standard 2BHK *interior* package of ₹38,000–₹65,000, which implies far less paintable area than 2,560 sq ft.
- Asian Paints, Birla Opus, Nerolac and Urban Company publish no Kochi price. Asian Paints' cost blog gives "₹75 to ₹115 per sq ft" for a 2BHK without saying which area it means, so it is left out.
- Before `/founder-pricing` relies on these numbers, get three real site-visit quotes in Kochi: Asian Paints, Birla Opus and one Justdial contractor.

### 3. Positioning map (text)

The two axes that matter to this buyer:
- **Who carries the risk of a late or bad job:** you, a platform, or the brand.
- **Price for the full 2BHK.**

Placement is by what each business publicly promises. The complaints in section 4 show the promises often slip in delivery.

| Who carries the risk ↓ / Price → | Under ₹40k | ₹40k–₹80k | Over ₹80k | Price not published |
|---|---|---|---|---|
| **Brand claims it** (supervision, trained crew, warranty, fixed timeline) | | **Turbolux target ₹78k** (fixed date + workmanship guarantee) | Berger Express (about ₹99.7k, one report) | Asian Paints BHPS (4-day 2BHK claim; 1-yr service warranty on top tier only). Birla Opus PaintCraft (1-yr free repaint) |
| **A platform stands in between** | HomeTriangle (₹17,055 package) | | | Urban Company. Nerolac NXTGEN (referral, product warranty only) |
| **You carry it** (you find, brief and check the painter) | Dealer paint + daily-wage painter (₹27k–46k labour + paint). DIY (paint only). Magic Brush basic (₹35.6k) | | Magic Brush full system (₹89k). Contractor at guide rates (₹91.6k–₹1.32L) | Xpress Painters, Paint House, Elements, The Painting Company (rated 4.7–4.9 on Justdial) |

**Reading the map:**
- No one in Kochi sits in the "brand carries the risk, published price" cell except Turbolux's planned offer.
- The two paint makers that already claim to carry the risk, Asian Paints and Birla Opus, publish no price.
- The businesses that publish a price either carry no outcome risk (contractors, substitutes) or are low-end platform packages (HomeTriangle).

### 4. Complaints, ranked

The top 3–5 reviewed are Asian Paints BHPS, Berger Express Painting, Urban Company and HomeTriangle. I found no public negative reviews of the Kochi Justdial contractors.

These are national complaints, not Kochi ones. Quotes are short and verbatim **as shown in the search index**, labelled as research and not as testimonials. Complaint titles are quoted as their authors posted them. The count is the number of separate linked reviews that support each theme.

**1. Delays: the crew thins out or stops coming, and jobs are left unfinished. (9 reviews, strong)**
- Asian Paints: "Painting contractor not completed the work even after 6 months and not responding" ([consumercomplaints.in](https://www.consumercomplaints.in/asian-paints-painting-contractor-not-completed-the-work-even-after-6-months-and-not-responding-c3115192)).
- Asian Paints: "Poor Quality, delayed service" ([link](https://www.consumercomplaints.in/asian-paints-poor-quality-delayed-service-c3532342)) and "Project delay and Quality of Work" ([link](https://www.consumercomplaints.in/asian-paints-project-delay-and-quality-of-work-c3487349)).
- Asian Paints: a Trustpilot reviewer reports a delay of 20+ days and days with no labour on site ([Trustpilot](https://www.trustpilot.com/review/asianpaints.com)).
- Berger: "after paying 90% of the amount, the labour is not coming" ([consumercomplaints.in](https://www.consumercomplaints.in/berger-paints-b115745)).
- Berger: a 1-month quote that stretched to two months ([voxya](https://voxya.com/consumer-complaints/complaint-on-express-paint-service-by-berger-paints/211600)).
- Berger: a worker left mid-job and demanded payment before returning ([consumercomplaints.in p.11](https://www.consumercomplaints.in/berger-paints-b115745/page/11)).
- Urban Company: a 5-working-day contract ran past 12 days ([consumercomplaints.in](https://www.consumercomplaints.in/urban-company-painting-c2960268)).
- Urban Company: a one-room job took 10 days instead of 2 ([Trustpilot](https://www.trustpilot.com/review/urbanclap.com?page=10)).

**2. Poor finish: thin coats, peeling, wrong shade. (7 reviews, strong)**
- Asian Paints: "The Paint peeled and deterioation" ([consumercomplaints.in](https://www.consumercomplaints.in/asian-paints-the-paint-peeled-and-deterioation-c3539687)). Also the two Asian Paints quality complaints listed in theme 1.
- Urban Company: thin coats and patchy walls ([Trustpilot](https://www.trustpilot.com/review/urbanclap.com?page=8)), and "Urban company paint service is a fraud" ([MouthShut](https://www.mouthshut.com/review/urbancompany-review-qunurnqoplp)).
- Berger: "Berger Paints Defects in shades" ([voxya](https://voxya.com/consumer-complaints/berger-paints-defects-in-shades/149235)).
- HomeTriangle: one reviewer calls it the worst painting service they had used and says the company blamed wall conditions on the last day ([Trustpilot UK p.5](https://uk.trustpilot.com/review/hometriangle.com?page=5); the page was matched from the search index).

**3. The brand sells the job, a local subcontractor does it, and escalation goes nowhere. (4 reviews plus the brand's own terms, moderate)**
- Asian Paints: a reviewer says they were never told a local contractor, not an Asian Paints-managed team, would do the work ([Trustpilot](https://www.trustpilot.com/review/asianpaints.com)).
- Berger: a reviewer says Berger acted as a "body shopper" ([MouthShut](https://www.mouthshut.com/review/berger-paints-review-stqturlonmm)).
- Berger: "no one responding even contractor & relationship manager" ([voxya](https://voxya.com/consumer-complaints/complaint-on-express-paint-service-by-berger-paints/211600)).
- Asian Paints: "...not responding" (the 6-month complaint linked in theme 1).
- Asian Paints' own terms say it has limited control over the contractor's work and is not liable for some delays ([T&Cs](https://www.asianpaints.com/campaign/unified-aphs/terms-and-conditions.html)).

**4. The final bill is higher than the quote. (thin: 2 reviews)**
- Urban Company: a 929 sq ft job was billed at ₹30,000 against a ₹22,000 in-app quote ([MouthShut](https://www.mouthshut.com/review/urbancompany-review-qunurnqoplp)).
- Berger: "The EXPRESS PAINTING IS CHEATING" ([MouthShut](https://www.mouthshut.com/review/berger-paints-review-qtprstuntrm)).
- No hidden-charge complaints were found for Asian Paints.

**5. Mess left behind and furniture damaged. (thin: 1 pinned review)**
- Berger: "doors, floors and slabs were not cleaned and we had to arrange it separately" ([consumercomplaints.in](https://www.consumercomplaints.in/berger-paints-b115745)).

**6. Warranty claims refused. (thin: 1 review)**
- Asian Paints: "ASIAN PAINTS CLAIM FOR 10 WARRANTY DAMP PROOF" ([MouthShut](https://m.mouthshut.com/review/beautiful-homes-service-review-sqpsqpmstto)). Reviewers say damp and cracks were treated as outside the warranty.

### 5. THE GAP

**No one in Kochi publishes an all-in price for a 2BHK interior + exterior repaint that comes with a finish date backed by a penalty and a workmanship guarantee from the paint maker.**

The evidence:
- The top complaint against the big brands is delay and crews that stop showing up (theme 1, 9 reviews). Next come poor finish (theme 2) and the brand pointing at its subcontractor (theme 3).
- The two paint makers that already claim to carry the risk publish no price (section 3).
- Their guarantees are narrower than they look. Asian Paints' service warranty covers only its top tier. Nerolac's warranty covers the paint, not the workmanship, and depends on how many litres you use.

**Be honest about how narrow this is:**
- Birla Opus already offers a free repaint within a year.
- Asian Paints already claims a 4-day 2BHK repaint, a supervised trained-painter panel, and has Kochi customers.
- Turbolux's "vetted, trained crew" is the same model as Asian Paints' "panel of contractors... trained by us" ([service pages](https://www.asianpaints.com/services/asian-paints-safe-painting-service.html)). That model is exactly what the complaints are about.

So the promise on its own is not the gap. The gap is:
- **(a)** a published fixed price in Kochi;
- **(b)** a finish date with a stated consequence if it is missed, such as a per-day credit. No such penalty was found anywhere;
- **(c)** a guarantee written for the failures a Kerala monsoon causes (bubbling, peeling, damp), backed by visible proof of delivery: crew attendance, photos of the surface prep, and the date met.

Without (b) and (c), Turbolux is a smaller Asian Paints at a similar price.

### 6. The threat: who could copy this fastest

1. **Asian Paints (fastest).** It already has the service, the trained contractor panel, Kochi customers, tiered packages and a 4-day 2BHK claim. Publishing a fixed Kochi 2BHK price and adding a delay credit is a policy change, not a build. It could match Turbolux within one season.
2. **Birla Opus PaintCraft.** It already has an instant online quote and a 1-year free-repaint guarantee. It is a new entrant spending to win share, so a published 2BHK price is a short step. Its Kochi coverage is unconfirmed.
3. **HomeTriangle.** It already sells fixed-price 2BHK packages in Kochi. It could add exterior work and a guarantee, but it has no paint brand behind it.
4. **Local contractors** (Xpress Painters, Paint House and others) can match the price and the finish date. They cannot offer a paint maker's guarantee.

**Defence:** move first in the Sept–Jan season, publish the delay penalty, and use Turbolux's dealer network for referrals. A large national brand is slow to make a Kochi-only pricing exception.

---
Next: `/founder-consumer` should turn themes 1–3 into buyer objections ("will the crew actually turn up?", "who do I call when it peels?"). `/founder-pricing` should use the section 2 range, ₹89,000–₹1,32,160 like-for-like with a median of ₹95,620, and test it against real Kochi quotes.

## The buyer panel

**4 buy · 16 pass** (20% buy) out of 20 simulated buyers. Seed 2611, so the same cards can be dealt again.

These are simulated buyers, not customers. Use this to find objections and weak spots, then confirm the big ones with real people before you spend.

### By segment

| group | buyers | buy rate |
| --- | ---: | ---: |
| Upper-middle professional or business family | 6 | 33%  (thin) |
| Salaried middle-class family | 8 | 25% |
| Gulf-earning (NRI) household | 4 | 0%  (thin) |
| Retired couple on a pension | 2 | 0%  (thin) |

### By buying behaviour

| group | buyers | buy rate |
| --- | ---: | ---: |
| Zero-hassle | 4 | 50%  (thin) |
| Managing from abroad | 2 | 50%  (thin) |
| Three quotes and haggles | 4 | 25%  (thin) |
| Reads every review | 2 | 0%  (thin) |
| Brand-loyal | 2 | 0%  (thin) |
| Uses the family's painter | 4 | 0%  (thin) |
| Waits until it is bad | 2 | 0%  (thin) |

### By income

| group | buyers | buy rate |
| --- | ---: | ---: |
| $1,118,000 to $2,220,000 | 7 | 43%  (thin) |
| $2,220,000 and up | 7 | 14%  (thin) |
| under $1,118,000 | 6 | 0%  (thin) |

### Why they pass

| reason | buyers | in their words |
| --- | ---: | --- |
| habit | 6 | "Our painter has done this house for years, my parents know him and are comfortable letting him in while I am in Dubai, and he does it for less. I am not handing the house and two elderly people to a crew from a brand that has only just come to Kochi." (P007) · "The house is due after six years, but I will just call our painter like we always do. He has done our walls for years, he picks the paint, and I have never had to chase him, so I have no reason to bring in a company crew I don't know." (P008) |
| trust | 5 | "I would let them do the free site visit, but I will not book a brand I have never heard of until I have Asian Paints and Berger quotes in hand to compare per square foot. Rs 89,000 is not small money for a name with no track record I can check." (P002) · "The wedding means I really do need the house painted, and the price and pay-after-checking terms are fine for us. But this crew is new in Kochi with no Google reviews and nobody in my WhatsApp groups has used them. The founding-homes offer tells me there are no finished homes yet, so I will take the free site visit and still go with someone my neighbours have used." (P004) |
| price | 3 | "The house is due, so I'd take the free site visit, but only as one of my three quotes. ₹89,000 is a fixed package price with nothing to bargain on, and I'm not booking anything until I've compared their per-square-foot rate with two local contractors and pushed everyone down." (P003) · "The signed date, the late penalty and paying 70% only after I check the work are exactly what I want. But ₹89,000 for our house is about two months of our pension, so I would take the free visit and compare it with the big-brand painting service and our old local painter before I commit to anything." (P005) |
| need | 2 | "With the wedding coming I do want the front of the house and the hall looking fresh, but I only need some walls done, not the whole house, and ₹89,000 is more than a month of my salary for work I don't need. The coordinator and the WhatsApp photos are good for someone sitting in the Gulf, but I am not paying for the full package to get them." (P013) · "I like that someone else handles everything and works within the building's hours, but I only need a few walls redone after the monsoon, not the whole flat. ₹59,000 is a whole-flat price, and I'm not paying for rooms that don't need paint." (P016) |

### Why they buy

| reason | buyers | in their words |
| --- | ---: | --- |
| convenience | 2 | "The bedroom wall is bubbling, so the house has to be done before next monsoon anyway. One company with a written price, a signed finish date, one person to call and the balance paid only after I check the work means I don't have to chase painters myself, so I would book the free visit and pay the 30% if the visit checks out." (P010) · "The house needs doing after this monsoon and I cannot keep flying back to chase a contractor; one named coordinator, daily WhatsApp photos and 70% held back until the work is checked is the first setup I have seen that I could actually manage from Dubai without leaving it all on my parents. I would book the free site visit and, if the written quote lands near ₹89,000, pay the 30% for a date that falls during my December leave." (P019) |
| need | 1 | "The house has to be repainted before the wedding anyway, and a signed finish date plus paying 70% only after I check the work is exactly what I need. I will still take two other quotes, but if their per-square-foot rate is close I would book Turbolux for the inside-and-outside job and push them for the founding ₹10,000 off." (P001) |
| timing | 1 | "The wedding is a few months away and I have no time to chase painters, so a signed finish date, one coordinator on WhatsApp and paying 70% only after I check the work is what I need. ₹89,000 for the whole house inside and out is fine if it means I don't have to manage anyone." (P011) |

### What would flip a no

- A written site-visit quote that beats the big-brand quotes per square foot, with damp treatment on the outside walls included and covered by the 3-year guarantee, plus a chance to see a Kochi house they painted at least one monsoon ago.
- If the per-square-foot rate in the written quote came in level with the cheapest of my other two quotes, then pay-after-checking and the late-day penalty would tip it to them.
- Being able to see two or three Kochi homes Turbolux has already finished and phone those owners, or read real Google reviews from them, along with a written guarantee that also covers dampness and seepage.
- A written quote at the site visit that comes to about ₹70,000 for the house after the founding discount, or seeing a finished Turbolux home near us and hearing from the owner that they finished on the date.
- If the same crew, fixed written price and late-day penalty came with Asian Paints or Berger paint on my walls, or if I could see a neighbour's flat they painted a few years ago still looking good.
- A guarantee that covers damp and seepage on the exterior walls for at least 5 years, in writing.
- If our painter could not take the job this season, or if a neighbour I know had their house done by them on the date they promised.
- If damp patches or peeling actually show up, or we have a function at home coming up, I would book the free site visit and compare their written price against my painter's.
- If the written quote from the site visit comes within about 10% of my best local quote on a per-square-foot basis, with the 3-year guarantee and the late-day penalty still included, I would book it, because then I am not paying extra for someone to watch the job while I am away.
- A clear partial-job price, for example only the living room, the front exterior wall and the gate side for around ₹25,000 to ₹30,000, with the same 3-year guarantee, WhatsApp photo updates and finish date before the wedding.
- If our painter can't fit us in before the wedding, or if I could walk through a finished Turbolux home in Kochi and hear from the owners that it held up through a monsoon.
- A damp patch showing up or a family function on the calendar, plus a Kakkanad flat owner I can call who says their crew finished on the signed date.

Buyers say they would buy **1.0 times** in the first month on average.

20 buyers gave all four price answers. Run founder-pricing's van_westendorp.py on the answers folder.

## Pricing

All amounts are Indian rupees. Prices to the buyer **include 18% GST** (assumed rate for painting work; an accountant should confirm). The CFO's numbers use the price before GST. The tools print `$`; read it as ₹.

### 1. The price

**Independent house, interior + exterior: ₹89,000, up from ₹78,000.** Test ₹95,000 against it.

Why ₹89,000:

- **Buyers:** the simulated panel's acceptable range is **₹40,188 to ₹95,088** (`founder/pricing-curve.md`; median "getting expensive" ₹85,000, median "too expensive" ₹1,10,000). ₹89,000 sits inside it, above the point where half the panel starts to call it expensive. Only 1 of 19 buyers who passed gave price as the main reason; 10 passed on trust. Raising the price is a smaller risk than the trust gap.
- **Competitors:** like-for-like Kochi repaints (surface prep, interior + exterior, ~3,560 sq ft) run **₹89,000 to ₹1,32,160, median ₹95,620** (`founder/competitors.md`). That range rests on a stated area assumption and per-sq-ft rates, so check it against real site-visit quotes. The national brands publish no Kochi price. ₹89,000 still undercuts the median.
- **The business:** at ₹78,000 each job leaves only ₹7,467 after its own costs. Break-even is 26 jobs a month against a plan of 30, and year 1 loses ₹14.75 lakh. At ₹89,000 a job leaves ₹16,789 (22%), break-even falls to about 12 jobs a month, and the year 1 operating loss shrinks to ₹3.66 lakh. All from `unit_economics.py --price`:

| Buyer price (incl. GST) | Before GST | Contribution per job | Break-even (jobs/month) | Margin at 30 jobs/month | Year 1 operating result | Cash needed |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| ₹78,000 | ₹66,102 | ₹7,467 (11.3%) | 26.4 | 1.4% | −₹14,75,464 | ₹22,75,464 |
| ₹85,000 | ₹72,034 | ₹13,399 (18.6%) | 14.7 | 9.5% | −₹7,69,531 | ₹17,69,066 |
| **₹89,000** | **₹75,424** | **₹16,789 (22.3%)** | **11.7** | **13.6%** | **−₹3,66,141** | **₹15,65,676** |
| ₹95,000 | ₹80,508 | ₹21,873 (27.2%) | 9.0 | 19.0% | +₹2,38,943 | ₹12,82,327 |

These runs hold the percentage-based costs (dealer fee, guarantee reserve, payment fees) at their ₹78,000 values. At ₹89,000 they rise by about ₹1,280 per job. `founder/numbers.json` is updated for that, and the CFO re-runs with it.

> **Update:** this table was run before `/founder-ops` cut capacity to 20 jobs a month and added EPF. The current numbers are in `founder/cfo.md`. At ₹95,000 the year 1 result is now −₹3.56 lakh. Only ₹95,000 combined with a lower crew rate and the real paint cost turns year 1 positive.

### 2. The ladder

Four of the 20 buyers live in flats, where the building association owns the exterior. All four said half of the package was useless to them. Two others wanted only part of the house done. One package cannot serve them all.

| Rung | What it is | Price (incl. GST) | Why step up |
| --- | --- | ---: | --- |
| **Flat Finish** | 2BHK flat, interior only (walls + ceilings), same crew, date and guarantee. Works within building contractor hours. | **₹59,000** (to test) | The entry point for flat owners. The CFO's rough cut: ~₹40,200 variable cost, ~₹9,800 left per job (≈20%). Confirm before publishing. |
| **Home Finish** | Independent 2BHK house, interior + exterior | **₹89,000** | The core package. |
| **Home Finish + Damp Shield** | Home Finish plus damp treatment and a waterproof coat on the exterior walls, with a longer guarantee | **Price after costing** | Answers the buyers whose real problem is damp (P002, P010). Waterproofing materials and labour are not costed yet, so no price is set. |

A part-house option ("hall, front room and road-facing wall", P013) is not a rung yet. On jobs that small, the site visit and travel eat the margin. Revisit once the CFO can see cost per room.

### 3. The opening offer

**Founding homes, Kochi: the first 10 bookings before 31 January 2027 get ₹10,000 off** if the owner agrees that:

- their finished home can be photographed and visited by two future buyers;
- they will give an honest review after 30 days.

This is not a discount to "buy" customers. It pays for the proof the panel asked for again and again ("a finished home nearby I can go and look at"). It is capped at 10 homes and paid from the ₹1 lakh show-home budget in startup costs, and it has an end date. No "was ₹X" price will be shown, because none was ever charged.

### 4. What to test with real buyers

- **₹89,000 vs ₹95,000** for Home Finish. Split site-visit bookings from the website and dealers into two groups, quote each group one price, and track conversion from site visit to booking. Run until each price has at least 15 site visits.
- **₹59,000 Flat Finish**: quote it to flat owners who book a visit and track the same conversion.
- **Three competitor quotes:** book real site visits from Asian Paints, Birla Opus and one Kochi contractor for a 2BHK house. That replaces the area-based estimate in `founder/competitors.md`.

### 5. The panel's price objections (verbatim, simulated buyers: research only)

1. "₹78,000 is close to a month of my salary, and our local painter would do the inside and outside of a 2BHK for much less." (P012)
2. "₹78,000 for the whole house is close to a month's pay when the wedding is already eating our savings, and I'm not going to pay for bedrooms nobody will see." (P013)
3. "...a fixed ₹78,000 with no room to bargain means I cannot check it against the per-square-foot rate my local contractor gives me." (P001)

Marketing answers these with a printed per-sq-ft breakdown at the site visit, the Flat Finish rung, and the written final-bill promise (see `founder/offer.md`).

## The offer

Built with the Offers lens method (`.claude/skills/founder-board/lenses.md`). It answers the objections from the 20-buyer panel (`founder/panel-v1/results.md`), the competitor complaints (`founder/competitors.md`) and the board's conditions (`founder/board.md`). All money is in Indian rupees, including GST, unless marked otherwise.

### 1. The problem list (in the buyer's words)

**Before buying**
1. "I've never heard of Turbolux. Is it as good as the big brands?"
2. "There are no reviews, and nobody I know has used them."
3. "I want to see a home they actually painted."
4. "₹78,000 is a month's salary."
5. "I can't compare a fixed price with my contractor's per-sq-ft rate."
6. "The bill will go up once they see the damp walls."
7. "I live in a flat. The outside isn't mine, so half the package is useless."
8. "I only need a few walls done."
9. "Our family painter is someone we trust."
10. "My building only allows contractors at certain hours."

**During the job**
11. "Crews stop turning up halfway."
12. "A promised date costs them nothing if they miss it."
13. "They'll send a subcontractor, and then nobody answers."
14. "I'm in Dubai and my parents would have to manage the crew."
15. "They'll skip the surface preparation to finish fast."
16. "They'll leave a mess and scratch the furniture."
17. "I'll pay most of it up front, then they disappear."

**After the job**
18. "It will bubble again after the next monsoon."
19. "The guarantee doesn't say how long it lasts or what it covers."
20. "They'll blame the damp, not their work."
21. "Who do I even call in month 8?"
22. "The shade won't match what I picked."

### 2. Solutions, scored

Value to the buyer runs from 1 (low) to 5 (high). Cost to deliver runs from 1 (cheap) to 5 (costly), based on the CFO's numbers.

| # | Solution | Answers | Value | Cost | Keep? |
| --- | --- | --- | :-: | :-: | --- |
| A | **Late-day credit:** ₹2,000 off the bill for every day past the signed finish date, capped at ₹20,000 | 11, 12, 17 | 5 | 2 | ✅ Bonus. Expected cost ≈ ₹800/job (estimate: 20% of jobs run 2 days late) |
| B | **Written final price** at the site visit, with a per-sq-ft breakdown; the bill never goes above it | 5, 6 | 5 | 1 | ✅ Bonus. Risk: margin leaks on bad walls, so the size and condition bands must be set before the visit |
| C | **Pay 30% to book, 70% after you check the finished work** | 13, 17 | 5 | 1 | ✅ In the core terms (costs working capital only) |
| D | **One named Turbolux coordinator** who takes calls and sends daily WhatsApp photo updates | 13, 14, 21 | 5 | 1 | ✅ Bonus. Already covered by the coordinator's salary in fixed costs |
| E | **3-year written guarantee:** any wall that bubbles or peels is repainted free, paint and labour | 18, 19, 21 | 5 | 2 | ✅ The guarantee. Reserve: 3% of price (₹2,670) |
| F | **Moisture reading recorded at the site visit**, so damp exclusions are agreed in writing before work starts | 20 | 4 | 1 | ✅ In the core (meters are in startup costs) |
| G | **Next-monsoon check visit and touch-up** | 18, 21 | 4 | 2 | ✅ Bonus. ≈ ₹800/job (estimate) |
| H | **Flat Finish:** interior only, within building hours, ₹59,000 | 7, 10 | 5 | 1 | ✅ A ladder rung (`founder/pricing.md`) |
| I | **Founding homes:** visit a finished Kochi home; first 10 bookings get ₹10,000 off for allowing visits | 1, 2, 3 | 5 | 2 | ✅ Urgency + proof. Capped at ₹1 lakh, from the startup budget |
| J | Prep checklist with photos, checked by a Turbolux supervisor before any paint goes on | 15 | 4 | 1 | ✅ In the core (supervisors are in fixed costs) |
| K | Furniture and floor covering, plus cleanup | 16 | 3 | 1 | ✅ In the core (₹1,500 consumables) |
| L | Shade sample patch on the wall, signed off before painting | 22 | 3 | 1 | ✅ In the core |
| M | Damp Shield: waterproof exterior coat with a longer guarantee | 18, 20 | 5 | 4 | ⏳ A ladder rung, priced once costed |
| N | Partial jobs (a few rooms) | 8 | 4 | 4 | ❌ Not yet: the site visit and travel eat the margin on small jobs |
| O | Bring the family's painter into the Turbolux certification | 9 | 4 | 3 | ⏳ Belongs in the crew model (`founder/ops.md`), not the offer |
| P | Lower price to match local painters | 4 | 3 | 5 | ❌ Each job would lose money (see `founder/pricing.md`) |

### 3. The stack

- **The core:** *Your 2BHK repainted, finished on the date you sign, at the price you sign.*
  - A Turbolux-certified crew, Turbolux paint and full surface preparation, checked and photographed by a Turbolux supervisor before any paint goes on.
  - A shade patch signed off first, furniture and floors covered, cleaned up after.
  - Pay 30% to book and 70% after you have checked the work.
  - Independent house, inside and out: **₹89,000**. Flat, inside only: **₹59,000**.
- **Bonus 1: the On-Date Promise.** ₹2,000 off for every day late, up to ₹20,000. *Kills: "crews stop turning up", "a date costs them nothing".*
- **Bonus 2: the Final Price.** Written at the site visit, with a per-sq-ft breakdown, and never raised. *Kills: "the bill will go up", "I can't compare".*
- **Bonus 3: One Person.** A named Turbolux coordinator and daily WhatsApp photos. *Kills: "a subcontractor and nobody answers", "I'm abroad".*
- **The guarantee.** 3 years against bubbling and peeling on every wall Turbolux paints: repainted free, paint and labour. Damp found at the site visit is recorded with a moisture reading. It is either treated (Damp Shield) or excluded in writing before work starts, so there are no surprises later. A free check visit after the next monsoon is included.
- **Urgency and scarcity, both true:**
  - Crews are limited: 10 certified crews, about 20 homes a month at most (`founder/ops.md`).
  - Founding homes: the first 10 bookings before 31 January 2027 get ₹10,000 off in return for allowing two visits from future buyers.
- **The name:** **Turbolux On-Date Repaint.** It names the outcome buyers said they care about, a job finished on the date.

**What the stack adds to the CFO's numbers:**
- About ₹1,600 more variable cost per job (late-day credit + check visit).
- At ₹89,000, each job now leaves **₹14,309 (19.0%)** after its own costs.
- Break-even is **14.3 jobs a month** (after the ops update: EPF added, 10 crews, 20 jobs a month capacity).
- Source: `unit_economics.py` on the updated `founder/numbers.json`.

### 4. Value equation, before → after (1 to 10)

| Element | Before (v1 pitch) | After | What moved it |
| --- | :-: | :-: | --- |
| Dream outcome | 7 | 7 | Unchanged: a freshly painted home, done. Damp Shield could lift it later. |
| Perceived likelihood | 4 | 7 | Late-day credit, paying after checking the work, a named coordinator, show homes to visit, a 3-year written guarantee |
| Time to result | 6 | 7 | A signed finish date with a penalty behind it |
| Effort and sacrifice (higher = less effort) | 8 | 9 | WhatsApp photos for owners abroad, flats done within building hours, written final price (no haggling) |

### 5. Re-test (same 20 buyers, seed 2611)

The old pitch is in `founder/pitch-v1.md` and its panel in `founder/panel-v1/`. The new pitch is in `founder/pitch.md` and its panel in `founder/panel/`.

| | v1 (₹78,000, plain promise) | v2 (On-Date Repaint, ₹89,000 / ₹59,000) |
| --- | :-: | :-: |
| **Buy** | **1 of 20 (5%)** | **4 of 20 (20%)** |
| Pass: trust | 10 | 5 |
| Pass: habit (family painter) | 4 | 6 |
| Pass: price | 1 | 3 |
| Pass: need (only some walls) | 2 | 2 |
| Pass: timing | 2 | 0 |

**Who flipped to yes:**
- **P001** (three quotes, wedding coming): "The signed finish date and paying the last 70% only after she checks the work answer her main fear."
- **P010** (zero-hassle, bubbling wall): wants the written price, the signed date and one coordinator.
- **P019** (owner in Dubai, parents at home): won by the named coordinator, daily WhatsApp photos and 70% held back.

**What dropped:** trust objections halved. The written final price, paying after checking the work and the named coordinator did most of that work.

**What didn't move, and what to do about it:**

1. **The family painter (6 buyers, now the biggest group).** No offer feature moves them. Two said they would switch if their own painter recommended Turbolux or was unavailable. That points to the board's crew model: certify existing local painters as Turbolux crews (`founder/ops.md`). It is not an offer problem.
2. **"₹2,000 a day is too small."** Five buyers said it, including two of the four who bought. Their real fear is a half-finished house before a function. Next version: raise the credit to ₹3,000 a day, and promise that "if the crew misses two days in a row, a second crew is sent within 48 hours". Cost both in the CFO before promising them.
3. **The guarantee doesn't cover damp (5 buyers).** The Damp Shield rung exists for exactly this. It needs costing so it can be priced and offered.
4. **No proof in Kochi yet (5 buyers).** Only real finished homes fix this. The founding-homes offer is the start. Until then, the panel's buy rate is an upper bound.
5. **Price at ₹89,000 (3 buyers).** All three are "three quotes" or budget-tight buyers. The per-sq-ft breakdown lets them compare. Don't cut the price, because the margin can't take it (`founder/pricing.md`).
6. **Partial jobs (2 buyers).** These buyers want only some walls painted. Still not offered; revisit once cost per room is known.

**Verdict on the offer:** it moved the buy rate from 5% to 20%, mostly by answering trust. The remaining no's are about habit and proof, which marketing and ops have to answer, not more bonuses. These are simulated buyers. Confirm with the founding homes.

## The numbers

> **Read first:** all amounts are **Indian rupees**; the tool prints `$`. Volumes are **per month**: this business sells about one job a day at most, so `days_per_month` is set to 1. Every "a day" below means **a month**. The price in the table is **before GST**: ₹75,424 = ₹89,000 to the buyer including 18% GST (rate to confirm with an accountant). Nearly every cost is an **ESTIMATE** (`founder/cfo-sources.md`). Replace them with Turbolux's real paint cost, real painter rates and real salaries before deciding anything.
>
> **Updated after `/founder-ops`:** a 3-painter crew needs about 13 working days per house (about 40 painter-days), not one week. So 10 crews can do about **20 jobs a month**, not 35. Year 1 is now planned at 10 crews: capacity 20, plan 20. Exterior work avoids May and October (heavy rain). Employer EPF on 4 staff is added (+₹7,200 a month, pending the accountant).

- **The margin.** Each Home Finish job at ₹89,000 leaves **₹14,309 (19%)** after its own costs. At the plan of 20 jobs a month, the profit margin is only **5%** after all costs. Break-even is **14.3 jobs a month** (the tool rounds it up to 15), against a capacity of 20. That leaves little room.
- **The line to watch: the painter crew's piece rate.** At ₹36,320 it is 48% of the pre-GST price. Unit costs +15% turns the plan margin to **−7%**. Price −10% makes it **−5%**. This business lives on labour cost and on holding the price.
- **Year 1 loses money: −₹9.05 lakh on operations, −₹17.05 lakh after the ₹8 lakh startup.** The cause is the calendar and capacity, not the unit. Months 1–3 are ramp-up, and the monsoon (months 6–8) carries the full ₹2.04 lakh-a-month team. Even at full capacity, 20 jobs only just covers it.
- **Cash: ₹18.4 lakh** is needed before it pays for itself. The startup money is not earned back within year 1.
- **The ramp is still the weakest number.** It runs from 3 to 20 jobs a month. The re-tested panel buys at 20%, an upper bound for simulated buyers. If volume comes in 40% lower, year 1 is **−₹15.2 lakh** and the cash needed is **₹23.2 lakh**.

**Ways to improve the margin (each one run through the tool, all else equal):**

| Change | Contribution per job | Break-even (jobs/month) | Margin at plan | Year 1 operating | Cash needed |
| --- | ---: | ---: | ---: | ---: | ---: |
| Base: ₹89,000, 10 crews | ₹14,309 | 14.3 | 5.0% | −₹9,05,057 | ₹18,40,389 |
| **Crew piece rate −10%** (volume commitment to certified crews) | ₹17,941 | 11.4 | 10.2% | −₹5,12,801 | ₹15,97,238 |
| **Price ₹95,000** (the test price in `pricing.md`) | ₹19,393 | 10.5 | 11.4% | −₹3,55,905 | ₹15,12,979 |
| **Paint at 40% of retail**, not 50% (Turbolux knows the real figure) | ₹16,984 | 12.0 | 9.0% | −₹6,16,157 | ₹16,53,139 |
| Off-season interior jobs (6/6/8 instead of 2/2/3 in the monsoon months) | ₹14,309 | 14.3 | 5.4% | −₹7,19,044 | ₹16,54,375 |
| Pause ads in the monsoon months (averaged as ₹30,000 a month) | ₹14,309 | 13.6 | 6.1% | −₹7,85,057 | ₹17,40,389 |
| **All three bold changes together** (₹95,000, crew −10%, paint 40%) | **₹25,700** | **7.9** | **19.2%** | **+₹3,25,251** | **₹11,99,977** |

**Year 2 at scale.** With 15 crews certified, a full year at up to 30 jobs a month makes **+₹9.55 lakh** on operations at today's ₹89,000 estimates. That excludes about ₹1.5 lakh to train and kit 5 more crews. The tool's cash and payback lines for this run re-count the startup spend, so ignore them. The business works at scale and in season. Year 1 is the cost of getting there.

The "price ₹95,000" runs hold the percentage-based costs (dealer fee, guarantee reserve, payment fees) at their ₹89,000 values. At ₹95,000 those costs rise by about ₹480 per job.

**The board's money conditions (`founder/board.md`):**
- [x] Margin positive at the price: Home Finish leaves 19% per job. Flat Finish has a rough cut of about 20% (in `pricing.md`), not yet run through the tool.
- [x] Guarantee costed: a 3% reserve plus a next-monsoon visit. The claim rate is an estimate.
- [x] Dealers earn on each package: 4% referral fee.
- [ ] **Year 1 makes an operating profit: NOT MET** on these estimates. It is met only with the three bold changes together.
- [ ] Crew wages and paint cost from real figures: still estimates.

*Not financial, tax or legal advice. An accountant should check GST treatment (works contract), payroll costs (EPF/ESI) and whether painters are employees or contractors before money moves.*

---

## Unit economics: Turbolux Home Finish, 2BHK paint + painter package, Kochi pilot (all amounts in Indian rupees; volumes are PER MONTH: days_per_month is 1, so every 'a day' in the tool's output means 'a month')

Every number below comes from the input file. Nothing is looked up or guessed.

### One job

| line | per job |
| --- | ---: |
| Price | $75,423.73 |
| Paint, primer and putty at Turbolux's own cost (ESTIMATE: 50% of ~Rs 26,750 retail for ~84 L + 40 kg) | -$13,375.00 |
| Painter crew, piece rate (interior 2,560 sq ft x Rs 9.5 + exterior 1,000 sq ft x Rs 12; public Kochi labour-only rates) | -$36,320.00 |
| Dealer referral fee, 4% of Rs 89,000 (ESTIMATE, a policy choice) | -$3,560.00 |
| Guarantee reserve, 3% of Rs 89,000 (ESTIMATE, claim rate unknown) | -$2,670.00 |
| Masking, floor covers, clean-up consumables (ESTIMATE) | -$1,500.00 |
| Site visit and quality-check travel (ESTIMATE) | -$1,200.00 |
| Payment fees, mostly UPI, ~1% (ESTIMATE) | -$890.00 |
| Late-day credit, expected cost (ESTIMATE: 20% of jobs late by 2 days x Rs 2,000) | -$800.00 |
| Next-monsoon check visit and touch-up (ESTIMATE) | -$800.00 |
| **Contribution** (what each job leaves to pay the fixed costs) | **$14,308.73** (19%) |

### The margin that matters

Fixed costs: $204,200 a month (Service manager (ESTIMATE) $55,000, Two site supervisors for prep and quality checks (ESTIMATE) $60,000, Booking and customer-care coordinator (ESTIMATE) $22,000, Booking software, CRM, phone (ESTIMATE) $5,000, Supervisor travel (ESTIMATE) $10,000, Always-on local ads, Google and Meta (ESTIMATE) $40,000, Liability and workmen insurance (ESTIMATE) $5,000, Employer EPF on 4 staff, 12% x Rs 15,000 x 4 (pending accountant; founder/ops.md) $7,200).

- **Break-even: 15 jobs a day.** Below that you lose money every month.
- **Profit margin at your plan** (20 a day): **5%** of every sale, after every cost.
- Capacity: 20 a day.

### Year 1, month by month

| month | jobs a day | revenue | profit | cumulative (after $800,000 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 3 | $226,271 | -$161,274 | -$961,274 |
| 2 | 6 | $452,542 | -$118,348 | -$1,079,621 |
| 3 | 10 | $754,237 | -$61,113 | -$1,140,734 |
| 4 | 14 | $1,055,932 | -$3,878 | -$1,144,612 |
| 5 | 8 | $603,390 | -$89,730 | -$1,234,342 |
| 6 | 2 | $150,847 | -$175,583 | -$1,409,925 |
| 7 | 2 | $150,847 | -$175,583 | -$1,585,507 |
| 8 | 3 | $226,271 | -$161,274 | -$1,746,781 |
| 9 | 10 | $754,237 | -$61,113 | -$1,807,894 |
| 10 | 12 | $905,085 | -$32,495 | -$1,840,389 |
| 11 | 18 | $1,357,627 | $53,357 | -$1,787,032 |
| 12 | 20 | $1,508,475 | $81,975 | -$1,705,057 |

- **Year 1 operating profit: -$905,057** on $8,145,763 of revenue.
- After the $800,000 startup spend: -$1,705,057.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$1,840,389**.

### What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 5% | 15 | -$905,057 |
| Price -10% | -5% | 31 | -$1,719,633 |
| Volume -20% | 2% | 15 | -$1,214,126 |
| Unit costs +15% | -7% | 40 | -$1,895,120 |

### Red flags

- Year 1 loses money on operations (-$905,057).
- The startup spend is not earned back within year 1.

## Marketing

Built from:
- the re-tested buyer panel (`founder/panel/results.md`; 4 of 20 buy);
- the competitor map (`founder/competitors.md`);
- the offer and pricing (`founder/offer.md`, `founder/pricing.md`);
- the CFO's numbers (`founder/cfo.md`).

All ₹. Panel quotes are research from simulated buyers. Never use them as customer quotes in ads.

### 1. Who to reach first

The panel's buyers are people with **a deadline or a distance**, not people hunting for the lowest price:

- **Zero-hassle** buyers: 2 of 4 buy (50%, thin).
- **Managing from abroad**: 1 of 2 (50%, thin).
- **Three quotes and haggles**: 1 of 4 (25%), when a wedding is coming.
- By income: the ₹11–22 lakh band buys most (3 of 7).
- Nobody bought among family-painter loyalists (0 of 4), brand-loyal buyers (0 of 2) or "waits until it's bad" buyers (0 of 2).

**The first audience:**
- Kochi homeowners with a family function coming up (wedding, housewarming, Onam/Christmas guests).
- Gulf-earning families whose parents live in the Kochi house.

What they want, in their words: *"I have no time to chase a local contractor, buy paint and argue about dates"* (P011). *"...doesn't have to put it on his elderly parents"* (P019).

### 2. Positioning

**A. Deadline (recommended)**
> For Kochi families with a wedding or function coming, who can't risk a crew walking off halfway, Turbolux On-Date Repaint is the home repaint finished on the date you sign, at the price you sign, unlike painting services that won't put a date or a final price in writing.

**B. From abroad**
> For Gulf-based families whose parents live in the Kochi house, Turbolux On-Date Repaint is the repaint you can run from your phone: one coordinator, daily photos, and you pay the balance only after it's checked. Unlike a contractor your parents have to chase.

**C. The maker owns it**
> For Kochi homeowners tired of the painter blaming the paint and the paint shop blaming the painter, Turbolux On-Date Repaint is the only repaint where the paint maker owns the whole result, with a 3-year guarantee, unlike big-brand services run through subcontractors.

**Recommend A**, with B as a separate campaign for Gulf families. Why:

- **The evidence.** Three of the four buyers named the signed date or the deadline as the reason (P001, P011, P019). The top competitor complaint is delays, with 9 reviews (`competitors.md` theme 1).
- **The gap.** No Kochi competitor publishes a price plus a date with a penalty. That is the one gap `competitors.md` found.
- **Why not C yet.** It is true, but the panel still doubts a brand that is new to Kochi (5 trust passes), and "only the maker" claims invite comparison with Asian Paints and Birla Opus, who already guarantee their own work. Use C as a supporting line, not the lead.

### 3. Channels

| Channel | Why it fits this buyer | Rough cost | How we know it worked |
| --- | --- | --- | --- |
| **1. Turbolux dealers in Kochi** ✅ | Already in front of homeowners buying paint. Dealers earn 4% per package, so they have a reason to refer instead of resisting (board condition). | Counter display + staff briefing ≈ ₹30,000 one-off; 4% referral fee is already in the CFO's cost per job | Site visits booked with a dealer code; target ≥ 30% of all site visits |
| **2. Google Search + Maps, plus the blog** ✅ | High-intent searches ("house painting Kochi", "painting contractors Ernakulam", "paint bubbling wall"). Turbolux already has posts on bubbling, 2BHK paint quantity and when to paint in Kerala, so link each to the booking page. | ≈ ₹22,000/month of the ₹40,000 ads line | Cost per site visit booked; target ≤ ₹800 |
| **3. Meta (Instagram/Facebook) + WhatsApp** ✅ | Two audiences: Kochi 28–55 near Kakkanad/Edappally/Palarivattom, and Keralites in the UAE, Saudi Arabia and Qatar with family in Kochi (positioning B). Founding-home owners share their photos on WhatsApp. | ≈ ₹13,000/month + ₹5,000 content | Site visits booked from Gulf numbers; WhatsApp click-to-chat conversations |
| Painter certification outreach (B2B) | Six buyers stay with the family painter. Recruit those painters as certified crews, so the painter becomes the referrer (`founder/ops.md`). | Inside crew training budget | Painters certified; jobs referred by painters |

**Not doing yet:**
- **TV or newspaper:** too broad and costly for one city.
- **Influencers:** no finished homes to show yet.
- **Paid Justdial / Urban Company listings:** they put us next to cheaper per-sq-ft painters, where we lose on price.
- **Discount ads:** the margin can't take them (`founder/cfo.md`, price −10% → 0% margin).

### 4. The 30-day campaign: Mon 28 Dec 2026 → Wed 27 Jan 2027

Launch day (booking opens) is **Monday 11 January 2027**. The founding-homes offer (₹10,000 off for the first 10 bookings, in return for allowing two visits) ends **31 January 2027**. Dates follow `founder/launch.md`.

| Date | Channel | What goes out |
| --- | --- | --- |
| Mon 28 Dec (L−14) | Dealers | Counter displays up at Kochi dealers; 20-minute staff briefing on the offer and the referral code |
| Tue 29 Dec | Blog + Google | Update the 3 existing blog posts with a "Book a site visit" box; Google Business Profile for "Turbolux Home Finish, Kochi" live |
| Wed 30 Dec | Instagram | Teaser: "Painted on the date you sign. Kochi, January." (hook 1) |
| Thu 31 Dec | WhatsApp | Waitlist link shared through dealer networks: "Founding homes: first 10 in Kochi" |
| Fri 1 Jan | Instagram | New Year reel: the prep check, what a supervisor checks before paint goes on (hook 9) |
| Mon 4 Jan (L−7) | Meta (Gulf) | Positioning B campaign starts: "In Dubai? Your coordinator sends photos every evening." (hook 4) |
| Tue 5 Jan | Google Search | Search campaign live on intent keywords; landing page = booking + per-sq-ft example |
| Wed 6 Jan | Instagram | Carousel: "The price we write is the price you pay", with a sample written quote (hook 2) |
| Thu 7 Jan | Blog | New post: "How to plan a repaint before a wedding in Kerala" (links to booking) |
| Fri 8 Jan | Meta (Kochi) | "Wedding in March? Book the date now. 10 crews, limited slots." (hook 8, true scarcity) |
| Sat 9 Jan | Dealers | Painter meet at the main dealer: Turbolux certification for local painters (hook 10) |
| **Mon 11 Jan (L)** | All | **Booking opens.** Post: the On-Date Promise. Dealers start site-visit referrals |
| Tue 12 Jan | Instagram | Reel: "₹2,000 off for every day we're late. Here's why we can promise that." (hook 1) |
| Wed 13 Jan | Meta (Kochi flats) | "Flat in Kakkanad? Inside only, inside your building's hours: ₹59,000." (hook 7) |
| Thu 14 Jan | Instagram | "Pay 70% only after you've checked every wall." (hook 3) |
| Fri 15 Jan | WhatsApp | Update to the waitlist: founding-home slots left (true number only) |
| Mon 18 Jan (L+7) | Instagram | First founding home, day 1: covering and prep photos (owner's consent) |
| Tue 19 Jan | Google | Review keywords and cut what costs > ₹1,500 per site visit |
| Wed 20 Jan | Blog + Meta | "That bubble on your wall: why it happens, and how we prep so it doesn't" (hook 6) |
| Thu 21 Jan | Instagram | Behind the scenes: the shade patch sign-off |
| Fri 22 Jan | Instagram | "The paint maker paints it, so there's nobody else to blame." (hook 5) |
| Mon 25 Jan | Instagram | First founding home finished: before/after, real and dated, finished on the signed date (only if true) |
| Tue 26 Jan | WhatsApp + Meta | "Founding homes close 31 Jan": real slots left |
| Wed 27 Jan (L+16) | All | The 3-year guarantee explained in plain words (hook 11) |

**When there is nothing new to say:** prep-check photos, the crew lead's 30-second intro, how a moisture meter works, a supervisor's day, answers to questions from the site visits.

### 5. Ten hooks (plus one), each answering an objection

| # | Hook | Format | Answers |
| --- | --- | --- | --- |
| 1 | "Finished on the date you sign. Or ₹2,000 off for every day we're late." | 3-second video opener / ad headline | "Crews stop turning up halfway" |
| 2 | "The price at your site visit is the price you pay, per square foot, in writing." | Carousel / search ad | "The bill will go up", "I can't compare" |
| 3 | "Pay 70% only after you've checked every wall." | Ad headline | "I'll pay, then they disappear" |
| 4 | "In Dubai? Your coordinator sends you photos every evening." | Gulf Meta ad | "My parents would have to manage the crew" |
| 5 | "The paint maker paints it, so there's nobody else to blame." | Sign / dealer counter | "They'll blame the subcontractor" |
| 6 | "That bubble on your bedroom wall? Here's why it happens." | Blog / reel | Bubbling after monsoon |
| 7 | "Flat in Kakkanad? Inside only, inside your building's hours: ₹59,000." | Local Meta ad | "Half the package is useless to me" |
| 8 | "Wedding in March? Book the date now: 10 crews, limited slots." | Ad headline | Timing, with real scarcity |
| 9 | "What our supervisor checks before a drop of paint goes on." | Reel | "They'll skip the prep" |
| 10 | "Kochi painters: get Turbolux-certified." | Dealer poster / WhatsApp | The family-painter habit (B2B) |
| 11 | "3 years. Any wall we painted bubbles or peels, we repaint it free." | Ad / site board | "What does the guarantee cover?" |

### 6. Budget and the numbers

**Launch budget: ₹2,00,000** (the CFO's startup line)

| Item | Amount |
| --- | ---: |
| Google Search/Maps | ₹70,000 |
| Meta (Kochi + Gulf) | ₹50,000 |
| Dealer displays + briefing | ₹30,000 |
| Founding-home photo/video | ₹30,000 |
| Site boards | ₹20,000 |

After launch: **₹40,000/month** (Google ₹22k, Meta ₹13k, content ₹5k). Pause Meta in the monsoon months: the CFO's what-if shows year 1 improves by about ₹1.2 lakh.

**The most we can pay to win a customer:**
- Each job leaves **₹14,309** after its own costs, dealer fee included (`cfo.md`).
- Each buyer buys **1** job (the panel's buyers average 1.0 purchases in the first month; a repaint is a once-in-years purchase).
- So the hard ceiling is **₹14,309 × 1 = ₹14,309** per customer. Spending that leaves nothing for the team.
- **Target: ≤ ₹4,000 per booked job.** That is ≤ ₹600 per site visit at 15% conversion from visit to booking. It keeps about ₹10,000 per job toward the ₹2.04 lakh monthly fixed costs.

**The three numbers to watch weekly**

| Number | Target | Change something when |
| --- | --- | --- |
| Site visits booked per week | ≥ 25 by week 4 | < 10 for two weeks: shift budget to whichever of dealers or Google is booking more |
| Site visit → booking | ≥ 15% | < 8% for two weeks: the problem is the quote or the trust, not the ads; revisit `offer.md` |
| Cost per site visit (paid channels) | ≤ ₹600 | > ₹1,500: pause that ad set |

**Rules:**
- Before/after photos only from real Turbolux jobs, with the owner's consent and the date.
- No "as seen on", no invented reviews, no countdowns that aren't real.
- Scarcity claims ("10 crews", "slots left") must match the real numbers that week.
- Follow Indian advertising rules (ASCI code) for the guarantee and "finished on the date" claims. Not legal advice.

## Brand

Built from `idea.md`, `marketing.md` (positioning A, B for Gulf families, C as a supporting line), `competitors.md`, `panel/results.md`, `offer.md`, `pricing.md` and `pitch.md`. All money in ₹, prices include GST. Researched 11 Nov 2026. **Not legal advice:** a trademark attorney must confirm every trademark point below.

### 0. The answer in brief

- **Name:** **Turbolux Home Finish**: the service, under the Turbolux house mark.
- **The promise has its own name:** **the On-Date Promise** (₹2,000 off for every day late, up to ₹20,000).
- **Promise line:** *Your home, finished on the date you sign, at the price you sign.*
- **Top tagline:** *Signed date. Signed price.*
- **Look:** extend the parent brand. Turbolux supplies its own palette, logo and fonts; the service adds one accent, **Brass #845A00**, which is used for the date and the price. Type is Anek Malayalam and Noto Sans Malayalam, both free under the OFL licence and both covering English and Malayalam.
- **Checks:** fonts and licences verified; contrast and distance from competitor colours computed. The IP India search, the domain and the handles **could not be checked** from here; the steps are in §3.

### 1. Fix the name architecture first

The pack uses five names for one thing: "Turbolux Home Finish" (the service and also the ₹89,000 rung), "Turbolux On-Date Repaint" (the offer), "Flat Finish" and "Damp Shield" (rungs). A buyer who sees three of them in one week will think they are three different companies. Use one name the customer sees, and give the packages plain labels:

| Level | Name | Where it appears |
| --- | --- | --- |
| House mark | **Turbolux** (the parent's logo, unchanged) | Everywhere: it is the trust the panel asked for |
| Service | **Turbolux Home Finish** | Site board, quote sheet, WhatsApp display name, Google Business Profile, web path |
| Packages | **Home Finish: Flat** (inside only) ₹59,000 · **Home Finish: House** (inside and outside) ₹89,000 · **+ damp treatment** (price after costing) | Booking page, quote sheet |
| The promise | **the On-Date Promise** | Quote sheet, ads, site board, complaint replies |

- **Retire "On-Date Repaint" as a product name.** It is long (7 syllables), and "on-date" is not everyday English. Keep "On-Date" as the name of the promise, where it already works in `marketing.md` ("Booking opens. Post: the On-Date Promise").
- **Rename "Flat Finish".** In the paint trade, "flat finish" means a matt sheen of paint, so dealers and painters will hear a product, not a flat.
- **Rename "Damp Shield".** Berger, a direct competitor, sells **DampShield Elasto**, and Star Paints sells **Star Damp Shield** ([Berger](https://shop.bergerpaints.com/product/dampshield-elasto), [Star](https://starshieldpaints.com/products/star-damp-shield-water-based)). Use the plain label "+ damp treatment" until a distinctive name has passed a trademark search.

### 2. Ten name candidates

The Malayalam script below is my **transliteration, not a translation**. Have a native speaker check it before anything is printed. "Home", "finish", "date", "paint" and "sign" are English words that, as far as I know, are widely used as-is in Kerala speech; test them with five Kochi homeowners.

| # | Name | Style | What it says | Out loud / in Malayalam | Risk |
| --- | --- | --- | --- | --- | --- |
| 1 | **Turbolux Home Finish** | descriptive sub-brand | Your home, finished. "Finish" is also the paint coat. | 5 syllables, all common loanwords. ടർബോലക്സ് ഹോം ഫിനിഷ് | "Home Finish" alone is descriptive, so it can only be owned together with "Turbolux". It clashed with the rung name (fixed in §1). |
| 2 | Turbolux On-Date | promise in the name | The date is kept | "On" can be heard as "own". ഓൺ ഡേറ്റ് | Any late job contradicts the name. Written as one word, "Ondate" reads like a dating app. |
| 3 | Turbolux On-Date Repaint | promise + what it is | The current offer name | 7 syllables, a mouthful | Too long for a board or an icon (see §1) |
| 4 | Painted by Turbolux | maker endorsement (line C) | The maker owns the result | Very easy to say | Says nothing about the date or the price. Better as a board line than a name. |
| 5 | Turbolux Signed Date | promise | The date is in writing | The "-ned d" is usually softened to "sign date" | Sounds like paperwork, not a home |
| 6 | Turbolux Finish Line | evocative | The deadline met, plus the paint finish | Easy. ഫിനിഷ് ലൈൻ | "Finish Line" is a known US sportswear retailer's name. The race idiom also implies speed, which drifts towards Berger's "Express". |
| 7 | Turbolux Painting Service | plain descriptive | What it is | Easy | A me-too of "Beautiful Homes Painting Service" (Asian Paints) and "Express Painting" (Berger). Nothing to own. |
| 8 | Turbolux Kochi Homes | place | Local | Easy | Blocks expansion to Thrissur or Kozhikode. Place names make weak marks. |
| 9 | Turbolux Niram | Malayalam word | *Niram* (നിറം) is the everyday Malayalam word for colour | Natural for Malayalam speakers; Gulf and English readers need it explained | Probably a crowded word among Kerala businesses (check). It says colour, not date or price. |
| 10 | Finishday | invented, standalone | The day it is finished | 3 syllables. ഫിനിഷ്ഡേ | Throws away the parent name, and the panel already doubts an unknown brand (5 trust passes). It means building a second brand from zero. |

- A founder's-name option was not drafted: the founder's name isn't in the brief, and a person's name cuts against "the maker owns it".
- The competitor map rules out these words: Beautiful Homes, PaintCraft, Express, NXTGEN, Urban, Triangle, Magic, Paint House, Elements.

**Shortlist:**
1. **Turbolux Home Finish (recommended).** It is already in the plan (pitch, Google Business Profile), it is easy in Malayalam, and it still holds up on the day a job runs late. The date and the price live in the promise line, which can carry proof.
2. **Turbolux On-Date.** Only if Turbolux wants the promise in the name and is sure of hitting the date.
3. **Finishday.** For comparison only, as the standalone route.

### 3. The checks (what I ran, what you must run)

I can only run public searches, and this session's network blocked the IP India search hosts (`tmrsearch.ipindia.gov.in`), turboluxpaints.com, the domain registry lookups (RDAP and WHOIS), Instagram and fonts.google.com. Only the web search index, the Google Fonts API and the google/fonts repository were reachable. **Nothing is registered until Turbolux registers it, and a trademark attorney confirms availability.**

| Check | Turbolux Home Finish | Turbolux On-Date | Finishday |
| --- | --- | --- | --- |
| IP India trademark search | **Not run** (unreachable). Search TURBOLUX in Classes 2 and 37, and HOME FINISH in Classes 37 and 2. | **Not run.** Search ON DATE and ONDATE in Class 37. | **Not run.** Search FINISHDAY and FINISH DAY in Classes 37 and 2. |
| Web index (not the register) | No Indian painting brand called "Home Finish" found | No paint brand "Ondate" found | No paint brand "Finishday" found |
| Domain | Default: **turboluxpaints.com/home-finish**, with a print short link **/kochi**. Not checked: the domain did not resolve here, which is an access limit, not proof it is down. | turboluxpaints.com/on-date | finishday.com and finishday.in: **not checked** (registry lookups blocked) |
| Handles | **Not checked** (Instagram, Facebook and YouTube blocked). The search index showed no Turbolux Paints accounts at all. | same | same |
| Confusion with `competitors.md` | Clear: no competitor uses "Finish" | Close in spirit to Berger "Express" (speed); not close in name | Clear |

**Trademark: how to run it (India).**
1. Open the Trade Marks Registry public search: https://tmrsearch.ipindia.gov.in/tmrpublicsearch/ (the older address, ipindiaonline.gov.in/tmrpublicsearch, is still cited by several guides).
2. Choose **Wordmark**, then "Contains", and enter `TURBOLUX`. Pick **Class 2** (paints, varnishes, coatings) and run the search. Repeat for **Class 37** (building construction and repair, which includes interior and exterior painting and damp-proofing services). The portal searches one class at a time.
3. Repeat with **Phonetic** search, to catch spellings like "Turbo Lux" and "Turbolax".
4. Repeat steps 2 and 3 for `HOME FINISH`, `ON DATE`, `ONDATE` and any name you pick for the damp rung.
5. For each hit, open its status by application number in the e-Register (https://tmrsearch.ipindia.gov.in/eregister/): registered, objected, opposed or abandoned.
6. For a logo, also run a **Vienna code** (device) search once the logo exists.

**What to bring to the attorney:**
- **Turbolux's existing certificates.** The house mark is probably registered in Class 2 (paints) only. The service may need **TURBOLUX** or **TURBOLUX HOME FINISH** filed in **Class 37**.
- **Descriptive words.** Under India's Trade Marks Act, descriptive words like "Home Finish" or "On-Date" are hard to register alone, so file them with the house mark or as a logo.
- **The fee.** The government fee for an e-filed application (Form TM-A) is ₹4,500 per class for individuals, startups and small enterprises, and ₹9,000 per class for others. Confirm the current fee on the IP India site.
- **The symbols.** Use ™ now; ® only after registration (falsely claiming registration is an offence in India).
- **Flag this to the attorney:** the only "Turbolux" result in the search index was a **Madurai (Tamil Nadu) dealer** listing Turbolux emulsions ([IndiaMART](https://m.indiamart.com/skytraders-madurai)). Confirm it is Turbolux's own product. If it isn't, the house mark needs the attorney's attention before any sub-brand filing.

**Domain:** keep the service on the parent site. The blog SEO is already there, and a new domain starts from zero.
- **Canonical page:** `turboluxpaints.com/home-finish`, with the Malayalam page at `/home-finish/ml`.
- **Print short link:** `turboluxpaints.com/kochi` redirects to the canonical page. It is short enough to type from a site board.
- **Standalone domains:** register `turboluxhomefinish.com` or `.in` only as a defensive buy, after checking at any registrar.

**Handles and listings:** check what Turbolux already owns before making anything new. One brand account with a "Home Finish" highlight or playlist keeps the proof (finished homes) selling paint too.

| Where | Proposed |
| --- | --- |
| Instagram | `@turboluxhomefinish` (18 characters; Instagram allows 30) |
| Facebook | Page "Turbolux Home Finish", username `turboluxhomefinish` |
| YouTube | `@turboluxhomefinish` |
| WhatsApp Business | Display name "Turbolux Home Finish", on a dedicated number for the coordinators, separate from dealer sales |
| Google Business Profile | Name it "**Turbolux Home Finish**", not "Turbolux Home Finish, Kochi" as `marketing.md` says. Google's guidelines don't allow added location words unless they are part of the real-world name. |

### 4. Voice and promise

**The one-line promise** (what the customer can count on, every time):
> **Your home, finished on the date you sign, at the price you sign.**

**Taglines:**

1. **"Signed date. Signed price." (recommended).** Factual, so it is easy to stand behind under the ASCI code; it reads in one second from the road; it names the two things three of the four panel buyers bought on.
2. **"We make the paint. We keep the date."** Joins line C (the maker owns it) to line A (the date). "Keep the date" is a promise, so always print the ₹2,000-a-day remedy next to it.
3. **"Painted by the people who make the paint."** Line C on its own: for dealer counters and the board's second line.

**The voice in three adjectives:**

| Adjective | Do | Don't |
| --- | --- | --- |
| **Exact** | "Finished by Sat 23 Jan. ₹89,000, in writing." Real dates with the day, ₹ amounts with Indian grouping, people's names. | "Quick turnaround at the best prices." "Hassle-free." "Premium quality." |
| **Accountable** | "We were a day late. ₹2,000 is off your bill." Say "we", own the miss, give the fix and its date. | "Due to unforeseen circumstances…" Never blame the painter, the paint, the weather or "the damp". |
| **Courteous** | "Your coordinator, Anu, will call your father before the crew arrives at 8:30." Write for elderly parents and for a son in Dubai. | Slang, emoji runs, ALL CAPS, pressure ("Hurry!") or fake scarcity |

**Words we don't use:**
- "best", "#1", "cheapest" and "guaranteed satisfaction" (we can't prove them, and the ASCI code requires proof);
- any panel quote presented as a customer review.

**Before and after** (the opening line of `pitch.md`):
- *Before:* "Turbolux Home Finish, from Turbolux Paints, a Kerala paint brand. Now in Kochi."
- *After:* "We make Turbolux paint. Now we paint your Kochi home with it, and sign the date we'll finish."

### 5. The look: a brief that extends the parent brand

**Colour.** Turbolux's palette is unknown to me, and none is invented here. The parent supplies its primary colour, logo and neutrals. The service adds one accent.

| Role | Name | Hex | Job |
| --- | --- | --- | --- |
| Parent primary | Turbolux brand colour | **supplied by Turbolux** | The Turbolux logo only |
| **Service accent** | **Brass** | **#845A00** | The signed date, the final price, the "Book a site visit" button, the band on the site board |
| Accent tint | Brass tint | #F5ECD9 | Background of the date and price boxes |
| Text (default) | Ink | #1F1B18 | Body text. Use Turbolux's dark neutral if it has one. |
| Background (default) | Paper | #FAF7F2 | Page and quote-sheet background. Use Turbolux's light neutral if it has one. |
| Secondary text | Muted | #5E5852 | Captions and small print |

**Contrast** (WCAG 2.x ratios, computed from relative luminance; AA needs 4.5:1 for normal text and 3:1 for large text and UI):

| Pair | Ratio | AA |
| --- | ---: | --- |
| White text on a Brass button | 6.10:1 | Pass |
| Brass text on white | 6.10:1 | Pass |
| Brass on Paper | 5.71:1 | Pass |
| Brass on Brass tint | 5.19:1 | Pass |
| Ink on Paper | 16.00:1 | Pass |
| Ink on Brass tint | 14.56:1 | Pass |
| Muted on Paper | 6.56:1 | Pass |
| Ink text on a Brass fill | 2.80:1 | **Fail**: always use white text on Brass |
| Brass text on Ink | 2.80:1 | **Fail**: on dark backgrounds use light brass #D9B26A (8.57:1), small text only |

**Why Brass:**
- **It is the only hue family I tested that is clear of every competitor's colour.** Brass is at least 31 CIEDE2000 units (a visible difference starts at about 2) from Asian Paints' reds, orange (#FDBA3D) and violet; Berger's blue, indigo, red and green; Urban Company's black; and WhatsApp's green and teal (#25D366, #075E54).
- **Rejected:** laterite red (only 13–18 units from the Berger and Asian Paints reds); teal-blue (11 from Berger blue); teal (our WhatsApp updates would look like WhatsApp's own screens).
- **It looks right on a seal.** Brass reads as warm and permanent, like an official stamp on the signed date.
- **Caveats:** the competitor hex values come from aggregator sites, not official guidelines. **Light brass is close to Asian Paints' orange** (#D9B26A sits 9.1 units from it), so never use it as a large fill.

**Rules:**
- **Parent clash:** when Turbolux sends its palette, re-check it. If its primary is itself a brown, gold or orange near #845A00, drop Brass and use the parent primary for the date and price. The date seal (below) then carries the service identity.
- **Print:** hex is for screens. For the site-board flex and printed quotes, approve a printed proof by eye. Pantone codes were not invented here.
- **Colour is never the only signal.** "On track" and "At risk" are always written out in words.

**Type** (verified 11 Nov 2026):
- Each font's Google Fonts CSS serves the Malayalam block (U+0D00–0D7F) and the ₹ sign (U+20B9).
- Each font's METADATA in the google/fonts repository lists the **OFL** licence (free for web and print, including commercial use) and both Latin and Malayalam.
- Get them free at fonts.google.com.

| Job | Font | Notes |
| --- | --- | --- |
| **Display:** headlines, the date, the price | **Anek Malayalam** (Ek Type) | Variable weight 100–800 and width 75–125. Use 600–700 for the date and the price. One family for both scripts, so English and Malayalam match. |
| **Text:** body, quote sheet, WhatsApp images | **Noto Sans Malayalam** (Google) | Weight 100–900. Plain and very legible in both scripts. |
| Alternative for long Malayalam reading | Manjari (Santhosh Thottingal) | Softer; good for the guarantee terms in Malayalam |
| Not for this brand | Baloo Chettan 2 (Ek Type) | Rounded and playful: fine for a festive post, wrong on a signed quote |

- **If Turbolux has its own licensed fonts:** keep them for English and use Anek or Noto Sans Malayalam for Malayalam only, matched by weight. Confirm the parent font's licence covers both web and print.
- **Malayalam setting:**
  - At least 16px on screen.
  - About 1.6–1.7 line height, to make room for tall conjuncts (test it).
  - Never fake bold or stretch the letters.
- **Malayalam copy is written by a native speaker, never machine-translated.** The quote is a signed document.

**Logo brief:**
- **What it must say:**
  - The **Turbolux** mark, unchanged. Never redraw it.
  - **"Home Finish"** set beside or below it in Anek Malayalam 600, in Brass or Ink, following Turbolux's own clear-space rule.
  - One signature element: the **date seal**. This is a round stamp reading "FINISHED BY" around the edge with the signed date in the centre ("SAT 23 JAN 2027"), in Brass on Paper. It changes for every home, and it is the thing customers will photograph.
- **Where it must work:** the site board, read from the road at about 10 m; an A4 quote, including a black-and-white photocopy (Brass prints as dark grey, which still reads); the WhatsApp profile photo (a circle crop, where the seal fits naturally); the Google Business Profile logo; the back of a crew T-shirt; a dealer counter card; and the 32px favicon, which uses the parent's mark alone.
- **Avoid:** category clichés (brush strokes, paint splashes, rollers, drops, rainbow swatches, house-roof outlines); speed lines (Berger "Express") and "360" (Birla Opus); tick marks; anything red, violet or blue that could be read as Asian Paints or Berger; stock icons or images without a licence.
- **Concepts and rights:** I can generate logo and seal concepts with a connected image tool if you want them. They would be **concepts, not a finished logo**. Final artwork goes to a designer, who hands over source files and **assigns copyright to Turbolux in writing**.

### 6. The first five touchpoints

**1. The booking page** (`turboluxpaints.com/home-finish`)
- **Headline:** "Your home, finished on the date you sign, at the price you sign."
- **Subhead:** "Turbolux paints it, with Turbolux paint. Kochi, from January 2027."
- **Two cards:**
  - **Flat, inside only, within your building's hours: ₹59,000.**
  - **House, inside and outside: ₹89,000.**
  - Both include GST. Damp treatment is priced at the visit, once costed.
- **"In writing at your free site visit":**
  1. Your final price, with a per-sq-ft breakdown.
  2. Your finish date, signed. ₹2,000 off for each day late, up to ₹20,000.
  3. Pay 30% to book and 70% after you've checked every wall.
- **Buttons:**
  - Brass button, white text: **"Book a free site visit"**;
  - secondary link: "Ask on WhatsApp".
- **Gulf strip:** "Living abroad? One coordinator, photos every evening, and you pay the balance only after it's checked."
- **Language switch:** English | മലയാളം.
- **Proof:** real founding homes only, with true slot counts. No stock "happy family" photos.

**2. The written quote / site-visit sheet** (A4, English front, Malayalam back)
- **Header:** the Turbolux Home Finish lockup, the quote number, the visit date, and the coordinator's name and phone number.
- **Your home:** type (Flat or House), measured areas in sq ft, and the **moisture reading per wall** with a photo reference.
- **Price box** (Brass outline): "Final price **₹89,000** incl. GST: ₹__ per sq ft × ____ sq ft. **This is the most you will pay.**"
- **Date box** (Brass outline, with the date seal): "Finished by **Sat 23 Jan 2027**. If we finish late, ₹2,000 comes off for each day, up to ₹20,000."
- **Payment:** "₹26,700 to book (30%). ₹62,300 after you have checked every wall (70%)."
- **Agreed today:** damp walls are either treated or excluded, in writing, with their readings.
- **Guarantee:**
  - 3 years against bubbling and peeling, repainted free, paint and labour;
  - a check visit after the next monsoon.
- **Signatures:** owner and Turbolux.

**3. The WhatsApp daily update** (every evening at the same time, in the customer's chosen language)
> **Turbolux Home Finish · Day 3 of 7** (example)
> Mr Thomas, today at your home:
> • Done: putty and sanding in both bedrooms; primer in the hall.
> • Crew on site: 4 (8:30 am to 5:30 pm).
> • Tomorrow: first coat in the bedrooms.
> • Finish date: **Sat 23 Jan 2027, on track.**
> Photos below: the prep, before any paint goes on. Reply here or call me.
> Anu, your Turbolux coordinator, 9XXXX XXXXX

- **When a date slips:** on the day the risk is known, write "**At risk:** [why]. **What we're doing:** [the fix]. If we're late, ₹2,000 a day comes off, as your quote says."
- **The job length is an example only.** Ops sets the real schedule.
- **Templates:** on the WhatsApp Business *Platform* (the API), a message sent more than 24 hours after the customer's last reply needs a pre-approved template, so register this one as a utility template. The WhatsApp Business *app* needs no template.

**4. The site board at the gate** (only with the owner's written consent; about 90 × 60 cm flex, Paper background, Brass band)
> TURBOLUX HOME FINISH
> This home will be finished by
> **SAT 23 JAN 2027**
> Signed date. Signed price.
> Painted by Turbolux · 3-year guarantee against bubbling and peeling
> turboluxpaints.com/kochi · WhatsApp 9XXXX XXXXX

- **Size:** make the date figures at least 10 cm tall.
- **Malayalam:** add a Malayalam line under the headline, written by a native speaker.
- **If the job runs late, the board stays up.** That is the promise being kept in public. If ops isn't confident, use a version with no date.
- **Local rules:** check the local body's rules for boards (not legal advice).

**5. The reply to the first complaint**

**The rules:** reply on the same channel, within the working-hours window ops sets, signed by a named person. State the fact, give the fix with a date, apply the credit as written, blame no one, and never write "sorry for the inconvenience caused".

**The private WhatsApp reply:**
> Mrs Menon, you're right. No crew came on Tuesday, and we finished on Sun 24 Jan, one day after the date we signed. ₹2,000 is off your bill, as your quote says, so the balance is now ₹60,300. The patch by the staircase will be redone on Thu 28 Jan at 9:00 am, and I'll be there. Anu, Turbolux Home Finish coordinator, 9XXXX XXXXX

**The public Google reply** (short, with no amounts):
> Mrs Menon, thank you for telling us here. We finished one day late; the late-day credit came off your bill as written in your quote, and the stair-wall patch is booked for Thu 28 Jan. Anu, Turbolux Home Finish.

### 7. What Turbolux must supply before anything is printed

- [ ] Logo files, the brand palette (hex), the fonts and their licences, plus any brand guidelines.
- [ ] Trademark certificates or application numbers for TURBOLUX, and the classes they cover.
- [ ] The social accounts and WhatsApp numbers Turbolux already owns.
- [ ] Confirmation that the Madurai IndiaMART Turbolux listing is Turbolux's own product.
- [ ] A native Malayalam writer for the quote, the board, the WhatsApp template and the guarantee terms.
- [ ] A yes or no on the renames in §1 (Flat and House labels; no "Damp Shield"; "On-Date" for the promise only).

**Sources:**
- Trademark search guides: [Intepat](https://www.intepat.com/blog/trademark/conduct-trademark-public-search-india/), [iPleaders](https://blog.ipleaders.in/trademark-search-report-a-guide/).
- Damp Shield name clashes: [Berger DampShield Elasto](https://shop.bergerpaints.com/product/dampshield-elasto), [Star Damp Shield](https://starshieldpaints.com/products/star-damp-shield-water-based).
- Turbolux in the search index: [IndiaMART Sky Traders](https://m.indiamart.com/skytraders-madurai).
- Competitor colours (aggregators, unverified): [Asian Paints](https://www.brandcolorcode.com/asian-paints), [Berger](https://brandpalettes.com/berger-paints-colors/), [Urban Company](https://www.brandcolorcode.com/urban-company).
- Fonts: the Google Fonts CSS API (fonts.googleapis.com) and the google/fonts `METADATA.pb` files (raw.githubusercontent.com).

Next: `/founder-ops` (coordinator scripts, board consent, WhatsApp setup) and `/founder-launch`.

## Operations

Prepared 2026-11-11 for the pilot that starts in January 2027. All money is in Indian rupees (₹). Inputs: `founder/idea.md`, `offer.md`, `numbers.json`, `board.md`, `pricing.md`, `competitors.md`.

**Limits of this research.** This session could not open razorpay.com or developers.facebook.com: the session's network settings blocked them. After that I stopped opening pages and read every source through its search-engine index entry. Prices below are as that index showed them, so open each link and check before you sign anything. Where no public price exists, the text says **get a quote**, and the item is in the open questions (section 9).

### 0. The three things that matter most

1. **The job takes about two weeks with a crew of three, not one.** The CFO pays ₹36,320 piece rate per job. Kochi painters earn ₹700–₹1,000 a day ([Kerala cost guide](https://aapkapainter.com/blog/house-painting-cost-in-kerala)), so that money buys **36–52 painter-days**. One published rate analysis allows 0.12 painter-days per m² for primer plus two coats ([InfraLens](https://infralens.in/rate-analysis/premium-exterior-emulsion)). That works out to about 40 painter-days for 3,560 sq ft (331 m²), before putty. So a crew of three needs about 13 working days. At that rate, **10 crews of 3 can do about 15–22 jobs a month, not 35.** They cover the year-1 ramp up to October 2027. The plan of 30 jobs a month needs about 15 crews (46 painters). Time the three January jobs before changing any promise or number.
2. **The weather decides the calendar.** Kochi gets about 6 mm of rain in January and 37 mm in March, but 284 mm in May and 310 mm in October ([monthly averages](https://www.weather2travel.com/kerala/climate)). The monsoon normally sets in over Kerala on 1 June, give or take about 7 days ([IMD via The News Minute](https://www.thenewsminute.com/amp/story/kerala/monsoon-hits-kerala-its-onset-date-imd-predicts-normal-rainfall-year-125715)), and in 2025 it came on 24 May ([Business Standard](https://www.business-standard.com/amp/india-news/india-monsoon-2025-kerala-onset-imd-forecast-rainfall-125052400509_1.html)). Book exterior work for **December to mid-April**. In May and October, do interiors and flats only, or sign finish dates with rain days built in.
3. **Labour rules are changing in Kerala right now.** India's four Labour Codes have been in force since 21 November 2025 ([HSF Kramer](https://www.hsfkramer.com/notes/employment/2025-posts/india-labour-codes-implemented-a-landmark-reform)), but Kerala has only draft state rules ([L&S tracker](https://employmentlaw.lkslaw.com/states/kerala)). A draft report handed to the Chief Minister on 4 November 2026 proposes **higher minimum wages** ([South First](https://thesouthfirst.com/keralam/keralam-draft-report-on-labour-codes-implementation-proposes-higher-minimum-wages-stronger-worker-safeguards/)). Whether certified painters count as Turbolux employees or as independent crews decides who pays EPF, ESI and compensation insurance. That decision is for the accountant and lawyer, and it has to be made before January.

### 1. The daily cycle (one working day at planned volume)

👁 marks the steps the customer sees.

1. **7:30** The coordinator checks the crew sheet. Every active job has a named crew lead and a start time. Any gap goes to the service manager by 7:45.
2. **8:00** 👁 Crews arrive. Houses start at 8:00; flats start when the association's hours allow. The crew lead sends an "on site" photo to the coordinator.
3. **8:30** Supervisors set out on their route: prep checks first, because paint cannot start until they pass, then site visits for new quotes.
4. **9:00–13:00** 👁 Site visits: measure, take moisture readings, set the band, write the quote (SOP A). 👁 Prep checks (SOP C).
5. **All day** 👁 Crews prep and paint to the job sheet. The supervisor drops in on any job on its first or last day.
6. **13:00–17:00** 👁 Handover inspections with the owner (SOP E), more site visits, and guarantee visits (SOP F).
7. **16:30** The crew lead sends 3–5 photos, the percentage done and tomorrow's plan to the coordinator.
8. **17:00** 👁 The crew covers open tins, cleans tools outside, clears the floor and locks up.
9. **By 18:00** 👁 The coordinator sends each customer their daily WhatsApp update (SOP D).
10. **18:00** The coordinator updates each job's stage in the CRM, flags any job at risk of finishing late, and confirms the paint for jobs starting in 2 days with the depot.
11. **Friday 16:00** Weekly reorder and crew schedule (SOP G).

### 2. Suppliers

| Input (numbers.json line) | Where from | Public price found | Notes |
|---|---|---|---|
| Paint, primer, putty (₹13,375/job, estimate) | **Internal: Turbolux factory and Kochi depot** | n/a, transfer cost | Issue each job's paint against a job sheet (litres by product and shade). Return unused tins and reconcile every week (SOP G). The CFO's cost is an estimate until finance sets a transfer price. |
| Masking tape | 1) Turbolux's Kochi dealers (**get a quote**; this also gives dealers a share of each job). 2) [Robocraze 48 mm × 50 m generic tape, ₹220 incl. GST](https://robocraze.com/products/masking-tape-high-temperature-resistant-adhesive-tape-48mm-x-50-meter) (sold for 3D printers, so test it on paint first). 3) [3M 7120 48 mm × 50 m, ₹1,293 incl. GST via Tanotis](https://tanotis.com/products/3m-7120-tape-masking-paper-48-mm-1-89-50-m-164-04-ft) | ₹220–₹1,293 a roll | No MOQ found for single rolls. Time each job's usage in the pilot. |
| Floor and furniture covers | 1) Reusable branded drop cloths (startup line; **get a quote** from a Kochi canvas or tarpaulin maker). 2) [LDPE sheet rolls on IndiaMART, about ₹100/kg](https://m.indiamart.com/impcat/ldpe-sheet.html). 3) [Ubuy imported 4-mil LDPE, 150 sq ft, ₹3,351](https://www.ubuy.co.in/product/8DBVASKAA-plastic-sheeting-4-mil-3-x-50-150-sq-ft-thick-semi-clear-plastic-sheeting-for-painting-construction-home-use-heavy-duty-ldpe-film-roll) (too dear) | ₹100/kg bulk | Prefer reusable cloths and one-use poly sheet only over furniture. |
| Moisture meters (startup) | 1) [Stanley 0-77-030 masonry meter, ₹3,315 at BuySupplies](https://buysupplies.in/products/stanley-0-77-030-moisture-meter-for-measuring-masonry). 2) [Aadarsh Technologies concrete meter, ₹6,000, 1-yr warranty](https://m.indiamart.com/aadarshtechnologies/moisture-meter.html). 3) [Lutron MS-7002 from ₹5,000 (seller's claim)](https://www.insuzo.com/p/1217/0/lutron-ms-7002-concretewood-moisture-meter) | ₹3,315–₹6,000 each | Buy **4**: one each for the manager and the 2 supervisors (who do all site visits and prep checks), plus a spare. Crews don't need them. Use one model so readings are comparable. |
| Ladders (crew kit) | 1) [Bathla Advance 8-step, ₹7,999 (out of stock when checked)](https://www.bathla.com/products/advance-8-step-ladder). 2) [Bathla 10.5 ft telescopic, ₹6,099](https://www.bathla.com/collections/telescopic-ladders). 3) [Smarty 10-step 10 ft via Moglix, ₹5,329](https://www.moglix.com/smarty-10-step-10ft-aluminium-foldable-telescopic-ladder-with-locking-mechanism/mp/msnq946nzlmn50) | ₹5,329–₹7,999 | Local painters usually own ladders. Fund one good ladder per crew only where a crew's own fails the safety check. |
| Scaffolding hire (2-storey exteriors) | [Unity Scaffoldings, Vazhakkala](https://m.indiamart.com/unity-scaffoldings); [Sundaram Scaffolding, Edappally](https://m.indiamart.com/sundaram-scaffolding); [Brightscaff, Vennala](https://m.indiamart.com/brightscaff-ernakulam) | **No rates published: get a quote** | Ask for a weekly rate for one house front, with delivery and erection. A single-storey 2BHK is normally done from ladders. |
| CRM / booking | See section 5 | ₹400–₹1,080 per user a month | |
| WhatsApp | See section 5 | free app; API from ₹1,500 a month | |
| Payments | See section 5 | UPI 0.4% capped at ₹300; gateway about 2% + GST | |
| Insurance | New India Assurance employees' compensation ([proposal form](https://newindia.co.in/assets/docs/know-more/miscellaneous/employee-compensation/Employees%20Compensation%20Proposal%20Form.pdf)); general liability from HDFC ERGO, ICICI Lombard, Bajaj or National ([list](https://joinditto.in/articles/general/commercial-general-liability-insurance/)) | Liability for contractors: about ₹15,000–₹40,000 a year ([BimaKavach](https://www.bimakavach.com/blog/commercial-general-liability-insurance-for-contractors/)). Compensation cover is priced on annual wages and occupation ([Upstox](https://upstox.com/learning-center/corporate-insurance/the-ultimate-guide-to-employee-compensation-insurance-in-india/article-1931/)) | **Get 2–3 quotes.** Workers employed through a contractor need a rider ([Upstox](https://upstox.com/learning-center/corporate-insurance/the-ultimate-guide-to-employee-compensation-insurance-in-india/article-1931/)). |

### 3. People

**Wage reference points**

| | Rate | Source |
|---|---|---|
| Kerala legal minimum, building-construction painter (semi-skilled) | ₹820 a day. Skilled masons are ₹890 and helpers ₹730. The table rests on a 2019 notification. | [WageIndicator](https://wageindicator.org/en-in/work-in-india/minimum-wage/18414-kerala/41870-stone-crushing-construction-sector) |
| Revisions | Kerala notified revised minimum wages on 19 May 2026 (applying from 1 April 2026), but it isn't clear whether construction is covered. A Labour Code draft proposes higher minimums. | [FactoHR](https://factohr.com/minimum-wages-in-india/kerala/), [South First](https://thesouthfirst.com/keralam/keralam-draft-report-on-labour-codes-implementation-proposes-higher-minimum-wages-stronger-worker-safeguards/) |
| Kochi/Ernakulam market rate, skilled painter | ₹700–₹1,000 a day, or ₹7–₹12/sq ft labour only | [aapkapainter Kerala guide](https://aapkapainter.com/blog/house-painting-cost-in-kerala) |
| Turbolux piece rate (CFO) | ₹9.5/sq ft interior, ₹12 exterior = ₹36,320 a job. That is ₹12,107 per painter per job. | `numbers.json` |

At 36–44 painter-days a job, the piece rate pays ₹825–₹1,009 a day, above the ₹820 minimum. At 52 painter-days it would pay only ₹698, which is below it. **Pay a daily minimum guarantee** (the higher of piece rate or the legal day rate), so that a slow job never takes a painter below the minimum.

**Roles**

| Role | Who | Hours | Owns |
|---|---|---|---|
| Service manager (1) | Turbolux hire, ₹55,000 a month (CFO estimate) | Mon–Fri 9–6, Sat 9–1; on call for escalations | Crew certification, pricing bands, any refund or credit above ₹5,000, dealer relations, backup for the coordinator |
| Site supervisors (2, north and south Kochi) | Turbolux hires, ₹30,000 each | Mon–Sat 8–5 | Site visits and quotes, prep checks, handovers, guarantee inspections |
| Coordinator (1) | Turbolux hire, ₹22,000 | Mon–Sat 9:30–6:30 | **The one named owner of every customer**, from booking to guarantee claim |
| Crews (crew lead + 2 painters) | Existing Kochi painters certified by Turbolux, paid piece rate | Mon–Sat 8–5 (flats: building hours); Sunday off | The job sheet, daily photos, clean-up |
| Dealers | Existing Turbolux dealers | n/a | Referrals (4% fee), local consumables, introducing good painters for certification |
| Accounts | Existing Turbolux finance team | n/a | GST invoices, crew payouts, reconciling the paint issued to each job |

**Workload at plan (30 jobs a month).** At about 13 days a job, about 15 jobs are running at once. That means the coordinator sends about 15 updates a day. Supervisors make about 45 quote visits (assuming 1 booking per 1.5 visits), 30 prep checks, 30 mid-job checks and 30 handovers. That is about 135 visits, or **about 2.6 a day each**, which is feasible.

From June 2027, the free next-monsoon check visits (one per job sold) land on the same two supervisors in September and October. By the second season, add a third supervisor or a guarantee technician. One coordinator is also a single point of failure: the service manager must know every live job by name and take over on leave days.

**Weekly rota: planned volume (30 jobs a month, about 15 crews)**

| | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|---|---|---|---|---|---|---|---|
| Service manager | 9–6 office, escalations | 9–6 dealer visits | 9–6 crew audits | 9–6 | 9–6; 16:00 weekly plan (SOP G) | 9–1 handovers | on call |
| Supervisor North | 8–5 prep checks, then quotes | 8–5 | 8–5 | 8–5 | 8–5 | 8–5 handovers | off |
| Supervisor South | 8–5 prep checks, then quotes | 8–5 | 8–5 | 8–5 | 8–5 | 8–5 handovers | off |
| Coordinator | 9:30–6:30 | 9:30–6:30 | 9:30–6:30 | 9:30–6:30 | 9:30–6:30 | 9:30–6:30 | off; manager sends any Sunday reply |
| Crews (~15 × 3) | 8–5 | 8–5 | 8–5 | 8–5 | 8–5 | 8–5 | off |

Start new jobs on **Monday or Tuesday**, so that the prep check falls mid-week and handovers fall on Friday or Saturday, when owners are home.

**Weekly rota: slow first month (January 2027, 3 founding homes)**

| Week | Jobs on site | Crews | Supervisors | Manager / coordinator |
|---|---|---|---|---|
| 4–9 Jan | Job 1 (crew A starts Mon 4 Jan) | A on site. The other 9 crews do 1 paid shadow day each on job 1 or 2 as part of certification and keep their own private work. | North: job 1 every morning, quotes in the afternoon. South: quotes and dealer demos. | The manager goes to every site visit. The coordinator builds the update and quote templates. |
| 11–16 Jan | Jobs 1 and 2 (crew B starts 11 Jan) | A, B | North: job 1. South: job 2. | The manager times each stage (painter-days per room) |
| 18–23 Jan | Jobs 1–3 (crew C starts 18 Jan); job 1 hands over about 20 Jan | A, B, C | Both on jobs, 1 handover | The manager is at the handover |
| 25–30 Jan | Jobs 2 and 3; handovers about 27 Jan and 3 Feb | B, C; A ready for February's jobs | Quote visits for February's 6 jobs | Review: painter-days, late days, photos, the owner's score |

**Payroll costs beyond wages: flag for the accountant (not advice).**
- **EPF:** the employer pays 12% of wages ([Zoho Payroll EPF guide](https://www.zoho.com/in/payroll/academy/taxes-and-compliance/epf-scheme-2026-guide.html)). Sources disagree on whether the wage ceiling is still ₹15,000 or has been raised to ₹25,000 ([Fox Mandal](https://foxmandal.in/News/epfo-wage-ceiling-raised-what-employers-need-to-do-now)). That puts the employer cost at ₹1,800–₹3,000 a month for each staff member above the ceiling.
- **ESI:** the employer pays 3.25% and the employee 0.75%, for staff earning up to ₹21,000 a month ([Petpooja](https://blog.petpooja.com/finance-compliance/esi-esic-contribution-rate-employer-employee-share/)). The four salaried staff are just above that level. Painters in slow months may fall under it.
- **Painters' status:** if certified painters are Turbolux employees (piece-rated workers can be), EPF and ESI apply to them as well. If a crew lead engages the other two painters, Turbolux is the principal employer. Contract-labour licensing under the OSH Code starts at **50 contract workers** ([JSA](https://www.jsalaw.com/corporate/labour-codes-summary-november-2025/)), and the plan's 15 crews are 45 workers.
- **Also ask about:** bonus and gratuity under the Codes, any local-body professional tax, and Kerala's final Labour Code rules.

### 4. Routines (SOPs): one page each

**SOP A: Site visit and written quote** (supervisor or manager, 60–90 min)
1. Confirm by WhatsApp the day before: the time, your name and photo, "no charge, no obligation".
2. On arrival, ask whether it is a house or a flat. For a flat, ask for the association's contractor rules **in writing** (hours, lift use, debris, Sundays). Photograph them.
3. Measure each room and the exterior walls with a laser or tape. Record paintable sq ft (walls + ceilings) in the CRM form.
4. Take moisture readings on every exterior-facing wall and every wall with stains, at 3 points each. Photograph each reading with the meter in the frame.
5. Grade the condition: A (sound), B (cracks or patches), C (damp above the threshold or flaking). The threshold is set by Turbolux's technical team from its own product data sheets.
6. Set the band from the published size × condition table. Grade C walls are either quoted as Damp Shield, once it is priced, or **excluded in writing** with the reading attached.
7. Choose shades with the owner. Note the 1–2 walls where the shade patch will go.
8. Fill in the quote template: the price, the per-sq-ft breakdown, the signed finish date (crew days from the crew sheet + 1 buffer day; + 2 rain days for exteriors in Apr–May and Sep–Nov), the exclusions, the 30/70 terms, the coordinator's name and the 3-year guarantee.
9. Send the PDF on WhatsApp before you leave the street. Log the visit in the CRM as *Quoted*.
10. Follow-ups are the coordinator's job (day 2 and day 7). Don't discount without the manager.

**SOP B: Job start, days 1–2** (crew lead)
1. Arrive at the booked time. Send the "on site" photo. Meet the owner, who has already received the crew's names and photos.
2. Walk the job sheet with the owner: the rooms, the order, and where furniture goes.
3. Move furniture to the centre of the room. Cover it with poly sheet, and cover floors with drop cloths. Mask switches, frames, skirting and fittings. Take a photo of each room covered.
4. Paint the shade patch (about 1 × 1 m) on the agreed walls. **The owner signs it off on WhatsApp** ("approved") before any full coat goes on.
5. Prep: scrape loose paint, fill cracks, apply putty, sand and dust. Take photos of each wall at every stage.
6. Tell the coordinator when prep is done, so the supervisor's check can be booked. **No primer or paint goes on before the check passes.**

**SOP C: Supervisor prep check before paint** (supervisor, 30–45 min a job)
1. Arrive within 4 working hours of the "prep done" message.
2. Check every wall against the written prep standard: no loose paint, cracks filled, putty sanded smooth, dust removed, masking complete.
3. Re-read moisture on the walls flagged at the visit. If a reading is above the threshold, stop and call the manager.
4. Photograph each wall, with the room name, before any primer.
5. Mark the result in the CRM: Pass, or Fix with a list. The crew fixes the items and the supervisor re-checks the same day or the next morning.
6. Only once the check passes does the coordinator tell the owner: "Prep checked by Turbolux, painting starts today".

**SOP D: Daily WhatsApp update** (coordinator, by 18:00, Mon–Sat)
1. By 16:30, collect 3–5 photos, the percentage done and tomorrow's plan from each crew lead.
2. Send each owner one message: what was done today, 2–3 photos, tomorrow's plan, and whether the job is on date or at risk.
3. If the job is at risk, say so plainly, give the new date, and state any late credit that applies. Don't wait for the owner to ask.
4. Answer any owner question within 2 working hours. Pass anything about quality to the supervisor the same day.
5. Log the update in the CRM. If no update went out, the job shows red on the next morning's sheet.

**SOP E: Handover and the 70% payment** (supervisor + owner, about 60 min)
1. The crew finishes, removes masking, cleans floors, puts furniture back and takes away its waste.
2. The supervisor does an internal snag walk first, and the crew fixes what it finds.
3. Walk every room with the owner, using the checklist: coverage, edges, shade and cleanliness. Write any snags down, with photos.
4. Snags are fixed within 2 working days. The finish date counts from the end of the snag fixes only if the snags are Turbolux's fault.
5. The owner signs the handover form on paper or by WhatsApp "accepted". The coordinator then sends the 70% invoice, net of any late credit (₹2,000 a day, capped at ₹20,000).
6. Payment goes by UPI to the Turbolux current-account QR, or by bank transfer. A payment link is sent only for card payers.
7. Send the guarantee certificate (3 years, the walls covered, the exclusions with moisture readings) and book the next-monsoon check visit in the CRM.
8. Ask for a review after 30 days. Founding homes: confirm the 2 visits by future buyers.

**SOP F: Complaint or guarantee claim** (coordinator owns it; supervisor inspects)
1. Acknowledge every complaint within 2 working hours, whatever the channel, and log it as a ticket against the job.
2. Ask for photos. Book an inspection within 3 working days.
3. The supervisor inspects: takes a moisture reading, photographs the wall, and compares it with the site-visit and prep photos.
4. If the wall bubbles or peels and was not excluded in writing, it is **covered**. Book a repaint (paint and labour free) within 14 days, weather permitting.
5. If it was excluded (a damp wall recorded at the visit), show the owner the recorded reading and photo, then offer Damp Shield at the published price.
6. Anything that isn't clear goes to the service manager, who decides within 48 hours. Don't argue on WhatsApp.
7. Close the ticket only when the owner confirms. Record the cost against the guarantee reserve, so the CFO can check the 3% assumption.
8. Each month, review every claim by crew and by condition grade. A crew with 2 upheld claims is retrained.

**SOP G: Weekly reorder and crew schedule** (manager + coordinator, Friday 16:00, 45 min)
1. Pull next week's starts and all running jobs from the CRM.
2. Give each job a crew, and check the crew's availability by phone. Keep 1 crew as a standby for no-shows.
3. Check the 7-day weather forecast. Move exterior coats away from forecast rain, and update any finish date at risk today, not at handover.
4. Paint: send the depot each job's list (product, shade, litres) for collection 2 days before the start. Reconcile last week's issued litres against the litres used and the returns, crew by crew.
5. Consumables: count tape, poly sheet and sandpaper, and order from the dealer to keep 2 weeks' stock.
6. Book the supervisors' routes for prep checks and handovers.
7. Review last week: jobs on date, late days, claims, quotes sent, and quotes converted.

### 5. Tools: the smallest stack

| Need | Product | Published price | Why |
|---|---|---|---|
| CRM: leads, quotes, job stages, guarantee tickets | **Bigin by Zoho**, Premier edition | ₹720 per user a month, billed yearly, + GST. Express is ₹400. ([Bigin India pricing](https://www.bigin.com/articles/bigin-india-pricing-clarification.html)) | It is a simple pipeline. 4 users (manager, 2 supervisors, coordinator) cost about ₹2,880 a month + GST. Upgrade path: [Zoho FSM, ₹1,000–₹1,800 per user a month, free for 2 users (partner listing)](https://precisiontech.in/software/zoho/zoho-fsm/zoho-fsm-in-puducherry/), once there are more than 20 jobs a month. |
| Daily customer updates | **WhatsApp Business app** on one company phone | Free to download ([App Store listing](https://apps.apple.com/app/id1386412985)) | Labels per job stage and quick replies. At 15 updates a day the app is enough. |
| WhatsApp at scale (later) | WhatsApp Business API through a provider such as AiSensy | Basic plan about ₹1,500 a month + GST ([TechJockey](https://www.techjockey.com/detail/aisensy)), plus Meta's charge of about ₹0.115 per utility message ([baat.ai summary](https://baat.ai/blog/whatsapp-api-pricing-india); [Meta's own page](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing) could not be reached) | Only when several staff need the same number, or for automated reminders. |
| Payments | UPI QR and bank transfer into Turbolux's current account; **Razorpay** or **Cashfree** payment links for card payers | Since 15 Oct 2026, UPI merchant payments above ₹2,000 carry a 0.4% fee capped at ₹300 ([ThePrint](https://theprint.in/economy/govt-sets-0-4-fee-on-upi-merchant-payments-above-rs-2000-caps-charge-at-rs-300/3043550/)). Razorpay's standard rate is 2% + 18% GST ([Razorpay blog](https://razorpay.com/blog/cheapest-payment-gateway-for-businesses-under-%e2%82%b925-lakh-monthly-gmv-how-to-compare-real-costs/); the pricing page could not be reached). Cashfree lists 1.95–2.0% ([Cashfree](https://www.cashfree.com/payment-gateway-charges/)). | Per ₹89,000 job: about ₹356 + GST if both payments go by UPI, or about ₹2,100 if all of it goes through a gateway at 2% + GST |
| Crew calendar | A shared Google Sheet: one row per crew, one column per day | Free | Simplest to start with. It moves into the CRM or FSM later. |
| Photo records | The CRM's job record, or one Google Drive folder per job | Free tier, or already within Turbolux's plan | Prep and moisture photos are the guarantee's evidence. They must be kept 3+ years. |
| Bookkeeping and GST invoices | Turbolux's existing accounting system, with a "Home Finish" cost centre | Existing | No new tool needed |

### 6. Licences, permits and insurance

**Rules differ by place and change often. Confirm each item with the authority, or with a chartered accountant or lawyer. This is not legal advice.**

| # | Item | Likely needed? | Where to confirm |
|---|---|---|---|
| 1 | Business entity | Run it as a division of the existing Turbolux company, so no new entity is needed. Confirm with the company secretary. | n/a |
| 2 | GST | Add painting/works-contract services to Turbolux's existing GSTIN, and add the Kochi office as a place of business if it isn't one. Painting works contracts are taxed at **18%** since the September 2025 rate changes ([DisyTax](https://disytax.com/gst-for-painting-contractors/)); the sub-code is SAC 995473 ([Busy](https://busy.in/sac-code-995473/)). | [gst.gov.in](https://www.gst.gov.in) |
| 3 | Kerala Shops & Commercial Establishments registration | Needed for the Kochi service office. Online, within 60 days of opening, renewed yearly ([SpotOnz](https://www.spotonz.com/blog/shop-establishment-act-kerala-registration/)). | [Labour Commissionerate, lc.kerala.gov.in](https://lc.kerala.gov.in) |
| 4 | Kochi Corporation trade licence (IFTE & OS) | Needed for office or store premises inside corporation limits | [Kochi Corporation notice](https://kochicorporation.lsgkerala.gov.in/en/481) |
| 5 | Labour Codes (wages, social security, OSH) | In force nationally since 21 Nov 2025; Kerala has draft rules only (see section 0) | [L&S Kerala tracker](https://employmentlaw.lkslaw.com/states/kerala) |
| 6 | Minimum wages | Pay at least the notified rate, and recheck once Kerala's 2026 rules are final | [lc.kerala.gov.in](https://lc.kerala.gov.in) |
| 7 | EPF and ESI | Turbolux is presumably already registered as a manufacturer. Extend coverage to the new staff, and to painters if they are employees (section 3). | [epfindia.gov.in](https://www.epfindia.gov.in), [esic.gov.in](https://www.esic.gov.in) |
| 8 | Contract-labour rules | Licensing applies only at **50+ contract workers** under the OSH Code ([JSA](https://www.jsalaw.com/corporate/labour-codes-summary-november-2025/)). Watch it when crews grow past 16. | Labour Commissionerate |
| 9 | Guest (migrant) workers | If any painter is a guest worker, employers and contractors must register them on Kerala's Athidhi portal ([Onmanorama](https://www.onmanorama.com/news/kerala/2024/09/04/migrant-workers-registration-mandatory-in-kerala-govt-to-launch-unified-portal-mobile-app.html)) | Labour Commissionerate |
| 10 | Construction workers' welfare board and cess | Painters may be eligible for the Kerala BOCW welfare board ([board info](https://kannur.nic.in/the-kerala-building-and-other-construction-workers-welfare-board)). The 1% cess now applies only to houses above ₹50 lakh ([Onmanorama](https://www.onmanorama.com/news/kerala/2025/11/24/construction-cess-exemption-labour-codes-kerala.html)), so repaints are unlikely to trigger it. Confirm. | Labour Commissionerate |
| 11 | Flats: association rules | Not a government permit. Each association sets its contractor hours, lift use and debris rules. Get them in writing at the site visit (SOP A). | The association's secretary |
| 12 | Employees' compensation insurance | Needed for any employee not covered by ESI; crew workers need a contractor rider | [New India Assurance](https://newindia.co.in/assets/docs/know-more/miscellaneous/employee-compensation/Employees%20Compensation%20Proposal%20Form.pdf) or a broker |
| 13 | Public / general liability insurance (damage to homes or furniture, injury to the public) | Commercial cover, not a statutory duty. The Public Liability Insurance Act 1991 applies only to hazardous substances ([Ethika](https://ethika.co.in/commercial-general-liability)). | 2–3 insurer quotes |
| 14 | Customer contract and guarantee terms | Legal review is already budgeted (₹50,000 in startup costs) | A lawyer |

### 7. Risk register: the ten most likely failures

| # | What goes wrong | Likelihood | Impact | Plan |
|---|---|---|---|---|
| 1 | **A crew doesn't turn up, or leaves mid-job** (the top complaint about rivals, `competitors.md`) | High | High (late credit, trust) | Keep 1 standby crew. The 7:45 check (step 1). Hold back part of the piece rate until handover. Give priority work to crews with good records. Certify more crews than you need, so no crew becomes indispensable. |
| 2 | **Jobs take about 13 days, not about 7, so capacity falls short** (section 0) | High | High (missed plan, late days) | Time January's jobs. Sign dates from measured painter-days. Certify 3–5 more crews by Oct 2027, or move to 4–5-painter crews. |
| 3 | **Rain during exterior work** (May and Oct are the wettest working months) | High in Apr–May and Sep–Nov; low Dec–Mar | Medium | Exteriors Dec–mid-Apr. Add 2 rain days to exterior finish dates in wet months. Check the forecast every Friday (SOP G). Do interior work on rain days. |
| 4 | **Damp found at the site visit** | High (Kerala) | Medium (scope, margin) | Record the moisture reading. Exclude in writing or quote Damp Shield. Price Damp Shield before the season. Never absorb damp work inside the fixed price. |
| 5 | **The size or condition band is wrong, so the fixed price loses money** | Medium | High | A published band table. The manager approves any grade C quote. Track how often a visit moves the band (board condition). |
| 6 | **A wave of guarantee claims after the June–Sept 2027 monsoon** | Medium | High (a 3-year tail) | Prep photos and moisture records on every wall. Next-monsoon check visits planned for Sep–Oct. A monthly claims review by crew. Recheck the 3% reserve against real claims. |
| 7 | **Dealers or contractors push back** (they lose painting business) | Medium | High (core paint sales) | Pay dealers 4% on every referred job. Certify the dealers' own painters first. Buy consumables through dealers. Run a dealer briefing before launch. |
| 8 | **Building-hour conflicts in flats** (shorter days, lift bans, no Saturdays) | High for flats | Medium (late days) | Written association rules at the visit. Build those hours into the finish date. Schedule Flat Finish in May and October, when exteriors pause. |
| 9 | **The owner withholds or disputes the 70% payment** | Medium | High (cash) | Shade sign-off, a photo trail, a written snag list, and snags fixed within 2 days. Any dispute goes to the manager within 48 h, never argued on WhatsApp. |
| 10 | **A painter falls from a ladder or scaffold** | Low | Very high (injury, liability) | Safety check of ladders at certification. Scaffolding from a hire firm for 2-storey work. Compensation and liability insurance in place before job 1. |

**Also watch:** paint issued to a job that ends up on a crew's private work (the weekly litre reconciliation in SOP G); the coordinator being absent (the manager is the backup); a rise in Kerala's minimum wage (section 0).

### 8. Day-one checklist (before 4 January 2027)

- [ ] Painter status decided (employee or independent crew). EPF, ESI and insurance set up to match.
- [ ] 10 crews certified. Each has signed the written prep standard and had its ladders checked.
- [ ] Band table (size × condition) and quote template published. Damp Shield priced, or excluded for the pilot.
- [ ] 4 moisture meters bought (one model) and Turbolux's damp threshold set.
- [ ] Bigin set up with stages: Lead → Visit booked → Quoted → Booked (30%) → Prep checked → Painting → Handed over (70%) → Guarantee.
- [ ] WhatsApp Business on the coordinator's phone, with quick replies for SOP D.
- [ ] UPI QR on the current account, and a gateway account for card payers.
- [ ] Shops & Establishments registration and trade licence applied for. GSTIN amended.
- [ ] Insurance quotes accepted and policies issued.
- [ ] Dealer briefing held.

### 9. Open questions (get a quote or an answer)

1. Scaffolding weekly hire rate in Kochi (Unity, Sundaram, Brightscaff).
2. Masking tape, poly sheet and sandpaper prices from 2 Turbolux dealers, and reusable drop cloths from a canvas maker.
3. Employees' compensation and general liability premiums (2–3 insurers), once painter status is decided.
4. Do certified painters count as Turbolux employees under the Code on Social Security? Is the EPF wage ceiling ₹15,000 or ₹25,000?
5. Kerala's current minimum wage for building painters after the 19 May 2026 revision, and the final Labour Code rules.
6. Turbolux's transfer price for paint, primer and putty (the CFO's ₹13,375 is an estimate).
7. Does Turbolux's bank charge the 0.4% UPI fee on its current-account QR? Razorpay's and Cashfree's live UPI rates (the pages could not be opened here).
8. Real painter-days per job from January's 3 jobs, room by room.
9. The moisture threshold for "damp" in Turbolux's own technical data.
10. Kochi associations' typical contractor hours: collect them from the first 10 flat visits.

### 10. Changes for the CFO

I have not edited `numbers.json`, because another step is editing it. These are the changes my research supports. Re-run `/founder-cfo` after applying them.

| Line in numbers.json | Old | New | Source and reason |
|---|---|---|---|
| `capacity_per_day` (jobs a month) | 35 | **20** with 10 crews of 3 (range 15–22). Keep 35 only if about 18 crews are certified. | ₹36,320 ÷ ₹700–₹1,000 a day = 36–52 painter-days a job ([Kerala guide](https://aapkapainter.com/blog/house-painting-cost-in-kerala)); [InfraLens](https://infralens.in/rate-analysis/premium-exterior-emulsion) gives about 40. Capacity = 30 painters × 26 days ÷ about 40. |
| `plan_per_day` 30 / ramp Nov 20, Dec 24 | needs 10 crews | Keep, but **certify 3 more crews by Nov 2027** (Dec needs about 12–13 crews). The plan of 30 needs about 15 crews. | Same arithmetic. Months up to Oct (max 15 jobs) fit within 10 crews. |
| Crew training and certification (startup) | ₹1,50,000 (10 crews) | ₹2,25,000 if 15 crews are certified for the plan (the same ₹15,000 per crew) | Follows from the line above; the per-crew cost is still the CFO's estimate |
| Payment fees, about 1% | ₹890 a job | **Keep ₹890** if most customers pay by UPI or bank transfer (about ₹420 a job incl. GST when both payments go by UPI). Use **₹2,100** if everything goes through a gateway. | [UPI 0.4% capped at ₹300, from 15 Oct 2026](https://theprint.in/economy/govt-sets-0-4-fee-on-upi-merchant-payments-above-rs-2000-caps-charge-at-rs-300/3043550/); [Razorpay standard 2% + GST](https://razorpay.com/blog/cheapest-payment-gateway-for-businesses-under-%e2%82%b925-lakh-monthly-gmv-how-to-compare-real-costs/) |
| New fixed line: employer EPF on 4 staff | none | **+₹7,200 a month** (12% × ₹15,000 × 4), or +₹12,000 if the ceiling is ₹25,000. Pending the accountant. | [Zoho Payroll EPF guide](https://www.zoho.com/in/payroll/academy/taxes-and-compliance/epf-scheme-2026-guide.html), [Fox Mandal](https://foxmandal.in/News/epfo-wage-ceiling-raised-what-employers-need-to-do-now) |
| New variable line: painter EPF, only if painters are employees | none | **About +₹2,700 a job** (₹1,800 a month × 3 painters ÷ about 2 jobs a month each). Pending the accountant. | Same sources. Leave it at 0 if crews are independent. |
| Moisture meters within "meters, covers, kits" (startup) | part of ₹1,50,000 | No change to the total. Meters cost only ₹13,260–₹24,000 (4 × ₹3,315–₹6,000), which leaves room for covers and ladders. | [Stanley](https://buysupplies.in/products/stanley-0-77-030-moisture-meter-for-measuring-masonry), [Aadarsh](https://m.indiamart.com/aadarshtechnologies/moisture-meter.html) |
| Software, CRM, phone | ₹5,000 a month | No change: Bigin Premier for 4 users is about ₹3,400 a month incl. GST, and WhatsApp is free | [Bigin](https://www.bigin.com/articles/bigin-india-pricing-clarification.html) |
| Insurance | ₹5,000 a month | No change until quotes arrive. General liability alone is about ₹1,250–₹3,330 a month. Compensation cover depends on wages. | [BimaKavach](https://www.bimakavach.com/blog/commercial-general-liability-insurance-for-contractors/) |
| Crew piece rate, consumables, travel | ₹36,320 / ₹1,500 / ₹1,200 | No change: the piece rate sits inside the published ₹7–₹12 and ₹9–₹15 per sq ft labour-only rates. Check whether the ₹1,200 site-visit travel per job and the ₹10,000 supervisor travel a month count the same trips twice. | [Kerala 2026 guide](https://aapkapainter.com/blog/house-painting-cost-in-kerala-rates-for-interior-exterior-work-2026/) |

GST at 18% on painting works contracts, which `pricing.md` assumed, matches [DisyTax](https://disytax.com/gst-for-painting-contractors/). The accountant should confirm it.

Next: `/founder-launch`.

## Launch plan

Today is Wed 11 Nov 2026.
- **The test:** 23 Nov – 13 Dec 2026.
- **Go / no-go:** Mon 14 Dec.
- **First founding home starts:** Mon 4 Jan 2027.
- **Public booking opens:** Mon 11 Jan 2027.

All ₹. Built from:
- `founder/ops.md`: lead times, the January rota, the day-one checklist, the risk register.
- `founder/marketing.md`: the campaign from L−14.
- `founder/cfo.md`: the numbers to beat.
- `founder/brand.md`: name, site board, profiles.

### 1. Test before you spend: the founding-homes pre-sale

The big costs are:
- the ₹8 lakh startup;
- ₹2.04 lakh a month of staff;
- certifying 10 crews.

None of that should be committed on the strength of 20 *simulated* buyers. The cheapest real test for a service is **paid pilot clients at the real price**.

**The test (23 Nov – 13 Dec 2026, 3 weeks):**
- Sell the **10 founding homes** at the real prices: Home Finish ₹89,000, Flat Finish ₹59,000, ₹10,000 off for allowing two visits. Each booking pays a real **30% deposit**.
- Start dates are 4 Jan to mid-Feb. The deposit is **fully refundable** if Turbolux cannot start by the signed date.
- **Who runs it:**
  - One Turbolux technical or sales person from the existing team does the site visits with a moisture meter and the written quote template.
  - Leads come from Kochi dealers (counter display, staff briefing), a one-page booking page on turboluxpaints.com, and a small Google Search budget (≈ ₹30,000).
- **What it costs:** ≈ ₹30,000 in ads, ≈ ₹15,000 in dealer displays, staff time, and 4 moisture meters (≈ ₹15,000). That is about ₹60,000 before anything big is signed.
- **Before the test:** certify 3 crews only (A, B, C), so the first jobs can actually happen.

**The success line, written now:**

| | Go | Rethink |
| --- | --- | --- |
| Site visits done | ≥ 40 | < 25 means a demand problem; go back to `/founder-marketing` |
| Paid bookings (30% deposit) | **≥ 6** (≥ 15% of visits) | **< 4** (< 10% of visits) |
| Bookings with a date the ops plan can meet | All | Any date we can't meet, refund it |

**Compare with the panel.** The re-tested panel bought at 20%, which is an upper bound for simulated buyers.
- Real buyers at 15% or more: the offer holds.
- Real buyers at 10–15%: go, but run the price test hard (₹89,000 vs ₹95,000, `pricing.md`) and watch the CFO's ramp.
- Real buyers under 10%: **trust the real buyers.** Pause the hiring and go back to `/founder-offer` and `/founder-pricing`. The likely fixes are proof, the damp guarantee and the partial-job option (`offer.md` §5).

### 2. The countdown

Weekly blocks. ⚑ marks the **critical path**: if one of these slips, job 1 moves.

**Owners:**
- **F**: founder or Turbolux leadership.
- **SM**: service manager, hired by the go/no-go date. Until then, the Turbolux person running the test.
- **A**: accountant / lawyer.
- **M**: marketing.
- **D**: dealer manager.

| Week | Task | Owner | Deadline |
| --- | --- | --- | --- |
| **16–20 Nov** | ⚑ Decide painter status: employee or independent crew, with EPF/ESI and insurance to match (`ops.md` §0.3, open question 4) | F + A | Fri 20 Nov |
| | ⚑ Set Turbolux's transfer price for paint, primer and putty, and replace the CFO's ₹13,375 estimate | F | Fri 20 Nov |
| | Confirm 18% GST on works-contract painting; amend the GSTIN for the service | A | Fri 20 Nov |
| | ⚑ Publish the band table (size × condition) and the written quote template; decide whether Damp Shield is priced or excluded for the pilot | SM | Fri 20 Nov |
| | Booking page on turboluxpaints.com (`brand.md` touchpoint 1); Google Business Profile | M | Fri 20 Nov |
| | Dealer briefing pack: offer, 4% referral, referral code | D | Fri 20 Nov |
| **23–27 Nov** | **Test starts Mon 23 Nov.** Dealer displays up; Google Search live | M + D | Mon 23 Nov |
| | ⚑ Certify crews A, B, C: prep standard signed, ladders checked, one shadow day | SM | Fri 27 Nov |
| | Buy 4 moisture meters; set the damp threshold from Turbolux's technical data | SM | Fri 27 Nov |
| | Insurance quotes: employees' compensation + general liability (2–3 insurers) | A | Fri 27 Nov |
| **30 Nov – 4 Dec** | Site visits and quotes; deposits into the current account (UPI QR + gateway for cards) | SM | ongoing |
| | Painter meet at the main dealer: Turbolux certification for local painters (`marketing.md` hook 10) | D + SM | Sat 5 Dec |
| **7–11 Dec** | Site visits continue; the test tally is kept daily | SM | ongoing |
| **Mon 14 Dec** | **GO / NO-GO** against the success line above. If no-go, refund the deposits and stop here. | F | **Mon 14 Dec** |
| **14–18 Dec** | ⚑ Hire the service manager, 2 supervisors and the coordinator (or second internal staff) | F | Fri 18 Dec |
| | ⚑ Accept insurance quotes; policies issued before job 1 | A | Fri 18 Dec |
| | Kerala Shops & Establishments registration and trade licence applied for (`ops.md` §6) | A | Fri 18 Dec |
| **21–24 Dec** | ⚑ Certify crews D–J (7 more): shadow days on the first jobs are scheduled in January (`ops.md` rota) | SM | Thu 24 Dec |
| | Bigin CRM stages set up; WhatsApp Business quick replies for the daily update (`ops.md` §5, SOP D) | Coordinator | Thu 24 Dec |
| | Site boards, uniforms and covers delivered (`brand.md`) | M | Thu 24 Dec |
| **28 Dec – 1 Jan** | Marketing L−14 starts Mon 28 Dec (`marketing.md` §4) | M | Mon 28 Dec |
| | **Soft open:** a full dry run of a site visit, quote, prep check and WhatsApp update at a Turbolux staff member's home (friends-and-family job) | SM | Wed 30 Dec |
| | ⚑ Day-one checklist complete (`ops.md` §8) | SM | Fri 1 Jan |
| **Mon 4 Jan 2027** | **Founding home 1 starts** (crew A) | SM | Mon 4 Jan |
| **Mon 11 Jan 2027** | **Public booking opens.** Founding home 2 starts (crew B) | All | Mon 11 Jan |
| **Mon 18 Jan** | Founding home 3 starts (crew C). Home 1 handover ≈ 20 Jan | SM | — |
| **Sun 31 Jan** | Founding-homes offer ends (no extension) | M | Sun 31 Jan |

**The critical path:**
painter status → insurance → crews A–C certified → the go/no-go on 14 Dec → staff hired → day-one checklist → job 1 on 4 Jan.

The finish dates signed in the test depend on real painter-days. Until January's jobs are timed, sign **13 working days + 1 buffer day** for a house. That means signing nothing shorter than about 2.5 weeks.

### 3. Launch day run sheet: Mon 11 Jan 2027

| Time | Who | What |
| --- | --- | --- |
| 07:45 | Supervisor North | Crew check at job 1 (day 6) and job 2 (day 1). Both crews on site? If not, call the standby crew (`ops.md` risk 1). |
| 08:00 | Crew B + Supervisor South | Job 2 starts: shade patch signed off, furniture and floors covered, prep begins. |
| 09:00 | Marketing | Launch post on Instagram and Facebook: the On-Date Promise (hook 1). Booking page switched from "founding homes waitlist" to "book a site visit". Google ads move to full budget. |
| 09:30 | Dealer manager | Calls every Kochi dealer: booking is open, referral codes are live. |
| 10:00 | Service manager | Site visits 1–2 of the day: moisture reading recorded, written quote, signed date, 30% by UPI. |
| 12:00 | Coordinator | Replies to every enquiry within 1 hour. Books site visits into Bigin. |
| 14:00 | Service manager | Site visits 3–4. |
| 16:00 | Supervisor North | Mid-job check at job 1: photos into the job folder. |
| 17:30 | Coordinator | Daily WhatsApp photo updates to the job 1 and job 2 owners (SOP D). |
| 18:30 | Service manager + marketing | Day tally: enquiries, site visits booked, quotes, deposits, cost per site visit. |

**If something breaks:**
- **A crew no-show:** the standby crew goes in that day, the owner is told before 09:00, and the date is held (risk 1).
- **Rain on an exterior:** switch to interior work and update the date today, not at handover (risk 3).
- **The booking page fails:** take bookings by WhatsApp click-to-chat and phone.
- **A complaint online:** the service manager replies within 2 hours (`brand.md` touchpoint 5). Never argue on WhatsApp.

### 4. The first 30 days: what to watch and when to change

**Weekly numbers**

| Number | Target | Change something when |
| --- | --- | --- |
| Site visits booked / week | ≥ 15 by week 2, ≥ 25 by week 4 (`marketing.md`) | < 10 for two weeks: move budget to the channel that books more (dealers or Google) |
| Site visit → paid booking | ≥ 15% | < 8% for two weeks: the quote or the trust is the problem. Look at `offer.md` §5 and the price test. |
| Cost per site visit (paid) | ≤ ₹600 | > ₹1,500: pause that ad set |
| Jobs booked for February | ≥ 6 (the CFO's month 2) | < 4 by 25 Jan: the ramp is wrong. Re-run `/founder-cfo` with `--volume 0.6`. |
| **Painter-days per job** (timed per room) | ≈ 40 or fewer | > 45: capacity is below 20 a month. Re-sign future dates and re-run the CFO. |
| On-date finish rate | 100% in the pilot | Any late job: root-cause review within 48 h. The late credit is paid without argument. |
| Band changed at site visit | < 20% of quotes | > 20%: the band table is wrong. Fix it before more quotes go out. |

**Reviews**

- **Day 7 (Mon 18 Jan):**
  - Did the site-visit volume match the test?
  - How many painter-days did job 1 take up to day 10?
  - Is the WhatsApp update going out every day?
- **Day 14 (Mon 25 Jan):**
  - Job 1 handover: on date? What was the owner's score? Anything on the snag list?
  - Was the 70% paid on the day?
  - How many founding homes are left? Is the price test giving a signal yet?
- **Day 30 (Wed 10 Feb):**
  - Real conversion vs the panel's 20%.
  - Real painter-days vs 40, and the real paint used vs the CFO's ~84 L.
  - Update `founder/numbers.json` with real costs and re-run `/founder-cfo` and `/founder-plan`.
  - Decide whether to move the price to ₹95,000, and whether to certify crews K–O ahead of the post-monsoon season.

_The panel is simulated buyers and the numbers are projections from your inputs. Confirm demand with real customers and costs with real quotes before you spend. Not financial, legal or tax advice._
