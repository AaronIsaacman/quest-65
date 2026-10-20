# Quest 65

A Quest 64 rebalance built on Merrow's French Vanilla preset.

**Bring your own ROM.** This repository contains no full game images,
extracted assets, emulator saves or private build inputs.

Apply `patches/quest65-test6-from-clean-us.ips` directly to your own clean US
`.z64` copy. Exact input/output hashes are in [the manifest](cloud/input-manifest.json).

- [Mod Details](MOD-DETAILS.md): current gameplay differences and unfinished design goals.
- [Current test notes](patches/test6-README.md): balance values and validation limits.
- [Cloud trial](CLOUD.md): verify the patch with a private input, independently of the laptop.
- [Third-party notices](THIRD_PARTY_NOTICES.md): Merrow attribution and license.

This initial public export contains the patch tools and Cloud trial. Broader
local decompilation, conversation handoffs and infrastructure records have
not been published. A full source rebuild of the game is not provided.

The current build reduces basic healing, strengthens Evade, unlocks Fire Ball
II at Fire 7, adjusts Agility-linked growth, eases Solvaring and repairs enemy
spell references after player-spell reordering. It retains the existing
linked growth and other supplied Test 5 changes. Playtesting remains ongoing.

The project is unofficial. Upstream notices remain applicable; this repository
does not grant rights to the original game. No blanket new license is applied
to all research or game-derived material.
