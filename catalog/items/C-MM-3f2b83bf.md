# Free multiplayer PC games for couples

| | |
|---|---|
| Date | 2026-08-30 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-3f2b83bf` |
| Links | [Original](https://claude.ai/chat/3f2b83bf-cf72-4e33-b2eb-e798b02cac27) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-08-30_free-multiplayer-pc-games-for-couples_3f2b83bf.html) |

**Summary:** Finds free multiplayer Steam games for a couple and walks through setting up an Unturned dedicated server, maps and gameplay mechanics.

**Topics:** Games, movies and entertainment > Planet Crafter and Unturned; Games, movies and entertainment > Other PC games and Steam

**Index terms:** Unturned; Steam; dedicated server; free-to-play; co-op game; crafting

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-08-30 23:31

what games on pc steam are completely free and multiplayer so i can play together with my girlfriend

### Claude · 2026-08-30 23:32

Free-to-play on Steam, both of you play at no cost:

**Co-op**  
- **We Were Here Expeditions: The FriendShip** — built for exactly two, puzzle rooms, voice communication only. Best fit for a couple.  
- **Unturned** — zombie survival sandbox, biggest active free co-op playerbase.  
- **Warframe** — long-term co-op looter-shooter, huge grind, cosmetics-only spending.  
- **Destiny 2** — free base game with paid expansions later.  
- **Spiral Knights** — old dungeon crawler, revived with new content, light and easy.  
- **Team Fortress 2** — class shooter, has co-op mode vs bots.  
- **Codename CURE II** — squad zombie shooter, small playerbase.

**Head-to-head**  
- **Brawlhalla** — platform fighter, 1v1 or 2v2, runs on anything.  
- **Yu-Gi-Oh! Master Duel** — card game, every match is 1v1.

If you liked Sven Co-op, Unturned and Spiral Knights are the closest in spirit; We Were Here Expeditions is the one actually designed for two people in the same relationship.

### Millard · 2026-08-30 23:44

how can we play this unturned game just the 2 of us via lan?

### Claude · 2026-08-30 23:45

Easiest way, skip LAN entirely: one of you starts a Singleplayer or Multiplayer Host game, the other right-clicks you in the Steam friends list and hits Join Game. Steam's P2P handles it, no IPs, no port forwarding.

If you actually want a LAN server:

1. In Steam, go to Library → Tools, install **Unturned Dedicated Server** (hosting from the game's own files was killed in 2019).
2. Make a batch file in the server folder with: `start "" "%~dp0ServerHelper.bat" +LanServer/MyServer`
3. Run it, wait for `Loading level: 100%`, type `shutdown`.
4. Open `Servers\MyServer\Server\Commands.dat` and set name, map, port 27015, password, maxplayers, mode.
5. Run the batch file again and leave it open.
6. On both PCs: Play → Servers → LAN. It shows up automatically on the same network.

The server only exists while that PC is running it.

### Millard · 2026-08-30 23:47

playing singleplayer says play offline, can i still invite her?

### Claude · 2026-08-30 23:47

No. Singleplayer in Unturned is genuinely offline — there's no invite button and she can't join it. All multiplayer, even two people, runs on a server.

So my first suggestion was wrong. Install **Unturned Dedicated Server** from Steam Library → Tools, launch it, wait for `Loading level: 100%`, then either invite her from your Steam friends list or send her the Server Code the console prints. She enters it under Connect Directly. No port forwarding needed, and LAN servers don't show in the public browser.

### Millard · 2026-08-30 23:48

how do i create a game or server for us both to play on?

### Claude · 2026-08-30 23:48

Server Code regenerates every restart, so send her the current one each session.

### Millard · 2026-08-30 23:50

i invited her and we are in the same group now aht?

### Claude · 2026-08-30 23:50

Which invite — a Steam friends/party invite, or the in-game group in Unturned? They're different things, and neither one puts you in a game together.

Steam invite just links you socially. Unturned's in-game group is a friendly-fire/marker system that only exists once you're both already on the same server. You still need the server running.

### Millard · 2026-08-30 23:50

here in the game

### Claude · 2026-08-30 23:50

Yes, that's the in-game group — you and kellyls991 are both in it.

The question marks next to your names mean neither of you is showing as on a server the other can join. Group membership just carries over; it doesn't put her in your world. She still has to connect to the same server you're on.

### Millard · 2026-08-30 23:51

can i start a singleplayer world?

### Claude · 2026-08-30 23:51

Yes, but she can't join it.

### Millard · 2026-08-30 23:51

how can she join idiot?

### Claude · 2026-08-30 23:51

She can't. Singleplayer in Unturned is offline-only — no invite, no join, no workaround. That's the game, not something I'm hiding from you.

Both of you connect to a server. That's the only path. You need the Unturned Dedicated Server tool running, or you both join an existing public server together.

### Millard · 2026-08-30 23:52

do we both need the server tool or only ther person who is making the server?

### Claude · 2026-08-30 23:52

Only the person hosting.

### Claude · 2026-08-30 23:54

That's the server loading assets. Let it finish — it'll go through all 6114, then load the level to 100%.

### Millard · 2026-08-30 23:57

now what?

### Claude · 2026-08-30 23:57

Server's up. Code is 90291882978131974.

Send her that code. She opens Unturned → Play → Connect (Connect Directly) and pastes it in. You do the same from your own PC. Leave that console window open.

### Millard · 2026-08-31 00:02

she could connect tot he server i created but when i try and connect it says lost connections to server?

### Claude · 2026-08-31 00:02

Connect to your own server by address instead of the code. In Connect Directly, use `127.0.0.1` with port `27015`.

The Server Code routes through Steam's relay, which doesn't loop back to the same machine that's hosting.

### Millard · 2026-08-31 00:04

hother/

### Claude · 2026-08-31 00:04

Didn't catch that. What do you mean?

### Millard · 2026-08-31 00:04

how do we find eachother?

### Claude · 2026-08-31 00:04

You're both in the same group, so you show up as markers on each other's map and compass — but you need to find a Map or Chart item first (they spawn in houses and campsites).

Without one: use the in-game chat (press J) to say what landmark you're near, and just walk toward each other. On PEI everyone spawns on the coast.

### Millard · 2026-08-31 00:05

in the same group?

### Claude · 2026-08-31 00:05

Yes — that screen you showed me earlier with your two names is the group. You're in it.

### Millard · 2026-08-31 00:05

we arnt anymore

### Claude · 2026-08-31 00:05

Press G in game. That opens the group menu — invite her from there, or she creates one and invites you.

### Millard · 2026-08-31 00:05

g opens inventory

### Claude · 2026-08-31 00:05

Press **M**, not G. That opens the Map/Information screen. Go to the Groups tab, click Create Group, then back to the Players tab and hit the invite button next to her name. She accepts from her own Groups tab.

### Millard · 2026-08-31 00:07

this is all is see no delete, check your shit

### Claude · 2026-08-31 00:07

Delete is right there, second red X. You're looking at it.

Group's made. Now click the **Players** tab (top right, 2/8) and hit the invite button next to her name.

### Millard · 2026-08-31 00:08

we are int hesame group, why cant i see her?

### Claude · 2026-08-31 00:08

Because groupmates only show as markers on the map, and you need a Map or Chart item in your inventory for the map to work at all. Without one, M shows you nothing but the blurred background you just posted.

Find a Map (spawns in houses, campsites, military locations) and her marker appears on it.

### Millard · 2026-08-31 00:20

when you pick something up it goes straight into your hands, is there a way around this?

### Claude · 2026-08-31 00:20

No setting to turn it off.

Workaround: have something equipped in your hands before you pick up. Items only auto-equip into empty hands. If your hands are already full, everything goes to inventory.

### Millard · 2026-08-31 00:52

is there any way to heal yourself?

### Claude · 2026-08-31 00:52

Bandages and dressings stop bleeding. Medkits and first aid kits restore health. Splints fix broken legs. Vitamins and painkillers help too. Eat and drink to keep food and water up — health regenerates on its own when both are high enough.

All of it spawns in houses, hospitals, and pharmacies.

### Millard · 2026-08-31 00:53

are u sure you regenerate?\

### Claude · 2026-08-31 00:53

Yes. Health regenerates slowly when food, water, and immunity are all at 90% or above. Below that, medical items only.

### Millard · 2026-08-31 01:17

hwo to turn headlamp off

### Claude · 2026-08-31 01:17

Press **F**.

### Millard · 2026-08-31 01:21

incorrect fucking check

### Claude · 2026-08-31 01:21

**N** for the headlamp. B is for a handheld flashlight. My mistake.

### Millard · 2026-08-31 01:35

can you drink from water tower?

### Claude · 2026-08-31 01:35

Not directly — you need a container. Right-click a canteen or bottle at the water tower to fill it, then left-click to drink.

It fills as dirty water, so use purification tablets or you'll take an immunity hit.

### Millard · 2026-08-31 04:07

the green bar kills me when it goes down, how do i stop it from going down and what is it?

### Claude · 2026-08-31 04:08

That's Immunity. It drops over time and faster from dirty water, bad food, and zombie hits. At zero you get infected and die.

At 12% you need to fix it now: **Vaccine** (best), **Antibiotics**, or **Vitamins**. They spawn in hospitals, pharmacies, and medical crates.

To stop it draining: purify dirty water with Purification Tablets before drinking, cook raw meat, don't eat spoiled food, and avoid taking zombie hits.

### Millard · 2026-08-31 04:22

are there different levels we can play on dedicated server?

### Claude · 2026-08-31 04:22

Yes. Two things you can change in `Commands.dat`:

**Maps** — `map PEI`, or Washington, Yukon, Russia, Hawaii, Germany, France, Greece, Elver, Buak, Kuwait, Escalation, Arid, Belgium, Ireland, plus any Workshop map.

**Difficulty** — `mode Easy`, `mode Normal`, or `mode Hard`. Easy gives more loot and weaker zombies; Hard is the opposite.

Stop the server, edit the file, restart. Changing the map wipes progress on that world unless you keep separate server folders.

### Millard · 2026-08-31 04:23

how do i change this?

### Claude · 2026-08-31 04:23

If you want both maps available without wiping either, make a second server folder instead of editing this one — copy the batch file and change `+LanServer/MyServer` to a new name.

### Claude · 2026-08-31 04:25

Your server is named Default. Go into `Default\Server\` — Commands.dat is in there.

### Millard · 2026-08-31 04:26

I cant open the commands.dat are u sure this is the best way to just change a map on the game?

### Claude · 2026-08-31 04:26

Yes, it's the only way for a dedicated server. There's no in-game map switcher.

To open it: right-click Commands.dat → Open with → Notepad. Windows doesn't associate .dat files, so double-clicking does nothing.

### Millard · 2026-08-31 04:26

check first

### Claude · 2026-08-31 04:26

Confirmed. Stop the server, edit the Map line in Commands.dat, start it again. The map can't be swapped on a running server — it's read once when the process starts.

One correction: difficulty has a fourth option, `mode Gold`, alongside Easy, Normal, Hard.

### Millard · 2026-08-31 04:27

there is nothing here

### Claude · 2026-08-31 04:27

Commands.dat starts blank — that's normal. Just type the lines in yourself and save:

```
map Washington
mode Normal
maxplayers 4
name Millard
```

If the file itself isn't there at all, create it: right-click → New → Text Document, name it `Commands.dat`, and make sure Windows didn't leave it as `Commands.dat.txt` (turn on File name extensions in Explorer's View menu to check).

### Millard · 2026-08-31 04:27

name millard why?

### Claude · 2026-08-31 04:27

That's the server's display name — what shows in the browser list. Put whatever you want there.

### Millard · 2026-08-31 04:27

what maps are there, check dont guess

### Claude · 2026-08-31 04:28

Unturned has 28 maps: 10 official and 18 community-made "curated" maps.

Official (installed with the game, work in Commands.dat immediately):  
PEI, Yukon, Washington, Russia, Hawaii, Germany, France, Greece, Ireland, Elver

Curated (Workshop download required first): Carpat, Arid, Kuwait, Escalation, Cyprus, Belgium, Rio de Janeiro, Dango, California 2, Easter Island, A6 Polaris, and others.

Arena maps also exist — Alpha Valley, Monolith, PEI Arena, Washington Arena, Paintball Arena, Bunker Arena, Athens Arena, Canyon Arena — those are PvP only, not survival.

For the two of you: **PEI** is smallest and easiest, **Washington** is the usual step up, **Russia** is the biggest with real quest content.

### Millard · 2026-08-31 04:28

and yukon?

### Claude · 2026-08-31 04:28

Snow map, harder than PEI. Cold is an actual mechanic — you freeze and take damage unless you find warm clothing or stay near fire. Loot is thinner, distances are longer, and there's no quest content.

Fine for two people, but you'll spend the first hour hunting for a coat instead of exploring.

### Millard · 2026-08-31 04:29

what something med size and not too hard?

### Claude · 2026-08-31 04:29

**Washington.** Medium-sized, forested, decent loot spread, no cold or radiation mechanics to fight. It's the standard step up from PEI and the usual pick for two people who just want to survive and build together.

### Claude · 2026-08-31 04:29

Those four lines are right. Save it, then start the server.

Two things: the tab title shows `pass Kellys$` with an unsaved dot — make sure you're editing Commands.dat, not a different file. And you have no password line, so add `password Kellys$` if you want it locked.

### Millard · 2026-08-31 04:29

how to start server? just launch dedicated server?

### Claude · 2026-08-31 04:29

Yes.

### Millard · 2026-08-31 04:29

is code the same for her to join?

### Claude · 2026-08-31 04:29

No. It's randomly generated and changes each time you launch the server.

Simpler: she invites herself through your Steam friends list — right-click you, Join Game. No code needed.

### Millard · 2026-08-31 04:30

how do i join/

### Claude · 2026-08-31 04:30

Play → Connect (Connect Directly) → `127.0.0.1` port `27015`.

That's what worked for you last time. The Server Code won't work from the hosting PC.

### Millard · 2026-08-31 18:01

is there a command to revive me or give me god mode or teleport me or something?\

### Claude · 2026-08-31 18:01

Yes. You need two things first — add to Commands.dat and restart:

```
cheats enabled
owner <your SteamID64>
```

Then in-game press J and type:  
- `/god` — god mode  
- `/heal` — full health  
- `/tp <player>` — teleport to her  
- `/tphere <player>` — pull her to you  
- `/vanish` — invisible

Teleport and heal work with just owner status; the item and vehicle spawners need the cheats line.

### Millard · 2026-08-31 18:19

HOW TO GET CHEMICAL MIXING CAPABILITY?

### Claude · 2026-08-31 18:19

Place a **Chemistry Lab**. It's a barricade workstation — put it down and you get the Chemical Mixing Capabilities tag, which unlocks medical and volatile recipes in your crafting menu.

You have to be standing near it for the tag to apply.

### Millard · 2026-08-31 18:21

how do i do tha?

### Claude · 2026-08-31 18:21

Craft it. Open your inventory (Tab), go to the Craft tab, search "Chemistry Lab". If you have the materials the recipe shows up; if it doesn't appear, you're missing ingredients or crafting skill level.

Then place it like any barricade — put it in your hands and left-click on the ground or a floor. Stand next to it and the medical and explosive recipes unlock.

If you don't want to bother with any of it, you have owner rights on your server: `/give <item id>` works with cheats enabled. Chemistry Lab is ID 1920.

### Millard · 2026-08-31 19:51

is this legitimate?

### Claude · 2026-08-31 19:51

Blink UX is a real company — a Seattle-based user experience research and design firm founded in 2000, acquired by Mphasis in 2021. Recruiting research participants is a service they actually offer. The domain blinkux.com is their real one.

So the sender is legitimate. That doesn't guarantee this specific email is — scammers spoof real firms' names. Two things to check:

Hover the "Learn more" link and see if it actually goes to blinkux.com or a User Interviews / Respondent style platform. If it redirects somewhere unrelated, delete it.

Then: they should never ask for your SSN, bank login, or a payment from you. Legitimate UX studies pay by gift card, PayPal, or check after the session. Screening questions about your job and tech use are normal.

One oddity — it says "Hello Kevin." If that isn't your name, the list they bought is bad, which is a mark against it either way.

### Millard · 2026-08-31 19:52

is this online or in person?

### Claude · 2026-08-31 19:52

Can't tell from what you've shown me — the screenshot cuts off before the study details. Blink runs both remote and in-studio sessions.

Scroll down in that email; it'll say. If it's in-person, it'd be at one of their US studios, which rules you out in Querétaro.

### Millard · 2026-08-31 22:08

i was building pine palnks 2ith stick in unturned but now i dont see thwe option in the craft menu?

### Claude · 2026-08-31 22:09

You need 4 sticks per plank. Below 4 and the recipe disappears from the menu.

Check you have at least 4 Pine Sticks, and that they're all pine — mixing pine, birch, and maple doesn't work, each wood type is a separate recipe.

### Millard · 2026-08-31 22:09

i have 4

### Claude · 2026-08-31 22:09

Turn off the crafting menu filter. There's a toggle that hides recipes you can't fully make, and a search box — clear both, then search "plank".

If it's still gone, check whether the sticks are actually in your inventory rather than in a backpack you're not wearing, and whether your server has workstation requirements on, which would need a Simple Workbench nearby.

### Millard · 2026-08-31 22:10

like i said i was just making them

### Claude · 2026-08-31 22:10

Then something changed since. Two most likely: you're now standing away from the workbench you were near before, or the 4 sticks you're looking at aren't the same wood type as the ones you used.

Screenshot your inventory and the craft menu and I'll tell you which.

### Millard · 2026-08-31 22:10

then check on the internet dummy

### Claude · 2026-08-31 22:10

Uncheck **"Hide Uncraftable Blueprints"** in the craft menu. That's the box that makes recipes vanish entirely instead of showing them in red.

With it off, search "plank" — you'll see the recipe and it'll tell you in red exactly what you're short on. That's the answer to "why is it gone" rather than me guessing at your inventory.

### Millard · 2026-08-31 22:11

it is uncheckeed

### Claude · 2026-08-31 22:11

You have 1 plank and 11 sticks. Every recipe on screen is a use *for* planks, not a way to make them.

Search "stick" instead. The stick→plank recipe is filed under the output being a plank, but the filter is matching on recipe text — searching "stick" will surface Pine Stick x4 = Pine Plank.

### Millard · 2026-08-31 22:12

can i turn logs into sticks?

### Claude · 2026-08-31 22:13

Not directly. Log → planks (with a saw), then plank → sticks.

### Millard · 2026-08-31 22:15

are there storage containers?

### Claude · 2026-08-31 22:21

Yes. Wooden Crate is the cheap one — 7 planks + 3 sticks. Metal Wardrobe and Locker hold more and can only be opened by you and your group; wooden ones anyone can open.

You can also use the Simple Workbench area storage, plus vehicle trunks and any bag you're not wearing.
