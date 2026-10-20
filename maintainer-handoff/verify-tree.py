#!/usr/bin/env python3
"""Read-only verification of the approved Option A application checkout."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess

ap = argparse.ArgumentParser()
ap.add_argument('--checkout', required=True)
args = ap.parse_args()
root = Path(__file__).resolve().parent
checkout = Path(args.checkout).resolve()
def git(*arguments):
    return subprocess.check_output(['git', '--no-optional-locks', '-C', str(checkout),
                                    *arguments], text=True).strip()
assert git('rev-parse', 'HEAD^{tree}') == 'c75546d5456ba655c7a1afa59ddc31dc80186347'
assert not git('status', '--porcelain')
files = json.loads((root / 'final-file-sha256.json').read_text())
assert set(git('ls-files', '-z').split('\0')) - {''} == set(files)
for relative, digest in files.items():
    assert hashlib.sha256((checkout / relative).read_bytes()).hexdigest() == digest, relative
for record in json.loads((root / 'merge-results.json').read_text()):
    subprocess.run(['git', '-C', str(checkout), 'merge-base', '--is-ancestor',
                    record['source'], 'HEAD'], check=True)
print('Verified final tree, clean checkout, all 233 file hashes and 17 PR ancestors.')
