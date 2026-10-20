# Option A maintainer handoff

This package documents the verified individual-PR merge workflow. It is based on fork master `848a7f4584fd69405ca745ac1c97a0f3ced175fa`; the documentation branch is not the final application tree.

The exact browser-test application is published separately at `ericp86/smm-course-viewer:test/option-a-final-verification`, commit `e14a6c1d5956b15cbfdaf00bd4bd1713a5dfaae9`.

**Required final application tree:** `c75546d5456ba655c7a1afa59ddc31dc80186347`.

**Recommended workflow:** merge the existing 17 PRs individually using Option A. The complete independent replay and automated validation are complete, and user-reported manual browser visual acceptance is **PASS**. See VALIDATION.md for scope and limitations; no new production PR is needed.

## Read and verify

- FINAL-STATUS.md: approved pins, independent replay outcome and remaining limitations.
- OPTION-A.md: exact 17-PR order, conflict-resolution map and manual merge commands.
- PR-INVENTORY.md / inventory.json: titles, branches, full HEADs, purposes and dependencies.
- ASSETS.md / asset-hashes.json: the 28 required base atlases and exact approved hashes.
- SOURCE-COMPARISON.md: six explained source differences from approved integration.
- VALIDATION.md: completed automated evidence and fresh packaging checks, kept distinct.
- BROWSER-TEST.md: user-reported acceptance, separate WSL viewer at port 8008 and retained visual checklist.
- OPTION-B.md: optional coordinated-PR alternative, not a request to open or merge one.
- MAINTAINER-MESSAGE.md: draft only; not sent.

Run with normal Python 3 (not optimization mode):

```bash
python3 maintainer-handoff/verify-manifest.py
```

FILE-MANIFEST.json records the exact byte length and SHA-256 of every other handoff file. The manifest excludes itself to avoid self-reference; its own SHA-256 is recorded in the publication report, and Git records its exact blob.

## Reproduce all 17 merges online

Run from the root of this documentation clone, choosing a new destination outside this package:

```bash
python3 maintainer-handoff/replay-online.py \
  --destination "$HOME/smm-option-a-replayed"
python3 maintainer-handoff/verify-tree.py \
  --checkout "$HOME/smm-option-a-replayed"
```

The script checks upstream and all source tips, performs 17 ordinary merges, applies each exact conflict patch, checks every intermediate tree, adds compatibility code and approved PNGs, then adds the final 19-line safety patch. It never pushes or edits PRs. Stop on any failed check; do not adapt patches or substitute tips automatically.

Git and Python 3 are sufficient for replay. Node.js is needed for the included application syntax/parser checks described in VALIDATION.md. Scripts receive explicit destination/bundle paths and use the package's own relative files. No hosted-agent directory is required.

## Offline replay

No large bundle or binary archive is included. An external Git bundle must contain the pinned upstream and 17 source histories, with HEAD pointing to an approved completed tree containing the base atlases. The preserved original rehearsal bundle qualifies. A bundle can also be produced locally from the published testing branch after cloning it:

```bash
git -C "$HOME/smm-option-a-final" bundle create \
  "$HOME/smm-option-a-history.bundle" HEAD
python3 maintainer-handoff/replay-offline.py \
  --bundle "$HOME/smm-option-a-history.bundle" \
  --destination "$HOME/smm-option-a-offline"
python3 maintainer-handoff/verify-tree.py \
  --checkout "$HOME/smm-option-a-offline"
```

The offline script verifies bundle integrity, retrieves only local objects, and checks every atlas byte against the approved hashes before reconstructing the final tree. It applies code and safety patches from this package. It requires no network and no separate binary compatibility patch.

## Browser test without replaying

Use a new checkout of the testing branch; follow BROWSER-TEST.md. The exact application tree is unchanged from the independently completed replay. The user reports PASS after comparing the complete collection of previously compiled test courses with approved enhanced integration. This is manual acceptance, not exhaustive or pixel-perfect automated verification; failure-injection browser testing is not reported complete.

This publication creates only the documentation and browser-test branches. Existing PRs, master branches and compare/enhanced are unchanged; no PR was created or edited. Contacting the maintainer or publishing a coordinated PR remains a separate decision.
