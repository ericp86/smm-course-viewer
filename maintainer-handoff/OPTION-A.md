# Exact Option A merge procedure

Start from upstream `f807f0247bac4c553288700bf7c08dd8502eead0` in a new disposable repository. Fork master is only the documentation branch base. PRs #18–#20 are superseded and excluded. This sequence was actually replayed; it is not claimed globally optimal.

| Step | PR | Purpose | Source SHA | Expected merge tree |
|---|---|---|---|---|
| 1 | #26 | Decode big-endian UTF-16 course names without dropping non-ASCII code units or surrogate pairs. | `aea7027b12014b9a45ecdfd5254dc9e89f5e3f9d` | `dd9d80c0236b4ba9317eac3bdf6c8bdc5b5ba6aa` |
| 2 | #7 | Signed and fractional depth sorting; direction parsing; gates, Burners, signs and checkpoint rendering. | `dd8eefd6022f32e01eb47785b35490568b94e7e4` | `4ff1703fa0ea2726608fbfc32c405b49a233d92e` |
| 3 | #10 | Fractional track coordinates, sprite segments, curves and endpoint A/B mapping; artwork protection. | `ae69e2d237a7e7bcd3860da8ccc0dfd77449d730` | `8cf99cc0b4c3fe6b9125dd5c68d004d277f3f824` |
| 4 | #11 | Single attached skull versus four free skulls; linked curved-track placement; rail/coaster artwork protection. | `fcb4f3b39eb45f9a05ac569a36f765a701895655` | `c87e894796ae8a8fb716479d1baf7af6926170de` |
| 5 | #8 | Style/theme-specific goals and surrounding scenery; missing-goal, canvas-state and optional-image protection. | `73a990cc04d20f761f825da4a5063de04af62962` | `b43b5a08f967ce908e629bcdb04f5478d67a896c` |
| 6 | #12 | Castle-only foreground lava; background/object completion coordination and artwork readiness. | `b0a20faf0251fe4fd01ea6027e134d0b76190aa3` | `74ef84d8637438cd02e324bd58722d8d3e354252` |
| 7 | #9 | Cannon source crops, mounting angles and size-dependent centers; invalid-rotation guard. | `e5352e338974e7fa3b3fc18352baeb379c78c1de` | `de2e6f4ce0a5dc419d42726d35213b3fcc2749b2` |
| 8 | #13 | Surface orientation and flipping for Spiny, Buzzy Beetle and Spike Top. | `dce2654abbcc4d22cac98f00e95c296559ca4864` | `ebe854cab2780c2ea1a970a19a6bac55cc07139a` |
| 9 | #24 | Theme-dependent Buzzy Beetle/Fire Piranha colors without changing metadata. | `b4df66491d2f6ad853761cc44b5f7a0c90b34dd9` | `4f8512da7eed153928a1572b07e080dc0158c49f` |
| 10 | #14 | Empty Spiny/Buzzy Shelmet custom artwork and appropriate theme colors. | `16daacfc6041866c5ef8f9c34311b6818cfb29c3` | `120a5de8906bba6d94707a76e84e1bedba195f17` |
| 11 | #15 | Fire Bar variable lengths, unsigned rotation data and guarded sprite drawing. | `368aaa17eb8ecc19dcc6fced3c5efebd426786df` | `44656b51893f495f780d8e8b43cda8b2b281f5ea` |
| 12 | #16 | Wiggler body/head/flower composition and loaded custom Angry Wiggler body artwork. | `7ebfc4aeb919bccccf8e0a671b54f065bf21bc29` | `9566d088d6ec81e7e14517a8b7537d2e29350c56` |
| 13 | #17 | Custom P Switch sprites for M1/WU with atlas fallback; preserve P Doors. | `e5192068dfaea0ba6968a446c15425eafcfe2e6f` | `a3b813ee593a0b232c877f41f41c42a03f6dfd9f` |
| 14 | #22 | Custom Shoe/Stiletto artwork, bottom anchoring and aspect ratio with safe atlas fallback. | `f2bac6fabcf114d4cb700a6771dd62ddebba53cb` | `05076cd5b511db517d038ff66216b17479e2ce39` |
| 15 | #25 | Playing-card symbols on linked normal/P/key doors with safe image completion. | `7b99e2d24d71bccf47acd685c6364dc62d0d7d9d` | `2c1c0f4c36e9fa4dd5b71002a7ec5022780d39e7` |
| 16 | #21 | Pipe-attached enemy/item/coin placement, finalized offsets and foreground pipe occlusion. | `5feca7b5f7732538d69f999eebfacbeaafcaa58e` | `916e3e405555f34fe99379ca2fd6a4544943052f` |
| 17 | #23 | One/two wings, supported-object dispatch, game-style offsets and wing artwork readiness. | `7c9caa284b5381fd762c7da8f1fa46e076f4c201` | `fb67df2b91bbc56d391f82a9df9f2e8539991ea6` |

## Exact conflict resolutions

Clean merges: #26, #7, #24. All other merges conflict in Draw.js; #10 also conflicts in the parser and #16 in MonsterDraw. Each supplied patch applies to the Git-conflicted working files, not to an unrelated clean source file.

| Step / PR | Conflicted files and regions | Resolution file and intent |
|---|---|---|
| 3 / #10 | draw/Draw.js:156 _drawObjects; lib/SmmCourseViewer.js:291 _objectInterpreter | `merges/03-pr10/resolution.patch` — Combine #7 sign prepasses with #10 rail dispatch in the remaining-object pass; retain fractional track X/Y and preserve fractional signed Z from #7. |
| 4 / #11 | draw/Draw.js:511 _drawObjectFromTheme | `merges/04-pr11/resolution.patch` — Keep #11 skull-atlas guard and curved-track anchor adjustment before the existing #7 specialized rotation renderers; explicitly close both inserted blocks. |
| 5 / #8 | draw/Draw.js:44 constructor; draw/Draw.js:542 _drawObjects; draw/Draw.js:931 _drawObjectFromTheme | `merges/05-pr8/resolution.patch` — Union rail and goal-tape image initialization; keep goal scenery before sign/object passes, retain Castle-only bridge guard alongside rail dispatch; retain all specialized rotations and append disjoint goal renderers. |
| 6 / #12 | draw/Draw.js:593 _drawObjects | `merges/06-pr12/resolution.patch` — Use #12 background-readiness and render-once gate while retaining #8 goal scenery and #7 sign prepasses; preserve standalone #12 single foreground lava pass. |
| 7 / #9 | draw/Draw.js:982 _drawObjectFromTheme; draw/Draw.js:1445 _drawObjectFromTheme | `merges/07-pr9/resolution.patch` — Retain all existing goal/track/rotation paths and insert the disjoint cannon renderer with its size-dependent geometry and invalid-index guard; close each canvas draw/restore/return block explicitly. |
| 8 / #13 | draw/Draw.js:983 _drawObjectFromTheme | `merges/08-pr13/resolution.patch` — Retain existing disjoint goal/rotation cases and add #13 specialized surface renderer with its own readiness guard and subtype-driven sprite selection; no pipe coexistence redesign yet. |
| 10 / #14 | draw/Draw.js:44 constructor; draw/Draw.js:1022 _drawObjectFromTheme | `merges/10-pr14/resolution.patch` — Union Shelmet image registration with rails/tape; run the empty-Shelmet custom-art early return before ordinary surface enemy handling, retaining curved-track positioning and all other special cases. |
| 11 / #15 | draw/Draw.js:1016 _drawObjectFromTheme | `merges/11-pr15/resolution.patch` — Retain existing special cases and append the disjoint Fire Bar renderer, preserving its artwork guard, unsigned rotation decode and per-fireball save/restore. |
| 12 / #16 | draw/Draw.js:44 constructor; draw/Draw.js:62 constructor; draw/Draw.js:101 constructor; draw/Draw.js:706 _drawObjects; draw/Draw.js:1715 _drawObjectFromTheme; draw/MonsterDraw.js:367 MonsterDraw._defitions[52], adjacent [54] | `merges/12-pr16/resolution.patch` — Union all custom/rail/tape image initialization and readiness registration, keep background gate and three-argument style/theme extend call; replace only Wiggler definition with #16 composition and retain #7 Burner on/off definition. |
| 13 / #17 | draw/Draw.js:44 constructor; draw/Draw.js:728 _drawObjects; draw/Draw.js:1751 _drawObjectFromTheme; draw/Draw.js:1819 _drawObjectFromTheme | `merges/13-pr17/resolution.patch` — Append P Switch artwork registration without replacing other image families; retain common guarded completion/background gate; combine disjoint P Switch and Angry Wiggler sprite selection before the common paint call. |
| 14 / #22 | draw/Draw.js:44 constructor; draw/Draw.js:1749 _drawObjectFromTheme | `merges/14-pr22/resolution.patch` — Append Shoe/Stiletto image registration without replacing prior families; combine ready custom-shoe selection/fallback with Wiggler/P Switch selection and carry customShoe aspect-ratio flag into the common painter. |
| 15 / #25 | draw/Draw.js:44 constructor; draw/Draw.js:108 constructor | `merges/15-pr25/resolution.patch` — Union linked-door symbol images with all previously registered artwork; preserve custom sprite initialization and guarded shared completion. |
| 16 / #21 | draw/Draw.js:689 _drawObjects; draw/Draw.js:1116 _drawObjectFromTheme; draw/Draw.js:1127 _drawObjectFromTheme; draw/Draw.js:2403 _drawObjectFromTheme; draw/Draw.js:2516 _drawObjectFromTheme | `merges/16-pr21/resolution.patch` — Retain background gate, goal scenery, sign passes, tracks and Castle bridge filter while introducing attached-before-pipe dispatch. Union pipe and coaster readiness. Put calibrated pipe geometry and pipe-only surface bodies before existing specialized renderers; preserve theme-aware extension, Wiggler/Chain Chomp composition and door symbols with balanced outer rotation. |
| 17 / #23 | draw/Draw.js:1094 _drawObjectFromTheme; draw/Draw.js:2539 _drawObjectFromTheme | `merges/17-pr23/resolution.patch` — Keep all existing calibrated and specialized renderers plus PR23 generic atlas readiness, wing helper and calls. Preserve single-cell pipeRotation when adding post-body wing dispatch. Leave combination-specific pivot forwarding for separately identified compatibility patch. |

## Manual commands

Before starting, fetch and verify the exact upstream and PR heads in inventory.json. Require a clean checkout before every merge. Use ordinary merge commits; do not rebase/squash the source PRs or accept all of ours/theirs.

```bash
git merge --no-ff --no-commit FULL_PINNED_PR_SHA
# If conflicting, require exactly the recorded conflictFiles:
git diff --name-only --diff-filter=U
git apply --check /path/to/maintainer-handoff/merges/NN-prN/resolution.patch
git apply /path/to/maintainer-handoff/merges/NN-prN/resolution.patch
git add -- EXACT_CONFLICTED_FILES
git diff --cached --check
git commit -m "Merge PR #N with documented resolution"
git rev-parse HEAD^{tree}
# Require the table's tree after this step.
```

For clean merges omit the patch/add commands and commit the automatic merge. A later compatibility PR cannot eliminate these earlier textual conflicts.

## Compatibility and final safety

After step 17, apply compatibility-code.patch and provision the 28 exact PNGs listed in ASSETS.md. replay-online.py extracts only those artwork bytes from approved integration and verifies their hashes; it never copies complete renderer source methods.

Commit that layer and require tree `47a1034c8c15b6fa12f64cb4d988c5640c6c76bc`. Then:

```bash
git apply --check /path/to/maintainer-handoff/final-artwork-safety.patch
git apply --index /path/to/maintainer-handoff/final-artwork-safety.patch
git diff --cached --check
git diff --cached --numstat
# Required: 19 insertions, 0 deletions, draw/Draw.js only.
git commit -m "Guard specialized rendering against failed monster atlases"
git rev-parse HEAD^{tree}
# Required: c75546d5456ba655c7a1afa59ddc31dc80186347
```

The compatibility code reconciles two-pass Castle lava, scene/pipe ordering, track dispatch, surface/theme/custom-artwork precedence, Wiggler pipe composition, body/wing pivots and approved enlarged one-wing adjustments. The type-45 body offsets already come from #21 and must not be added twice. Add the final failed-atlas guards once after compatibility.

Use README.md for complete online/offline commands and verify-tree.py for every final source hash and PR ancestor. Recreated commit SHAs vary with timestamps/identity; the source tree must match exactly.

## Stop conditions

Stop if upstream/source heads move, conflict files differ, a patch fails, any intermediate tree differs, an atlas hash differs, or the final tree is not exact. Do not silently substitute source versions or change calibration. Refresh the affected rehearsal separately before continuing.

Track #10 precedes coaster #11; the description of #11 still cites obsolete #4. #22 precedes #23. Custom body features precede #21/#23 combined compatibility. Most source PRs are independent contributions rather than a current Git stack; the final combination requires the separate compatibility layer.
