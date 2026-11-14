# -*- coding: utf-8 -*-
# Bộ dựng văn bản hành chính (thể thức theo Nghị định 30/2020/NĐ-CP) bằng python-docx.
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

FONT = "Times New Roman"
TEXTW = 16.5  # cm, A4 lề trái 3, phải 1.5


class Doc:
    def __init__(self, landscape=False):
        self.d = Document()
        sec = self.d.sections[0]
        sec.page_width, sec.page_height = Cm(21), Cm(29.7)
        sec.left_margin, sec.right_margin, sec.top_margin, sec.bottom_margin = Cm(3), Cm(1.5), Cm(2), Cm(2)
        st = self.d.styles["Normal"]
        st.font.name = FONT
        st.font.size = Pt(13)
        st.element.rPr.rFonts.set(qn('w:eastAsia'), FONT)
        st.paragraph_format.space_after = Pt(4)
        st.paragraph_format.line_spacing = 1.15
        fp = sec.footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = fp.add_run()
        for tag, val in (("begin", None), ("instr", "PAGE"), ("end", None)):
            if tag == "instr":
                e = OxmlElement('w:instrText'); e.text = val
            else:
                e = OxmlElement('w:fldChar'); e.set(qn('w:fldCharType'), tag)
            r._r.append(e)

    # ---- chữ ----
    def run(self, par, text, bold=False, italic=False, size=None, color=None, underline=False):
        r = par.add_run(text)
        r.bold, r.italic, r.underline = bold, italic, underline
        r.font.name = FONT
        r._element.rPr.rFonts.set(qn('w:eastAsia'), FONT)
        if size: r.font.size = Pt(size)
        if color: r.font.color.rgb = RGBColor(*color)
        return r

    def para(self, text="", align="justify", bold=False, italic=False, size=None, indent=True, before=0, keep=False):
        p = self.d.add_paragraph()
        p.alignment = {"justify": WD_ALIGN_PARAGRAPH.JUSTIFY, "center": WD_ALIGN_PARAGRAPH.CENTER,
                       "left": WD_ALIGN_PARAGRAPH.LEFT, "right": WD_ALIGN_PARAGRAPH.RIGHT}[align]
        if indent and align == "justify": p.paragraph_format.first_line_indent = Cm(1)
        if before: p.paragraph_format.space_before = Pt(before)
        if keep: p.paragraph_format.keep_with_next = True
        if text: self.run(p, text, bold=bold, italic=italic, size=size)
        return p

    def rich(self, parts, align="justify", indent=True):
        """parts: list of (text, style) với style chứa 'b' và/hoặc 'i'."""
        p = self.para("", align=align, indent=indent)
        for text, stl in parts:
            self.run(p, text, bold="b" in stl, italic="i" in stl)
        return p

    def h1(self, s): return self.para(s, align="center", bold=True, size=13.5, indent=False, before=10, keep=True)
    def h2(self, s): return self.para(s, align="left", bold=True, indent=False, before=8, keep=True)
    def h3(self, s): return self.para(s, align="left", bold=True, italic=True, indent=False, before=4, keep=True)

    def bullets(self, items, sym="- "):
        for x in items:
            p = self.para("", indent=False)
            p.paragraph_format.left_indent = Cm(1)
            p.paragraph_format.first_line_indent = Cm(-0.5)
            self.run(p, sym + x)

    def numbered(self, items, fmt="{}. "):
        for i, x in enumerate(items, 1):
            p = self.para("", indent=False)
            p.paragraph_format.left_indent = Cm(1)
            p.paragraph_format.first_line_indent = Cm(-0.6)
            self.run(p, fmt.format(i) + x)

    def note(self, s):
        p = self.para("", indent=False)
        self.run(p, "Ghi chú: ", bold=True, italic=True, size=12)
        self.run(p, s, italic=True, size=12)

    def pagebreak(self):
        self.d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    # ---- bảng ----
    def _shade(self, cell, hexcolor):
        tcPr = cell._element.get_or_add_tcPr(); s = OxmlElement('w:shd')
        s.set(qn('w:val'), 'clear'); s.set(qn('w:color'), 'auto'); s.set(qn('w:fill'), hexcolor); tcPr.append(s)

    def table(self, rows, widths, header=True, size=11, center_cols=(), border=True):
        tb = self.d.add_table(rows=len(rows), cols=len(rows[0]))
        if border: tb.style = "Table Grid"
        tb.alignment = WD_TABLE_ALIGNMENT.CENTER
        tb.autofit = False
        tot = sum(widths)
        for j, wv in enumerate(widths): tb.columns[j].width = Cm(wv * TEXTW / tot)
        for i, row in enumerate(rows):
            for j, val in enumerate(row):
                c = tb.cell(i, j)
                c.width = Cm(widths[j] * TEXTW / tot)
                lines = str(val).split("\n")
                pp = c.paragraphs[0]
                for k, ln in enumerate(lines):
                    if k: pp = c.add_paragraph()
                    pp.paragraph_format.space_after = Pt(1)
                    self.run(pp, ln, bold=(header and i == 0), size=size)
                    if (header and i == 0) or j in center_cols: pp.alignment = WD_ALIGN_PARAGRAPH.CENTER
                pass  # nền trắng
        if header:
            trPr = tb.rows[0]._tr.get_or_add_trPr(); h = OxmlElement('w:tblHeader'); h.set(qn('w:val'), 'true'); trPr.append(h)
        self.d.add_paragraph().paragraph_format.space_after = Pt(0)
        return tb

    # ---- thể thức ----
    def quoc_hieu(self, org_lines, so, date_text="An Giang, ngày     tháng     năm 2026"):
        """org_lines: [cơ quan chủ quản, cơ quan ban hành] ; so: 'Số:      /QĐ-BVNT'"""
        tb = self.d.add_table(rows=1, cols=2); tb.alignment = WD_TABLE_ALIGNMENT.CENTER; tb.autofit = False
        tb.columns[0].width, tb.columns[1].width = Cm(6.3), Cm(10.2)
        l, r = tb.rows[0].cells
        l.width, r.width = Cm(6.3), Cm(10.2)
        p = l.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for k, ln in enumerate(org_lines):
            self.run(p, ln + ("\n" if k < len(org_lines) - 1 else ""), bold=(k == len(org_lines) - 1), size=12.5)
        q = l.add_paragraph("_______"); q.alignment = WD_ALIGN_PARAGRAPH.CENTER
        q2 = l.add_paragraph(); q2.alignment = WD_ALIGN_PARAGRAPH.CENTER; self.run(q2, so, size=13)
        p = r.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        self.run(p, "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM\n", bold=True, size=12.5)
        self.run(p, "Độc lập - Tự do - Hạnh phúc", bold=True, size=13)
        q = r.add_paragraph("_______________________"); q.alignment = WD_ALIGN_PARAGRAPH.CENTER
        q2 = r.add_paragraph(); q2.alignment = WD_ALIGN_PARAGRAPH.CENTER; self.run(q2, date_text, italic=True)

    def du_thao(self):
        p = self.para("DỰ THẢO", align="center", bold=True, indent=False)
        pass  # chữ đen

    def ky(self, noi_nhan, chuc_vu, ten="", quyen=None):
        tb = self.d.add_table(rows=1, cols=2); tb.autofit = False
        tb.columns[0].width, tb.columns[1].width = Cm(8), Cm(8.5)
        a, b = tb.rows[0].cells
        a.width, b.width = Cm(8), Cm(8.5)
        p = a.paragraphs[0]
        if noi_nhan:
            self.run(p, "Nơi nhận:", bold=True, italic=True, size=12)
            for x in noi_nhan:
                q = a.add_paragraph(); q.paragraph_format.space_after = Pt(0); self.run(q, "- " + x, size=11)
        p = b.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if quyen: self.run(p, quyen + "\n", bold=True)
        self.run(p, chuc_vu, bold=True)
        q = b.add_paragraph("\n\n\n"); q.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if ten:
            q = b.add_paragraph(); q.alignment = WD_ALIGN_PARAGRAPH.CENTER; self.run(q, ten, bold=True)

    def sop_header(self, code, title, lan="01", ngay="…/…/2026", kind="QUY TRÌNH CHĂM SÓC"):
        tb = self.d.add_table(rows=1, cols=3); tb.style = "Table Grid"; tb.alignment = WD_TABLE_ALIGNMENT.CENTER; tb.autofit = False
        ws = [4.5, 7.5, 4.5]
        for j, w in enumerate(ws): tb.columns[j].width = Cm(w)
        c0, c1, c2 = tb.rows[0].cells
        for c, w in zip((c0, c1, c2), ws): c.width = Cm(w)
        p = c0.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        self.run(p, "BỆNH VIỆN ĐA KHOA\nNHẬT TÂN\n", bold=True, size=11); self.run(p, "Phòng Điều dưỡng", size=11)
        p = c1.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        self.run(p, kind + "\n", bold=True, size=11); self.run(p, title.upper(), bold=True, size=12)
        p = c2.paragraphs[0]
        self.run(p, "Mã số: " + code + "\nLần ban hành: " + lan + "\nNgày hiệu lực: " + ngay + "\nSố trang: theo bản in", size=10.5)
        self.d.add_paragraph()

    def sop_sign_table(self):
        self.table([
            ["", "Người biên soạn", "Người kiểm tra", "Người phê duyệt"],
            ["Họ tên", "", "", ""],
            ["Chức danh", "Điều dưỡng Phòng Điều dưỡng", "Trưởng phòng Điều dưỡng", "Giám đốc"],
            ["Chữ ký", "\n\n", "\n\n", "\n\n"],
            ["Ngày", "", "", ""],
        ], [2.6, 4.6, 4.6, 4.6], size=11)

    def save(self, path):
        self.d.save(path)
        return path
