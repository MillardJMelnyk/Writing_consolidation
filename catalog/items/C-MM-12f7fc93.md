# Sven Coop console commands

| | |
|---|---|
| Date | 2026-08-03 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-12f7fc93` |
| Links | [Original](https://claude.ai/chat/12f7fc93-6829-4980-ab2d-0a1bb050b4d8) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-08-03_sven-coop-console-commands_12f7fc93.html) |

**Summary:** Sven Co-op console commands, cheat requirements, and how to get unstuck or fly with noclip.

**Topics:** Games, movies and entertainment > Other PC games and Steam

**Index terms:** Sven Co-op; console command; sv_cheats; noclip; stuck command

[← Catalog home](../README.md)

---

### Millard · 2026-08-03 22:13

what sven coop console commands?

### Claude · 2026-08-03 22:13

Console must be enabled first (Options → Advanced → Enable Developer Console, or `-console` launch option; open with `~`).

**Cheats** — require `sv_cheats` on, and only work on servers with 3 or fewer max players (LAN is exempt). `sv_cheats 1` = everyone, `2` = admins, `3` = owner/operator only.  
- `godmode 0/1`  
- `cl_noclip 0/1`  
- `giveall`  
- `ghost 0/1`  
- `mygravity 0.75` (fraction of normal)  
- `impulse 101` (all weapons/ammo), `impulse 100` (flashlight), `impulse 201` (spray)  
- `notarget`, `kill`

**Server/game**  
- `map <name>`, `changelevel <name>`, `restart`  
- `maxplayers <n>`, `sv_lan 0/1`, `sv_password <pw>`  
- `mp_survival_mode 0/1/2`, `mp_flashlight 0/1`, `mp_timelimit <min>`  
- `mp_allowmonsterinfo`, `mp_banana`, `mp_barnacle_paralyze`, `mp_disablegaussjump`  
- `sk_*` skill variables (full list in svencoop/skill.cfg), e.g. `sk_headcrab_health`  
- `rcon_password <pw>`, `rcon <command>`, `status`, `kick <name>`

**Client**  
- `name <name>`, `bind <key> <command>`, `unbind <key>`  
- `fps_max`, `net_graph 3`, `hud_fastswitch 1`, `sensitivity`  
- `cmdlist`, `cvarlist` — dumps everything available on your build

Full reference: wiki.svencoop.com/Console/Variables

### Millard · 2026-08-04 00:39

is there a awy to fly or unstuck?

### Claude · 2026-08-04 00:39

**Unstuck:** yes — `stuck` is a built-in console command that frees you (bound to **L** by default). It only fires if the game actually detects you inside geometry — wedged between angled surfaces often won't register, in which case it's `kill` (K) or a server's own `/stuck` command. Drop rare weapons with G before killing yourself so you can pick them back up. Stuck on a teammate: have someone crowbar you and walk away — melee drags you loose.

**Fly:** only `cl_noclip 1` — a cheat, so `sv_cheats` must be set and, on internet servers, max players 3 or fewer. No way to do it on a normal public server.
