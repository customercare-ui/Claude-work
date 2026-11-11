# The CFO's note

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

# Unit economics: Turbolux Home Finish, 2BHK paint + painter package, Kochi pilot (all amounts in Indian rupees; volumes are PER MONTH: days_per_month is 1, so every 'a day' in the tool's output means 'a month')

Every number below comes from the input file. Nothing is looked up or guessed.

## One job

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

## The margin that matters

Fixed costs: $204,200 a month (Service manager (ESTIMATE) $55,000, Two site supervisors for prep and quality checks (ESTIMATE) $60,000, Booking and customer-care coordinator (ESTIMATE) $22,000, Booking software, CRM, phone (ESTIMATE) $5,000, Supervisor travel (ESTIMATE) $10,000, Always-on local ads, Google and Meta (ESTIMATE) $40,000, Liability and workmen insurance (ESTIMATE) $5,000, Employer EPF on 4 staff, 12% x Rs 15,000 x 4 (pending accountant; founder/ops.md) $7,200).

- **Break-even: 15 jobs a day.** Below that you lose money every month.
- **Profit margin at your plan** (20 a day): **5%** of every sale, after every cost.
- Capacity: 20 a day.

## Year 1, month by month

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

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 5% | 15 | -$905,057 |
| Price -10% | -5% | 31 | -$1,719,633 |
| Volume -20% | 2% | 15 | -$1,214,126 |
| Unit costs +15% | -7% | 40 | -$1,895,120 |

## Red flags

- Year 1 loses money on operations (-$905,057).
- The startup spend is not earned back within year 1.
