#!/usr/bin/env python3
"""Offline merge replay from an explicitly supplied Git bundle and text patches.

Creates only a new local disposable repository; never pushes. Its merge algorithm and patches follow the completed independent replay.
This portable packaging copy was syntax/CLI and patch-context checked.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
ap.add_argument('--destination', required=True)
ap.add_argument('--bundle', required=True)
args = ap.parse_args()
dest = Path(args.destination).resolve()
assert not dest.exists(), 'Destination must not exist'
assert root not in dest.parents, 'Destination must be outside the handoff directory'
records = json.loads((root / 'merge-results.json').read_text())
inventory = {x['number']: x for x in json.loads((root / 'current-pr-metadata.json').read_text())}
trees = json.loads((root / 'merge-tree-pins.json').read_text())
manifest = json.loads((root / 'FILE-MANIFEST.json').read_text())
required = ['merge-results.json', 'current-pr-metadata.json', 'merge-tree-pins.json',
            'compatibility-code.patch', 'compatibility-assets.txt', 'final-artwork-safety.patch',
            'published-integration-file-sha256.json']
required += [f"merges/{x['position']:02d}-pr{x['pr']}/resolution.patch"
             for x in records if x['conflictFiles']]
for relative in required:
    assert hashlib.sha256((root / relative).read_bytes()).hexdigest() == manifest[relative]['sha256'], relative
env = {**os.environ, 'GIT_AUTHOR_NAME': 'SMM merge rehearsal',
       'GIT_AUTHOR_EMAIL': 'rehearsal@example.invalid',
       'GIT_COMMITTER_NAME': 'SMM merge rehearsal',
       'GIT_COMMITTER_EMAIL': 'rehearsal@example.invalid', 'GIT_TERMINAL_PROMPT': '0'}
dest.mkdir(parents=True)

def run(*arguments, check=True):
    return subprocess.run(['git', '-c', 'core.autocrlf=false', *arguments], cwd=dest, env=env, capture_output=True, check=check)

def git(*arguments):
    return run(*arguments).stdout.decode().strip()

git('init')
bundle = Path(args.bundle).resolve()
assert bundle.is_file(), 'Supply an existing Git bundle'
git('bundle', 'verify', str(bundle))
git('fetch', '--no-tags', str(bundle), 'HEAD')
asset_ref = git('rev-parse', 'FETCH_HEAD')
baseline = 'f807f0247bac4c553288700bf7c08dd8502eead0'
git('cat-file', '-e', baseline + '^{commit}')
for record in records:
    git('cat-file', '-e', record['source'] + '^{commit}')
git('checkout', '--detach', baseline)

for record in records:
    assert not git('status', '--porcelain')
    result = run('merge', '--no-ff', '--no-commit', record['source'], check=False)
    conflicts = git('diff', '--name-only', '--diff-filter=U').splitlines()
    assert conflicts == record['conflictFiles'], (record['pr'], conflicts)
    if conflicts:
        patch = root / 'merges' / f"{record['position']:02d}-pr{record['pr']}" / 'resolution.patch'
        git('apply', '--check', str(patch))
        git('apply', str(patch))
        git('add', '--', *conflicts)
    else:
        assert result.returncode == 0, result.stderr.decode()
    git('diff', '--cached', '--check')
    git('commit', '-m', f"Merge PR #{record['pr']} with documented resolution")
    assert git('rev-parse', 'HEAD^{tree}') == trees[str(record['pr'])]

git('apply', '--check', str(root / 'compatibility-code.patch'))
git('apply', '--index', str(root / 'compatibility-code.patch'))
for relative in (root / 'compatibility-assets.txt').read_text().splitlines():
    path = dest / relative
    assert not path.exists(), f'Expected absent atlas: {relative}'
    data = run('show', asset_ref + ':' + relative).stdout
    expected = json.loads((root / 'published-integration-file-sha256.json').read_text())[relative]
    assert hashlib.sha256(data).hexdigest() == expected
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    git('add', '--', relative)
git('diff', '--cached', '--check')
git('commit', '-m', 'Reconcile renderer compatibility and approved atlas assets')
assert git('rev-parse', 'HEAD^{tree}') == '47a1034c8c15b6fa12f64cb4d988c5640c6c76bc'
git('apply', '--check', str(root / 'final-artwork-safety.patch'))
git('apply', '--index', str(root / 'final-artwork-safety.patch'))
assert git('diff', '--cached', '--numstat') == '19\t0\tdraw/Draw.js'
git('diff', '--cached', '--check')
git('commit', '-m', 'Guard specialized rendering against failed monster atlases')
assert git('rev-parse', 'HEAD^{tree}') == 'c75546d5456ba655c7a1afa59ddc31dc80186347'
assert not git('status', '--porcelain')
print(json.dumps({'head': git('rev-parse', 'HEAD'), 'tree': git('rev-parse', 'HEAD^{tree}'),
                  'published': False}, indent=2))
