# Large print program: source

`large-print-program.html` is the editable source for `../2026_Gala_Program_LargePrint.pdf`. Edit the text there, then rebuild:

1. Install Montserrat Regular and Bold as system fonts.
2. `node docs/source/build.js` (needs `playwright-core` and Chromium; prints a tagged PDF with bookmarks).
3. `python3 docs/source/mark-artifacts.py docs/2026_Gala_Program_LargePrint.pdf` (needs `pikepdf`; marks the page numbers as artifacts so screen readers skip them).

Keep: body text 18pt or larger, black on white, Montserrat only, one h1, real headings and lists, `lang` set, no em dashes, dates with ordinals (October 24th), donor-facing names spelled out (Bicknell Envision Vision Rehabilitation Center, Gigi & Carl Allen Envision Research Institute, Cathy G. Hudson Envision Child Development Center). Update the page count in the link on the Program page if it changes.
