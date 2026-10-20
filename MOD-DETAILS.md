# Quest 64: Definitive Edition — Mod Details

Master an element. Discover a combination. Make Brian your own.

This guide explains the mod's direction and the changes currently available compared with the original US Quest 64. **Our changes** are added by this project. **Inherited changes** come from Jonah Davidson (Hangedman)'s French Vanilla/Merrow mod; the reasons given explain why we are keeping them.

**Playable build:** The working file is `Quest65-test5.z64`; its internal name is **QUEST 65 TEST6**. It includes Claude's supplied spell/progression changes, the enemy spell repair, and the early balance adjustments below. The larger spell-kit redesign remains unfinished. [Current test notes](patches/test6-README.md) describe validation and recovery.

## The adventure we want to build

**These are design goals, not a claim that the full elemental rebalance is already playable or proven balanced.** The implemented gameplay changes begin under “Spells” below. Earlier support spells, linked growth, revised attacks and Solvaring tuning provide an initial foundation for these playstyles.

| Element | Intended playstyle |
| --- | --- |
| **Fire — end it fast** | Deal the greatest focused damage, weaken enemy defenses, and spend MP to finish dangerous enemies before they retaliate. Fire Ball is the efficient workhorse; premium attacks buy more damage in one turn at a higher MP cost. Staff buffs and selective life draining support aggressive play. |
| **Water — fight in the thick of it** | Control a dangerous opponent, strike nearby groups, and use openings for staff-based MP recovery. Direct healing supports recovery between exchanges. An attack that weakens enemy damage is being considered so Water can survive close combat on its own. |
| **Earth — stand your ground** | Use deliberate, long-range area attacks and strong defenses to win slowly and steadily. Stoneheart would reward enduring hits, even when Defense reduces their damage to zero. Earth has the lowest intended damage per enemy, compensated by coverage and staying power. |
| **Wind — control the battlefield** | Reposition, dodge, and land tracking attacks when an aimed shot would be awkward. Multiple smaller hits, a low-damage healing attack, and movement control reward an active fighting style. Misses must not generate healing. |

### Specialize or combine

A primary specialization in **any** element should support finishing the game. Heavy Water or Earth investment should not be a survival tax. Spreading spirits between elements should also remain a practical way to play: early tools should stay useful, while deeper investment earns stronger versions and distinctive late spells.

Combinations should sometimes outperform a single-element approach **at comparable total investment**, through tools that work together rather than a hidden bonus for choosing the right pair. No pair should be compulsory, and mixed builds should not require a guide or perfect planning.

| Pair | Intended cooperation |
| --- | --- |
| **Fire + Earth** | Earth's protection supports aggressive staff fighting; its MP conversion helps fund Fire's bursts. Fire's Defense debuffs help Earth's attacks finish enemies sooner. |
| **Fire + Wind** | Wind supplies positioning and reliable ranged hits; Fire supplies heavy finishing blows. A ranged Scorch can lower Defense before follow-up attacks, while Crosswind would lower Agility to improve hit reliability. |
| **Fire + Water** | Fire handles focused burst damage, while Water covers nearby groups and recovery. Water's proposed staff MP buff helps fuel expensive Fire attacks. |
| **Earth + Water** | Earth's defenses support walking into a group for Water's wide attacks. Their different recovery tools support endurance. |
| **Earth + Wind** | Wind's movement helps line up deliberate Earth attacks and avoid retaliation; Earth cushions failed dodges. Stoneform would trade dodging for stronger protection, letting players choose between an agile ranged style and deliberately enduring hits. This pairing still needs testing. |
| **Water + Wind** | Wind's movement helps Brian reach a group or a staff target; Water supplies close-area damage and recovery. Mobility and careful positioning help manage the risk of staying close. Extra MP recovery should require successful staff hits rather than enabling indefinite safe recovery at range. |

**These six pairings are design hypotheses.** Matched checkpoint encounters, focused interaction tests, and a main progression playthrough should establish whether the intended choices work without requiring a full story run for every pairing. The mod does not currently implement the proposed Fire/Wind/Earth healing, Scorch, Stoneheart, staff MP buff, or movement-growth changes. Channel remains excluded; Water's extra MP recovery requires successful staff hits.

### Working spell plan

The [current v2 design](docs/spell-plan-v2.md) revises the earlier roster around distinct playstyles and early discovery. By all elements at level 3, a balanced player should have attacks, healing, defense, and movement/evasion support. Filling every spell path is no longer a requirement. **The new roster is not implemented; several new effects remain proposals.** The existing playable changes remain listed under “Spells” below.

- **Fire's staff tools:** bring Power Staff and Vampire's Touch close together early. The selected design uses double/triple staff power and 3–5-turn buffs; Vamp should attack on activation, counting that strike toward its duration. Life drain should work well without Power Staff, with a smaller healing benefit from Power's extra damage. Exact recovery remains under review. These effects still need implementation. Siphon Flame and the proposed Fire Bomb splash role are removed from the current design.
- **Scorch:** ranged damage plus lower enemy Defense. Against sturdy enemies, its own hit plus the next connected attack should beat simply attacking twice. Duration is measured in turns, not three attack charges. Exact payoff needs testing.
- **Earth's defenses:** recommend one useful early Armor and a later Stoneform that trades dodging for stronger protection. Remove separate Armor II and Magic Barrier from the planned menu, along with the proposed extra recovery multiplier. Stoneheart should heal on every genuine connected hit, including zero-damage hits; a five-hit attack can trigger five recoveries.
- **Earth's attacks:** introduce Rolling Rock before Rock II. Preserve French Vanilla Avalanche's existing multi-hit behavior for the first test; it already has lower power than vanilla. Consider earlier reliable all-enemy Rock Shower and a later powerful Avalanche. Three further proposals would reward enduring hits, place a damaging ground field, and spend remaining protection on a finishing attack. These new effects require prototypes; see the [Earth proposal](docs/earth-spell-proposal.md).
- **Crosswind:** the preferred Wind Bomb rework; a ranged burst that lowers enemy Agility. This supports reliable multi-hit attacks. The severe movement-reduction alternative is set aside.
- **Cyclone:** one strong homing attack assigned to each living enemy, distinguishing tracking attacks against separate targets from Earth's aimed area damage. This targeting behavior needs a prototype; Merrow blocks the straightforward combination of Cutter projectiles with all-enemy modifiers, so it is not a confirmed data-only edit.
- **Ice Knife:** earlier single-enemy cold control. **Ice Wall:** later close-area cold control, with Ice Wall II included as a late upgrade in v1. Space these introductions rather than crowding the opening levels.
- **Chilled:** test reliable application on a connected attack, then a **50% chance to lose an action on each of the target's next 2–4 turns, including bosses**. This replaces the earlier boss-immunity proposal. It must not stack, and repeated casts should not reset an already-active timer. Boss impact and the risk of making Water investment compulsory need particular testing.
- **Channel:** remains excluded. Flowing Staff supplies Water's extra MP recovery through successful melee hits. No repeatable unconditional MP refill is planned.
- **Wind:** ordinary Cutters should hit 2/4/6 times, with lower early per-hit power. Tune the first tier to show growth soon after investment while Fire keeps the larger opening hits. Wind Walk should help actual running speed in combat; the existing movement code provides a prototype starting point. Prune redundant immobilization/slow spells while keeping Crosswind's Agility debuff. Remove Magnet Rock's automatic single-target role from the proposed Earth kit to reinforce Wind's targeting advantage.
- **Water's own combat loop:** bring Ice Knife and Flowing Staff earlier. A proposed Dousing Wave would combine forward-area damage with lower enemy damage output. Control, close-area attacks and staff MP recycling should work without requiring Earth or overpowering healing.
- **Linked growth:** the first implementation is playable, with rates listed under “Combat and character growth.” Its pacing and catch-up benefits still need a longer playthrough; no element exceeds level 50.
- **Premium MP costs:** prefer spell-specific costs independent of input count. An explicitly described fallback may require the normal 3 MP to cast and drain up to 5 MP, stopping at zero. No negative MP or unsigned wraparound is acceptable.

### Challenge that rewards the new tools

The target is a more demanding but fair adventure, with an approachable first boss and later fights that ask players to use their tools. This is a goal, not a completed difficulty mode. Better recovery and control can make Brian stronger, while reducing overpowered original effects can make some builds weaker; boss tuning must consider both.

Do not assume larger HP, Defense, or Agility values establish which boss is difficult. Compare primary-element, mixed, and evenly distributed builds at similar progress. Solvaring should not require deliberate grinding; later bosses can receive small, targeted adjustments if they become trivial. Avoid a blanket starting-stat reduction before those comparisons. See the [boss balance review plan](docs/boss-balance-plan.md) for current values and test priorities.

### Make choices understandable

A status move should visibly earn its turn and MP cost. Scorch should offer an understandable payoff in follow-up damage, and control effects should make clear what they affect. New-spell notifications and clearer combat feedback are planned so players can discover useful tools naturally.

Avoid displacement and teleport mechanics for this rebalance. We are setting aside forced pushes, pulls, and combat warps instead of making ordinary fights depend on unverified boundary behavior. Wind and Water can control combat through status effects while actors keep their normal movement.

## Spells

### Water spells — our changes

Water starts with healing, but gains a damaging spell at Water 2 so even a small investment provides both options. Healing uses repeated C-down inputs; Water Pillar branches from C-down to C-right.

These are the complete C-button sequences starting from normal movement. The first C-down opens spell selection and selects Healing Lv1; each additional input advances from there.

| Spell | Water level | Input | MP | Compared with French Vanilla |
| --- | ---: | --- | ---: | --- |
| Healing Lv1 | **1** | Down | **1** | Previously Water 7 and 2 MP |
| Healing Lv2 | **17** | Down → Down | **2** | Previously Water 25 and 3 MP |
| Healing Lv3 | **32** | Down → Down → Down | **3** | New tier |
| Water Pillar Lv1 | **2** | Down → Right | **2** | Previously Water 1 and 1 MP; wider area |
| Water Pillar Lv2 | **13** | Down → Right → Right | **3** | Previously Water 4 and 2 MP; wider area |
| Exit | **19** | Down → Left | **2** | Same unlock and cost; moved from Down → Right |
| Return | **24** | Down → Left → Left | **3** | Same unlock and cost; moved from Down → Right → Right |

**Why:** Basic healing should be available immediately, including to players who focus on another element. Stronger healing arrives later because recovering more HP in a single combat turn is a major advantage. Exit and Return move to the old healing inputs so the new Pillar inputs do not replace either travel spell.

The original Water Pillar Lv3 is removed as a separate spell. There are now two wider Pillar tiers:

- **Water Pillar Lv1** uses the old Lv2's area and appearance. Its effect radius increases from 5 to **10**; its power is **300**, compared with French Vanilla's 350.
- **Water Pillar Lv2** uses the old Lv3's area, placement, and appearance. Its effect radius increases from 10 to **15**; its power is **400**, compared with French Vanilla's 340.

**Why:** Water gets useful close-area coverage and a stronger later attack. Power values are calculation inputs, not damage dealt. The three original French Vanilla Pillar values were 350/340/330, compared with the original game's 365/374/382. The radius figures are game units, not a distance shown to players.

### Healing amounts — our changes

Let **W** be your Water level and **H** your maximum HP. Recovery before the existing small random bonus is:

| Spell | HP restored before bonus |
| --- | --- |
| Healing Lv1 | **3 + one third of W + 3% of H** |
| Healing Lv2 | **5 + two thirds of W + 5% of H** |
| Healing Lv3 | **7 + W + 7% of H** |

Round the Water contribution and HP percentage down separately. The game then adds a random amount from zero to one less than a quarter of that result, rounded down. Healing stops at maximum HP.

In the original game and French Vanilla, Healing Lv1 restored half your Water level plus 2% of maximum HP, and Healing Lv2 restored half your Water level plus 8% of maximum HP, with the same bonus rule. At Water 1 and 50 maximum HP, that basic formula would restore **1 HP**; ours restores **4 HP** for 1 MP. At Water 4 and 71 maximum HP, Healing I restores **6 HP**. These formulas affect Brian's direct healing spells; enemy healing retains its existing calculation.

At Water 32 and 200 maximum HP:

| Spell | HP restored, including possible bonus | MP |
| --- | ---: | ---: |
| Healing Lv1 | 19–22 | 1 |
| Healing Lv2 | 36–44 | 2 |
| Healing Lv3 | 53–65 | 3 |

**Why:** Basic healing should help immediately without making a tiny Water investment too strong. Higher tiers restore more in a single turn; basic healing remains economical as Water grows. All three formulas were reduced together to keep the tiers useful. These formulas work both in combat and in the field. Repeated field healing still requires separate casts.

### Earlier tools and revised attacks — our changes

Support tools arrive early enough for an evenly distributed player to discover each element's role. The larger redesign's new spells are still proposals. These are current unlock changes relative to the original game/French Vanilla:

| Spell | Original / FV level | Current level |
| --- | ---: | ---: |
| Power Staff I | 7 | 3 |
| Vampire's Touch | 32 | 5 |
| Fire Ball II | 4 | 7 |
| Power Staff II | 22 | 18 |
| Fire Bomb | 30 | 14 |
| Rock II | 4 | 14 |
| Spirit Armor I | 7 | 3 |
| Rolling Rock I | 10 | 7 |
| Rock III | 16 | 24 |
| Spirit Armor II | 21 | 12 |
| Avalanche | 24 | 38 |
| Rolling Rock II | 39 | 30 |
| Ice Knife | 17 | 4 |
| Invalidity | 46 | 42 |
| Wind Cutter II | 4 | 5 |
| Wind Cutter III | 12 | 18 |
| Evade I | 8 | 3 |
| Wind Bomb | 20 | 12 |
| Cyclone | 28 | 30 |

An early **Wind Walk at Wind 4** uses the former Restriction I path. Vampire's Touch and Homing Arrow I exchange paths, as do Ice Knife and Soul Searcher I, so the early support tools are easier to reach. Wind Walk remains the game's radius effect; the proposed running-speed effect is not implemented.

**Fire Ball:** I/II/III have powers **300/260/190**, with **1/2/3 projectiles**, costing **1/2/3 MP**. Why: Fire I should make a strong first impression. Fire II arrives after time to learn the opening tools and has stronger individual projectiles than French Vanilla's 220, so landing both rewards its extra MP cost. At Fire 7 with Earth 3/Water 4/Wind 4 against 6 Defense, controlled connected-hit results are **13–16 total damage for Fire I** versus **24–30 for Fire II**; this assumes both Fire II projectiles connect.

**Earth attacks:** Rock I/II/III powers are **230/360/440**, compared with French Vanilla's 310/300/290. Why: early Earth emphasizes protection and deliberate attacks, while deeper Earth investment earns stronger Rock upgrades.

Spell power records are shared with enemies, so these power changes also affect enemy casters using the same spells. Enemy-specific boss spells, including Solvaring's Fists and Roar, have separate records.

**Wind Cutters:** I/II/III fire **2/4/6 blades**, instead of 1/3/6, with powers **100/90/80** per blade. Why: multi-hit attacks should define Wind immediately, with less damage in each early blade. Brian's spells also have a minimum raw-power calculation of `power × (element level + 1) ÷ 130`, rounded down, before enemy Defense and damage variation. This helps low-level spells progress; it does not guarantee that every new level adds HP damage.

**Evade I/II:** temporarily use **8×/16× Brian's Agility** for hit checks, compared with the original 2×/4×. These are replacement values, not multiplying the previous buff again. Why: doubling a low starting stat barely affected boss accuracy. At Agility 9 against Solvaring's 17, ordinary hit checks give about **11% misses unbuffed, 35% with Evade I, and 52% with Evade II**. It remains a chance, not a guaranteed dodge, and does not protect against attacks that bypass normal hit checks.

Both Evade tiers last **4–5 enemy turns**, beginning with the enemy turn immediately after casting. Time advances when Brian finishes a turn; individual incoming attacks do not consume duration charges. Against one enemy making one normal hit check per turn, Evade I's 35% miss chance averages 1.4–1.75 dodges over that duration, about one additional dodge compared with Brian's unbuffed chance. A crowd can supply more eligible hit checks during the same time.

**Status application:** ordinary status rolls on enemy targets succeed; Freeze, Restriction and Silence use a **50%** application chance. Self-buff durations are **4–5 turns**. Why: support magic should more often repay its casting turn, while action-denying effects retain uncertainty. The proposed Chilled system is not implemented.

### Other spell balance — inherited from French Vanilla

The following tables show the inherited baseline. The project-specific values above override it for Fire Balls, Rocks, Water Pillars and Wind Cutters.

All player spells have an accuracy rating of **100**. This removes unusually low built-in accuracy as a reason to avoid a spell; enemies can still dodge, so it does not guarantee every hit.

The following are internal spell-power values, **not HP removed per hit**. Defenses, hit counts, and other parts of the calculation still matter.

**Fire:** Basic fireballs and homing arrows are stronger, giving Fire better ranged options. Hot Steam Lv2 is toned down so its close-range damage is less dominant within the element.

| Spell | Original strength | New strength |
| --- | ---: | ---: |
| Fire Ball Lv1 | 240 | 280 |
| Fire Ball Lv2 | 190 | 220 |
| Fire Ball Lv3 | 168 | 190 |
| Homing Arrow Lv1 | 50 | 100 |
| Homing Arrow Lv2 | 50 | 60 |
| Hot Steam Lv2 | 330 | 290 |

**Earth:** The first Rock spell gets a small increase. Later Rock spells, Rolling Rock Lv2, and especially Avalanche are reduced. We are keeping these changes to narrow Earth's offensive advantage while retaining its defensive role. These power values alone do not describe the full difference between spell levels.

| Spell | Original strength | New strength |
| --- | ---: | ---: |
| Rock Lv1 | 290 | 310 |
| Rock Lv2 | 310 | 300 |
| Rock Lv3 | 320 | 290 |
| Rolling Rock Lv2 | 280 | 260 |
| Avalanche | 460 | 350 |

**Wind:** Wind Bomb, Cyclone, and Ultimate Wind are stronger, while Large Cutter receives a small reduction. The aim is to give Wind more worthwhile offensive choices instead of concentrating its strength in one spell.

| Spell | Original strength | New strength |
| --- | ---: | ---: |
| Wind Bomb | 180 | 220 |
| Cyclone | 250 | 300 |
| Ultimate Wind | 100 | 250 |
| Large Cutter | 420 | 400 |

## Enemies and bosses

### Enemy spell choices

**Monsters retain their intended spells after Brian's spell menu is rearranged.** Big Mouth, Crawler and bats use Water Pillar again; enemies meant to heal themselves retain Healing. Ice Knife and Homing Arrow users also keep those attacks. Moving shared spell slots had accidentally changed these enemies' moves, including making Big Mouth cast Healing.

**Why:** Rearranging Brian's menu should not turn enemy attacks into heals or replace their intended abilities. The working ROM includes corrections to 16 spell choices across 13 enemy types. Enemies still inherit the shared spells' current strength and effects. Static checks passed; played enemy battles remain unverified. See the [enemy spell notes](patches/quest65-test5-enemy-fix-README.md) for the affected enemies.

### Solvaring — our changes

| Stat | Original / French Vanilla | Current |
| --- | ---: | ---: |
| HP | 200 | **180** |
| Defense | 15 | **6** |
| Close-range Fists spell power | 550 | **440** |

**Why:** The first boss should test the opening tools without requiring grinding. Lower Defense helps early attacks escape the one-damage floor, and the Fists reduction makes closing in less punishing. His HP stays at 180, Agility at 17, and Roar remains unchanged. Fists' actual pre-Defense power at his current attack level falls from 25 to 20 in the routine check; this is not a promise that every displayed damage number falls by exactly 20%. The revised battle still needs playtesting.

### Boss rewards and buffs — inherited from French Vanilla

- **Boss rewards split the usual maximum-HP bonus between maximum HP and maximum MP, and refill both.** Why: Defeating a boss should support spellcasting as well as health.
- **Boss spells no longer automatically remove your buffs through their hidden buff-cancelling effect.** Why: Defensive and support spells should remain useful in important fights.
- **A problematic Skelebat encounter group in Blue Cave is adjusted.** Why: Reduce the risk of severe slowdown or a crash associated with that group.

## Combat and character growth

These changes are inherited from French Vanilla:

- **Brian starts with 5 Defense instead of 4.** Why: Give a little more protection while learning combat. Starting HP, MP, and Agility are unchanged.
- **Successful staff hits restore 2 MP instead of 1.** Why: Staff attacks provide a more useful way to keep casting without relying as heavily on consumable items.

### Stats and elements grow together — our changes

Ordinary stat growth awards an associated element level at these milestones:

| Stat | Associated element | Milestone |
| --- | --- | --- |
| Maximum HP | Water | Every multiple of 20 |
| Maximum MP | Fire | Every multiple of 4 |
| Defense | Earth | Every multiple of 5 |
| Agility | Wind | Every multiple of 3 |

The other direction also works: each Water level grants **2 maximum/current HP**, and reaching an even Fire/Earth/Wind level grants **1 maximum/current MP / Defense / Agility**, respectively. These increases stop at the stat caps. Bonus writes do not recursively trigger the ordinary-stat milestone hooks.

If the associated element is already at 50, its bonus goes to the lowest element with room to grow. Once all four are at 50, a spirit level-up awards up to **5 HP and 2 MP** instead. HP/MP cap at 500, Defense/Agility at 255.

**Why:** A specialization should develop its supporting stat, while ordinary play gradually opens neglected elements. Agility uses a smaller interval because it grew more slowly than Defense in the first playtest. This is initial pacing, not a measured long-term catch-up rate. No retroactive milestone awards are applied to an existing save. Element levels still stop at 50. The proposed weakness/resistance redesign is not implemented.

## Exploration

These changes are inherited from French Vanilla:

- **Random battles happen less frequently**, using the Reduced encounter setting. Why: Exploring, finding spirits, and revisiting places should involve less repetitive fighting. We still need to assess character growth with fewer encounters.
- **Two easy-to-miss spirits move to clearer locations.** Why: Finding them should reward exploration without requiring a guide to reveal an effectively invisible collectible.
- **Wings work indoors.** Why: Return to town from more places without repeating the walk back. Wings are still restricted on the Isle of Skye.
- **Leaving Shamwood returns you to the Baragoon Tunnel exit.** Why: Cut down on repeated travel after visiting the village.
- **A misleading backward door in Mammon's World is locked.** Why: Make the route forward clearer.

## Items

These changes are inherited from French Vanilla:

- **Monsters can drop an item you already carry.** Why: Carrying a supply should not prevent finding more. This removes an ownership restriction; it does not increase drop rates or change chest rewards.
- **Dew Drops also restore 20 HP.** Why: Give an otherwise limited item another useful purpose.

## Interface and text

These changes are inherited from French Vanilla:

- **The HUD stays visible after it appears.** Why: Keep health and other information available.
- **Dialogue appears at maximum message speed.** Why: Reduce waiting during conversations and repeated messages.
- **The pause menu shows combat experience points needed for the next level instead of a percentage.** Why: Make progress easier to understand.
- **Some text is clarified.** Why: Reduce confusion caused by unclear original wording.

## Testing status

This remains a balance test build. The current changes passed **27,150 isolated routine checks** for healing, buff application, hit rolls, changed stat links, spell power and recipient damage. File checks cover enemy spell references, checksums and patch recovery. Earlier desktop emulator checks in the [emulator test notes](docs/emulator-test-notes.md) apply to test2, not the current ROM. Current rendered battles, projectile connections, Solvaring balance, save/load, Android/M64Plus FZ and a full playthrough remain unverified. The [first playtest checkpoint](docs/playtest-notes.md) records the actual Test 5 experience behind these adjustments.

For build history, source versions, file hashes, and technical verification, see the [development log](docs/development-log.md). Planned features remain in the [wishlist](docs/wishlist.md).
