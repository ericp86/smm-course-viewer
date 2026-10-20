# Final technical status

## Approved references

| Reference | Commit |
|---|---|
| Upstream master | f807f0247bac4c553288700bf7c08dd8502eead0 |
| Fork master | 848a7f4584fd69405ca745ac1c97a0f3ced175fa |
| Published compare/enhanced | 138004b530435efe423d9ed7065093101645963f |
| Independent Option A replay / testing branch | e14a6c1d5956b15cbfdaf00bd4bd1713a5dfaae9 |
| Original rehearsal compatibility commit | 392935f7f7ada15abb304058105f55d495580915 |

**Final Option A application tree:** c75546d5456ba655c7a1afa59ddc31dc80186347.

The actual independent replay started from pinned upstream and performed all 17 merges, not from the coordinated branch. Three merges were clean and fourteen required the supplied exact patches. Every intermediate tree matched. The compatibility layer and 19-line safety layer then produced the final tree.

The result contains all 17 pinned PR tips as ancestors, all 233 approved files and 173 PNGs, with no dirty/untracked files or conflict markers. Type-45 body calibration is supplied once by #21; compatibility supplies only the additional combined behavior; final artwork guards are supplied once by the last patch.

Actual fresh regression results on this independent replay: 35,559 primary + 5,392 artwork + 576 lifecycle = 41,527 passed, zero failed/skipped. All 192 previously failing artwork scenes recovered. The separate publication of this handoff does not represent a new full-suite run or browser sign-off.

Option A is technically ready with documented conflict resolutions on the pinned baseline. Complete the separate browser comparison before final visual sign-off. All 17 PRs were verified open at pinned tips; no claim is made about review approval, CI or live GitHub mergeability.

Retained limitations: upstream Player/type-69 xY versus yT typo (192 separate expected-failure diagnostics); unresolved synthetic winged empty-Shelmet/Skewer combinations; accepted skull-coaster curved midpoint behavior. No new surface-wing dispatch or speculative calibration was introduced.

Original rehearsal evidence, source patches, offline bundle and logs are preserved separately and unchanged. This is a compact copy-based handoff, not a replacement of the historical baseline evidence.
