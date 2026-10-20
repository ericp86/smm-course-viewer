#!/usr/bin/env python3
"""Read-only verification of all handoff payload bytes; no credentials needed."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parent
manifest = json.loads((root / 'FILE-MANIFEST.json').read_text())
for relative, expected in manifest.items():
    path = root / relative
    assert not Path(relative).is_absolute() and '..' not in Path(relative).parts
    assert path.is_file(), relative
    data = path.read_bytes()
    assert len(data) == expected['bytes'], relative
    assert hashlib.sha256(data).hexdigest() == expected['sha256'], relative
print(f"Verified {len(manifest)} handoff payload files.")
