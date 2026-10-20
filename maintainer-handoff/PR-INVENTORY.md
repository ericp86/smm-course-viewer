# Complete 17-PR inventory

All entries were verified open against upstream master. Source owner: ericp86. Titles and pinned tips match the original inventory.

| PR | Exact title | Source branch | Full HEAD |
|---|---|---|---|
| [#7](https://github.com/leomaurodesenv/smm-course-viewer/pull/7) | Fix object rotation, orientation, and rendering depth | `fix/object-depth-rotation` | `dd8eefd6022f32e01eb47785b35490568b94e7e4` |
| [#8](https://github.com/leomaurodesenv/smm-course-viewer/pull/8) | Add goal rendering and scenery across game styles | `fix/goal-rendering-scenery` | `73a990cc04d20f761f825da4a5063de04af62962` |
| [#9](https://github.com/leomaurodesenv/smm-course-viewer/pull/9) | Fix cannon rendering and rotation for all mounting surfaces | `fix/cannon-rendering-rotation` | `e5352e338974e7fa3b3fc18352baeb379c78c1de` |
| [#10](https://github.com/leomaurodesenv/smm-course-viewer/pull/10) | Fix track rendering, orientation, and endpoint caps | `fix/track-rendering-endpoints` | `ae69e2d237a7e7bcd3860da8ccc0dfd77449d730` |
| [#11](https://github.com/leomaurodesenv/smm-course-viewer/pull/11) | Fix skull coaster rendering positioning and object positioning on curved tracks | `fix/skull-coaster-rendering-positioning` | `fcb4f3b39eb45f9a05ac569a36f765a701895655` |
| [#12](https://github.com/leomaurodesenv/smm-course-viewer/pull/12) | Add Castle lava rendering with foreground layering | `fix/castle-lava-rendering` | `b0a20faf0251fe4fd01ea6027e134d0b76190aa3` |
| [#13](https://github.com/leomaurodesenv/smm-course-viewer/pull/13) | Fix Spiny, Buzzy Beetle, and Spike Top surface orientation | `fix/enemy-surface-orientation` | `dce2654abbcc4d22cac98f00e95c296559ca4864` |
| [#14](https://github.com/leomaurodesenv/smm-course-viewer/pull/14) | Add Spiny and Buzzy Shelmet rendering support | `feat/shelmet-rendering` | `16daacfc6041866c5ef8f9c34311b6818cfb29c3` |
| [#15](https://github.com/leomaurodesenv/smm-course-viewer/pull/15) | Fix fire bar rendering, length, and rotation | `fix/fire-bar-rendering` | `368aaa17eb8ecc19dcc6fced3c5efebd426786df` |
| [#16](https://github.com/leomaurodesenv/smm-course-viewer/pull/16) | Fix Wiggler rendering across all game styles | `fix/wiggler-rendering` | `7ebfc4aeb919bccccf8e0a671b54f065bf21bc29` |
| [#17](https://github.com/leomaurodesenv/smm-course-viewer/pull/17) | Fix P Switch sprites in SMB1 and NSMBU | `fix/p-switch-sprites` | `e5192068dfaea0ba6968a446c15425eafcfe2e6f` |
| [#21](https://github.com/leomaurodesenv/smm-course-viewer/pull/21) | Fix pipe-attached enemy and object positioning | `fix/pipe-attached-enemies-combined` | `5feca7b5f7732538d69f999eebfacbeaafcaa58e` |
| [#22](https://github.com/leomaurodesenv/smm-course-viewer/pull/22) | Add custom Shoe Goomba and Stiletto sprites | `fix/shoe-goomba-stiletto-artwork` | `f2bac6fabcf114d4cb700a6771dd62ddebba53cb` |
| [#23](https://github.com/leomaurodesenv/smm-course-viewer/pull/23) | Add wing rendering for objects across all game styles | `fix/winged-objects` | `7c9caa284b5381fd762c7da8f1fa46e076f4c201` |
| [#24](https://github.com/leomaurodesenv/smm-course-viewer/pull/24) | Fix theme specific enemy colors | `fix/theme-specific-enemy-colors` | `b4df66491d2f6ad853761cc44b5f7a0c90b34dd9` |
| [#25](https://github.com/leomaurodesenv/smm-course-viewer/pull/25) | Feature/linked door symbols | `feature/linked-door-symbols` | `7b99e2d24d71bccf47acd685c6364dc62d0d7d9d` |
| [#26](https://github.com/leomaurodesenv/smm-course-viewer/pull/26) | Fix UTF-16BE decoding of Unicode course names | `fix/unicode-course-names` | `aea7027b12014b9a45ecdfd5254dc9e89f5e3f9d` |

## #26

Decode big-endian UTF-16 course names without dropping non-ASCII code units or surrogate pairs.

Order/dependencies: Independent; first to separate parser-only work.

Files: `lib/SmmCourseViewer.js`.

## #7

Signed and fractional depth sorting; direction parsing; gates, Burners, signs and checkpoint rendering.

Order/dependencies: Independent foundation; merge before track XY normalization and later drawing passes.

Files: `draw/Draw.js`, `draw/MonsterDraw.js`, `lib/MonsterObject.js`, `lib/SmmCourseViewer.js`.

## #10

Fractional track coordinates, sprite segments, curves and endpoint A/B mapping; artwork protection.

Order/dependencies: Independent standalone; current implementation should precede #11.

Files: `draw/Draw.js`, `lib/SmmCourseViewer.js`.

## #11

Single attached skull versus four free skulls; linked curved-track placement; rail/coaster artwork protection.

Order/dependencies: Contains older track work; retain current #10 geometry and readiness protections when merging. Description incorrectly cites #4; actual predecessor is #10.

Files: `draw/Draw.js`, `draw/MonsterDraw.js`, `lib/SmmCourseViewer.js`.

## #8

Style/theme-specific goals and surrounding scenery; missing-goal, canvas-state and optional-image protection.

Order/dependencies: Independent standalone; shares image registration, drawing passes and specialized cases with later renderers.

Files: `draw/BlockDraw.js`, `draw/Draw.js`.

## #12

Castle-only foreground lava; background/object completion coordination and artwork readiness.

Order/dependencies: Independent standalone single-pass lava; combine its background gate with existing image completion. Approved combined viewer requires an extra background lava pass.

Files: `draw/Draw.js`.

## #9

Cannon source crops, mounting angles and size-dependent centers; invalid-rotation guard.

Order/dependencies: Independent standalone; #7 supplies general direction/depth foundation, but cannons decode their own flags.

Files: `draw/Draw.js`.

## #13

Surface orientation and flipping for Spiny, Buzzy Beetle and Spike Top.

Order/dependencies: Independent standalone; later combined surface path must coexist with #14, #21, #23 and #24.

Files: `draw/Draw.js`.

## #24

Theme-dependent Buzzy Beetle/Fire Piranha colors without changing metadata.

Order/dependencies: Independent standalone; generic extension gets mode/theme parameters. #13/#21 specialized bodies need equivalent color selection in compatibility patch.

Files: `draw/Draw.js`, `draw/MonsterDraw.js`.

## #14

Empty Spiny/Buzzy Shelmet custom artwork and appropriate theme colors.

Order/dependencies: Independent standalone; order after #13/#24 makes empty-Shelmet precedence explicit. No new winged-empty-Shelmet behavior.

Files: `draw/Draw.js`, `layout/draw/custom/nsmbu/buzzy-shelmet.png`, `layout/draw/custom/nsmbu/spiny-shelmet.png`, `layout/draw/custom/smb1/buzzy-shelmet-black.png`, `layout/draw/custom/smb1/buzzy-shelmet-green.png`, `layout/draw/custom/smb1/spiny-shelmet.png`, `layout/draw/custom/smb3/buzzy-shelmet-black.png`, `layout/draw/custom/smb3/buzzy-shelmet-green.png`, `layout/draw/custom/smb3/spiny-shelmet.png`, `layout/draw/custom/smw/buzzy-shelmet.png`, `layout/draw/custom/smw/spiny-shelmet.png`.

## #15

Fire Bar variable lengths, unsigned rotation data and guarded sprite drawing.

Order/dependencies: Independent; overlaps only the shared drawing method.

Files: `draw/Draw.js`.

## #16

Wiggler body/head/flower composition and loaded custom Angry Wiggler body artwork.

Order/dependencies: Independent; requires combined #21 pipe-aware composition contract in compatibility patch.

Files: `draw/Draw.js`, `draw/MonsterDraw.js`, `layout/draw/custom/nsmbu/angry-wiggler-body-nsmb.png`, `layout/draw/custom/smb1/angry-wiggler-body-smb1.png`, `layout/draw/custom/smb3/angry-wiggler-body-smb3.png`, `layout/draw/custom/smw/angry-wiggler-body-smw.png`.

## #17

Custom P Switch sprites for M1/WU with atlas fallback; preserve P Doors.

Order/dependencies: Independent; union image registration and custom selection with other sprite PRs.

Files: `draw/Draw.js`, `layout/draw/custom/nsmbu/p-switch.png`, `layout/draw/custom/smb1/p-switch.png`.

## #22

Custom Shoe/Stiletto artwork, bottom anchoring and aspect ratio with safe atlas fallback.

Order/dependencies: Independent; precede #23 to preserve approved Shoe/Stiletto aspect ratio and wing behavior.

Files: `draw/Draw.js`, `layout/draw/custom/smb1/shoe-goomba.png`, `layout/draw/custom/smb1/stiletto-goomba.png`, `layout/draw/custom/smb3/shoe-goomba.png`, `layout/draw/custom/smb3/stiletto-goomba.png`.

## #25

Playing-card symbols on linked normal/P/key doors with safe image completion.

Order/dependencies: Independent; union symbol images with other optional assets; preserve its safe completion behavior.

Files: `draw/Draw.js`, `layout/draw/custom/symbols/club.png`, `layout/draw/custom/symbols/diamond.png`, `layout/draw/custom/symbols/heart.png`, `layout/draw/custom/symbols/spade.png`.

## #21

Pipe-attached enemy/item/coin placement, finalized offsets and foreground pipe occlusion.

Order/dependencies: Independent calibrated branch. Final combined output requires #16/#22 where their custom features apply, plus #23 and pivot/dispatch compatibility. Do not repeat its published type-45 calibration.

Files: `draw/Draw.js`.

## #23

One/two wings, supported-object dispatch, game-style offsets and wing artwork readiness.

Order/dependencies: Independent free-standing wings. Final pipe/wing behavior requires #21, custom Shoes from #22, and separate integration-only pivot/artwork/calibration work.

Files: `draw/Draw.js`.

No pinned PR tip is an ancestor of another current pinned tip. Dependencies above describe implementation/behavior, not a claimed current Git stack. Closed superseded #18–#20 are excluded. No PR metadata has been changed by this publication.
