# Optional alternative: one coordinated PR

The maintainer may prefer one coordinated integration PR instead of 17 individual PR merges. Such a proposal can preserve all PR contributions, documented conflict resolutions, compatibility work and the final safety correction in one reviewable history.

Suggested title: **Integrate course rendering and Unicode fixes from 17 existing PRs**.

The independently replayed browser branch contains the approved combined application content, retaining 17 merge boundaries, the compatibility layer and the final safety commit. It is published for browser verification only; no coordinated PR is being opened by this handoff.

Compared with upstream, the combined result changes 57 files: five JavaScript files and 52 artwork files, with 3,208 textual insertions and 141 deletions. This removes fourteen merge-resolution operations from the maintainer's workflow, while presenting a larger aggregate renderer diff. Individual contributions remain traceable via source parents and merge commits.

Option A offers smaller review units but requires the exact sequence, fourteen patches and two final layers. A compatibility PR merged afterward does not prevent the earlier conflicts. Option B is technically easier to merge; either review preference is reasonable.

Suggested description:

> This combines #7–#17 and #21–#26, preserving original contribution history. It includes the tested conflict resolutions, separate renderer compatibility work, approved base atlases and a final failed-atlas safety fix. The exact final tree passed 41,527 automated checks with zero failures/skips; all 192 artwork-loading scene regressions recovered and 17,176 healthy recordings stayed unchanged. Browser visual sign-off is separate. The alternative is the documented individual-PR workflow. Please choose your preferred review approach.

Existing PRs stay open. Only after maintainer agreement and acceptance of a coordinated replacement should they be closed as superseded with a cross-reference. #18–#20 remain excluded. PR #11 still cites obsolete #4; current track dependency is #10. These facts are documented without editing metadata.

No PR creation, closure or maintainer contact is authorized by publishing these handoff/testing branches. Any coordinated submission requires a separate explicit decision.
