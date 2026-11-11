# Pricing: Turbolux Home Finish (Kochi pilot)

All amounts are Indian rupees. Prices to the buyer **include 18% GST** (assumed rate for painting work; an accountant should confirm). The CFO's numbers use the price before GST. The tools print `$`; read it as ₹.

## 1. The price

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

## 2. The ladder

Four of the 20 buyers live in flats, where the building association owns the exterior. All four said half of the package was useless to them. Two others wanted only part of the house done. One package cannot serve them all.

| Rung | What it is | Price (incl. GST) | Why step up |
| --- | --- | ---: | --- |
| **Flat Finish** | 2BHK flat, interior only (walls + ceilings), same crew, date and guarantee. Works within building contractor hours. | **₹59,000** (to test) | The entry point for flat owners. The CFO's rough cut: ~₹40,200 variable cost, ~₹9,800 left per job (≈20%). Confirm before publishing. |
| **Home Finish** | Independent 2BHK house, interior + exterior | **₹89,000** | The core package. |
| **Home Finish + Damp Shield** | Home Finish plus damp treatment and a waterproof coat on the exterior walls, with a longer guarantee | **Price after costing** | Answers the buyers whose real problem is damp (P002, P010). Waterproofing materials and labour are not costed yet, so no price is set. |

A part-house option ("hall, front room and road-facing wall", P013) is not a rung yet. On jobs that small, the site visit and travel eat the margin. Revisit once the CFO can see cost per room.

## 3. The opening offer

**Founding homes, Kochi: the first 10 bookings before 31 January 2027 get ₹10,000 off** if the owner agrees that:

- their finished home can be photographed and visited by two future buyers;
- they will give an honest review after 30 days.

This is not a discount to "buy" customers. It pays for the proof the panel asked for again and again ("a finished home nearby I can go and look at"). It is capped at 10 homes and paid from the ₹1 lakh show-home budget in startup costs, and it has an end date. No "was ₹X" price will be shown, because none was ever charged.

## 4. What to test with real buyers

- **₹89,000 vs ₹95,000** for Home Finish. Split site-visit bookings from the website and dealers into two groups, quote each group one price, and track conversion from site visit to booking. Run until each price has at least 15 site visits.
- **₹59,000 Flat Finish**: quote it to flat owners who book a visit and track the same conversion.
- **Three competitor quotes:** book real site visits from Asian Paints, Birla Opus and one Kochi contractor for a 2BHK house. That replaces the area-based estimate in `founder/competitors.md`.

## 5. The panel's price objections (verbatim, simulated buyers: research only)

1. "₹78,000 is close to a month of my salary, and our local painter would do the inside and outside of a 2BHK for much less." (P012)
2. "₹78,000 for the whole house is close to a month's pay when the wedding is already eating our savings, and I'm not going to pay for bedrooms nobody will see." (P013)
3. "...a fixed ₹78,000 with no room to bargain means I cannot check it against the per-square-foot rate my local contractor gives me." (P001)

Marketing answers these with a printed per-sq-ft breakdown at the site visit, the Flat Finish rung, and the written final-bill promise (see `founder/offer.md`).
