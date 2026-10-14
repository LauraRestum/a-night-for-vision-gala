// Prints large-print-program.html to a tagged PDF with bookmarks and page numbers kept out of the reading order.
// Usage: node docs/source/build.js   (needs playwright-core and Montserrat installed as a system font)
const { chromium } = require('playwright-core');
const path = require('path');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM || '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
  const p = await b.newPage();
  await p.goto('file://' + path.join(__dirname, 'large-print-program.html'));
  await p.pdf({
    path: path.join(__dirname, '..', '2026_Gala_Program_LargePrint.pdf'),
    format: 'Letter', tagged: true, outline: true, printBackground: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;text-align:right;padding-right:0.75in;font-family:Montserrat,Arial,sans-serif;font-size:14pt;color:#000">Page <span class="pageNumber"></span></div>',
    margin: { top: '0.75in', bottom: '1in', left: '0.75in', right: '0.75in' },
  });
  await b.close();
})();
