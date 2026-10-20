# Quest 65

A Quest 64 rebalance built on Merrow's French Vanilla preset. The aim is to make each element a useful primary specialization, with rewarding combinations and discoverable early tools. The full redesign is still in progress.

**ROMs are not included.** Apply `patches/quest65-test6-from-clean-us.ips` to your own clean US `.z64` copy. [Cloud setup](docs/cloud-setup.md) describes the private-input trial; [the handoff](docs/cloud-handoff.md) records the current project state. Creating a repository does not itself start a Cloud task.

**Open `Quest65-test5.z64` in the project root. Its internal name is `QUEST 65 TEST6`.** The filename stays the same to avoid duplicate game files. Fully restart the emulator and reopen the newly downloaded file; an old emulator save state can restore old code/data.

The current pass reduces healing, strengthens Evade, moves Fire Ball II to Fire 7 and increases its damage, gives Wind a three-Agility growth interval, and reduces Solvaring's Defense and Fists power. It also includes the enemy spell repair and preserves Claude's other Test 5 changes. [Current test notes](patches/test6-README.md) give old/new values, patch inputs, hashes and limitations.

- [Mod Details](MOD-DETAILS.md): the player's cumulative guide, grouped by category, with reasons and a separate explanation of unfinished design goals.
- [Playtest checkpoints](docs/playtest-notes.md): the reported Solvaring run and focused follow-up checks.
- [Development log](docs/development-log.md): dated research, tool/build changes and verification evidence.
- [Working spell plan](docs/spell-plan-v2.md): design discussion; some details predate the supplied Test 5 and current tuning. Check Mod Details for implemented behavior.
- [Wishlist](docs/wishlist.md): unfinished features.

Only two full ROM files are retained locally: the untouched `Quest 64 (USA).z64` and the working `Quest65-test5.z64`. Earlier builds are recoverable from verified IPS patches. The local-only inventory is `outputs/rom-storage.json`; generated reports and emulator saves are excluded from the public checkout. `PLAY-LATEST.z64` was an older test2 copy and has been retired.

## Patches and recovery

`patches/quest65-test6-from-clean-us.ips` applies directly to the untouched US ROM. `patches/quest65-test6-from-test5.ips` applies only to the supplied original Test 5. Neither requires adding another local full-ROM file.

To restore the supplied Test 5 in place while keeping the current state as a rollback patch:

```powershell
python scripts/restore_working_rom.py --patch patches/rollback/rom-cbda8d1b9356bfd9.ips
```

To return to the current balance test:

```powershell
python scripts/restore_working_rom.py --patch patches/quest65-test6-from-clean-us.ips
```

The static builder `scripts/apply_early_balance.py` reproduces the current pass from the exact supplied Test 5, the retained enemy-fix IPS and the saved remote verification result. It updates the working file in place and refuses a different input. The older foundation builder/profiles describe test1/test2 and do not include Claude's code. Claude's handoff is retained as [HANDOFF.md](HANDOFF.md); its listed source files were not supplied in this folder.

## Verification

The authorized Vercel VM passed 27,150 targeted routine checks and was stopped after results were downloaded. [Build and verification evidence](build/early-balance/) includes the bounded edits, checksum, output hash, exact patch replays and limitations. Full battles, actual projectile connections, save/load and Android remain untested for this ROM. Older [desktop emulator results](docs/emulator-test-notes.md) apply to test2 only.

[Incremental decompilation](decomp/README.md) provides combat C drafts and nine recovered combat/UI routines with remote comparison results. It is research tooling, not a full-ROM source rebuild. Compilation, assembly and game-code execution require a confirmed OS-isolated session; they must not run on the laptop. Static ROM/IPS processing can run locally.

The French Vanilla preset, settings, baseline patch and original technical reports are preserved under `patches/` and `build/baseline/`; its duplicate full ROM was retired. Attribution is in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
