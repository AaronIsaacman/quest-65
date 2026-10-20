# Early balance test

Use the existing **`Quest65-test5.z64`** in the project root. Its filename stays the same; its internal name is now **QUEST 65 TEST6**. Fully stop the emulator and reopen the newly downloaded file. An old emulator save state can restore old code/data, so load through the game's normal save system for this check. Save/load compatibility has not been newly verified.

## What to expect

| Change | Supplied Test 5 | Current |
| --- | --- | --- |
| Healing I at Water 4 / 71 maximum HP | 9–10 HP | 6 HP |
| Healing II at Water 17 / 101 maximum HP | 26–31 HP | 21–25 HP |
| Healing III at Water 32 / 200 maximum HP | 64–79 HP | 53–65 HP |
| Evade I/II effective Agility | 2× / 4× | 8× / 16× |
| Fire Ball II unlock | Fire 4 | Fire 7 |
| Fire Ball II power per projectile | 220 | 260 |
| Natural Agility milestone for a Wind level | Every multiple of 5 | Every multiple of 3 |
| Defense milestone for an Earth level | Every multiple of 5 | Unchanged |
| Solvaring Defense | 12 | 6 |
| Solvaring close-range Fists power | 550 | 440 |

Healing remains available immediately, with higher tiers saving turns and basic healing remaining economical as Water grows. Evade has a more noticeable effect at low Agility. Fire II's two projectiles reward the extra MP cost. Solvaring retains 180 HP, 17 Agility and his original Roar; lower Defense and weaker Fists should make the opening tools and close combat more practical. These are first-pass tuning choices awaiting another battle.

The enemy spell repair is included: 16 references across 13 enemy types now point to their intended spells after the menu rearrangement. Claude's other Test 5 changes are retained, including linked growth and the existing spell-power floor. Full player-facing explanations are in [Mod Details](../MOD-DETAILS.md).

## Validation and limitations

The authorized Vercel VM ran 27,150 routine checks with networking denied: 11,250 healing cases; 12 Evade applications; 4,000 hit rolls; 500 natural-stat link cases; 188 power cases; 11,200 recipient-damage cases. A focused follow-up checked Solvaring's close raw power (25 → 20) and Wind Cutter against his old/new Defense (1–2 → 2–3 per connected blade at the reported element levels). No full emulator battle or save/load test ran. Hit results do not guarantee avoidance of moves that bypass normal hit checks, or that every projectile connects.

The local build checks the exact source, bounded edits, preserved RSP microcode and enemy-healing branch, all 128 enemy action records, checksum, written output hash and both IPS replays. It changes 115 bytes from the supplied Test 5, including the header/checksum and the enemy fix. The VM is stopped. No assembler, compiler or game routine ran on the laptop.

- Working ROM SHA256: `a2db80ae41fe9c5dad3f339629ca49071ee2619f8c70ce9017deec8c8cae2285`.
- `quest65-test6-from-clean-us.ips` applies to the untouched US ROM.
- `quest65-test6-from-test5.ips` applies only to the supplied original Test 5, SHA256 `cbda8d1b9356bfd97baf929a8510323d3a5af0b239487e460a32bf6dc926ad3c`.
- The original Test 5 is recoverable using `rollback/rom-cbda8d1b9356bfd9.ips` with the clean US source. Do not apply that cumulative rollback patch over the modified ROM.

Recovery can update the working file in place:

```powershell
python scripts/restore_working_rom.py --patch patches/rollback/rom-cbda8d1b9356bfd9.ips
```

That first preserves the current state as another small rollback patch. Older generated ROMs were replaced by verified recovery patches so only the clean original and working ROM remain. Storage records are in [outputs/rom-storage.json](../outputs/rom-storage.json); routine evidence and build details are in [build/early-balance](../build/early-balance/) and the [development log](../docs/development-log.md).
