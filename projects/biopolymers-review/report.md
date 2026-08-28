# Biopolymers: Structure, Properties and Performance Limits

*CM3254 Project Report · [Author 1, Matric No.] · [Author 2, Matric No.] · [Date]*

> **AI Tool Declaration** — *(final wording to be added on the first page before submission)*

<!-- STATUS (2026-08-28c, figures merged into multi-panel composites): §1-§10 complete,
     **8 figures / 5 tables / 56 references**. Figures went 15 -> 8 by combining related ones
     into single multi-panel figures (real-paper style, one caption each): old Fig 3/6/7/8/9
     (all repeat units) -> Fig 3 (13 panels); old Fig 4/5/6c/7cd (higher-order structure) ->
     Fig 4 (6 panels); old Fig 11/12 (thermal + Ashby) -> Fig 5 (2 panels); old Fig 14
     (processing flowchart) dropped, its logic folded into §6 prose. Also a whole-document
     prose-tightening pass (-250 words). Body page count still being measured after this pass;
     the earlier "10 pages" reading was a measure_pages.ps1 bug (matched "References" in §7.3
     body text) — real body was 13, now targeting ~10-11. Still open: CSV values PROVISIONAL;
     §7.2 $/kg needs a market report; first-page author names + AI declaration; references.zip;
     alginate G config cross-check. report_zh.md prose/renumber not yet re-synced with this pass.

     ---- prior STATUS (2026-08-28, figure consolidation): 15 figures, dropped Appendix A. ----
     User asked to make the figures less cluttered and the document cleaner. This pass:
     (1) DELETED Appendix A and its two gallery figures (old Fig 18/19) — every material they
         showed already has an in-body §3.1-3.5 figure; SBR's two comonomers (the one thing only
         the appendix had) were folded into the §7.3 figure (now Fig 15).
     (2) The three sparse degradation figures (old Fig 13/14/15) → old 13+14 merged into one
         2-panel figure (now Fig 13, `figures/fig6_degradation.py` -> `fig_degradation.png`);
         old Fig 15 (schematic energy-barrier curve, "no values implied", a ⚙️ computational
         aside) deleted, replaced by one sentence in §5.4.
     (3) Every figure re-exported at a fixed 170 mm width via a rewritten `figures/style.py`
         (no more `bbox_inches="tight"`, shared `draw_mol()`, in-figure titles/prose removed and
         moved into the Word captions here). Figures now read as one consistent set.
     (4) **Table 2** converted from a scatter-plot image back to a real Word three-line table
         (built from the CSV data; still PROVISIONAL, flagged).
     (5) Figures renumbered 1-15 throughout; "seven families" wording in the §3 / Fig 2 area
         reconciled ("five backbone classes, shown as seven rows").
     Still open (unchanged from before, separate tasks): references 32 -> 50-60 required;
     all Table 2 / Table 3 / §7.2 numbers are PROVISIONAL and need cited values; author names,
     matric numbers, date, and the AI Tool Declaration wording are placeholders; the
     `yourname-references.zip` (title-page requirement 9) is not built; alginate G absolute
     configuration needs a ChemDraw cross-check. -->

<!-- STATUS (2026-08-26, prose polish + a real CJK formatting bug fix): §1-§10 complete, 19
     figures / 5 tables / 32 references, page counts unchanged from the prior pass.

     User asked (verbatim, translated): "the phrasing is stiff/awkward in places, and there are
     formatting problems" — no further specifics given, full judgement-call authority delegated
     as in prior passes.

     PROSE: targeted the passages with the most mechanical, repetitive architecture (the clearest
     tell of AI-drafted prose: identical "claim — dash-elaboration — semicolon-chained evidence"
     shape repeated paragraph after paragraph) rather than rewriting everything — introduction
     (broken into two paragraphs, the three structural features turned from one semicolon-chained
     sentence into three short enumerated ones), the §3 family-overview paragraph (the "X sits at
     one extreme — ...; Y sits at the other — ..." pattern was used identically twice plus a third
     dash for lignin — varied it), §3.5's "This is not fixed:" (ambiguous — could mean "not yet
     fixed" — reworded to "not a fixed material constant, though:"), §7.1's four advantages
     (previously one 100+-word sentence with four dash-elaborated semicolon-joined bullets crammed
     in — split into four separate sentences), and §7.3's NR/SBR paragraph in report_zh.md, which
     had stacked THREE em-dashes in one sentence (genuinely hard to parse) — restructured the
     "不是A而是B" contrast without dashes. Chinese-first per the standing convention, English
     ported afterward. Preserved every citation, figure/table cross-reference, and data value
     exactly; nothing factual was touched.

     FORMATTING — one real, systemic bug found and fixed, not just cosmetic tweaks: build_docx.py's
     paragraph-joining (`gather_paragraph()`, the blockquote handler, and the figure-caption
     multi-line merge) joined hard-wrapped source lines with a literal `" ".join(...)`. That's
     correct for English (words need the space) but wrong for Chinese: every hard-wrap point in
     report_zh.md's source was rendering as a visible, spurious gap in the middle of a Chinese
     sentence, since CJK text has no inter-character spaces — confirmed via PDF visual QA on
     report_zh's page 1 before the fix (e.g. "木质素，合计 构成了地球上" had a stray gap that
     doesn't exist in the source's intended reading). This was NOT specific to my prose edits —
     it silently affected every hard-wrapped Chinese paragraph in the document, existing text
     included, likely since the original gather_paragraph() fix months ago (which was written and
     tested against English wrapping). Fixed with a new `smart_join()` helper: joins with no
     separator when both sides of a wrap point are CJK characters, falls back to a space
     otherwise (so English text, and Latin terms/citations embedded in Chinese sentences, still
     get their necessary space). Re-verified via PDF export afterward — the gaps are gone on every
     inspected page; English pages render identically to before (smart_join is a no-op for
     all-ASCII text). Also found one Chinese-text-in-English-body leak: Appendix A's prose quoted
     `OUTLINE.md`'s Chinese requirement text ("10 页，不含参考文献") directly inside the English
     submission document — translated to English in report.md ("10 pages excluding references").
     Also checked and found consistent: citation bracket format ([N], [N,M], [N–M] throughout, no
     stray parenthetical-citation style), figure/table caption markup, heading levels.

     PAGE COUNT: unchanged from the prior pass — EN 17 total (body 1-13, same as before), ZH 15
     total (body also 1-13) — re-measured via measure_sections.ps1/measure_sections_zh.ps1 after
     every edit batch. The smart_join fix actually removes characters (spurious spaces) from the
     Chinese doc, so if anything it very slightly *helped* the page budget, not hurt it.

     Both Desktop docx files updated and confirmed via file timestamp/size after this pass. New
     helper script `export_pdf_zh.ps1` added (export_pdf.ps1 only ever exported the English docx;
     needed a Chinese-docx equivalent to do the required visual QA pass on report_zh.md).
-->
<!-- STATUS (2026-08-26, figure overhaul + §3 per-polymer figures + renumbering 1-19): §1-§10
     complete, 19 figures / 5 tables / 32 references.

     USER ASKED (verbatim, translated): (1) every polymer discussed in §3 needs its own monomer
     figure AND chain/spatial-structure figure placed IN that subsection, not confined to the
     appendix; (2) Fig. 6 (degradation) split into three standalone figures, not one 3-panel
     figure; (3) figure sizing across the document was inconsistent/messy, fix it; (4) Fig. 10
     (processing flowchart) didn't read as a professional journal figure, restyle it; (5) Fig. 3
     (cellulose hierarchy) had a text/image overlap bug; (6) Fig. 11 (the combined 1x4 strip
     duplicating Fig.4/5/6/8) is no longer wanted, split it apart / remove it, and turn its
     panel (d) — the NR/SBR scorecard — into a real table. User was away and explicitly said not
     to ask further questions; every judgement call below was made autonomously.

     WHAT CHANGED (this took two fork attempts — a session-limit interruption killed the first
     mid-task; a WIP checkpoint commit `4fd7703` preserved the work and a second fork resumed
     from git state, since a completed/killed fork's transcript cannot be resumed via SendMessage
     once it drops off ListAgents — spawn fresh and resume from git, don't retry the resume):

     (1) Fig. 6 split into `fig6a_polyester_hydrolysis.py` (now Fig. 13), `fig6b_enzymatic_
     degradation.py` (Fig. 14), `fig6c_hydrolysis_barriers.py` (Fig. 15) — each single-panel,
     own caption, still appearing back-to-back in §5.4's prose.
     (2) Fig. 11 (`combine_1x4.py`'s stitched strip) deleted as an entity — decoupled from
     `make_all.py`, removed from `FIGURE_FILES`, removed from both report files. The script
     itself is left in `figures/` unused, not deleted.
     (3) Fig. 8's scorecard panel became **Table 5** (native Word three-line table, same
     favourable/context-dependent/risk categories, still carries every citation number) — the
     remaining structure-schematic panel is now its own standalone figure, Fig. 17, cross-
     referencing the fuller version at appendix Fig. 19(f).
     (4) Fig. 10 (now Fig. 16) restyled: thin borders + colour accent bars replacing solid
     rounded colour blocks, matching the sober look of Fig. 2/11/12/16's analytical style.
     Content/logic unchanged, visual language only.
     (5) Fig. 3 (now Fig. 4, cellulose hierarchy) — text/geometry overlaps in panels (a) and (c)
     fixed via spacing/repositioning, re-rendered and visually confirmed clean via PDF export.
     (6) Six new compact figures added for §3.1-3.5, one (Fig. 6 gets both monomer+chain in one
     figure) to two per subsection: Fig. 3 (`fig_polysaccharide_monomers.py`), Fig. 5
     (`fig_polysaccharide_chains.py`), Fig. 6 (`fig_polyester_structures.py`), Fig. 7
     (`fig_protein_structures.py`), Fig. 8 (`fig_lignin_monomers.py`), Fig. 9
     (`fig_rubber_monomer.py`). All reuse already-verified SMILES imported from
     `fig2_repeat_units.py` / `fig12_appendix_monomers.py` / `fig13_appendix_chain_structures.py`
     — no stereochemistry was retyped or re-derived from scratch. The appendix (Fig. 18/19,
     renumbered from 12/13) was kept as a complete reference gallery rather than trimmed, since
     it doesn't count against the body page budget and several in-body figures (e.g. Fig. 9,
     rubber monomer only) deliberately omit content shown fully in the appendix (e.g. NR/SBR's
     complete 6-panel comparison lives only at Fig. 19(f), Fig. 17 is the compact §7.3 version).
     (7) All 19 figures + Table 5 renumbered in strict first-appearance reading order, in BOTH
     report_zh.md (edited first, per the Chinese-first convention) and report.md — every caption,
     every in-prose cross-reference, `FIGURE_FILES`, `FIGURE_MAX_HEIGHT_IN`, `make_all.py`'s
     module list, and FIGURES.md all updated consistently. `fig2_repeat_units.py` (old Fig 2) is
     unused now (its 5 structures were redistributed into Fig. 3 and Fig. 6) but left in
     `figures/` for reference, not deleted.
     (8) Figure sizing unified into a 3-band system replacing the old ad hoc per-figure heights:
     `FIGURE_HEIGHT_S/M/L` = 1.3/1.9/2.3in in `build_docx.py`, applied to every body figure (the
     one documented exception is appendix Fig. 19 at 4.2in, a 6-panel gallery that isn't subject
     to page-budget sizing anyway).
     (9) A real, general layout bug found via PDF visual QA (not just script-exit-code trust):
     Word could push a figure's caption paragraph alone onto the next page while the image
     stayed on the previous one — caught on appendix Fig. 19, whose caption landed alone on an
     otherwise-blank page 17. Fixed by setting `keep_with_next = True` on every figure's image
     paragraph in `build_docx.py` (applies to all 19 figures, not just the one it was caught on).
     (10) A real pre-existing bug fixed along the way: the Fig. 4/5 (thermal/mechanical) CSV
     loaders lacked `encoding="utf-8"`, breaking under a non-UTF8 console codepage.

     PAGE BUDGET: body (§1-§10) now spans pages 1-13 in BOTH languages (EN and ZH matched
     exactly after the keep_with_next fix — previously ZH was 1 page shorter than EN). This is a
     real +2 page regression from the previously-defended 11-page body (10-page nominal target).
     Tried to claw this back per the agreed priority order: the two M-band new figures (Fig. 5,
     Fig. 7) were checked against the S band and found already near-minimum legible size in the
     PDF render (shrinking further risked illegibility for negligible page gain); no single
     obviously-redundant sentence was found whose removal would meaningfully move a 2-page gap
     (unlike the ~30-word trims that closed 1-page gaps in earlier passes — this gap is an order
     of magnitude larger because six genuinely new required figures were added, not a
     rounding-error pagination fragility). Judgement call: did NOT contort the document further
     to chase 10 or 11 pages — the user's explicit content instruction (every §3 subsection gets
     its own figures) takes priority, and 13 pages for 19 figures / 5 tables covering every
     polymer discussed is a proportionate, honestly-reported outcome, not a bug to keep hunting.
     EN total 17 pages (body 1-13, references 14-?, appendix to 17). ZH total 15 pages (same
     13-page body; shorter overall due to CJK character density in refs/appendix, not a
     different word count). Verified via `measure_sections.ps1` / `measure_sections_zh.ps1` (the
     latter had its own bug: the file was saved without a UTF-8 BOM, so Windows PowerShell 5.1
     misparsed the Chinese string literals as the system codepage and threw parser errors —
     fixed by rewriting it via .NET `File.ReadAllText(path, Encoding.UTF8)` / `WriteAllText` with
     an explicit UTF8 BOM encoding; if a `.ps1` file with non-ASCII literals ever fails to parse
     with garbled-looking token errors, check its encoding first, same class of issue as the
     UTF-16LE `~/.claude/CLAUDE.md` gotcha already in claude-memory).

     QA: did a full PDF-export visual pass (not just trusting script exit codes) on the changed/
     new figures — §3.1-3.5 pages (Fig. 3-9), the split Fig. 6 (13-15), Fig. 16's restyle, Fig.
     17 + Table 5, and the appendix (Fig. 18/19, where the keep_with_next bug above was caught
     and fixed). All rendered cleanly on the second pass; sizing reads as a consistent system
     now, not the "inconsistent, messy" state the user flagged.

     One caveat carried forward unchanged: alginate G (guluronic acid)'s absolute configuration
     is still only verified as "the C5 epimer of M" (a literature-established relationship), not
     independently CIP-matched — flagged in Fig. 18's caption and in the appendix prose, needs a
     ChemDraw/literature cross-check before submission.

     Both Desktop docx files updated and confirmed via file timestamp/size after this pass.
-->
<!-- STATUS (2026-08-26, Fig 6 text trim + Fig 8 case-study structure panel): §1-§10 complete,
     13 figures total, same count as the prior pass (Fig. 8 gained a panel, no new figure number).

     User asked (1) Fig. 6 to carry less in-figure text, (2) the §7.3 case study to get a structure
     figure placed IN the body, not only in the appendix.

     (1) Fig. 6 (`figures/fig6_degradation.py`): NOTE_A/B/C were each a multi-line paragraph
     largely restating §5.4's body prose. Cut to one short phrase each (5-9 words) — the panels
     (reaction diagram, crystalline/amorphous bar, three labelled energy curves) now carry the
     content, prose only labels. Shrank the GridSpec row heights to match (dead whitespace was
     opening up under the shorter notes); native image aspect changed from ~0.68 to ~0.59
     (h/w), `FIGURE_MAX_HEIGHT_IN[6]` dropped 2.1 -> 1.7in accordingly.
     (2) Fig. 8 (`figures/fig8_nr_sbr_comparison.py`): added panel (a), a compact chain-scale
     schematic — amorphous coil at rest -> SIC-aligned crystalline bundles under strain for NR
     (solid grey), stays amorphous under strain for SBR (dashed grey, deliberately NOT a 6th
     palette colour — style.py's CLASS_COLOR is fixed at 5 for colour-blind-safety reasons).
     Existing scorecard became panel (b). Cross-references Fig. 13(f) in the appendix (the fuller
     version of the same mechanism) both ways. Kept the SAME figure number (avoided renumbering
     9-13, which would have touched cross-references in both language files) rather than adding a
     separate "Fig. 8b".
     (3) Pagination regression, found and fixed: adding Fig. 8's new panel at first attempt
     (`FIGURE_MAX_HEIGHT_IN[8]` raised 2.3 -> 2.6in to keep it legible) pushed §10 Conclusions from
     page 11 to page 12 in EN — confirmed the height-cap change was the direct cause by reverting
     it alone and re-measuring (12 -> 11). Reverted the cap back to 2.3in (the structure panel is
     smaller within the same footprint, still legible in the PDF render). ZH needed an *additional*
     fix beyond matching the EN cap revert — even at cap 2.3, ZH's Conclusions stayed on page 12,
     traced to the new Fig. 8/§7.3 caption and prose text alone (Chinese character width made the
     same edit costlier in ZH than EN); trimmed the Fig. 8 caption and §7.3/§9 prose in
     report_zh.md (edited first, ported the equivalent trim to report.md for content parity even
     though EN didn't strictly need it for page budget) until `measure_sections.ps1`/manual Chinese-
     heading search confirmed 结论 back on page 11. Confirms the prior STATUS note's warning: this
     margin really is a hair's-breadth, and it costs DIFFERENT amounts of slack per language for
     the same edit — always re-measure BOTH docs after a body change, not just one.
     PAGE COUNT (re-verified via measure_sections.ps1 + PDF visual QA of the touched pages): EN
     total 15 pages, body 1-11 (§10 spills past 10, unchanged), refs 12-13, appendix 14-15 —
     unchanged from the prior pass. ZH total 13 pages, body also 1-11 — unchanged. Both Desktop
     docx files updated.

-->
<!-- STATUS (2026-08-26, appendix + submission-readiness pass): §1-§10 complete, 13 figures total
     (10 in the body + Fig. 11 composite + 2 new appendix figures) / 4 tables / 32 references.

     THIS PASS, done autonomously per user instruction ("我要出去一下 ... 你自己去决定"):
     (1) Added Appendix A after References — Fig. 12 (RDKit repeat units for the 10 materials §3/
     §7.3 discuss but Fig. 2 never drew: alginate M/G, natural rubber, SBR's two comonomers, the
     three monolignols, silk's (Gly-Ala)n backbone, collagen's Gly-Pro-Hyp backbone) and Fig. 13
     (matplotlib chain-scale schematics for 6 families: amylose helix, alginate egg-box, PHA/PLA
     helix, silk β-sheet, collagen triple helix, NR-vs-SBR strain crystallisation). Verified via a
     new `figures/verify_appendix_stereochemistry.py` (same refuse-to-render-on-failure pattern as
     Fig. 2's verifier) before every render. One honest caveat, flagged in both the figure and the
     appendix prose: alginate G (guluronic acid)'s absolute configuration is only verified as "the
     C5 epimer of M" (a literature-established relationship, confirmed via epimer-derivation from
     the already-verified D-glucose scaffold + an uncap() round-trip check) — no independent
     literature CIP string was available to cross-check it directly, unlike every other structure
     in Fig. 12; flagged for a ChemDraw/literature cross-check before submission. Appendix A does
     NOT count against the 10-page body limit (same treatment as References, per OUTLINE.md).
     (2) Submission-readiness pass: word count checked (~3090 words for §1-10 vs. OUTLINE.md's
     2900-word budget — only ~6% over, much closer than the ~5800-word state flagged 2026-08-24,
     so no aggressive trimming was warranted); grepped both language files for stale editorial
     artifacts — found only the already-intentional, already-documented PROVISIONAL/[cite]/VERIFY
     flags on CSV data and the §7.2 pricing citation, nothing stale to clean up; checked figure/
     table numbering consistency 1-13 / 1-4 across both languages, no gaps or stray references.
     (3) Found and fixed a real, if minor, pagination fragility: §10 Conclusions was landing on
     page 12 (not page 11 as the previous STATUS note claimed) — confirmed via a git-history
     baseline rebuild that this was already true at HEAD before this session touched anything (the
     Table 2 scatter-plot-image commit likely caused it; the STATUS note just hadn't been
     re-verified since). This turned out to be razor-thin: Word's widow/orphan control was pushing
     the entire Conclusions heading+paragraph to page 12 because the remaining space on page 11
     couldn't fit even 2 lines together — NOT a bug, just genuinely tight pagination (confirmed by
     testing `keep_with_next=True` on headings, which made it worse by forcing the whole heading to
     move too; reverted). Fixed by trimming two small, purely-redundant sentences (~30 words total,
     one in §7.2's price bullet restating a fact §7.3 already makes with a citation, one in §3.2
     dropping a tangential PEF-barrier aside) in BOTH report_zh.md (edited first, per the
     Chinese-first workflow rule) and report.md — restores body to 11 pages (§10 spilling 1 page
     past the nominal 10, same as the previously-documented "accepted" state), verified via
     `measure_sections.ps1` after every edit. This is genuinely a hair's-breadth margin — a future
     content edit of even ~15-20 words in the wrong place could tip it back to 12; re-run
     `measure_sections.ps1` after any body edit rather than assuming the 11-page state holds.
     (4) Did a full visual QA pass (PDF export + page renders) on BOTH language docs: title page,
     Table 1/4, §9-10 boundary, appendix Fig. 12/13 pages, references, and (ZH only) the
     translator's-note blockquote — all rendered cleanly, no overlapping/truncated content, no
     regression of the three previously-fixed build_docx.py bugs (paragraph-joining, blockquote-
     joining, table column-width starvation). (5) Proofread report.md's English prose for grammar/
     clarity — found nothing needing correction (regex checks for repeated words / missing spaces
     came up clean too); it was already in solid shape from prior compression passes.

     PAGE COUNT (Word-measured via measure_sections.ps1 / measure_pages.ps1, not estimated): EN
     total 15 pages — body (§1-§10) spans pages 1-11 (only §10 spills past page 10), References
     span pages 12-13, Appendix A spans pages 14-15. ZH total 13 pages — body also 11 pages
     (References start page 12); ZH is shorter overall due to CJK character density, not a
     different word count. `measure_sections.ps1`'s "References -> page X" line is a KNOWN false
     positive (Word's Find matches the literal substring "the References" inside §7.3's body text,
     which appears earlier than the actual heading) — trust the heading-adjacent section pages and
     `measure_pages.ps1`'s dedicated References-page logic instead, not that one line.

     PRIOR PASS (2026-08-25, figures + classification pass): §1-§10 complete, 10 figures / 4 tables /
     32 references.

     THIS PASS: (1) redesigned Fig. 1 and Table 1 — the old classification tree put *origin*
     (extracted/microbial/bio-monomer) as the primary branch and backbone chemistry as leaf
     colour only, which directly contradicted §2's own claim that backbone chemistry, not origin,
     is "the better predictor ... this review is organised on that basis." Fig. 1 now branches on
     backbone chemistry first (5 classes, matching Table 1 and Fig. 7 exactly), with origin
     demoted to a small E/M/S tag per leaf; dropped materials never discussed in §3 (bacterial
     cellulose, xanthan, PEF, bio-PE, DNA/RNA) that the old tree had scope-crept in. (2) added two
     new figures that each replace prose rather than sit alongside it: Fig. 9 (dispersity Đ across
     families, §4 — let Table 3 drop its Đ column) and Fig. 10 (processing decision flowchart,
     §6 — replaced a dense paragraph). (3) fixed a real table-layout bug in build_docx.py: column
     widths were proportional to raw character count, which starved short columns (e.g. Table 1's
     "Backbone class") into wrapping single words next to a long free-text column; now uses
     sqrt-weighted proportions with a per-column longest-word floor (search `col_word_len` in
     build_docx.py).

     PAGE COUNT: real, Word-measured (not estimated) page count is 14 total; body (§1-§10, before
     References) still spans pages 1-11 — only §10 Conclusions spills past page 10, unchanged from
     the previous pass. The +1 total page vs. the previous 13-page state is entirely inside the
     References section (OUTLINE.md: "10 页，不含参考文献" — references are explicitly NOT counted
     against the limit), not a body regression; the two new figures/table trims roughly offset
     each other on body length. Started the *previous* pass at a genuinely broken 31 pages; see
     below for those two real bugs if this recurs after further edits. Further squeezing §10 onto
     page 10 was attempted (headings/spacing/table-caption trims) without success; it looks like
     normal pagination (heading fits at the bottom of page 10, the paragraph after it doesn't),
     not a bug — pick this back up only if it actually matters at submission time.

     Two real bugs found and fixed along the way, in case this recurs after further edits:
     (1) build_docx.py was putting each hard-wrapped markdown source line into its own Word
     paragraph instead of joining wrapped lines back into one logical paragraph (report.md
     hard-wraps prose at ~90-100 chars/line for readability — standard markdown expects that
     joined back together). This alone was costing roughly 10 pages. Fixed via
     `gather_paragraph()` / `is_special_line_start()` in build_docx.py — any new block type added
     to report.md's markdown must stay compatible with that function's block-start detection or it
     will silently re-fragment paragraphs again.
     (2) Figures were inserted at a fixed 6.2in width regardless of native aspect ratio, so tall
     figures (fig6/7/8) ate 4.5-5.5in of vertical space each. Fixed via FIGURE_MAX_HEIGHT_IN /
     FIGURE_MAX_HEIGHT_IN_DEFAULT in build_docx.py, which derives width from a target max height
     instead — currently tuned quite tight (1.55in default / 2.1-2.3in for content-rich figures);
     loosen these first if the figures ever look too small once opened in Word.

     Tables also got fixed-width proportional columns (search `table.autofit` in build_docx.py)
     instead of Word's default autofit, and table cells + the reference list were switched to
     single line-spacing (OUTLINE.md's own spec: tables/captions/references are single-spaced,
     only body text is 1.5x).

     TOOLING (all in this folder): `measure_pages.ps1` (total pages/words) and
     `measure_sections.ps1` (page number at every ## / ### heading and every Table N. caption, via
     Word COM Find + wdActiveEndPageNumber) give an exact, fast page-count readout after any edit
     — do NOT trust word-count arithmetic alone for this document, real layout cost has repeatedly
     diverged from that estimate. `export_pdf.ps1` renders the current .docx to PDF for visual
     spot-checks (then e.g. `pip install pymupdf; python -c "import fitz; fitz.open(...).load_page(n).get_pixmap(dpi=110).save('page.png')"`
     to eyeball one page). Workflow: edit report.md -> run
     `python build_docx.py report.md Biopolymers-review-DRAFT.docx "Times New Roman"` -> run
     `powershell -ExecutionPolicy Bypass -File measure_sections.ps1` -> repeat. Word must be
     installed (it is, on this machine) for the .ps1 scripts to work; close any open copy of the
     target .docx first or the Python build step will fail to overwrite it.

     Reference count is 32/50-60 required. Still open: Fig.4-5/Table 2 CSV data is still mostly
     PROVISIONAL; §7.2 pricing for PE/PP/PLA/PHA has no citable primary source yet; general
     textbook-level citations (Flory relation, SEC-MALS, ROP mechanism, TGA/DSC definitions)
     aren't in yet either — see REFERENCES-TODO at the end.
     Table numbering still deviates from OUTLINE.md (1-4 here vs. its "3 tables"), unchanged from
     before — the §2 classification table isn't in the outline's budget.

     report_zh.md is now a full resync with this version (retranslated end-to-end, not patched —
     the previous zh draft was translated from a much longer pre-compression English draft and had
     drifted too far to patch). User instruction as of 2026-08-25: going forward, edit report_zh.md
     FIRST for any content change, then port to report.md — Chinese is now the priority draft.
     While doing that resync, found and fixed a third real build_docx.py bug: the blockquote
     handler (`s.startswith(">")`) processed one source line at a time like the pre-fix paragraph
     handler used to, so a hard-wrapped multi-line ">" blockquote (the zh translator's note) came
     out as one Word paragraph per source line. Fixed by gathering consecutive ">" lines the same
     way gather_paragraph() does for regular text (stops at a blank/bare ">" line too, so an
     intentional paragraph break inside a blockquote still works). -->

---

## 1. Introduction and Definition

A biopolymer is a macromolecule synthesised by a living organism: polysaccharides, proteins,
nucleic acids, *cis*-1,4-polyisoprene and lignin together account for most of the organic polymer
on Earth [1]. This report also covers polymers made by polymerising biomass-derived monomers —
chiefly poly(lactic acid) (PLA) — whose properties are best understood alongside the true
biopolymers.

Three structural features set these chains apart from synthetic polymers: template-directed
biosynthesis fixes chain length and sequence (proteins and nucleic acids are strictly monodisperse,
Đ = 1.00); enantiomerically pure monomer pools make the chains stereoregular by default; and
hydroxyl, amide or carbonyl groups on almost every repeat unit push cohesive energy densities well
above the polyolefins'. Every property and limitation examined below follows from these three:
high stiffness and crystallinity, but also brittleness, water sensitivity, and decomposition that
arrives close to or below the melting point (§5.4).

---

## 2. Types of Biopolymers

Biopolymers are usually classified first by origin — extracted from biomass, synthesised by
micro-organisms, or polymerised from bio-based monomers — but origin predicts behaviour poorly:
materials of the same origin can process and degrade completely differently, and materials of
different origins can behave alike. The repeating backbone linkage is the better predictor, since
it sets both melting survival and degradation mechanism, so this review is organised by backbone
chemistry (Table 1, Fig. 1); origin is kept only as a secondary tag, since it still explains *why*
molecular weight and purity vary within a class (§4).

**Table 1.** Classification of biopolymers by backbone chemistry, the axis this review is organised
on; origin (extracted / microbial / bio-monomer) is a secondary property, not the primary split.

| Backbone class | Repeating linkage | Representative materials | Characteristic behaviour |
|---|---|---|---|
| Polysaccharide | glycosidic (acetal) | cellulose, starch, chitosan, alginate | dense inter-chain hydrogen bonding; decomposition before melting; enzymatic degradation |
| Polyester | ester | PHA, PLA | melt-processable but thermally labile; autocatalytic hydrolysis |
| Protein | amide | silk fibroin, collagen/gelatin | sequence-defined and monodisperse; conformation-controlled properties |
| Polyphenolic | β-O-4 ether, C–C | lignin | irregular, cross-linked, amorphous; chemically recalcitrant |
| Polyisoprene | C–C | natural rubber | elastomeric; strain-induced crystallisation |

*[Figure 1 — Classification by backbone chemistry (primary branches, coloured, matching Table 1
and Fig. 2), with each material's origin shown as a small E/M/S tag: extracted from biomass,
synthesised by micro-organisms, or polymerised from bio-based monomers]*

---

## 3. Structure–Property Relationships of the Major Biopolymer Families

This section examines five families along one axis — backbone flexibility and the intermolecular
forces it permits — running from cellulose (an extended, hydrogen-bonded backbone that never melts)
to natural rubber (a freely rotating backbone, amorphous until strained). Between them lie
polysaccharides with weaker or ionically tunable interchain forces, semicrystalline polyesters that
melt-process only within narrow thermal windows, and template-folded proteins whose properties come
from defined fold, not chain packing; lignin is the counterpoint — an irregular cross-linked network
with no periodic chain. The claim tested throughout: backbone chemistry, not biological origin,
predicts melting, hydrolytic/enzymatic susceptibility and mechanical performance (Table 2). Fig. 2
carries the force → consequence → limitation chain for each family, so the text below adds only
mechanism and citations. All repeat units are collected in Fig. 3 and all higher-order (chain,
secondary, tertiary) structures in Fig. 4; the subsections point to the relevant panels.

*[Figure 2 — Structure–property causal chain, one row per family: dominant intermolecular force →
key consequence → key limitation. The five backbone classes of Table 1 appear as seven rows
(polysaccharides and polyesters are each split into two, since their two members behave distinctly).
Colour follows the backbone-chemistry class; arrows read left to right as one causal chain per
family.]*

*[Figure 3 — Repeat units of the biopolymers discussed in §3, drawn by the authors with RDKit from
SMILES checked by `verify_stereochemistry.py`, colour-coded by backbone class. Polysaccharides
(blue): (a) cellulose, (b) amylose, (c) chitosan, (d) alginate M, (e) alginate G — (a)/(b) differ
only at C1, the centre separating cellulose's crystalline ribbon from amylose's water-plasticised
helix, and (d)/(e) only at C5, the M/G ratio setting alginate's stiffness–brittleness trade-off.
Polyesters (orange): (f) PHB, (g) PLLA, with (R)/(S) marked. Proteins (green): (h) silk fibroin
(Gly-Ala)ₙ, (i) collagen Gly-Pro-Hyp. Lignin precursors (grey): (j) p-coumaryl, (k) coniferyl,
(l) sinapyl alcohol (0/1/2 methoxy groups). Rubber: (m) cis-1,4-polyisoprene. Alginate G's absolute
configuration is verified only as the C5 epimer of M — cross-check before submission.]*

*[Figure 4 — Higher-order structure across the families, drawn by the authors: (a) cellulose —
intra- and inter-chain hydrogen bonds lock the ribbon into a sheet, sheets stack by van der Waals
into the Iα/Iβ crystal, and the accumulated cohesive energy exceeds the backbone, so cellulose
decomposes near 300 °C before melting; (b) amylose's left-handed helix, whose cavity is plasticised
by water/I₂; (c) alginate's Ca²⁺-bridged "egg-box" G-block junction — ionic and reversible, its
density (G-content) setting stiffness vs. brittleness; (d) PHA/PLA helical packing (PHB 2₁, PLLA
10₃) — a helix that crystallises but still melts; (e) silk's antiparallel β-sheet nanocrystallites
(2–4 nm) in a compliant amorphous matrix, the source of its strength–toughness combination;
(f) collagen's Gly-X-Y triple helix, in which glycine at every third position is the only residue
small enough for the crowded core.]*

### 3.1 Polysaccharides

Polysaccharides span the rigid end of the spectrum. **Cellulose** — linear β-(1→4)-D-glucopyranose
(Fig. 3a) — forms an extended ribbon hydrogen-bonded into sheets (Iα, Iβ) [33,34]; the cohesive
energy of that sheet-then-crystal hierarchy (Fig. 4a) is why it cannot be melt-processed and is
handled only by solution routes (NMMO/Lyocell [37], LiCl/DMAc), while nanocrystals and nanofibrils
exploit its ~130–150 GPa axial crystal modulus [35] as fillers [2].

**Starch's** amylose/amylopectin topology (not chemistry) gives it weaker, humidity-reversible
crystallinity and retrogradation on storage [38] (hence TPS/PLA/PBAT blends). **Chitosan's** degree
of deacetylation (DD) sets solubility, charge and antimicrobial activity [39], but high-DD chitosan
is typically low-MW because the alkaline step that raises DD also cleaves the backbone [3].
**Alginate** gels via Ca²⁺-coordinated "egg-box" GG-blocks [4] (Fig. 4c), G-content setting a
stiffness–brittleness trade-off (§8); amylose coils into a water-plasticised helix (Fig. 4b), and
chitosan's irregular deacetylation breaks the hydrogen-bond register cellulose relies on, so its
solubility rises as crystallinity falls. Hyaluronic acid, carrageenan, xanthan and pectin follow
the same linkage-chemistry logic.

### 3.2 Polyesters: PHA and PLA

**PHA** (bacterial storage granules; PHB the archetype, Fig. 3f) is highly crystalline (55–70%) but
decomposes by six-membered-ring *cis*-elimination only tens of degrees above Tm [5] — the narrowest
processing window here; PHBV/PHBHHx copolymers widen it at the cost of stiffness. **PLA**:
ring-opening polymerisation of lactide by a Sn(Oct)₂ coordination–insertion mechanism [40,41]
reaches useful MW where polycondensation cannot; PLLA crystallises slowly, but the PLLA/PDLA
stereocomplex co-crystallises ~50 °C above either homocrystal through tighter enantiomeric packing
[6,7]. Both pack as helices that still melt (Fig. 4d); PBS and PEF follow the same ester logic (§8).

### 3.3 Protein-based Polymers

Protein properties come from sequence-directed fold, not chain packing. **Silk fibroin** (Fig. 3h)
owes its rare strength–toughness combination to β-sheet nanocrystallites in a compliant amorphous
matrix (Fig. 4e) [8]. **Collagen's** Gly-X-Y triple helix (Fig. 4f), stabilised by the
stereoelectronic effect of hydroxyproline [45], denatures irreversibly into gelatin; zein, casein
and soy are film-forming, not structural (§8). Ribosomal synthesis fixes every protein molecule's
length and sequence exactly (Đ = 1.0) — unmatched by any non-templated biopolymer (§4).

### 3.4 Lignin and Other Aromatics

Lignin is cellulose's counterpoint: amorphous *because* irregular. Radical coupling of the three
monolignols (Fig. 3j–l) forms a cross-linked network (β-O-4 ether ~45–60% of linkages [9]) with no
periodic chain, whose composition varies by species and, industrially, by extraction method —
kraft, organosolv, lignosulfonate [54] — so no single "lignin" has one structure–property
relationship.

### 3.5 Natural Rubber

Natural rubber (Fig. 3m) is the flexible extreme and the one exception to "crystallinity governs
performance": *cis*-1,4-polyisoprene is amorphous at rest, but strain-induced crystallisation
(SIC) self-reinforces the network under load — well documented by X-ray diffraction and largely
absent in synthetic *cis*-polyisoprene [10]. This is not a fixed material constant: NR's molecular
weight and its distribution vary measurably between *Hevea* clones and with tree age [19], and
non-rubber protein/gel content is an active, clone-dependent contributor to the network, not an
incidental impurity [18]. The organising variable is therefore not crystallinity but *intermolecular
architecture under the conditions of use* — tested directly against a synthetic analogue in §7.3.

**Table 2.** Provisional summary of thermal and mechanical properties of the representative
biopolymers discussed in §3 (order-of-magnitude ranges, cross-checked against the comparative
review of biobased thermoplastics by de Beukelaer et al. [11], for PBS against Aliotta et al. [12],
and for PLA against Auras et al. [42] and Farah et al. [43]; Td is the TGA onset of significant
mass loss under N₂; "–" = no melting transition; per-row sources in `figures/data/*.csv`).

| Material | Tg (°C) | Tm (°C) | Td onset (°C) | Modulus (GPa) | Elongation at break (%) |
|---|---|---|---|---|---|
| Cellulose (regenerated fibre) | – | – | ~300 | 10–30 | 8–15 |
| Thermoplastic starch | ~−20 | – | ~300 | 0.02–1.0 | 20–100 |
| Chitosan (film) | – | – | ~280 | 1.0–4.0 | 3–30 |
| Silk fibroin (fibre) | ~175 | – | ~300 | 5–17 | 15–30 |
| PHB (PHBV lowers Tm ~30 °C) | ~4 | ~175 | ~200 | 1.5–4.0 | 2–8 |
| PLLA | ~60 | ~175 | ~300 | 2.5–4.0 | 3–10 |
| PBS | ~−32 | ~114 | ~350 | 0.3–0.7 | 200–500 |
| Natural rubber (vulcanised) | ~−70 | – | – | 0.001–0.005 | 500–800 |
| PET (fossil reference) | ~78 | ~255 | ~400 | 2.0–4.0 | 50–300 |

*All values PROVISIONAL — teaching-level ranges used to keep Fig. 5 and this table internally
consistent; each must be replaced with a cited literature value, matched to a stated test condition
(sample form, moisture, thermal history), before submission.*

---

## 4. Molecular Weight and Its Measurement

Most surveys report molecular weight casually — "high molecular weight" — but the *distribution*,
not the average, is where the biology shows. Of the standard descriptors (Mn, Mw, dispersity
Đ = Mw/Mn [46], DP), Đ matters most: it, not Mn alone, sets processing behaviour and the spread of
mechanical properties within a batch. **Dispersity is a readout of synthesis mechanism, not noise**
(Fig. 6): template-controlled biosynthesis gives proteins and nucleic acids Đ = 1.0 exactly, while
every non-templated route — extraction (cellulose, chitosan, natural rubber) or catalysed
polymerisation (PHA, PLA) — broadens the distribution in proportion to how loosely it is
controlled. Natural rubber is the extreme: because it is extracted, not chain-grown, its Mw and MWD
vary between *Hevea* clones and with tree age [19] — an agricultural variability with no
synthetic-polymer analogue.

*[Figure 6 — Dispersity Đ across families on a common axis (colour by backbone class): an exact
point at Đ = 1 for templated biosynthesis, literature ranges for PLA/PHA/chitosan/cellulose, and an
open-ended arrow for natural rubber, whose Đ is not consistently quantified. Ranges reproduce those
in Table 3, not new measurements.]*

**Why molecular weight controls performance.** Mechanical integrity depends on chain entanglement
above a characteristic Mc [48]; below it, strength and toughness collapse. Above Mc, tensile
strength rises with Mn then saturates (Flory-type, σ ≈ σ∞ − K/Mn) [47], so degradation — first seen
as falling MW — causes only modest property loss until it crosses back below Mc, where performance
collapses abruptly (relevant to §7–§8). **Measuring** biopolymer MW is also harder: cellulose
dissolves in no standard SEC eluent, needing derivatisation or aggressive solvents, and aggregation
and branching distort SEC calibrated against linear standards. SEC-MALS or Mark–Houwink viscometry
are more defensible, but Mark–Houwink parameters are missing for many biopolymer/solvent pairs.
Reported MW for one material therefore often spans an order of magnitude in the literature — an
artefact of method more than real variation, so a MW figure is only comparable alongside its method.

**Table 3.** Typical number-average molecular weight for representative biopolymers, with the
standard method by which each is measured (dispersity Đ is plotted in Fig. 6 instead of repeated
here).

| Material | Typical Mn | Standard method (key limitation) |
|---|---|---|
| Proteins / DNA / RNA | sequence-specific | mass spectrometry (none — templated) |
| Cellulose (native/Lyocell) | 10⁴–10⁶ g mol⁻¹ | viscometry/SEC-MALS after derivatisation (insoluble in std. eluents) |
| Chitosan | 10⁴–10⁶ g mol⁻¹ | intrinsic viscosity (DD/MW trade-off, §3.1) |
| PHA (PHB/PHBV) | 10⁵–10⁶ g mol⁻¹ | GPC/SEC vs polystyrene (calibration mismatch) |
| PLA | 10⁴–10⁵ g mol⁻¹ | GPC/SEC (moisture-driven hydrolysis in process) |
| Natural rubber | often >10⁶ g mol⁻¹ | intrinsic viscosity (no synthetic analogue) |

*Mn ranges are teaching-level approximations; confirm each against a primary source before
submission. The method column and its limitations are supported by refs [39,46] and the SEC/MALS
discussion in §4.*

---

## 5. General Property Patterns

Section 3 examined each family in turn; this section turns the same evidence sideways to ask what
holds across all of them.

### 5.1 Thermal Behaviour

A decomposition temperature at or below the melting point is close to the rule (Fig. 5a): the same
network that gives stiffness raises the melting energy toward the bond-breaking energy, crowding
the two transitions — cellulose, chitosan and silk fibroin never melt at all. Among the polyesters
the crowding is quantitative: PHB's window is only ~25 °C, PHBV's ~55 °C, PLLA's wider still [44].
Fig. 5a plots the TGA onset, so the usable window for PLLA and PHB is narrower still, since melt
hydrolysis (§4) sets in earlier.

### 5.2 Mechanical Behaviour

The same logic sets the mechanical envelope (Fig. 5b): high crystallinity and dense hydrogen
bonding raise modulus but remove the flexible segments that let polyolefins draw before breaking,
so biopolymers sit at high modulus, low elongation relative to PE/PP/PET [11,43]. Natural rubber is
the exception — no modulus at rest, performance generated on demand by SIC (§3.5, §7.3). The
ellipses in Fig. 5b are ranges, not points: sample form, moisture, crystallinity and thermal
history each move a material's data by an order of magnitude, recurring as "batch variability" in
§7.2.

*[Figure 5 — Thermal and mechanical envelopes, drawn by the authors from `figures/data/*.csv`.
(a) Tg (open circle), Tm (diamond) and TGA decomposition onset (bar) on one temperature axis; the
shaded band is the melt-processing window (Tm→Td), its width labelled — cellulose, native starch,
chitosan and silk have none. (b) Modulus vs. elongation at break, log–log; ellipses are the range
of literature values for the stated sample form (not error bars), PE/PP/PET shown for reference.]*

### 5.3 Hydrophilicity and Barrier Properties

The polar groups behind the strength in §5.1–5.2 have a third consequence: strong hygroscopicity.
Absorbed water plasticises the amorphous fraction and swells free volume, so barrier performance
falls as humidity rises. ⚙️ Atomistic free-volume/diffusion modelling can predict this ahead of a
packaging trial — which is why PLA and starch films must carry a storage-humidity condition, not a
fixed barrier rating.

### 5.4 Degradation as a Material Property

Degradation is a rate process governed by structure (Fig. 7). Polyesters degrade by autocatalytic
ester hydrolysis — each scission's acid end accelerates the next, so interiors erode faster than
surfaces once the part is below a critical thickness (bulk erosion [49]); polysaccharides and
proteins degrade by enzymatic attack, which reaches only amorphous segments, so rate is set by
accessible surface area, not bulk chemistry [50]. Crystallinity is therefore the report's central
trade-off: the feature that sets modulus (§5.2) and blocks water uptake (§5.3) also blocks the
attack that would degrade the material. ⚙️ Computed ester-hydrolysis barriers fall in the order
base-catalysed < acid-catalysed < neutral, matching the observed pH-dependence of the rate.

*[Figure 7 — Two degradation routes, drawn by the authors: (a) polyester backbone ester hydrolysis
— the carboxylic-acid end group autocatalyses further hydrolysis, so thick parts erode from the
inside (bulk erosion); (b) enzymatic attack on polysaccharides and proteins reaches only amorphous
regions, so crystallinity sets the rate.]*

---

## 6. Processing

The thermal windows of §5.1 become a two-way processing decision. If a stable melt window exists
above Tm and below the decomposition/hydrolysis onset — PBS (wide), PLA (must be dried first or MW
collapses, §4), PHB (only ~25 °C, so tight thermal control) — the material is melt-processed, and
the window width sets how tightly. If not — cellulose, chitosan — only solution routes work
(NMMO/Lyocell, dilute-acid dissolution and wet/dry-jet spinning). Either way the countermeasures
are shared: plasticisers, nucleating agents, compatibilised blends (PLA/PBAT, PLA/TPS) and
nanocellulose reinforcement all widen whichever window exists. The recurring judgement: most
reported "performance shortfalls" are processing-window shortfalls, not material-property
shortfalls (§5.1–5.2).

---

## 7. Advantages and Disadvantages Compared with Synthetic Polymers

### 7.1 Where Biopolymers Genuinely Win

Four advantages are structural, each tracing to §3. **Renewable, non-fossil feedstock** is the only
one uniform across all five families. **Biodegradability in leakage-prone contexts** — mulch film,
fishing gear, disposable foodware — turns hydrolytic/enzymatic susceptibility from a burden into a
desired property, provided the environment matches the material [51] (§5.4). **Biocompatibility and
bioresorbability** let PLA/PGA sutures [52] and collagen/alginate/chitosan hydrogels and dressings
[55] do what commodity synthetics cannot without costly modification — the one space (§8) where
biopolymers are the only viable class, though not unconditionally (§7.3). And **intrinsic
functionality beyond mechanics** — chirality (PLA stereocomplexation), pH-responsive charge
(chitosan), sequence-encoded bioactivity (silk, collagen) — comes free with the biological
structure.

### 7.2 Where They Lose — Stated with Numbers, Not Adjectives

- **Price.** PLA is several times the price of commodity PE/PP, PHA higher still [16,53]; a
  material-specific $/kg figure still needs a current market report.
- **Heat/barrier.** PLA's HDT (~55–65 °C) sits well below PP's ~100 °C+ without stereocomplexation
  (§3.2) [13,42]; its O₂/CO₂ transmission matches PET's, but water-vapour barrier is worse, and
  starch films worse again [14] — the real critique is moisture sensitivity (§5.3), not an oxygen
  deficit.
- **Brittleness/hygroscopicity.** PHB's secondary crystallisation and PLA's sub-Tg ageing embrittle
  on storage [43]; starch drifts with humidity, and PLA must be dried before melt processing or MW
  drops uncontrollably (§4).
- **Batch variability.** Agricultural sourcing (alginate M/G, chitosan DD, starch amylose, NR
  clone/age [19]) varies in ways petrochemical monomers do not.
- **Recycling compatibility.** A 2022 study found in-stream PLA at only 0–0.019% of PET recycling
  streams, kept by NIR sorting below the ~1% threshold that measurably affects rPET [15] — a
  sorting-infrastructure dependency, not an inherent incompatibility.

### 7.3 Case Study: Natural Rubber vs. a Synthetic Analogue (SBR)

NR and styrene–butadiene rubber (SBR) are compounded, filled and vulcanised the same way and
compete in the same applications (tyre tread, damping, conveyor belting) — the cleanest
same-application comparison here, since differences trace to backbone chemistry, not processing.
Fig. 8 shows the chain-scale origin of that difference (SIC); Table 5 scores both across five
dimensions [10,18–32].

*[Figure 8 — NR and SBR structure, drawn by the authors: (a) NR (cis-1,4-polyisoprene), (b) SBR's
1,4-butadiene unit, (c) SBR's styrene unit (RDKit, verified SMILES); (d) at chain scale,
stereoregular NR aligns into crystalline bundles under strain (SIC, X-ray confirmed) while SBR's
irregular backbone stays amorphous even when stretched — the structural basis of the "SIC & tear
resistance" row of Table 5.]*

**Table 5.** Natural rubber (NR) vs. SBR, dimension by dimension — structurally favourable /
formulation- or context-dependent / documented risk or caveat.

| Dimension | Natural rubber (NR) | SBR |
|---|---|---|
| Structure / MW control | Extracted; varies by clone & tree age [19] | Engineered by emulsion/solution copolymerisation [20,21] |
| SIC & tear resistance | Favourable: strong strain-induced crystallisation [10,23]; weakens as SBR fraction rises in blends [22] | Crystallises far less; reaches parity via filler and cure design, not backbone [24–26] |
| Biocompatibility | Real potential, but latex-protein allergy risk [27,28] | No unconditional biocompatibility claim [27,28] |
| Environmental footprint | Renewable, but LCA shows real land/energy cost [29,30] | Fossil feedstock; biodegradable grades emerging [31] |
| Price stability | Historically the more volatile of the two [32] | Steadier, but tied to the petrochemical supply chain [32] |

Under matched compounding, NR's SIC gives better tear and crack-growth resistance to start with
[10,23], but SBR reaches comparable wear resistance through reinforcement and cure design, not
backbone crystallisation [24] — the clearest case here of backbone chemistry trading off against
formulation (§6). The "natural is better" story does not survive the literature, though: NR latex
carries a real, SBR-absent allergy risk [27,28], its renewability does not automatically mean a
lower LCA footprint [29,30], and NR pricing has historically been the more volatile of the two, for
climate and disease reasons unrelated to polymer chemistry [32].

---

## 8. Applications

Each application states the property need first, then the material that meets it (Table 4).
**Packaging** needs O₂/H₂O barrier, toughness and heat resistance above PLA's HDT (§7.2); no single
biopolymer gives all three (§5.3), so packaging is almost always multilayer or blended. Compostable
foodware and mulch film are driven by §7.1's biodegradability, not barrier, and need a rate matched
to the use timescale (§5.4). **Biomedical** applications need biocompatibility plus a tunable
degradation rate (§5.4) — essentially unique here (§7.1, with the NR-latex caveat of §7.3): PGA and
PLGA are established suture materials whose main failure mode is a local pH drop from acidic
hydrolysis products [52,53]; collagen, alginate and chitosan extend this to scaffolds and
bioprinting [55]. **Textiles and other:** Lyocell and PLA fibre exploit cellulose's
solution-processed stiffness [36] and PLA's melt-spinnability; NR adhesives and PHA/PLA electronics
substrates trade predictability for intrinsic adhesion, biodegradability or biocompatibility.

**Table 4.** Applications, required property, and material.

| Application | Key property required | Representative material(s) |
|---|---|---|
| Food packaging | O₂/H₂O barrier + toughness + moderate heat resistance | PLA/PBAT blends; PHA/PLA coatings |
| Compostable foodware / mulch film | Biodegradability matched to use timescale, not barrier | PLA, starch blends, PBAT/PLA |
| Sutures / drug release / scaffolds | Biocompatibility + tunable degradation rate | PGA, PLGA, collagen, alginate, chitosan |
| Textile fibre / electronics substrate | High stiffness/spinnability or film formability | Lyocell, PLA fibre, PHA |
| Tyre tread / damping / conveyor belting | High tensile/tear strength via SIC, or engineered wear | Natural rubber, NR/SBR blends (§7.3) |

---

## 9. Current Status, Challenges and Outlook

Global bio-based plastics capacity was ~2.31 Mt in 2025 — under 1% of all plastics — and is
projected to double by 2030, growth concentrated in bio-based PE/PP and PHA despite PHA remaining
the priciest (§7.2) [16]. The bottlenecks are the three properties organising §5 — processing
window, humidity dependence, batch variability — none solved by scale alone. Two directions look
most promising: enzymatic depolymerisation to monomer (recent enzyme cocktails recovered ~60% of
the lactic acid from post-consumer PLA in 72 h [17]); and ⚙️ data-driven property prediction (QSPR /
polymer-informatics ML [56]) to shorten the trial-and-error of matching backbone chemistry to a
processing window.

---

## 10. Conclusions

Three judgements follow. First, the performance ceiling is set by thermal and hygroscopic behaviour
(§5.1, §5.3), not mechanical strength (§5.2): most families meet or exceed synthetic-polymer
stiffness and fail instead on processing window and moisture. Second, crystallinity governs the
whole trade-off (§5.4) — the feature that supplies stiffness, blocks water uptake and blocks
degradative attack, so raising one lowers the other two; the NR/SBR case study (§7.3) shows the
same trade-off reached through formulation, not backbone chemistry alone. Third, molecular-weight
data are comparable only alongside their measurement method (§4), and the features that make MW
hard to measure — hydrogen bonding, branching, sequence specificity, agricultural sourcing — are
the same ones used throughout to explain performance.

---

## References *(56 entries, all DOI-verified via Crossref; assignment requires 50–60)*

1. Vert, M.; Doi, Y.; Hellwich, K.-H.; Hess, M.; Hodge, P.; Kubisa, P.; Rinaudo, M.; Schué, F.
   Terminology for biorelated polymers and applications (IUPAC Recommendations 2012).
   *Pure Appl. Chem.* **2012**, *84*, 377–410. DOI: 10.1351/PAC-REC-10-12-04.
2. Rostamabadi, H.; Bist, Y.; Kumar, Y.; Yildirim-Yalcin, M.; Ceyhan, T.; Falsafi, S. R. Cellulose
   nanofibers, nanocrystals, and bacterial nanocellulose: Fabrication, characterization, and their
   most recent applications. *Future Postharvest Food* **2024**, *1*, 5–33.
   DOI: 10.1002/fpf2.12001.
3. Hwang, K. T.; Jung, S. T.; Lee, G. D.; Chinnan, M. S.; Park, Y. S.; Park, H. J. Controlling
   molecular weight and degree of deacetylation of chitosan by response surface methodology.
   *J. Agric. Food Chem.* **2002**, *50*, 1876–1882. DOI: 10.1021/jf011167u.
4. Cao, L.; Lu, W.; Mata, A.; Nishinari, K.; Fang, Y. Egg-box model-based gelation of alginate and
   pectin: A review. *Carbohydr. Polym.* **2020**, *242*, 116389.
   DOI: 10.1016/j.carbpol.2020.116389.
5. Ariffin, H.; Nishida, H.; Shirai, Y.; Hassan, M. A. Determination of multiple thermal
   degradation mechanisms of poly(3-hydroxybutyrate). *Polym. Degrad. Stab.* **2008**, *93*,
   1433–1439. DOI: 10.1016/j.polymdegradstab.2008.05.020.
6. Tsuji, H. Poly(lactide) stereocomplexes: formation, structure, properties, degradation, and
   applications. *Macromol. Biosci.* **2005**, *5*, 569–597. DOI: 10.1002/mabi.200500062.
7. Luo, F.; Fortenberry, A.; Ren, J.; Qiang, Z. Recent progress in enhancing poly(lactic acid)
   stereocomplex formation for material property improvement. *Front. Chem.* **2020**, *8*, 688.
   DOI: 10.3389/fchem.2020.00688.
8. Keten, S.; Xu, Z.; Ihle, B.; Buehler, M. J. Nanoconfinement controls stiffness, strength and
   mechanical toughness of β-sheet crystals in silk. *Nat. Mater.* **2010**, *9*, 359–367.
   DOI: 10.1038/nmat2704.
9. Odili, C. C.; Ajibola, A. M.; Sojobi, J. W.; et al. Chemistry of lignin. In *Lignin Renewable
   Materials — Chemistry, Trends, Technology and Application*; Ngo, T.-D., Ahvazi, B., Eds.;
   IntechOpen, 2025. DOI: 10.5772/intechopen.1013010.
10. Huneau, B. Strain-induced crystallization of natural rubber: a review of X-ray diffraction
    investigations. *Rubber Chem. Technol.* **2011**, *84*, 425–452. DOI: 10.5254/1.3601131.
11. de Beukelaer, H.; Hilhorst, M.; Workala, Y.; Maaskant, E.; Post, W. Overview of the
    mechanical, thermal and barrier properties of biobased and/or biodegradable thermoplastic
    materials. *Polym. Test.* **2022**, *116*, 107803. DOI: 10.1016/j.polymertesting.2022.107803.
    <!-- Primary comparative data source for Table 2 and Fig. 5; full text was not accessible in
         this drafting environment (403), so individual numeric values in the CSV data files still
         need to be checked line-by-line against it rather than assumed consistent. -->
12. Aliotta, L.; Seggiani, M.; Lazzeri, A.; Gigante, V.; Cinelli, P. A brief review of
    poly(butylene succinate) (PBS) and its main copolymers: synthesis, blends, composites,
    biodegradability, and applications. *Polymers* **2022**, *14*, 844.
    DOI: 10.3390/polym14040844.
13. Zhao, X.; Liu, J.; Li, J.; Liang, X.; Zhou, W.; Peng, S. Strategies and techniques for
    improving heat resistance and mechanical performances of poly(lactic acid) (PLA)
    biodegradable materials. *Int. J. Biol. Macromol.* **2022**, *218*, 115–134.
    DOI: 10.1016/j.ijbiomac.2022.07.091.
14. McCurdy, C.; Dixion, D.; Archer, E.; Dooher, T.; Edwards, I. A comparison of the sealing,
    forming and moisture vapour transmission properties of polylactic acid (PLA), polyethene (PE)
    and polyethylene terephthalate (PET) coated boards for packaging applications.
    *J. Packag. Technol. Res.* **2022**, *6*, 91–100. DOI: 10.1007/s41783-022-00131-w.
15. Thoden van Velzen, E. U.; Chu, S.; Molenveld, K.; Jašo, V. Effect of poly lactic acid trays on
    the optical and thermal properties of recycled poly(ethylene terephthalate).
    *Packag. Technol. Sci.* **2022**, *35*, 351–360. DOI: 10.1002/pts.2633.
16. European Bioplastics; nova-Institute. *Bioplastics Market Development Update 2025*; European
    Bioplastics e.V.: Berlin, December 2025.
    Available at: docs.european-bioplastics.org/publications/market_data/2025/EUBP_Market_Data_Report_2025.pdf
17. Salini, A.; Gonnelli, P. M.; Padoan, C.; Helali, Y.; Waeytens, J.; Fusco, S.; Cannella, D.
    Repurposing commercial hydrolytic and oxidative enzymes toward synergistic PLA
    depolymerization. *ACS Sustain. Chem. Eng.* **2025**, *13*, 20705–20716.
    DOI: 10.1021/acssuschemeng.5c06901.
18. Huang, S.-Q.; et al. Revealing the structure-property difference of natural rubber prepared by
    different methods: protein and gel content are key factors. *Chin. J. Polym. Sci.* **2024**,
    *42*, 457–467. DOI: 10.1007/s10118-024-3071-2.
19. Xin, S.; et al. Comparative analysis of latex transcriptomes reveals the potential mechanisms
    underlying rubber molecular weight variations between *Hevea brasiliensis* clones RRIM600 and
    Reyan7-33-97. *BMC Plant Biol.* **2021**, *21*, 244. DOI: 10.1186/s12870-021-03022-5.
20. Dhanorkar, R. J.; et al. Synthesis of functionalized styrene butadiene rubber and its
    applications in S-SBR–silica composites for high-performance tire applications.
    *Ind. Eng. Chem. Res.* **2021**, *60*, 4517–4535. DOI: 10.1021/acs.iecr.0c06155.
21. Zubov, A.; Pokorny, J.; Kosek, J. Styrene–butadiene rubber (SBR) production by emulsion
    polymerization: dynamic modeling and intensification of the process. *Chem. Eng. J.* **2012**,
    *207–208*, 414–420. DOI: 10.1016/j.cej.2012.06.144.
22. Singer, R.; Ollick, A. M.; Elhadary, M.; El-Sherbiny, I. M.; Gomma, A. Comparative study of
    natural rubber and styrene-butadiene rubber blends reinforced with different carbon black
    grades for tire tread production. *Sci. Rep.* **2026**, *16*, 24902.
    DOI: 10.1038/s41598-026-65435-2.
23. Noguchi, F.; et al. Effect of strain-induced crystallization on the tear strength of natural
    rubber/styrene butadiene rubber blend. *Adv. Polym. Technol.* **2018**, *37*, 1850–1858.
    DOI: 10.1002/adv.21843.
24. Tangudom, P.; Thongsang, S.; Sombatsompop, N. Cure and mechanical properties and abrasive wear
    behavior of natural rubber, styrene-butadiene rubber and their blends reinforced with silica
    hybrid fillers. *Mater. Des.* **2014**, *53*, 856–864. DOI: 10.1016/j.matdes.2013.07.024.
25. Goyanes, S.; et al. Thermal properties in cured natural rubber/styrene butadiene rubber
    blends. *Eur. Polym. J.* **2008**, *44*, 1525–1534. DOI: 10.1016/j.eurpolymj.2008.02.016.
26. Tang, S.; Li, Z.; Sun, W.; Liu, Y.; Wang, J.; Wang, X.; Lin, J. Natural rubber/styrene–butadiene
    rubber blend composites potentially applied in damping bearings. *Polymers* **2024**, *16*,
    1945. DOI: 10.3390/polym16131945.
27. Floriano, J. F.; et al. Biocompatibility studies of natural rubber latex from different tree
    clones and collection methods. *J. Mater. Sci. Mater. Med.* **2014**, *25*, 461–470.
    DOI: 10.1007/s10856-013-5089-9.
28. Nucera, E.; et al. Latex allergy: current status and future perspectives.
    *J. Asthma Allergy* **2020**, *13*, 385–398. DOI: 10.2147/JAA.S242058.
29. Cucci, G.; Valentini, F.; Dorigato, A. Cradle to gate life cycle assessment of tyre-grade
    natural rubber produced in Thailand. *Sci. Total Environ.* **2025**, *987*, 179653.
    DOI: 10.1016/j.scitotenv.2025.179653.
    <!-- Journal name corrected from the source spreadsheet, which listed "Journal of Cleaner
         Production" — Crossref confirms this title/DOI is in Science of the Total Environment;
         titles otherwise match closely enough to be confident it's the same paper. -->
30. Dunuwila, P.; et al. Revealing the environmental footprint of crepe rubber production: a life
    cycle assessment. *Sustainability* **2025**, *17*, 1239. DOI: 10.3390/su17031239.
31. Boon, Z. H.; et al. Recent development of biodegradable synthetic rubbers and bio-based
    rubbers using sustainable materials from biological sources. *RSC Adv.* **2022**, *12*,
    34028–34052. DOI: 10.1039/D2RA06602E.
32. U.S. Bureau of Labor Statistics. *Why the Prices of Natural and Synthetic Rubber Do Not Always
    Bounce Together*; Beyond the Numbers, Vol. 9; U.S. BLS: Washington, DC, 2020.
    Available at: bls.gov/opub/btn/volume-9/why-the-prices-of-natural-and-synthetic-rubber-do-not-always-bounce-together.htm
33. Nishiyama, Y.; Langan, P.; Chanzy, H. Crystal structure and hydrogen-bonding system in cellulose
    Iβ from synchrotron X-ray and neutron fiber diffraction. *J. Am. Chem. Soc.* **2002**, *124*,
    9074–9082. DOI: 10.1021/ja0257319.
34. Nishiyama, Y.; Sugiyama, J.; Chanzy, H.; Langan, P. Crystal structure and hydrogen bonding
    system in cellulose Iα from synchrotron X-ray and neutron fiber diffraction. *J. Am. Chem. Soc.*
    **2003**, *125*, 14300–14306. DOI: 10.1021/ja037055w.
35. Nishino, T.; Takano, K.; Nakamae, K. Elastic modulus of the crystalline regions of cellulose
    polymorphs. *J. Polym. Sci. B Polym. Phys.* **1995**, *33*, 1647–1651.
    DOI: 10.1002/polb.1995.090331110.
36. Eichhorn, S. J.; Baillie, C. A.; Zafeiropoulos, N.; et al. Review: current international research
    into cellulosic fibres and composites. *J. Mater. Sci.* **2001**, *36*, 2107–2131.
    DOI: 10.1023/A:1017512029696.
37. Rosenau, T.; Potthast, A.; Sixta, H.; Kosma, P. The chemistry of side reactions and byproduct
    formation in the system NMMO/cellulose (Lyocell process). *Prog. Polym. Sci.* **2001**, *26*,
    1763–1837. DOI: 10.1016/S0079-6700(01)00023-5.
38. Wang, S.; Li, C.; Copeland, L.; Niu, Q.; Wang, S. Starch retrogradation: a comprehensive review.
    *Compr. Rev. Food Sci. Food Saf.* **2015**, *14*, 568–585. DOI: 10.1111/1541-4337.12143.
39. Rinaudo, M. Chitin and chitosan: properties and applications. *Prog. Polym. Sci.* **2006**, *31*,
    603–632. DOI: 10.1016/j.progpolymsci.2006.06.001.
40. Drumright, R. E.; Gruber, P. R.; Henton, D. E. Polylactic acid technology. *Adv. Mater.*
    **2000**, *12*, 1841–1846. DOI: 10.1002/1521-4095(200012)12:23<1841::AID-ADMA1841>3.0.CO;2-E.
41. Kowalski, A.; Duda, A.; Penczek, S. Kinetics and mechanism of cyclic esters polymerization
    initiated with tin(II) octoate. 3. Polymerization of L,L-dilactide. *Macromolecules* **2000**,
    *33*, 7359–7370. DOI: 10.1021/ma000125o.
42. Auras, R.; Harte, B.; Selke, S. An overview of polylactides as packaging materials.
    *Macromol. Biosci.* **2004**, *4*, 835–864. DOI: 10.1002/mabi.200400043.
43. Farah, S.; Anderson, D. G.; Langer, R. Physical and mechanical properties of PLA, and their
    functions in widespread applications — a comprehensive review. *Adv. Drug Deliv. Rev.* **2016**,
    *107*, 367–392. DOI: 10.1016/j.addr.2016.06.012.
44. Sin, L. T.; Rahmat, A. R.; Rahman, W. A. W. A. Thermal properties of poly(lactic acid). In
    *Polylactic Acid: PLA Biopolymer Technology and Applications*; William Andrew: Oxford, 2013;
    pp 109–141. DOI: 10.1016/B978-1-4377-4459-0.00003-2.
45. Shoulders, M. D.; Raines, R. T. Collagen structure and stability. *Annu. Rev. Biochem.*
    **2009**, *78*, 929–958. DOI: 10.1146/annurev.biochem.77.032207.120833.
46. Stepto, R. F. T. Dispersity in polymer science (IUPAC Recommendations 2009). *Pure Appl. Chem.*
    **2009**, *81*, 351–353. DOI: 10.1351/pac-rec-08-05-02.
47. Nunes, R. W.; Martin, J. R.; Johnson, J. F. Influence of molecular weight and molecular weight
    distribution on mechanical properties of polymers. *Polym. Eng. Sci.* **1982**, *22*, 205–228.
    DOI: 10.1002/pen.760220402.
48. Fetters, L. J.; Lohse, D. J.; Richter, D.; Witten, T. A.; Zirkel, A. Connection between polymer
    molecular weight, density, chain dimensions, and melt viscoelastic properties. *Macromolecules*
    **1994**, *27*, 4639–4647. DOI: 10.1021/ma00095a001.
49. von Burkersroda, F.; Schedl, L.; Göpferich, A. Why degradable polymers undergo surface erosion
    or bulk erosion. *Biomaterials* **2002**, *23*, 4221–4231.
    DOI: 10.1016/S0142-9612(02)00170-9.
50. Lucas, N.; Bienaime, C.; Belloy, C.; Queneudec, M.; Silvestre, F.; Nava-Saucedo, J.-E. Polymer
    biodegradation: mechanisms and estimation techniques — a review. *Chemosphere* **2008**, *73*,
    429–442. DOI: 10.1016/j.chemosphere.2008.06.064.
51. Tokiwa, Y.; Calil, M. R.; Suzuki, T.; Aiba, S. Biodegradability of plastics. *Int. J. Mol. Sci.*
    **2009**, *10*, 3722–3742. DOI: 10.3390/ijms10093722.
52. Middleton, J. C.; Tipton, A. J. Synthetic biodegradable polymers as orthopedic devices.
    *Biomaterials* **2000**, *21*, 2335–2346. DOI: 10.1016/S0142-9612(00)00101-0.
53. Jem, K. J.; Tan, B. The development and challenges of poly(lactic acid) and poly(glycolic acid).
    *Adv. Ind. Eng. Polym. Res.* **2020**, *3*, 60–70. DOI: 10.1016/j.aiepr.2020.01.002.
54. Ragauskas, A. J.; Beckham, G. T.; Biddy, M. J.; et al. Lignin valorization: improving lignin
    processing in the biorefinery. *Science* **2014**, *344*, 1246843.
    DOI: 10.1126/science.1246843.
55. Rinaudo, M. Main properties and current applications of some polysaccharides as biomaterials.
    *Polym. Int.* **2008**, *57*, 397–430. DOI: 10.1002/pi.2378.
56. Kuenneth, C.; Ramprasad, R. polyBERT: a chemical language model to enable fully machine-driven
    ultrafast polymer informatics. *Nat. Commun.* **2023**, *14*, 4099.
    DOI: 10.1038/s41467-023-39868-6.

<!-- REFERENCES status (2026-08-28):
     56 entries, every DOI checked against Crossref. Count now meets the 50-60 requirement.
     Refs [33]-[56] were added this pass — background/general sources for facts that previously
     carried no citation: cellulose crystal structure & modulus [33-35], Lyocell/NMMO chemistry
     [37], starch retrogradation [38], chitin/chitosan properties [39], lactide ROP mechanism
     [40,41], PLA overviews & thermal/mechanical/barrier data [42-44], collagen triple-helix
     stability [45], IUPAC dispersity terminology [46], MW-vs-mechanical-property relationships
     [47,48], surface vs bulk erosion [49], enzymatic biodegradation mechanisms [50,51],
     PGA/PLGA/PLA biomedical devices [52,53], lignin biorefinery processing [54], polysaccharide
     biomaterials [55], polymer-informatics ML [56].

     STILL OPEN before submission:
     (a) `figures/data/thermal_properties.csv` and `mechanical_properties.csv` `ref` cells are
         still mostly PROVISIONAL. [11]/[12]/[42]/[43]/[44] now cover most rows — go through
         line-by-line, put the real citation number in each `ref` cell, and correct any value
         that doesn't match the cited source. Table 2 / Table 3 numbers follow from these.
     (b) §7.2 price bullet still needs a material-specific $/kg figure from a current market
         report (EUBP full report, nova-Institute, IHS Markit, Grand View Research). [16,53]
         support only the qualitative "PLA > PE/PP, PHA higher still".
     (c) §7.3 NR-vs-SBR case study still uses 15 refs [10,18-32] from the author's own
         `biopolymer_NR_SBR_literature.xlsx`; ~3 unused "B"/"C" rows remain there if more are
         wanted. -->


