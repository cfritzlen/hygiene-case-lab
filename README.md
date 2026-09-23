# Dental hygiene case-test prep

Study page for a dental hygiene student (user's stepdaughter) at Northampton Community College, Litwak Dental Clinic. Built 2026-09-23.

## What's here
- `case-lab.html` — the one-file study page (open in any browser; also published at https://claude.ai/artifact/22V5o2ddKAf9fip3cp4umM). Four patient cases, anesthetic picker + max-dose calculator, flashcards, quiz, cram sheet. Progress saves in the browser.
- `casefiles/` — source: `Case Test 1_Alison.pdf`, `Clinic Manual_26-27.pdf`, `manual.txt` (text extract of the manual, page markers `=====PAGE n=====` are PDF page numbers; printed page = PDF page − 5).
- `Xerox Scan_09162026195955.pdf` — scan of the other three cases (Jack/John Williams, Grace, Robert). No text layer; `scan/` has PNG renders.
- `casefiles.zip` — original upload.

## Decisions baked into the page (check against her class notes)
- Alison: ASA III (not IV), generalized Stage III Grade C, lido 1:100k or articaine 1:200k, avoid prilocaine/benzocaine (pernicious anemia).
- Jack: no BP on form → must take vitals; ASA III; localized Stage III Grade B; INR/medical referral for Coumadin; taste loss = enalapril.
- Grace: BP taken on mastectomy arm (manual p.97 forbids); Stage 2 BP; Coreg = non-selective beta blocker → cardiac epi cap; generalized Stage IV Grade B; #19 abscess.
- Robert: Stage 2 BP retaken, proceed; stable perio on reduced periodontium Stage III Grade B, D4910; sulfite/asthma; declination form for fluoride.
- Max-dose numbers are textbook (Malamed), not from the manual.
- Unknowns: Grace's and Robert's weights, Jack's BP.

## Rules for edits
- Every answer is tagged "Manual p.__" (printed page) or "Standard teaching". Keep that.
- Edit `case-lab.html`, syntax-check the script, republish to the same artifact URL.
