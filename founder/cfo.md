# The CFO's note

> **Read first:** all amounts are **Indian rupees**; the tool prints `$`. Volumes are **per month**: this business sells about one job a day at most, so `days_per_month` is set to 1. Every "a day" below means **a month**. The price in the table is **before GST**: ₹75,424 = ₹89,000 to the buyer including 18% GST (rate to confirm with an accountant). Nearly every cost is an **ESTIMATE** (`founder/cfo-sources.md`). Replace them with Turbolux's real paint cost, real painter rates and real salaries before deciding anything.

- **The margin.** Each Home Finish job at ₹89,000 leaves **₹14,309 (19%)** after its own costs. At the plan volume of 30 jobs a month, the profit margin is **10%** of every sale after all costs. Break-even is **14 jobs a month**, and capacity is about 35.
- **The line to watch: the painter crew's piece rate.** At ₹36,320 it is 48% of the pre-GST price, the biggest cost by far. Unit costs +15% turns the plan margin to **−2%** and year 1 to **−₹17.5 lakh**. Price −10% takes the margin to **0%**. This business lives on labour cost and on holding the price.
- **Year 1 loses money: −₹6.6 lakh on operations, −₹14.6 lakh after the ₹8 lakh startup spend.** The cause is the calendar, not the unit. Months 1–3 are ramp-up, and the monsoon (months 6–8, 2–3 jobs) carries the full ₹1.97 lakh-a-month team. Peak months make money: month 12 (24 jobs) earns **+₹1.46 lakh**.
- **Cash: ₹17.1 lakh** is needed before it pays for itself (₹8 lakh startup + the deepest monthly losses). The startup is not earned back within year 1.
- **The ramp is the weakest number.** It assumes 3 → 24 jobs a month. The re-tested panel buys at 20%, which is an upper bound for simulated buyers. At a real 10% site-visit-to-booking rate, 24 jobs needs about 240 site visits a month. If volume comes in 40% lower (`--volume 0.6`), year 1 is **−₹13.4 lakh** and cash needed is **₹21.5 lakh**.

**Ways to improve the margin (each one run through the tool, all else equal):**

| Change | Contribution per job | Margin at plan | Year 1 operating | Cash needed |
| --- | ---: | ---: | ---: | ---: |
| Base (₹89,000) | ₹14,309 | 10.0% | −₹6,61,261 | ₹17,14,476 |
| **Crew piece rate −10%** (volume commitment to certified crews) | ₹17,941 | 15.1% | **−₹2,29,053** | ₹14,96,556 |
| **Price ₹95,000** (the test price in `pricing.md`) | ₹19,393 | — | **−₹56,177** | ₹14,09,392 |
| **Paint at 40% of retail** instead of 50% (Turbolux knows the real figure) | ₹16,984 | 13.8% | −₹3,42,936 | ₹15,53,976 |
| Off-season interior jobs (6/6/8 jobs instead of 2/2/3 in the monsoon months) | ₹14,309 | 10.3% | −₹4,75,248 | ₹15,28,463 |
| Pause ads in the 3 monsoon months (averaged as ₹30,000/month) | ₹14,309 | 10.7% | −₹5,41,261 | ₹16,24,476 |

The first three together would very likely turn year 1 positive. Run them together once the real figures are in. The "price ₹95,000" run holds the percentage-based costs at their ₹89,000 values, so it slightly flatters the result.

**The board's money conditions (`founder/board.md`):**
- [x] Margin positive at the price: Home Finish leaves 19% per job. Flat Finish has a rough cut of about 20% (in `pricing.md`), not yet run through the tool.
- [x] Guarantee costed: a 3% reserve plus a next-monsoon visit. The claim rate is an estimate.
- [x] Dealers earn on each package: 4% referral fee.
- [ ] **Year 1 makes money: NOT MET** on these estimates.
- [ ] Crew wages from real quotes: still public-rate estimates.

*Not financial, tax or legal advice. An accountant should check GST treatment (works contract), payroll costs (EPF/ESI) and structure before money moves.*

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

Fixed costs: $197,000 a month (Service manager (ESTIMATE) $55,000, Two site supervisors for prep and quality checks (ESTIMATE) $60,000, Booking and customer-care coordinator (ESTIMATE) $22,000, Booking software, CRM, phone (ESTIMATE) $5,000, Supervisor travel (ESTIMATE) $10,000, Always-on local ads, Google and Meta (ESTIMATE) $40,000, Liability and workmen insurance (ESTIMATE) $5,000).

- **Break-even: 14 jobs a day.** Below that you lose money every month.
- **Profit margin at your plan** (30 a day): **10%** of every sale, after every cost.
- Capacity: 35 a day.

## Year 1, month by month

| month | jobs a day | revenue | profit | cumulative (after $800,000 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 3 | $226,271 | -$154,074 | -$954,074 |
| 2 | 6 | $452,542 | -$111,148 | -$1,065,221 |
| 3 | 10 | $754,237 | -$53,913 | -$1,119,134 |
| 4 | 14 | $1,055,932 | $3,322 | -$1,115,812 |
| 5 | 10 | $754,237 | -$53,913 | -$1,169,725 |
| 6 | 2 | $150,847 | -$168,383 | -$1,338,107 |
| 7 | 2 | $150,847 | -$168,383 | -$1,506,490 |
| 8 | 3 | $226,271 | -$154,074 | -$1,660,564 |
| 9 | 10 | $754,237 | -$53,913 | -$1,714,476 |
| 10 | 15 | $1,131,356 | $17,631 | -$1,696,845 |
| 11 | 20 | $1,508,475 | $89,175 | -$1,607,671 |
| 12 | 24 | $1,810,170 | $146,410 | -$1,461,261 |

- **Year 1 operating profit: -$661,261** on $8,975,424 of revenue.
- After the $800,000 startup spend: -$1,461,261.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$1,714,476**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 10% | 14 | -$661,261 |
| Price -10% | 0% | 30 | -$1,558,804 |
| Volume -20% | 8% | 14 | -$1,001,809 |
| Unit costs +15% | -2% | 39 | -$1,752,164 |

## Red flags

- Year 1 loses money on operations (-$661,261).
- The startup spend is not earned back within year 1.
