"""C387 labs + LG Markdown mirror: rewrite course identity in .md and their ReportLab .pdf twins (in place)."""
import re
from pathlib import Path
import pypdf

OLD_T, NEW_T = 'Video Editing with Premiere Pro', 'Adobe Premiere Pro Masterclass'
OLD_C, NEW_C = 'TGS-2026064536', 'C387'

for md in Path('labs').rglob('*.md'):
    md.write_text(md.read_text().replace(OLD_T, NEW_T).replace(OLD_C, NEW_C))
for pdf in Path('labs').rglob('*.pdf'):
    w = pypdf.PdfWriter(clone_from=str(pdf))
    for pg in w.pages:
        co = pg.get_contents()
        co.set_data(co.get_data().replace(OLD_T.encode(), NEW_T.encode()).replace(OLD_C.encode(), NEW_C.encode()))
        pg.replace_contents(co)
    if w.metadata:
        w.add_metadata({k: str(v).replace(OLD_T, NEW_T).replace(OLD_C, NEW_C) for k, v in w.metadata.items()})
    with open(pdf, 'wb') as f:
        w.write(f)

# LG Markdown mirror
lg = Path('LEARNER-GUIDE.md')
t = lg.read_text().replace(OLD_T, NEW_T).replace(OLD_C, NEW_C)
t = re.sub(r'## TSC alignment\n.*?(?=\n## )', '', t, flags=re.S)
t = re.sub(r'(LO\d)( · [KA]\d)+', r'\1', t)
t = re.sub(r'- \*\*(Legacy course deck|Original WA from LMS-TMS|Original PP from LMS-TMS):\*\*.*\n', '', t)
t = t.replace('https://www.tertiarycourses.com.sg/casl-video-editing-with-premiere-pro.html',
              'https://www.tertiarycourses.com.sg/adobe-premiere-pro-masterclass.html')
t = re.sub(r'\n{3,}', '\n\n', t)
lg.write_text(t)
print('done')
