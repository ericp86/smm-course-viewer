# Approved asset provisioning

The 17 standalone PR merges omit four base monster atlases and 24 terrain atlases. The approved self-contained result includes those exact 28 PNGs; all 173 PNGs in the final viewer match approved integration. Custom artwork already supplied by individual PRs is retained.

This compact package does not include a binary compatibility patch or PNG copies. Both replay scripts apply compatibility-code.patch and retrieve only the exact approved atlas bytes from Git objects, then verify SHA-256 before staging them.

- Online source: compare/enhanced at 138004b530435efe423d9ed7065093101645963f.
- Offline source: HEAD of the explicitly supplied bundle; every selected atlas must match the same approved hashes.
- Expected compatibility tree before safety: 47a1034c8c15b6fa12f64cb4d988c5640c6c76bc.
- Expected final application tree: c75546d5456ba655c7a1afa59ddc31dc80186347.

Original upstream README workflow: obtain images for layout/draw/monster/ and layout/draw/titleset/ separately, open index.html, then Load Example or Browse to an existing CDT. External provisioning is compatible, but the exact listed bytes are required to reproduce the validated self-contained tree. Do not generate, recompress or substitute artwork.

Use the replay scripts or binary-safe git show COMMIT:PATH extraction. Do not copy renderer source from the integration branch. No full binary patch is needed when this asset route is used.

| Exact file | Bytes | SHA-256 |
|---|---:|---|
| `layout/draw/monster/WU.png` | 2361068 | `b391b87e7124c6e7219f266d7325da686d596283587820036eee5651cde79e29` |
| `layout/draw/monster/MW.png` | 16859 | `f9f2e2e50c4ad1600c6e6306dca846da9b32b4147c8840ff71057b60c3c617ca` |
| `layout/draw/monster/M3.png` | 11499 | `80c6382eb9a6ca816d756d12cee4b44b2e31f7d3d13879aaff76314d7db4283f` |
| `layout/draw/monster/M1.png` | 11389 | `7bde4b03c9ce4a0125c3e28e4a6896bb7260d1736e88d81f00e3747e14ef4772` |
| `layout/draw/titleset/WU-water.png` | 1487118 | `19ea27647e175b3ad42b8247686a73a17d192143a238f77ed493b67ae0544531` |
| `layout/draw/titleset/WU-underground.png` | 1413738 | `1ddb29587a9a727e9d366cbc677f033cd76ad142ee815ebfff416defaba3657e` |
| `layout/draw/titleset/WU-overworld.png` | 1447464 | `8603b461119f7337b70211e2bb9f25d9a051b869b1f937f801da2f3b27c697b3` |
| `layout/draw/titleset/WU-ghostHouse.png` | 1026156 | `3418f6f1bc4e32560e1f7fe8327dfded0f84b455dd3f66963a34aa76d31b8d87` |
| `layout/draw/titleset/WU-castle.png` | 1086967 | `0f933ec578069cc16693131ab37c8148cac9aada326f74d8362054c33e0f476b` |
| `layout/draw/titleset/WU-airship.png` | 1248588 | `7b6dde11a2ce0ee25220fb50166df07dc2e20ba3c69f1efd44ccd59bd522c813` |
| `layout/draw/titleset/MW-water.png` | 24092 | `b09ec17b6a3512ebaeeca7b12d2cf75e99e2d841575058962cfb01aebc4a7a55` |
| `layout/draw/titleset/MW-underground.png` | 22759 | `d0f87a044a5633c236322a07fc9f8d2fd5bab70eb1be1dd6e87511d4965d9cd9` |
| `layout/draw/titleset/MW-overworld.png` | 22004 | `f1ce68453dcd59debcfc1ce6eb26b343f650af2e587b34aa37a5e201511231b3` |
| `layout/draw/titleset/MW-ghostHouse.png` | 21080 | `26d02885dbde0edb3bf73125c4795dde6d7bbfd15a126f5e39b88114f4b6ca2f` |
| `layout/draw/titleset/MW-castle.png` | 26025 | `429db88f40953acf2f3714a674dbfe5c27b2fe5c74e2586b27a7040b5ccec25c` |
| `layout/draw/titleset/MW-airship.png` | 22168 | `1765549e3fdc0039c7566691386c3292a9499a05901b41ef96ab8086bb173c9b` |
| `layout/draw/titleset/M3-water.png` | 16317 | `7ff9288ba4f538aaed42d95ab2cc50e714521af2939a87236d8d58b78229d050` |
| `layout/draw/titleset/M3-underground.png` | 18408 | `a9faeefb1d8a9ecc97f46d02cbe6d0b74ad315592060bc109b9b18e25a09224d` |
| `layout/draw/titleset/M3-overworld.png` | 18524 | `eed71e80d275f37866951626b7f6596a7278c0647b7218e08f62fb04ebfa92f1` |
| `layout/draw/titleset/M3-ghostHouse.png` | 17061 | `467426069579e7e90c0336a088734447440af63682f6d3c80f2686cf8f0ccf47` |
| `layout/draw/titleset/M3-castle.png` | 16200 | `f650e28acc7fe232d589b91b5612d0558a74a21bdcbcfbf544ef4b06948a627e` |
| `layout/draw/titleset/M3-airship.png` | 18415 | `9f89a1b2440f80cb4133a780d0092950615d68802e5e3f3e14254ae299a669e4` |
| `layout/draw/titleset/M1-water.png` | 15930 | `39ea1e9259a4791db1055458d72a8c1f71065dffe7ddc0b96a95fffa5c2ba889` |
| `layout/draw/titleset/M1-underground.png` | 14236 | `acc95856f47c2adf0c471ea936a0841b228413d3917e74ae14868d8b7e878d47` |
| `layout/draw/titleset/M1-overworld.png` | 15085 | `c57a1f677b530fc3ea9979a23555a9bf29b111a7b54cdbe38086751ac3d57307` |
| `layout/draw/titleset/M1-ghostHouse.png` | 14991 | `14a1729923f78af93413edb6c230dfd3220dde0a33d2a559c0eeac71eee7f31d` |
| `layout/draw/titleset/M1-castle.png` | 14934 | `d0bc763dbf59e0a323523cf871db75410e16c2afdb4a0ce9b6ff0724375ddced` |
| `layout/draw/titleset/M1-airship.png` | 15357 | `00d85418c9d59216ae177352d0111cdaac5c451944a97e46e3b4da857da7c5a1` |
