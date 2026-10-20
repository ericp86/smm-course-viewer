# Validation evidence and scope

## Completed independent Option A verification

A new disposable checkout started at upstream f807f0247bac4c553288700bf7c08dd8502eead0. All 17 actual merges were performed in the documented order. Three were clean; fourteen had exactly the recorded conflicts. Every intermediate tree matched. Compatibility and the final safety patch then yielded c75546d5456ba655c7a1afa59ddc31dc80186347.

| Actual executed collection | Passed | Failed | Skipped |
|---|---:|---:|---:|
| Primary regressions | 35,559 | 0 | 0 |
| Supplemental artwork/custom-renderer checks | 5,392 | 0 | 0 |
| Loading lifecycle | 576 | 0 | 0 |
| Total | 41,527 | 0 | 0 |

All process statuses were zero; no cancellations. All 192 formerly failing artwork-loading mixed scenes recovered. Healthy comparisons: 3,160 pipe/wing + 13,056 all-object + 960 mixed = 17,176 unchanged. Repaired integration parity additionally covers all 1,152 primary mixed scenes and 576 lifecycle recordings.

Primary coverage includes Groups A/B/C/D0/D1/D2, final pipe-wing calibration, all-object comparisons, combined scenes, Unicode/parser, goals, cannons, tracks, coasters, lava, depth and rotation. Historical standalone controls remain part of the matrix; not every case is a separate assertion on every current branch.

Supplemental checks cover pending/failed/missing/successful atlases, actual supplied-theme identity, later ready invocations and independent custom artwork. Lifecycle checks cover cached failure, background-first atlas failure and simultaneous background/atlas failure. Later terrain draws, canvas state balances, and duplicate callbacks do not redraw scenes.

Nine JavaScript syntax checks, the 115-object parser smoke test, source/asset hashes, clean tree, all PR ancestors and diff checks also passed on the replayed checkout. No production or test expectations changed during that independent verification.

## Publication/package checks

The testing branch retains the exact replay commit and source tree. The publication check verifies ancestry, tree/file/asset hashes, guard patch identity, syntax/parser checks and clean state. It does not claim a newly repeated 41,527-case run or new browser testing.

The compact package retains exact original patches, intermediate trees and small result summaries. Full harness fixtures and raw logs remain in preserved original evidence rather than this Git documentation branch. They are required for a new full 41,527-case rerun. Node's existing test/test.js remains available in the application checkout.

The original offline replay and independent end-to-end replay already ran successfully. The portable packaging copies of replay-online.py/replay-offline.py are syntax/CLI reviewed; their patch/asset operations and tree outcomes are checked against that evidence. Their rewritten packaging entry points are not claimed as a newly executed full merge rehearsal.

After replay or cloning the browser branch:

```bash
python3 maintainer-handoff/verify-tree.py --checkout /absolute/path/to/new/application
# In the application checkout:
node --check draw/Draw.js
node test/test.js
git diff --check HEAD^ HEAD
git status --porcelain
```

## Test adapters and retained limitations

The old broken-atlas baseline was retained as a reproduction control. Recovery assertions now require scene completion, no invalid drawing, later terrain, balanced state and no duplicate render instead of matching the baseline exception. A historical healthy-geometry helper was corrected to mark its intended healthy images complete; its geometry assertions were unchanged, and explicit pending/failed tests remain. Those adapter changes preceded the independent run and are not new publication changes.

Player/type-69 xY versus yT remains a pre-existing issue with 192 separate expected-failure diagnostics; those are not hidden primary failures or skipped cases. Synthetic winged empty-Shelmet/Skewer combinations remain unresolved. Accepted coaster midpoint behavior is unchanged. Public metadata does not establish review approval, CI or branch protection. Browser visuals remain the next user check.
