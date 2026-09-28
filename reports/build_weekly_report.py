"""Build the combined Marketing Weekly Task Report (21-09-2026 to 26-09-2026)
from the six daily task report sheets.

Weekly WTG % = (sum of daily WTG %) / number of days
Weekly score = (sum of daily ACH / SCORE) / number of days
so the weekly grand total = average of the daily grand totals.
"""
from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

DAYS = 6
OUT = "reports/Marketing_Weekly_Task_Report_21-26_Sep_2026.xlsx"

# (section, KRA, [(task, days, target, achievement, sum_daily_wtg, sum_daily_score, bottleneck)])
# Reach rows carry no weight (merged with WhatsApp weight in the daily sheets).
DATA = [
    (None, "Website - Google Indexing & Linking", [
        ("Page linking, internal linking & submit/verify priority pages in Google Search Console",
         "21, 22, 24", 16, 16, 70, 70, ""),
    ]),
    (None, "Website Updation", [
        ("Images changing", "21", 4, 4, 2, 2, ""),
        ("Some texts removal (like image briefs)", "21", 1, 1, 2, 2, ""),
        ("Removing open jobs", "21", 1, 1, 2, 2, ""),
        ("Redirecting to Contact Us / Find Dealer", "21", 1, 1, 2, 2, ""),
        ("Website updation / business-related marketing activity", "25", 1, 1, 10, 10, ""),
        ("Updation of products based on the TDS sheet", "25", 7, 7, 20, 10, ""),
    ]),
    (None, "Video / Content", [
        ("Influencer videos follow-up", "21", 2, 2, 20, 20, ""),
        ("Content planning", "21", 4, 4, 20, 20, ""),
        ("SMM video editing - Insta trend office reel", "23", 1, 1, 7.5, 7.5, ""),
    ]),
    (None, "Influencer Marketing Management", [
        ("Finding through Instagram & getting rates", "22", 5, 5, 15, 5, ""),
        ("Logistics follow-up - 500ml Extra Life sample to Kollam influencer", "24", 1, 1, 5, 5, ""),
    ]),
    (None, "Token Tracking App", [
        ("SAP automation follow-up", "21", 1, 0, 4, 0, "Token expired Claude"),
        ("Painter / joined / incentive / shop-wise painters data report creation", "23", 1, 1, 20, 20, ""),
        ("Testing QR scanning with hand-held scanner in factory", "23", 1, 1, 10, 10, ""),
    ]),
    (None, "Epoxy Campaign - SEO", [
        ("Keyword research - Google Keyword Planner, Google Search Console", "26", 1, 1, 10, 10, ""),
    ]),
    (None, "Google Analytics & Tag Manager", [
        ("Setting up the account - connecting the website", "26", 2, 0, 10, 0, ""),
    ]),
    (None, "Promotional Gift Purchase - Pen", [
        ("Finding vendors & quotations", "24, 25, 26", 3, 0, 30, 0, ""),
    ]),
    ("Team", "Product Container / Label Design - DampShield", [
        ("DampShield review", "21", 1, 0, 3, 0, ""),
        ("Design revisions based on feedback", "22, 23", 2, 1, 12.5, 5, ""),
        ("Changes from feedback & reprinting", "26", 1, 1, 10, 10, ""),
    ]),
    ("Team", "Promotional Gift Design - Diary", [
        ("Concept, layout, branding & artwork development", "22, 23, 24, 25, 26", 6, 2, 45, 15, ""),
    ]),
    ("Team", "Branding / Printing", [
        ("Layout, branding, content placement, dieline & print-ready artwork", "22", 1, 1, 10, 10, ""),
        ("Brochure - resize to another size", "23", 1, 1, 10, 10, ""),
        ("Shop hoarding design - Kunnath H/W", "25", 1, 1, 6, 6, ""),
        ("Warranty card design for website", "25", 1, 0, 5, 0, ""),
    ]),
    ("Team", "Epoxy Campaign", [
        ("Planning of content for office shoot", "26", 3, 3, 5, 5, ""),
        ("Planning dealer / site / consumer testimonials", "26", 1, 1, 8, 8, ""),
        ("AI video - Epoxy AI videos for social media & LED wall", "26", 2, 0, 10, 0, ""),
    ]),
    ("Operational Follow up", "SMM / Meta Ads - DM", [
        ("Reach generated", "21-26", "1800k", "913k", None, None, ""),
    ]),
    ("Operational Follow up", "WhatsApp Broadcast / WATI - DM", [
        ("Painter message creation & WhatsApp broadcast execution", "21-26", 1500, 1100, 31, 17, ""),
        ("Dealer database collection, cleaning & WATI upload", "22", 500, 544, 10, 10, ""),
    ]),
    ("Operational Follow up", "SMM / Posting in Meta - DM", [
        ("Normal reel", "22", 1, 1, 5, 5, ""),
        ("Extra Life influencer video", "23, 24", 2, 1, 10, 5, ""),
    ]),
    ("Operational Follow up", "Leads ROI Follow-up - DM", [
        ("Extra Life ad video leads - checking sales with Customer Service dept.", "24", 31, 23, 10, 7.5, ""),
    ]),
    ("Operational Follow up", "Website SEO - DM", [
        ("AI site crawling research", "22, 23, 24, 25", 4, 4, 20, 20, ""),
        ("Topical authority research", "22, 23, 24, 25", 4, 3, 20, 15, ""),
        ("Review on DM research - ways to implement AI crawling & topical authority", "24", 1, 1, 5, 5, ""),
    ]),
    ("Operational Follow up", "Website Blog - DM", [
        ("SEO blog posts - research, create & publish in website", "21, 23, 24, 25, 26",
         18, 15, 60, 45, "Token expired Claude (21-09)"),
    ]),
    ("Operational Follow up", "SMM Google Ads - DM", [
        ("Setting up ad (Ezy Cover) - finding a call to action", "25", 1, 0, 6, 0, ""),
        ("Setting up ad - Prestige Epoxy", "26", 1, 0, 5, 0, ""),
    ]),
    ("Operational Follow up", "Promotional Gift - T-Shirt", [
        ("T-shirt readiness / delivery follow-up with vendor", "22, 23, 24, 25, 26", 5, 3, 17, 11, ""),
        ("T-shirt payment follow-up", "22, 23, 24, 25, 26", 5, 2, 17, 6, ""),
    ]),
]

# Day-wise summary (date, tasks, daily grand total)
DAILY = [
    ("21-09-2026", 14, 80.5),
    ("22-09-2026", 14, 70),
    ("23-09-2026", 14, 81.5),
    ("24-09-2026", 14, 70.5),
    ("25-09-2026", 14, 58.5),
    ("26-09-2026", 14, 50),
]

# sanity: weights add to 100/day, scores match the daily totals
tot_w = sum(t[4] or 0 for _, _, ts in DATA for t in ts)
tot_s = sum(t[5] or 0 for _, _, ts in DATA for t in ts)
assert tot_w == 100 * DAYS, tot_w
assert tot_s == sum(d[2] for d in DAILY), tot_s

# ---------- styles (matching the daily sheets) ----------
BROWN = PatternFill("solid", fgColor="843C0C")
PEACH = PatternFill("solid", fgColor="F8CBAD")
BLUE = PatternFill("solid", fgColor="D9E1F2")
TEAL = PatternFill("solid", fgColor="DDEBF7")
YELLOW = PatternFill("solid", fgColor="FFFF00")
GREY = PatternFill("solid", fgColor="EDEDED")
F = "Calibri"
thin = Side(style="thin", color="000000")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)
LEFT = Alignment(horizontal="left", vertical="center", wrap_text=True)

wb = Workbook()
ws = wb.active
ws.title = "Weekly Report"
ws.sheet_view.showGridLines = False

widths = {"A": 6, "B": 34, "C": 62, "D": 16, "E": 11, "F": 10, "G": 14, "H": 12, "I": 26,
          "K": 13, "L": 13}
for col, w in widths.items():
    ws.column_dimensions[col].width = w

HEAD = ["No", "KRA", "KPI TASK (WEEK)", "DAYS (Sep)", "TARGET", "WTG %", "ACHIEVEMENT",
        "ACH / SCORE", "BOTTLE NECK"]
LAST = "I"


def style(cell, fill=None, bold=False, align=CENTER, color="000000", size=10):
    cell.font = Font(name=F, bold=bold, color=color, size=size)
    cell.alignment = align
    cell.border = BORDER
    if fill:
        cell.fill = fill


# title
ws.merge_cells(f"A1:{LAST}1")
ws["A1"] = "MARKETING - WEEKLY TASK REPORT [21-09-2026 to 26-09-2026]"
for c in ws["A1":f"{LAST}1"][0]:
    style(c, BROWN, True, CENTER, "FFFFFF", 13)
ws.row_dimensions[1].height = 24

for i, h in enumerate(HEAD, 1):
    style(ws.cell(2, i, h), PEACH, True)
# helper columns (calculation basis)
for col, h in (("K", "Σ Daily WTG %"), ("L", "Σ Daily Score")):
    c = ws[f"{col}2"]
    c.value = h
    style(c, GREY, True, color="595959")
ws["K2"].comment = Comment(
    f"Calculation basis: sum of the daily WTG % / ACH-SCORE values for this task across the "
    f"{DAYS} daily reports (21-26 Sep). Weekly WTG % and ACH/SCORE = these / {DAYS}.", "Report")
ws["N2"] = "No. of days"
ws["N2"].font = Font(name=F, bold=True, size=10)
ws["O2"] = DAYS
ws["O2"].font = Font(name=F, color="0000FF", size=10)
DAYS_REF = "$O$2"

row = 3
no = 0
section = None
first_data = row
for sec, kra, tasks in DATA:
    if sec != section:
        section = sec
        ws.merge_cells(f"A{row}:B{row}")
        ws.cell(row, 1, sec)
        for col in range(1, 10):
            style(ws.cell(row, col), YELLOW, True, LEFT if col == 1 else CENTER)
        row += 1
    no += 1
    fill = TEAL if sec == "Team" else BLUE
    start = row
    for task, days, tgt, ach, sw, ss, bn in tasks:
        ws.cell(row, 3, task)
        ws.cell(row, 4, days)
        ws.cell(row, 5, tgt)
        ws.cell(row, 7, ach)
        ws.cell(row, 9, bn or None)
        if sw is not None:
            ws.cell(row, 11, sw)
            ws.cell(row, 12, ss)
            ws.cell(row, 6, f"=ROUND(K{row}/{DAYS_REF},2)")
            ws.cell(row, 8, f"=ROUND(L{row}/{DAYS_REF},2)")
        for col in range(1, 10):
            style(ws.cell(row, col), fill, align=LEFT if col == 3 else CENTER,
                  color="C00000" if col == 9 else "000000")
        for col in (11, 12):
            style(ws.cell(row, col), GREY, color="0000FF")
        for col in (6, 8):
            ws.cell(row, col).number_format = "0.##"
        ws.row_dimensions[row].height = 30 if len(task) > 60 else 18
        row += 1
    ws.cell(start, 1, no)
    ws.cell(start, 2, kra)
    if row - start > 1:
        ws.merge_cells(f"A{start}:A{row - 1}")
        ws.merge_cells(f"B{start}:B{row - 1}")
    ws.cell(start, 2).font = Font(name=F, bold=False, size=10)
last_data = row - 1

# grand total
ws.cell(row, 2, "GRAND TOTAL")
ws.cell(row, 6, f"=ROUND(SUM(F{first_data}:F{last_data}),1)")
ws.cell(row, 8, f"=ROUND(SUM(L{first_data}:L{last_data})/{DAYS_REF},2)")
ws.cell(row, 11, f"=SUM(K{first_data}:K{last_data})")
ws.cell(row, 12, f"=SUM(L{first_data}:L{last_data})")
for col in range(1, 10):
    style(ws.cell(row, col), PEACH, True)
for col in (11, 12):
    style(ws.cell(row, col), GREY, True)
ws.cell(row, 8).number_format = "0.0#"
total_row = row
ws.row_dimensions[row].height = 20

# ---------- day-wise score summary ----------
row += 2
ws.merge_cells(f"A{row}:{LAST}{row}")
ws.cell(row, 1, "DAY-WISE SCORE SUMMARY")
for col in range(1, 10):
    style(ws.cell(row, col), BROWN, True, color="FFFFFF", size=11)
row += 1
sum_head = ["No", "DATE", "REMARKS", "", "TASKS", "WTG %", "", "ACH / SCORE", "vs WEEKLY AVG"]
for i, h in enumerate(sum_head, 1):
    style(ws.cell(row, i, h or None), PEACH, True)
ws.merge_cells(f"C{row}:D{row}")
row += 1
d_first = row
remarks = {
    "21-09-2026": "Blog posts & SAP automation blocked - token expired (Claude)",
    "23-09-2026": "DampShield revision score taken as 5 (= its WTG); sheet showed 10",
    "24-09-2026": "Row scores add up to 70.5 (sheet grand total showed 65.5)",
    "26-09-2026": "Epoxy campaign kick-off; GA/Tag Manager, AI videos, Diary pending",
}
tasks_per_day = {"21-09-2026": 12, "22-09-2026": 15, "23-09-2026": 14, "24-09-2026": 14,
                 "25-09-2026": 14, "26-09-2026": 14}
for i, (d, _, score) in enumerate(DAILY, 1):
    ws.cell(row, 1, i)
    ws.cell(row, 2, d)
    ws.cell(row, 3, remarks.get(d))
    ws.merge_cells(f"C{row}:D{row}")
    ws.cell(row, 5, tasks_per_day[d])
    ws.cell(row, 6, 100)
    ws.cell(row, 8, score)
    ws.cell(row, 9, f"=H{row}-$H${d_first + DAYS}")
    for col in range(1, 10):
        style(ws.cell(row, col), BLUE, align=LEFT if col == 3 else CENTER,
              color="0000FF" if col in (5, 8) else "000000")
    ws.cell(row, 9).number_format = '+0.0;-0.0;0.0'
    ws.row_dimensions[row].height = 18
    row += 1
ws.cell(row, 2, "WEEKLY AVERAGE")
ws.cell(row, 5, f"=SUM(E{d_first}:E{row - 1})")
ws.cell(row, 6, f"=AVERAGE(F{d_first}:F{row - 1})")
ws.cell(row, 8, f"=ROUND(AVERAGE(H{d_first}:H{row - 1}),2)")
ws.merge_cells(f"C{row}:D{row}")
for col in range(1, 10):
    style(ws.cell(row, col), PEACH, True)
ws.cell(row, 8).number_format = "0.0#"
row += 1
ws.cell(row, 2, "Check: ACH/SCORE grand total above = weekly average")
ws.cell(row, 8, f'=IF(ABS(H{total_row}-H{row - 1})<0.01,"OK","MISMATCH")')
ws.cell(row, 2).font = Font(name=F, italic=True, size=9, color="595959")
ws.cell(row, 8).font = Font(name=F, bold=True, size=9)
ws.cell(row, 8).alignment = CENTER

row += 2
notes = [
    "Notes:",
    f"• Weekly WTG % = sum of daily WTG % for the task / {DAYS} days; weekly ACH / SCORE = sum of daily scores / {DAYS}. Grand total therefore = average of the daily grand totals.",
    "• TARGET and ACHIEVEMENT are totals across the days the task appeared (see DAYS column).",
    "• Meta Ads reach carries no separate weight (it shares the WhatsApp broadcast weight in the daily sheets).",
    "• Grey columns K-L hold the summed daily values the weekly figures are calculated from (blue = values taken from the daily reports).",
]
for n in notes:
    ws.merge_cells(f"A{row}:{LAST}{row}")
    ws.cell(row, 1, n).font = Font(name=F, size=9, bold=n == "Notes:", color="404040")
    ws.cell(row, 1).alignment = LEFT
    row += 1

ws.freeze_panes = "A3"
ws.page_setup.orientation = "landscape"
ws.page_setup.fitToWidth = 1
ws.page_setup.fitToHeight = 0
ws.sheet_properties.pageSetUpPr.fitToPage = True
ws.print_area = f"A1:{LAST}{row}"

wb.save(OUT)
print("saved", OUT, "total row", total_row)
