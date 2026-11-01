"""
Build script for lectures/ccp-exam-review.pptx (CLF-C02 Foundations wrap-up deck).

Regenerates the deck from scratch each run — this is a build script, not an
editor. To change the deck: edit the slide-builder calls in the "BUILD THE
DECK" section below, then re-run.

Usage:
    pip install python-pptx
    python scripts/build-ccp-exam-review-deck.py
    # writes directly to certifications/clf-c02-cloud-practitioner/lectures/

The palette, fonts, and slide layouts (title/closing on navy, content on
light gray, the white/dark two-card split, the numbered list, the table,
the resource list) were reverse-engineered from the existing hand-built
decks in that lectures/ folder so this one would match visually.
"""

import os

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ---------- palette (lifted from the existing decks) ----------
NAVY     = RGBColor(0x23, 0x2F, 0x3E)
NAVY_TXT = RGBColor(0x23, 0x2F, 0x3E)
ORANGE   = RGBColor(0xFF, 0x99, 0x00)
ORANGE2  = RGBColor(0xEC, 0x72, 0x11)
TEAL     = RGBColor(0x1E, 0x8F, 0xA5)
WHITE    = RGBColor(0xFF, 0xFF, 0xFF)
LIGHTBG  = RGBColor(0xF4, 0xF6, 0xF8)
BODYGRAY = RGBColor(0x5B, 0x65, 0x70)
MUTEDGRAY= RGBColor(0x8A, 0x97, 0xA6)
CARDLINE = RGBColor(0xDC, 0xE1, 0xE6)
ONDARK_1 = RGBColor(0xC7, 0xD2, 0xDE)
ONDARK_2 = RGBColor(0xCA, 0xDC, 0xE8)
ROWALT   = RGBColor(0xEC, 0xEF, 0xF2)

FONT = "Calibri"
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)
MARGIN = Inches(0.7)
CONTENT_W = SLIDE_W - 2 * MARGIN

prs = Presentation()
prs.slide_width = SLIDE_W
prs.slide_height = SLIDE_H
BLANK = prs.slide_layouts[6]

DECK_LABEL = "AWS CCP  ·  Exam Review  ·  Foundations Complete"

# ---------- low level helpers ----------

def add_slide():
    return prs.slides.add_slide(BLANK)

def set_bg(slide, color):
    bg = slide.background
    bg.fill.solid()
    bg.fill.fore_color.rgb = color

def add_rect(slide, l, t, w, h, fill=None, line_color=None, line_w=Pt(1)):
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, l, t, w, h)
    shp.shadow.inherit = False
    if fill is None:
        shp.fill.background()
    else:
        shp.fill.solid()
        shp.fill.fore_color.rgb = fill
    if line_color is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line_color
        shp.line.width = line_w
    return shp

def add_oval(slide, l, t, w, h, fill):
    shp = slide.shapes.add_shape(MSO_SHAPE.OVAL, l, t, w, h)
    shp.shadow.inherit = False
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    shp.line.fill.background()
    return shp

def add_text(slide, l, t, w, h, runs, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
             line_spacing=None, space_after=None, wrap=True):
    """runs: list of paragraphs; each paragraph is a list of (text, size_pt, bold, color) tuples."""
    box = slide.shapes.add_textbox(l, t, w, h)
    tf = box.text_frame
    tf.word_wrap = wrap
    tf.vertical_anchor = anchor
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    for i, para_runs in enumerate(runs):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        if line_spacing:
            p.line_spacing = line_spacing
        if space_after is not None:
            p.space_after = space_after
        for text, size, bold, color in para_runs:
            r = p.add_run()
            r.text = text
            r.font.name = FONT
            r.font.size = Pt(size)
            r.font.bold = bold
            r.font.color.rgb = color
    return box

def kicker(slide, text, color=ORANGE2, top=Inches(0.5)):
    add_text(slide, MARGIN, top, CONTENT_W, Inches(0.3),
             [[(text.upper(), 12, True, color)]])

def big_title(slide, text, top=Inches(0.8), size=30, color=NAVY_TXT, width=None):
    add_text(slide, MARGIN, top, width or CONTENT_W, Inches(0.7),
             [[(text, size, True, color)]], line_spacing=1.0)

def subtitle(slide, text, top=Inches(1.55), size=14.5, color=BODYGRAY, width=None):
    add_text(slide, MARGIN, top, width or CONTENT_W, Inches(0.5),
              [[(text, size, False, color)]], line_spacing=1.15)

def footer(slide, page, dark=False):
    color = ONDARK_1 if dark else BODYGRAY
    add_text(slide, MARGIN, Inches(7.08), Inches(9.5), Inches(0.3),
              [[(DECK_LABEL, 9, False, color)]])
    add_text(slide, SLIDE_W - MARGIN - Inches(0.6), Inches(7.08), Inches(0.6), Inches(0.3),
              [[(str(page), 9, False, color)]], align=PP_ALIGN.RIGHT)

def bullet_row(slide, l, t, w, lead, rest, dot_color=TEAL, text_color=NAVY_TXT, size=14):
    add_oval(slide, l, t + Pt(4), Inches(0.09), Inches(0.09), dot_color)
    runs = [[(lead, size, True, text_color)]] if not rest else [[(lead + "  ", size, True, text_color), (rest, size, False, text_color)]]
    add_text(slide, l + Inches(0.28), t - Inches(0.03), w - Inches(0.28), Inches(0.5), runs, line_spacing=1.1)

# ---------- slide builders ----------

def title_slide():
    s = add_slide()
    set_bg(s, NAVY)
    # decorative circles, orange, echoing the module-deck title style
    add_oval(s, Inches(9.8), Inches(-1.4), Inches(5.2), Inches(5.2), ORANGE)
    add_oval(s, Inches(11.0), Inches(0.4), Inches(3.4), Inches(3.4), ORANGE)
    add_oval(s, Inches(10.4), Inches(1.6), Inches(2.2), Inches(2.2), ORANGE)
    add_text(s, Inches(10.9), Inches(2.35), Inches(1.4), Inches(0.8),
             [[("CCP", 26, True, NAVY_TXT)]], align=PP_ALIGN.CENTER)

    add_text(s, MARGIN, Inches(1.15), Inches(9.0), Inches(0.35),
             [[("CCP EXAM REVIEW  ·  AWS ACADEMY CLOUD FOUNDATIONS", 13, True, ORANGE)]])
    add_text(s, MARGIN, Inches(1.75), Inches(9.0), Inches(2.0),
             [[("Ten Modules,", 46, True, WHITE)], [("One Exam Map", 46, True, WHITE)]],
             line_spacing=1.0)
    add_text(s, MARGIN, Inches(3.95), Inches(9.0), Inches(0.5),
             [[("CLF-C02 — AWS Certified Cloud Practitioner  ·  Foundations, Complete", 16, False, ONDARK_2)]])

    add_rect(s, MARGIN, Inches(5.55), Inches(5.6), Pt(1), line_color=RGBColor(0x44,0x53,0x6A), line_w=Pt(1.5))
    add_text(s, MARGIN, Inches(5.7), Inches(9.0), Inches(0.35),
             [[("Instructor  ", 13, False, MUTEDGRAY), ("Dr. Mycal “Mike” Brown", 13, True, WHITE)]])
    add_text(s, MARGIN, Inches(6.05), Inches(9.0), Inches(0.6),
             [[("Not new content — the map that shows how everything since Module 1 lines up", 12, False, MUTEDGRAY)],
              [("against what the exam actually scores.", 12, False, MUTEDGRAY)]], line_spacing=1.2)
    return s


def content_slide(title, sub, page, kicker_text):
    s = add_slide()
    set_bg(s, LIGHTBG)
    kicker(s, kicker_text)
    big_title(s, title)
    if sub:
        subtitle(s, sub)
    footer(s, page)
    return s


def split_card_slide(kicker_text, title, sub, page,
                      left_header, left_items, right_header, right_lead, right_body_lines,
                      right_lead_color=WHITE):
    s = content_slide(title, sub, page, kicker_text)
    top = Inches(2.05)
    h = Inches(4.35)
    # left card (white)
    lw = Inches(5.9)
    add_rect(s, MARGIN, top, lw, h, fill=WHITE, line_color=CARDLINE, line_w=Pt(1))
    add_text(s, MARGIN + Inches(0.4), top + Inches(0.3), lw - Inches(0.8), Inches(0.3),
              [[(left_header.upper(), 12, True, TEAL)]])
    y = top + Inches(0.85)
    for lead, rest in left_items:
        bullet_row(s, MARGIN + Inches(0.4), y, lw - Inches(0.8), lead, rest)
        y += Inches(0.62)
    # right card (dark)
    rx = MARGIN + lw + Inches(0.44)
    rw = SLIDE_W - MARGIN - rx
    add_rect(s, rx, top, rw, h, fill=NAVY)
    add_text(s, rx + Inches(0.4), top + Inches(0.3), rw - Inches(0.8), Inches(0.3),
              [[(right_header.upper(), 12, True, ORANGE)]])
    add_text(s, rx + Inches(0.4), top + Inches(0.72), rw - Inches(0.8), Inches(0.6),
              [[(right_lead, 18, True, right_lead_color)]], line_spacing=1.05)
    add_text(s, rx + Inches(0.4), top + Inches(1.5), rw - Inches(0.8), h - Inches(1.8),
              [[(line, 13, False, ONDARK_1)] for line in right_body_lines], line_spacing=1.25, space_after=Pt(8))
    return s


def four_up_slide(kicker_text, title, sub, page, items):
    """items: list of (number, heading, body) tuples, length 4"""
    s = content_slide(title, sub, page, kicker_text)
    top = Inches(2.35)
    card_w = Inches(2.72)
    gap = Inches(0.2)
    x = MARGIN
    for num, heading, body in items:
        add_rect(s, x, top, card_w, Inches(3.6), fill=WHITE, line_color=CARDLINE, line_w=Pt(1))
        add_oval(s, x + Inches(0.3), top + Inches(0.3), Inches(0.55), Inches(0.55), ORANGE)
        add_text(s, x + Inches(0.3), top + Inches(0.3), Inches(0.55), Inches(0.55),
                 [[(str(num), 20, True, NAVY_TXT)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        add_text(s, x + Inches(0.3), top + Inches(1.05), card_w - Inches(0.6), Inches(0.7),
                 [[(heading, 15, True, NAVY_TXT)]], line_spacing=1.05)
        add_text(s, x + Inches(0.3), top + Inches(1.75), card_w - Inches(0.6), Inches(1.7),
                 [[(body, 12, False, BODYGRAY)]], line_spacing=1.2)
        x += card_w + gap
    return s


def numbered_list_slide(kicker_text, title, sub, page, items, note=None):
    """items: list of (heading, body)"""
    s = content_slide(title, sub, page, kicker_text)
    top = Inches(2.25)
    row_h = Inches(0.78)
    for i, (heading, body) in enumerate(items):
        y = top + i * row_h
        add_oval(s, MARGIN, y, Inches(0.42), Inches(0.42), TEAL)
        add_text(s, MARGIN, y, Inches(0.42), Inches(0.42),
                 [[(str(i + 1), 15, True, WHITE)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        add_text(s, MARGIN + Inches(0.65), y - Inches(0.02), CONTENT_W - Inches(0.65), Inches(0.35),
                 [[(heading, 15, True, NAVY_TXT)]])
        add_text(s, MARGIN + Inches(0.65), y + Inches(0.32), CONTENT_W - Inches(0.65), Inches(0.4),
                 [[(body, 12.5, False, BODYGRAY)]], line_spacing=1.1)
    if note:
        ny = top + len(items) * row_h + Inches(0.05)
        add_rect(s, MARGIN, ny, CONTENT_W, Inches(0.7), fill=RGBColor(0xFF,0xF3,0xE0))
        add_text(s, MARGIN + Inches(0.3), ny + Inches(0.13), CONTENT_W - Inches(0.6), Inches(0.5),
                 [[(note, 12.5, False, RGBColor(0x8A,0x4B,0x00))]], line_spacing=1.1)
    return s


def table_slide(kicker_text, title, sub, page, headers, rows, col_widths, note=None):
    s = content_slide(title, sub, page, kicker_text)
    top = Inches(2.05)
    total_w = sum(col_widths)
    scale = CONTENT_W / total_w
    col_widths = [Emu(int(w * scale)) for w in col_widths]
    rows_h = Inches(0.42)
    header_h = Inches(0.5)
    # header bar
    add_rect(s, MARGIN, top, CONTENT_W, header_h, fill=NAVY)
    x = MARGIN
    for htext, cw in zip(headers, col_widths):
        add_text(s, x + Inches(0.15), top + Inches(0.08), cw - Inches(0.25), Inches(0.35),
                  [[(htext.upper(), 11.5, True, ORANGE)]])
        x += cw
    y = top + header_h
    for i, row in enumerate(rows):
        rowfill = WHITE if i % 2 == 0 else ROWALT
        add_rect(s, MARGIN, y, CONTENT_W, rows_h, fill=rowfill)
        x = MARGIN
        for j, (cell) in enumerate(row):
            color = NAVY_TXT if j == 0 else BODYGRAY
            bold = j == 0
            add_text(s, x + Inches(0.15), y + Inches(0.06), col_widths[j] - Inches(0.25), Inches(0.32),
                      [[(cell, 11.5, bold, color)]])
            x += col_widths[j]
        y += rows_h
    add_rect(s, MARGIN, top, CONTENT_W, y - top, line_color=CARDLINE, line_w=Pt(1))
    if note:
        add_text(s, MARGIN, y + Inches(0.15), CONTENT_W, Inches(0.5),
                  [[(note, 10.5, False, MUTEDGRAY)]], line_spacing=1.1)
    return s


def resource_list_slide(kicker_text, title, sub, page, items):
    """items: list of (heading, body)"""
    s = content_slide(title, sub, page, kicker_text)
    top = Inches(2.1)
    row_h = Inches(0.86)
    for i, (heading, body) in enumerate(items):
        y = top + i * row_h
        add_rect(s, MARGIN, y, Inches(0.06), Inches(0.62), fill=ORANGE)
        add_text(s, MARGIN + Inches(0.28), y - Inches(0.02), CONTENT_W - Inches(0.28), Inches(0.35),
                  [[(heading, 14.5, True, NAVY_TXT)]])
        add_text(s, MARGIN + Inches(0.28), y + Inches(0.33), CONTENT_W - Inches(0.28), Inches(0.5),
                  [[(body, 12, False, BODYGRAY)]], line_spacing=1.1)
    return s


def closing_slide():
    s = add_slide()
    set_bg(s, NAVY)
    add_oval(s, Inches(10.9), Inches(4.4), Inches(4.6), Inches(4.6), ORANGE)
    add_oval(s, Inches(11.9), Inches(3.5), Inches(2.6), Inches(2.6), ORANGE)
    add_text(s, MARGIN, Inches(2.3), Inches(10.0), Inches(0.4),
              [[("QUESTIONS?", 14, True, ORANGE)]])
    add_text(s, MARGIN, Inches(2.8), Inches(11.0), Inches(1.4),
              [[("Ten modules down.", 40, True, WHITE)], [("One exam to go.", 40, True, WHITE)]],
              line_spacing=1.0)
    add_text(s, MARGIN, Inches(4.35), Inches(10.5), Inches(0.6),
              [[("Schedule the exam, work the Skill Builder plan, and trust the map.", 15, False, ONDARK_2)]])
    add_rect(s, MARGIN, Inches(5.3), Inches(5.6), Pt(1), line_color=RGBColor(0x44,0x53,0x6A), line_w=Pt(1.5))
    add_text(s, MARGIN, Inches(5.5), Inches(10.5), Inches(0.4),
              [[("Dr. Mycal “Mike” Brown    ·    AWS Certified Solutions Architect, Instructor", 12, False, MUTEDGRAY)]])
    return s

# =====================================================================
# BUILD THE DECK
# =====================================================================

title_slide()  # 1

split_card_slide(
    "Why This Matters", "You Don't Need to Re-Learn Ten Modules",
    "Tonight is the map, not new material.", 2,
    "What Tonight Is",
    [
        ("How ten modules line up", "against the four domains the exam actually scores."),
        ("Official AWS resources", "for the final stretch of studying before test day."),
        ("A weak-spot finder,", "not a re-teach — you already sat through all ten modules."),
    ],
    "What Tonight Isn't",
    "If you take one thing from tonight, take this:",
    [
        "You don't need to re-learn ten modules from scratch.",
        "You need to know which domain each module feeds, and where your personal weak spots sit inside that map.",
    ],
)  # 3

numbered_list_slide(
    "Tonight's Mission", "What You'll Walk Out With", None, 3,
    [
        ("Exam logistics, memorized", "Format, timing, cost, and the passing score — no surprises at the test center."),
        ("Every module mapped to its domain", "All ten modules, tied to the four domains CLF-C02 actually scores."),
        ("A study plan weighted by domain %", "Not just by which module felt hardest at the time."),
        ("The short list of official AWS resources", "To use for the remaining stretch before you sit the exam."),
        ("What's different if you find CLF-C01 material online", "AWS retired it — know what changed before you study from it."),
        ("What comes right after this exam", "Cloud Architecting, and the road to SAA-C03."),
    ],
)  # 5

table_slide(
    "Exam Snapshot", "CLF-C02, at a Glance", "Confirm against the official exam guide before test day.", 4,
    ["Field", "Detail"],
    [
        ["Exam code", "CLF-C02"],
        ["Format", "65 questions — multiple choice or multiple response"],
        ["Duration", "90 minutes"],
        ["Cost", "$100 USD"],
        ["Scoring", "Scaled 100–1,000; passing score is 700"],
        ["Delivery", "Pearson VUE testing center, or online proctored"],
        ["Validity", "3 years"],
    ],
    [3, 9],
    note="Format, cost, and scoring are current as of this writing — AWS updates these periodically.",
)  # 6

four_up_slide(
    "The Big Picture", "Four Domains, One Exam", "Every module you've taken feeds one or more of these.", 5,
    [
        (1, "Cloud Concepts — 24%", "Modules 1 and 9. What the cloud is, and how to reason about architecture."),
        (2, "Security & Compliance — 30%", "Module 4. The shared responsibility model and AWS security services."),
        (3, "Cloud Technology & Services — 34%", "Modules 3, 5, 6, 7, 8, 10. The biggest slice — and the widest spread."),
        (4, "Billing, Pricing & Support — 12%", "Module 2. Pricing models, cost tools, and AWS support tiers."),
    ],
)  # 7

split_card_slide(
    "Spotlight", "Domain 3 Is the One to Prioritize",
    "The biggest slice of the exam, built from the widest spread of modules.", 6,
    "What It Is",
    [
        ("34% of the exam —", "the single largest domain, by a clear margin."),
        ("Built from six modules,", "3, 5, 6, 7, 8, and 10 — global infrastructure, networking, compute, storage, databases, and scaling."),
        ("The widest spread", "of any domain — a weak module almost always means a Domain 3 gap."),
    ],
    "Why It Matters",
    "One block is worth more than the rest combined.",
    [
        "If you only have time to review one thing this week, review Modules 3 and 5 through 8 and 10 together as a single block.",
        "A shaky Module 6 or 7 costs more exam points than a shaky Module 2 — Domain 4 is only 12%.",
    ],
)  # 8

table_slide(
    "Every Module, One More Time", "The Full Map", None, 7,
    ["#", "Module", "Domain(s)"],
    [
        ["1", "Cloud Concepts Overview", "Domain 1"],
        ["2", "Cloud Economics and Billing", "Domain 4"],
        ["3", "AWS Global Infrastructure Overview", "Domain 3"],
        ["4", "AWS Cloud Security", "Domain 2"],
        ["5", "Networking and Content Delivery", "Domain 3"],
        ["6", "Compute", "Domain 3"],
        ["7", "Storage", "Domain 3"],
        ["8", "Databases", "Domain 3"],
        ["9", "Cloud Architecture", "Domain 1 (touches 2 and 4)"],
        ["10", "Auto Scaling and Monitoring", "Domain 3"],
    ],
    [1, 8, 4.5],
)  # 9

numbered_list_slide(
    "Use It Tonight", "A Practical Way to Study This Map", None, 8,
    [
        ("Be honest about which modules felt shaky", "Use your quiz and knowledge-check scores — don't guess."),
        ("Cross-reference against the domain column", "A shaky Domain 3 module is worth more review time than a shaky Domain 4 one."),
        ("Spend remaining time proportional to domain weight", "Not just to which module felt hardest — Domain 2 at 30% deserves real time even if Module 4 felt fine."),
    ],
)  # 10

split_card_slide(
    "If It's Online", "Seen “CLF-C01” Material? Skip It.",
    "AWS retired CLF-C01 — CLF-C02 is the current exam.", 9,
    "What Changed",
    [
        ("Generative AI and modern services", "added to the exam's coverage."),
        ("Domain weights rebalanced", "across the four scored domains."),
        ("Sample questions refreshed", "to match current AWS offerings."),
    ],
    "The Bottom Line",
    "Everything in this course was built against CLF-C02.",
    [
        "You don't need to cross-reference CLF-C01 material anywhere in your remaining study time.",
        "Doing so risks studying content that isn't tested anymore — stick to CLF-C02-labeled resources only.",
    ],
)  # 11

resource_list_slide(
    "Final Review", "Official AWS Resources — Start Here", None, 10,
    [
        ("Exam Guide", "What's actually tested, section by section — the single source of truth for scope."),
        ("Certification overview & scheduling", "The overview page, plus where to book your test date."),
        ("Skill Builder Exam Prep Plan", "AWS's official 4-step path — guide, courses, flashcards, and a full practice exam, free."),
        ("AWS Cloud Practitioner Essentials", "The full course this class is built around."),
        ("Official Practice Question Set", "Real practice questions, with answers included."),
    ],
)  # 12

resource_list_slide(
    "Deeper Reading", "Four Whitepapers Behind the Exam", None, 11,
    [
        ("Overview of Amazon Web Services", "The broad “what is AWS” foundation behind Domain 1."),
        ("AWS Well-Architected Framework", "The six pillars from Module 9, in full official depth."),
        ("How AWS Pricing Works", "The pricing models behind Module 2's billing content."),
        ("Compare AWS Support Plans", "The support-tier material from Module 2 and Module 9's Trusted Advisor content."),
    ],
)  # 13

numbered_list_slide(
    "Before You Sit the Exam", "Key Takeaways", None, 12,
    [
        ("Foundations is complete", "Ten modules, all four exam domains covered at least once."),
        ("Domain 3 is the priority if time is short", "34% of the exam, built from the widest spread of modules — review it first."),
        ("Use AWS's own resources first", "The exam guide defines scope; the Skill Builder plan structures your review."),
        ("This exam tests a conceptual map, not production experience", "You are not expected to have hands-on AWS experience — just what these ten modules built."),
    ],
)  # 14

split_card_slide(
    "What's Next", "Foundations Done. Architecting Starts Next.",
    "This course is ultimately named for where it's headed.", 13,
    "Where You've Been",
    [
        ("Ten modules,", "all four CLF-C02 domains, foundation-level AWS knowledge."),
        ("A conceptual map", "of the AWS Cloud you can now navigate with confidence."),
    ],
    "Where You're Headed",
    "AWS Academy Cloud Architecting — 16 modules.",
    [
        "Builds directly on these ten modules toward the AWS Certified Solutions Architect – Associate (SAA-C03) exam.",
        "Real architectural depth and hands-on labs, on the same services you just met at a conceptual level.",
    ],
)  # 15

numbered_list_slide(
    "Before Test Day", "Your Action Items", None, 14,
    [
        ("Schedule your CCP exam", "Don't wait until the end of term — you're ready once your weak spots are handled."),
        ("Work the Skill Builder Exam Prep Plan front to back", "Guide, courses, flashcards, then the full practice exam."),
        ("Prioritize Domain 3 in your remaining review", "The widest, heaviest chunk of the exam — Modules 3, 5–8, and 10."),
        ("Re-check the exam guide and FAQs before test day", "AWS periodically updates format, pricing, and policy details."),
    ],
    note="Reminder:  the exam guide and Skill Builder links are on the slide from earlier — verify they're still current at aws.amazon.com before relying on them.",
)  # 16

closing_slide()  # 17

OUT = os.path.join(os.path.dirname(__file__), "..", "certifications",
                   "clf-c02-cloud-practitioner", "lectures", "ccp-exam-review.pptx")
prs.save(OUT)
print(f"Saved {len(prs.slides)} slides to {OUT}")
