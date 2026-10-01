"""C387 deck: WSQ/CASL TGS-2026064536 -> non-WSQ C387 (2 days). Edits the built deck in place."""
import re
from pptx import Presentation

SRC = 'source-wsq/courseware/Video Editing with Premiere Pro-v12.pptx'
OUT = 'courseware/Adobe Premiere Pro Masterclass-v12.pptx'
OLD_T, NEW_T = 'Video Editing with Premiere Pro', 'Adobe Premiere Pro Masterclass'
OLD_C, NEW_C = 'TGS-2026064536', 'C387'
# Digital Attendance, Skills Framework, K1-K7, A1-A7, Learning Outcomes,
# Briefing for Assessment, Assessment, Assessment Flow, Final Reminder, Assessment Flow
DROP = [1, 8, 9, 10, 11, 13, 14, 15, 138, 139]
FEEDBACK = 140        # closing Digital Attendance -> Course Feedback (rewritten in place)

p = Presentation(SRC)
W, H = p.slide_width, p.slide_height

def walk(shapes):
    for sh in shapes:
        if sh.shape_type == 6:
            yield from walk(sh.shapes)
        else:
            yield sh

def set_para(para, text):
    runs = para.runs
    runs[0].text = text
    for r in runs[1:]:
        r.text = ''

def set_shape(slide, sid, lines):
    sh = next(s for s in walk(slide.shapes) if s.shape_id == sid)
    paras = sh.text_frame.paragraphs
    assert len(paras) == len(lines), (sid, len(paras), lines)
    for pa, t in zip(paras, lines):
        if t is not None:
            set_para(pa, t)

S = p.slides
# --- cover ---
set_shape(S[0], 8, ['COURSE SLIDES · NON-WSQ'])
cover = next(s for s in S[0].shapes if s.shape_id == 11).text_frame.paragraphs
cover[1].runs[0].text = 'Duration  '
cover[1].runs[1].text = '2 days · 15 instructional hours'
# --- inline WSQ / assessment references ---
set_shape(S[5], 28, ['Protect learner work and project files.'])
set_shape(S[7], 31, ['Day 1 develops editorial structure and shot control; Day 2 integrates sound, graphics, colour, QC and delivery.'])
set_shape(S[18], 16, ['This course does not award an Adobe credential.'])
set_shape(S[136], 4, ['CHANGE CONTROL'])
set_shape(S[137], 32, ['Do not share course media or learner work publicly.'])
# --- Course Feedback (was TRAQOM closing admin) ---
F = S[FEEDBACK]
set_shape(F, 4, ['COURSE FEEDBACK'])
set_shape(F, 5, ['Course Feedback'])
set_shape(F, 11, ['Rate the course'])
set_shape(F, 12, ['Tell us how well the content, pace and labs met your goals.'])
set_shape(F, 15, ['Rate the trainer'])
set_shape(F, 16, ['Share feedback on explanations, demonstrations and lab support.'])
set_shape(F, 19, ['Keep practising'])
set_shape(F, 20, ["Complete any remaining labs using each lab folder's README."])

# --- global paragraph rewrites: title, code, K/A criteria (LO kept) ---
for i, s in enumerate(S):
    for sh in walk(s.shapes):
        if not sh.has_text_frame:
            continue
        for pa in sh.text_frame.paragraphs:
            t = pa.text
            n = t.replace(OLD_T, NEW_T).replace(OLD_C, NEW_C)
            n = re.sub(r'(LO\d)( · [KA]\d)+', r'\1', n)
            if n == t:
                continue
            # keep run formatting: rewrite run by run when a single run holds the change
            done = False
            for r in pa.runs:
                rt = re.sub(r'(LO\d)( · [KA]\d)+', r'\1', r.text.replace(OLD_T, NEW_T).replace(OLD_C, NEW_C))
                if rt != r.text:
                    r.text = rt
                    done = True
            if pa.text != n:
                set_para(pa, n)

# --- hyperlinks: repoint the labs-repo button at the non-WSQ repo ---
OLD_REPO = 'https://github.com/tertiarycourses/TGS-2026064536-Video-Editing-with-Premiere-Pro'
NEW_REPO = 'https://github.com/tertiarycourses/C387-Adobe-Premiere-Pro-Masterclass'
for s in S:
    for rel in s.part.rels.values():
        if rel.is_external and rel.target_ref == OLD_REPO:
            rel._target = NEW_REPO
            rel.__dict__['target_ref'] = NEW_REPO

# --- drop WSQ slides ---
lst = p.slides._sldIdLst
ids = list(lst)
for idx in sorted(DROP, reverse=True):
    el = ids[idx]
    p.part.drop_rel(el.rId)
    lst.remove(el)

# --- renumber the static footer page number (bottom-right, whole-number text) ---
for n, s in enumerate(p.slides, 1):
    for sh in walk(s.shapes):
        if sh.has_text_frame and sh.top > H * 0.85 and sh.left > W * 0.5 and sh.text_frame.text.strip().isdigit():
            set_para(sh.text_frame.paragraphs[0], str(n))
p.save(OUT)
print('saved', OUT, len(p.slides), 'slides')
