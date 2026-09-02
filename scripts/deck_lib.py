"""
Shared deck-building library for AWS Academy Cloud Architecting lecture decks
(certifications/saa-c03/lectures/*.pptx). Matches the visual style of the
existing Modules 1-6 decks: Calibri, navy/orange/teal/red palette, title and
closing slides on dark navy with three orange circles + a big module-number
badge, content slides alternating light-gray and dark-navy backgrounds.

Import this from a per-module build script (e.g. build-module-07-deck.py)
rather than editing it per module.
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ---------- palette ----------
NAVY      = RGBColor(0x23, 0x2F, 0x3E)   # main dark background
CARD_NAVY = RGBColor(0x2E, 0x3E, 0x52)   # card fill on dark backgrounds
ORANGE    = RGBColor(0xFF, 0x99, 0x00)
ORANGE2   = RGBColor(0xEC, 0x72, 0x11)
TEAL      = RGBColor(0x1E, 0x8F, 0xA5)
RED       = RGBColor(0xC0, 0x39, 0x2B)
WHITE     = RGBColor(0xFF, 0xFF, 0xFF)
LIGHTBG   = RGBColor(0xF4, 0xF6, 0xF8)
BODYGRAY  = RGBColor(0x5B, 0x65, 0x70)
MUTEDGRAY = RGBColor(0x8A, 0x97, 0xA6)
CARDLINE  = RGBColor(0xDC, 0xE1, 0xE6)
ONDARK_1  = RGBColor(0xC7, 0xD2, 0xDE)
ONDARK_2  = RGBColor(0xCA, 0xDC, 0xE8)
ROWALT    = RGBColor(0xEC, 0xEF, 0xF2)

FONT = "Calibri"
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)
MARGIN = Inches(0.7)
CONTENT_W = SLIDE_W - 2 * MARGIN


class Deck:
    def __init__(self, module_num, module_title, subtitle_line):
        self.prs = Presentation()
        self.prs.slide_width = SLIDE_W
        self.prs.slide_height = SLIDE_H
        self.BLANK = self.prs.slide_layouts[6]
        self.module_num = module_num
        self.module_title = module_title
        self.footer_label = f"AWS SAA-A  ·  Lecture {module_num}  ·  {module_title}"
        self.subtitle_line = subtitle_line
        self.page = 0

    # ---- low level ----
    def add_slide(self):
        return self.prs.slides.add_slide(self.BLANK)

    def set_bg(self, slide, color):
        bg = slide.background
        bg.fill.solid()
        bg.fill.fore_color.rgb = color

    def add_rect(self, slide, l, t, w, h, fill=None, line_color=None, line_w=Pt(1)):
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

    def add_oval(self, slide, l, t, w, h, fill):
        shp = slide.shapes.add_shape(MSO_SHAPE.OVAL, l, t, w, h)
        shp.shadow.inherit = False
        shp.fill.solid()
        shp.fill.fore_color.rgb = fill
        shp.line.fill.background()
        return shp

    def add_text(self, slide, l, t, w, h, runs, align=PP_ALIGN.LEFT,
                 anchor=MSO_ANCHOR.TOP, line_spacing=None, space_after=None, wrap=True):
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

    def kicker(self, slide, text, color=ORANGE2, top=Inches(0.5)):
        self.add_text(slide, MARGIN, top, CONTENT_W, Inches(0.3),
                       [[(text.upper(), 12, True, color)]])

    def big_title(self, slide, text, top=Inches(0.8), size=30, color=NAVY, width=None):
        self.add_text(slide, MARGIN, top, width or CONTENT_W, Inches(0.7),
                       [[(text, size, True, color)]], line_spacing=1.0)

    def subtitle(self, slide, text, top=Inches(1.55), size=14.5, color=BODYGRAY, width=None):
        self.add_text(slide, MARGIN, top, width or CONTENT_W, Inches(0.5),
                       [[(text, size, False, color)]], line_spacing=1.15)

    def footer(self, slide, dark=False):
        self.page += 1
        color = ONDARK_1 if dark else BODYGRAY
        self.add_text(slide, MARGIN, Inches(7.08), Inches(9.5), Inches(0.3),
                       [[(self.footer_label, 9, False, color)]])
        self.add_text(slide, SLIDE_W - MARGIN - Inches(0.6), Inches(7.08), Inches(0.6), Inches(0.3),
                       [[(str(self.page), 9, False, color)]], align=PP_ALIGN.RIGHT)

    def bullet_row(self, slide, l, t, w, lead, rest, dot_color=TEAL, text_color=NAVY, size=14):
        self.add_oval(slide, l, t + Pt(4), Inches(0.09), Inches(0.09), dot_color)
        runs = [[(lead, size, True, text_color)]] if not rest else \
            [[(lead + "  ", size, True, text_color), (rest, size, False, text_color)]]
        self.add_text(slide, l + Inches(0.28), t - Inches(0.03), w - Inches(0.28), Inches(0.5), runs, line_spacing=1.1)

    # ---- slide types ----
    def title_slide(self, lecture_label, title_lines):
        s = self.add_slide()
        self.set_bg(s, NAVY)
        self.add_oval(s, Inches(9.8), Inches(-1.4), Inches(5.2), Inches(5.2), ORANGE)
        self.add_oval(s, Inches(11.0), Inches(0.4), Inches(3.4), Inches(3.4), ORANGE)
        self.add_oval(s, Inches(10.4), Inches(1.6), Inches(2.2), Inches(2.2), ORANGE)
        self.add_text(s, Inches(10.9), Inches(2.35), Inches(1.4), Inches(0.8),
                      [[(str(self.module_num), 26, True, NAVY)]], align=PP_ALIGN.CENTER)
        self.add_text(s, MARGIN, Inches(1.15), Inches(9.0), Inches(0.35),
                      [[(f"MODULE {self.module_num}  ·  AWS ACADEMY CLOUD ARCHITECTING", 13, True, ORANGE)]])
        self.add_text(s, MARGIN, Inches(1.75), Inches(9.0), Inches(2.0),
                      [[(line, 46, True, WHITE)] for line in title_lines], line_spacing=1.0)
        self.add_text(s, MARGIN, Inches(3.95), Inches(9.0), Inches(0.5),
                      [[(lecture_label, 16, False, ONDARK_2)]])
        self.add_rect(s, MARGIN, Inches(5.55), Inches(5.6), Pt(1), line_color=RGBColor(0x44, 0x53, 0x6A), line_w=Pt(1.5))
        self.add_text(s, MARGIN, Inches(5.7), Inches(9.0), Inches(0.35),
                      [[("Instructor  ", 13, False, MUTEDGRAY), ("Dr. Mycal “Mike” Brown", 13, True, WHITE)]])
        self.add_text(s, MARGIN, Inches(6.05), Inches(9.0), Inches(0.6),
                      [[(self.subtitle_line, 12, False, MUTEDGRAY)]], line_spacing=1.2)
        self.footer(s, dark=True)
        return s

    def content_slide(self, title, sub, kicker_text, dark=False):
        s = self.add_slide()
        self.set_bg(s, NAVY if dark else LIGHTBG)
        tcolor = WHITE if dark else NAVY
        scolor = ONDARK_1 if dark else BODYGRAY
        self.kicker(s, kicker_text, color=ORANGE if dark else ORANGE2)
        self.big_title(s, title, color=tcolor)
        if sub:
            self.subtitle(s, sub, color=scolor)
        self.footer(s, dark=dark)
        return s

    def split_card_slide(self, kicker_text, title, sub,
                          left_header, left_items, right_header, right_lead, right_body_lines):
        s = self.content_slide(title, sub, kicker_text)
        top = Inches(2.05)
        h = Inches(4.35)
        lw = Inches(5.9)
        self.add_rect(s, MARGIN, top, lw, h, fill=WHITE, line_color=CARDLINE, line_w=Pt(1))
        self.add_text(s, MARGIN + Inches(0.4), top + Inches(0.3), lw - Inches(0.8), Inches(0.3),
                      [[(left_header.upper(), 12, True, TEAL)]])
        y = top + Inches(0.85)
        for lead, rest in left_items:
            self.bullet_row(s, MARGIN + Inches(0.4), y, lw - Inches(0.8), lead, rest)
            y += Inches(0.62)
        rx = MARGIN + lw + Inches(0.44)
        rw = SLIDE_W - MARGIN - rx
        self.add_rect(s, rx, top, rw, h, fill=NAVY)
        self.add_text(s, rx + Inches(0.4), top + Inches(0.3), rw - Inches(0.8), Inches(0.3),
                      [[(right_header.upper(), 12, True, ORANGE)]])
        self.add_text(s, rx + Inches(0.4), top + Inches(0.72), rw - Inches(0.8), Inches(0.6),
                      [[(right_lead, 18, True, WHITE)]], line_spacing=1.05)
        self.add_text(s, rx + Inches(0.4), top + Inches(1.5), rw - Inches(0.8), h - Inches(1.8),
                      [[(line, 13, False, ONDARK_1)] for line in right_body_lines],
                      line_spacing=1.25, space_after=Pt(8))
        return s

    def four_up_slide(self, kicker_text, title, sub, items):
        """items: list of (number, heading, body), length 4"""
        s = self.content_slide(title, sub, kicker_text)
        top = Inches(2.35)
        card_w = Inches(2.72)
        gap = Inches(0.2)
        x = MARGIN
        for num, heading, body in items:
            self.add_rect(s, x, top, card_w, Inches(3.6), fill=WHITE, line_color=CARDLINE, line_w=Pt(1))
            self.add_oval(s, x + Inches(0.3), top + Inches(0.3), Inches(0.55), Inches(0.55), ORANGE)
            self.add_text(s, x + Inches(0.3), top + Inches(0.3), Inches(0.55), Inches(0.55),
                          [[(str(num), 20, True, NAVY)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
            self.add_text(s, x + Inches(0.3), top + Inches(1.05), card_w - Inches(0.6), Inches(0.7),
                          [[(heading, 15, True, NAVY)]], line_spacing=1.05)
            self.add_text(s, x + Inches(0.3), top + Inches(1.75), card_w - Inches(0.6), Inches(1.7),
                          [[(body, 12, False, BODYGRAY)]], line_spacing=1.2)
            x += card_w + gap
        return s

    def numbered_list_slide(self, kicker_text, title, sub, items, note=None, dark=False):
        s = self.content_slide(title, sub, kicker_text, dark=dark)
        top = Inches(2.25)
        row_h = Inches(0.78)
        hcolor = WHITE if dark else NAVY
        bcolor = ONDARK_1 if dark else BODYGRAY
        for i, (heading, body) in enumerate(items):
            y = top + i * row_h
            self.add_oval(s, MARGIN, y, Inches(0.42), Inches(0.42), TEAL)
            self.add_text(s, MARGIN, y, Inches(0.42), Inches(0.42),
                          [[(str(i + 1), 15, True, WHITE)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
            self.add_text(s, MARGIN + Inches(0.65), y - Inches(0.02), CONTENT_W - Inches(0.65), Inches(0.35),
                          [[(heading, 15, True, hcolor)]])
            self.add_text(s, MARGIN + Inches(0.65), y + Inches(0.32), CONTENT_W - Inches(0.65), Inches(0.4),
                          [[(body, 12.5, False, bcolor)]], line_spacing=1.1)
        if note:
            ny = top + len(items) * row_h + Inches(0.05)
            self.add_rect(s, MARGIN, ny, CONTENT_W, Inches(0.7), fill=RGBColor(0xFF, 0xF3, 0xE0) if not dark else CARD_NAVY)
            self.add_text(s, MARGIN + Inches(0.3), ny + Inches(0.13), CONTENT_W - Inches(0.6), Inches(0.5),
                          [[(note, 12.5, False, RGBColor(0x8A, 0x4B, 0x00) if not dark else ONDARK_1)]], line_spacing=1.1)
        return s

    def table_slide(self, kicker_text, title, sub, headers, rows, col_widths, note=None):
        s = self.content_slide(title, sub, kicker_text)
        top = Inches(2.05)
        total_w = sum(col_widths)
        scale = CONTENT_W / total_w
        col_widths = [Emu(int(w * scale)) for w in col_widths]
        rows_h = Inches(0.42)
        header_h = Inches(0.5)
        self.add_rect(s, MARGIN, top, CONTENT_W, header_h, fill=NAVY)
        x = MARGIN
        for htext, cw in zip(headers, col_widths):
            self.add_text(s, x + Inches(0.15), top + Inches(0.08), cw - Inches(0.25), Inches(0.35),
                          [[(htext.upper(), 11.5, True, ORANGE)]])
            x += cw
        y = top + header_h
        for i, row in enumerate(rows):
            rowfill = WHITE if i % 2 == 0 else ROWALT
            self.add_rect(s, MARGIN, y, CONTENT_W, rows_h, fill=rowfill)
            x = MARGIN
            for j, cell in enumerate(row):
                color = NAVY if j == 0 else BODYGRAY
                bold = j == 0
                self.add_text(s, x + Inches(0.15), y + Inches(0.06), col_widths[j] - Inches(0.25), Inches(0.32),
                              [[(cell, 11.5, bold, color)]])
                x += col_widths[j]
            y += rows_h
        self.add_rect(s, MARGIN, top, CONTENT_W, y - top, line_color=CARDLINE, line_w=Pt(1))
        if note:
            self.add_text(s, MARGIN, y + Inches(0.15), CONTENT_W, Inches(0.5),
                        [[(note, 10.5, False, MUTEDGRAY)]], line_spacing=1.1)
        return s

    def resource_list_slide(self, kicker_text, title, sub, items, dark=False):
        s = self.content_slide(title, sub, kicker_text, dark=dark)
        top = Inches(2.1)
        row_h = Inches(0.86)
        hcolor = WHITE if dark else NAVY
        bcolor = ONDARK_1 if dark else BODYGRAY
        for i, (heading, body) in enumerate(items):
            y = top + i * row_h
            self.add_rect(s, MARGIN, y, Inches(0.06), Inches(0.62), fill=ORANGE)
            self.add_text(s, MARGIN + Inches(0.28), y - Inches(0.02), CONTENT_W - Inches(0.28), Inches(0.35),
                          [[(heading, 14.5, True, hcolor)]])
            self.add_text(s, MARGIN + Inches(0.28), y + Inches(0.33), CONTENT_W - Inches(0.28), Inches(0.5),
                          [[(body, 12, False, bcolor)]], line_spacing=1.1)
        return s

    def quad_box_slide(self, banner_text, title, sub, boxes, note=None):
        """Dark-bg 2x2 grid. boxes: list of 4 (heading, body). note: optional red-banner callout."""
        s = self.add_slide()
        self.set_bg(s, NAVY)
        self.add_rect(s, MARGIN, Inches(0.5), Inches(3.6), Inches(0.42), fill=RED)
        self.add_text(s, MARGIN + Inches(0.2), Inches(0.58), Inches(3.4), Inches(0.3),
                      [[(banner_text.upper(), 11.5, True, WHITE)]])
        self.add_text(s, MARGIN, Inches(1.05), CONTENT_W, Inches(0.7),
                      [[(title, 32, True, WHITE)]], line_spacing=1.0)
        if sub:
            self.add_text(s, MARGIN, Inches(1.8), CONTENT_W, Inches(0.4),
                          [[(sub, 15, False, ONDARK_1)]])
        top = Inches(2.4)
        box_w = Inches(5.74)
        box_h = Inches(1.35)
        gap_x = Inches(0.49)
        gap_y = Inches(0.34)
        positions = [
            (MARGIN, top),
            (MARGIN + box_w + gap_x, top),
            (MARGIN, top + box_h + gap_y),
            (MARGIN + box_w + gap_x, top + box_h + gap_y),
        ]
        for (bx, by), (heading, body) in zip(positions, boxes):
            self.add_rect(s, bx, by, box_w, box_h, fill=CARD_NAVY)
            self.add_text(s, bx + Inches(0.4), by + Inches(0.2), box_w - Inches(0.8), Inches(0.4),
                          [[(heading, 16.5, True, ORANGE)]])
            self.add_text(s, bx + Inches(0.4), by + Inches(0.6), box_w - Inches(0.8), Inches(0.6),
                          [[(body, 13.5, False, ONDARK_1)]], line_spacing=1.15)
        if note:
            ny = top + 2 * box_h + gap_y + Inches(0.24)
            self.add_rect(s, MARGIN, ny, CONTENT_W, Inches(1.0), fill=RED)
            self.add_text(s, MARGIN + Inches(0.45), ny + Inches(0.18), CONTENT_W - Inches(0.9), Inches(0.7),
                      [[(note, 14.5, True, WHITE)]], line_spacing=1.15)
        self.footer(s, dark=True)
        return s

    def closing_slide(self, line1, line2, sub):
        s = self.add_slide()
        self.set_bg(s, NAVY)
        self.add_oval(s, Inches(10.9), Inches(4.4), Inches(4.6), Inches(4.6), ORANGE)
        self.add_oval(s, Inches(11.9), Inches(3.5), Inches(2.6), Inches(2.6), ORANGE)
        self.add_text(s, MARGIN, Inches(2.3), Inches(10.0), Inches(0.4),
                      [[("QUESTIONS?", 14, True, ORANGE)]])
        self.add_text(s, MARGIN, Inches(2.8), Inches(11.0), Inches(1.4),
                      [[(line1, 40, True, WHITE)], [(line2, 40, True, WHITE)]], line_spacing=1.0)
        self.add_text(s, MARGIN, Inches(4.35), Inches(10.5), Inches(0.6),
                      [[(sub, 15, False, ONDARK_2)]])
        self.add_rect(s, MARGIN, Inches(5.3), Inches(5.6), Pt(1), line_color=RGBColor(0x44, 0x53, 0x6A), line_w=Pt(1.5))
        self.add_text(s, MARGIN, Inches(5.5), Inches(10.5), Inches(0.4),
                      [[("Dr. Mycal “Mike” Brown    ·    AWS Certified Solutions Architect, Instructor", 12, False, MUTEDGRAY)]])
        self.footer(s, dark=True)
        return s

    def save(self, path):
        self.prs.save(path)
        return len(self.prs.slides)
