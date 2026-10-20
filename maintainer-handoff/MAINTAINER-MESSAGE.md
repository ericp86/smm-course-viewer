# Draft only — not sent

I recommend merging the existing 17 PRs (#7–#17 and #21–#26) individually using the prepared Option A procedure. No new production PR is needed for this workflow.

The complete 17-PR sequence was independently replayed. All 14 textual merge conflicts have documented, independently verified resolutions, followed by the required compatibility and artwork-loading safety patches.

- [Option A handoff package and merge instructions](https://github.com/ericp86/smm-course-viewer/tree/handoff/option-a-merge-package/maintainer-handoff)
- [Verified Option A testing branch](https://github.com/ericp86/smm-course-viewer/tree/test/option-a-final-verification)

The verified testing commit is `e14a6c1d5956b15cbfdaf00bd4bd1713a5dfaae9`, with application tree `c75546d5456ba655c7a1afa59ddc31dc80186347`.

Previously completed automated validation passed 35,559 primary, 5,392 artwork/custom-renderer and 576 lifecycle checks: **41,527 passed, zero failed or skipped**. All 192 formerly failing artwork-loading scenes recovered, and all 17,176 previously healthy drawing recordings stayed unchanged. These suites were not rerun for this documentation update.

The user reports **manual browser visual acceptance: PASS**. The complete collection of previously compiled test courses was visually inspected in the independently merged Option A viewer against approved enhanced integration (`138004b530435efe423d9ed7065093101645963f`). No differences were observed; all inspected rendering features, positions, rotations, artwork and layering appeared correct. This is user-reported acceptance, not exhaustive course coverage, pixel-perfect automated comparison or completed failure-injection browser testing.

The merge recipe and resolutions apply to the pinned upstream and PR references. If those references or merge contexts change, stop and revalidate the affected steps; future merges are not guaranteed conflict-free.

If you prefer one coordinated integration PR, it can be prepared instead. The existing PRs remain open, and no coordinated replacement or PR closure is requested by this message.
