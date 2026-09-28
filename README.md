# Dental hygiene case-test prep

Study page for a dental hygiene student (user's stepdaughter) at Northampton Community College, Litwak Dental Clinic. Built 2026-09-23.

## What's here
- `case-lab.html` — the one-file study page (open in any browser; also published at https://claude.ai/artifact/22V5o2ddKAf9fip3cp4umM). Four patient cases, anesthetic picker + max-dose calculator, flashcards, quiz, cram sheet. Progress saves in the browser.
- `casefiles/` — source: `Case Test 1_Alison.pdf`, `Clinic Manual_26-27.pdf`, `manual.txt` (text extract of the manual, page markers `=====PAGE n=====` are PDF page numbers; printed page = PDF page − 5).
- `Xerox Scan_09162026195955.pdf` — scan of the other three cases (Jack/John Williams, Grace, Robert). No text layer; `scan/` has PNG renders.
- `casefiles.zip` — original upload.

## Two tests in one page (added 2026-09-28)
The page title is a dropdown that switches tests. Each test has its own tabs, flashcard progress, quiz best score and remembered tab. XP and level are shared. First visit opens the newest test; after that it opens whichever was used last.

- **Case Lab** (Test 1): Cases, Anesthetic lab, Flashcards, Quiz, Cram sheet. Unchanged.
- **Test 2 Lab**: Ask instructor (34 items), Practice (148 questions in three sections), Flashcards (59), Quiz, Cram sheet. Opens on Practice.

**Ask instructor tab** (`ASK`, `renderAsk()`): every place a slide conflicts with itself or with a handwritten note, asks a question it never answers, or leaves something out. Each item shows why it is unclear and what the page assumes for now, with a box for the instructor's answer. Answers are saved under `S.ask` and are kept when "Start over" erases progress. When the instructor answers one, update the matching Practice question and mark the item here.

**Known limits of Test 2 Lab:** no photos (picture-identification slides 127, 133, 134, 158–161 of the SRP deck must be studied from the slides), nothing from the embedded videos, nothing from the textbook, and a handful of handwritten notes that could not be read (listed in the "Check your own notes" item).

Test 2 sources are three slide decks in `Docs/Study Materials/Test 2/`, exported with her handwritten notes on them:
- `Perio index.pdf`: Dental Indices, 59 slides (PSR, PerioWise, and the indices).
- `Sealants .pdf`: Pit and Fissure Sealants, 36 slides.
- `SCALING AND ROOT PLANING .pdf`: Nonsurgical Periodontal Therapy, 168 slides.

In the code: `TESTS` (the dropdown), `T2` (sections and questions), `CARDS2`, `renderCram2()`. Test 2 question ids start `t2i-`, `t2s-`, `t2p-`. Saved keys: `<profile>-test`, `<profile>-tab-t2`, card keys `t2-<n>`, `best_t2`. To add a Test 3, add an entry to `TESTS` and follow the same pattern.

Test 2 answers are tagged with deck and slide number ("Indices slide 37"). A ★ or "class note" means it came from the handwriting. Multiple-choice options are shuffled once per question id so the right answer is not always in the same slot.

### Themes (added 2026-09-28)
The 🎨 button in the header switches the look: **Sakura** (original, follows the device's light/dark setting), **Anime** (ink outlines, hard comic shadows, stars, an original chibi tooth mascot), **Wednesday** (dark, spider web), **Steelers** (black and gold stripes, football; colors only, no team logo), **Hazelnut** (the student's light brown bunny, hazelnuts and clover). Shape rules for each theme sit at the end of the stylesheet, just above the reduced-motion rule. The choice is saved per student name under `<profile>-skin`. In the code: `SKINS` and `applySkin()`; colors are the `:root[data-skin="..."]` blocks; corner art is the `.deco-anime`, `.deco-wed`, `.deco-steel` and `.deco-hazel` SVGs. All artwork is original; no show characters or logos. To add a theme, add a `SKINS` entry and a matching `:root[data-skin]` block.

### Test 2 items to check with the instructor
- PSR Code 3: the slide says both "chart the affected sextant or full mouth, depending on how many sextants" and "a complete examination is required."
- Periodontal Index: slide says clinical exam alone or with radiographs; her note says "must be done with radiographs."
- OHI-S rating table (slide 36) has two columns, "OHI" and "OHI-S". The page uses the OHI-S column.
- Review slides 162–164: the answers shown are her handwriting (opposite arch at 8 o'clock; knuckle rest and finger assist).
- Re-evaluation is 4–8 weeks in this deck. Test 1 content says 4–6 weeks.
- Root anatomy comes from her handwritten notes; tooth lengths in the notes were left out because they were hard to read.

## Decisions baked into the page (check against her class notes)
- Alison: ASA III (not IV), generalized Stage III Grade C, lido 1:100k or articaine 1:200k, avoid prilocaine/benzocaine (pernicious anemia).
- Jack: no BP on form → must take vitals; ASA III; localized Stage III Grade B; INR/medical referral for Coumadin; taste loss = enalapril.
- Grace: BP taken on mastectomy arm (manual p.97 forbids); Stage 2 BP; Coreg = non-selective beta blocker → cardiac epi cap; generalized Stage IV Grade B; #19 abscess.
- Robert: Stage 2 BP retaken, proceed; stable perio on reduced periodontium Stage III Grade B, D4910; sulfite/asthma; declination form for fluoride.
- Max-dose numbers are textbook (Malamed), not from the manual.
- Unknowns: Grace's and Robert's weights, Jack's BP.

## Where she opens it
**https://cfritzlen.github.io/hygiene-case-lab/** — GitHub Pages from `cfritzlen/hygiene-case-lab` (public, `main` branch root). No login needed.

Two builds from one source, made by `build.py`:
- `index.html` — web layout. A tiny script redirects phones to `phone.html` unless the viewer chose "Web version" (`?web`, remembered in localStorage).
- `phone.html` — phone layout forced at every width (questions first, chart as a slide-up sheet, big buttons). Clears the remembered choice.

The repo holds only those two pages, `build.py`, `README.md`, `.gitignore`; `.gitignore` blocks everything else (manual, scans) from ever being pushed.

To update: edit `case-lab.html` → `python build.py` → commit → `git push`. Pages rebuilds in about a minute. Republish `case-lab.html` to the artifact separately if wanted (the artifact host adds its own viewport tag; the GitHub build adds one itself).

## Rules for edits
- Every answer is tagged "Manual p.__" (printed page) or "Standard teaching". Keep that. Test 2 answers are tagged with the deck and slide number.
- The slide PDFs are too large to read directly. Render them to page images with PyMuPDF (`fitz`, installed) and read the images; the handwriting only shows up in the images, not the text layer.
- Edit `case-lab.html`, syntax-check the script, republish to the same artifact URL.
