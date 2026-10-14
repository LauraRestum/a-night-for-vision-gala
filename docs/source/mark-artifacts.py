"""Marks the untagged footer ("Page N") that Chromium emits as a PDF Artifact, so screen readers skip it.
Usage: /usr/bin/python3 docs/source/mark-artifacts.py docs/2026_Gala_Program_LargePrint.pdf  (needs pikepdf)"""
import sys, pikepdf
from pikepdf import Operator, Name

def wrap_unmarked(ops):
    out, i, n, mc = [], 0, len(ops), 0
    while i < n:
        inst = ops[i]; op = str(inst.operator)
        if op in ('BDC', 'BMC'): mc += 1
        elif op == 'EMC': mc -= 1
        if op == 'q' and mc == 0:
            q, j = 0, i
            while j < n:
                o = str(ops[j].operator)
                if o == 'q': q += 1
                elif o == 'Q':
                    q -= 1
                    if q == 0: break
                j += 1
            seg = ops[i:j + 1]
            names = {str(x.operator) for x in seg}
            if not names & {'BDC', 'BMC'} and names & {'Tj', 'TJ', 'Do', 'S', 'f', 'f*', 'B'}:
                out.append(pikepdf.ContentStreamInstruction([Name.Artifact], Operator('BMC')))
                out.extend(seg)
                out.append(pikepdf.ContentStreamInstruction([], Operator('EMC')))
            else:
                out.extend(seg)
            i = j + 1
            continue
        out.append(inst); i += 1
    return out

path = sys.argv[1]
pdf = pikepdf.open(path, allow_overwriting_input=True)
for pg in pdf.pages:
    ops = list(pikepdf.parse_content_stream(pg))
    pg.Contents = pdf.make_stream(pikepdf.unparse_content_stream(wrap_unmarked(ops)))
pdf.save(path)
