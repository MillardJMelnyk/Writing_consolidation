# Ethernet cable affecting internet speed

| | |
|---|---|
| Date | 2026-09-05 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-d89e1fda` |
| Links | [Original](https://claude.ai/chat/d89e1fda-f2b9-415b-8363-369fd8a622a8) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-09-05_ethernet-cable-affecting-internet-speed_d89e1fda.html) |

**Summary:** Troubleshoots slow internet when a neighbor's ethernet cable is plugged into the shared modem, covering QoS, router login and Telmex support.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting; Practical & personal > Restaurants and local services in Mexico

**Index terms:** ethernet cable; bandwidth; quality of service; router admin; Telmex; ipconfig

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-09-05 18:36

is there a type of ethernet cable that would take up all the internet on a modem making it so even though i have an ethernet cable my internet will still be sl`ow?

### Claude · 2026-09-05 18:36

No — no cable "takes" bandwidth, but a damaged or old Cat5 cable can cap the link at 100 Mbps.

### Millard · 2026-09-05 18:37

it seems like when our neighbour has his cable plugged in my internet drops dramatically

### Claude · 2026-09-05 18:37

That's him consuming shared bandwidth, not his cable — your connection is split between everyone on the modem.

### Millard · 2026-09-05 18:37

what could he be doing taking so much bandwidth?

### Claude · 2026-09-05 18:37

Torrenting, cloud/game downloads, 4K streaming, or console/PC updates.

### Millard · 2026-09-05 18:38

is there something i can do to stop it or make my connection better?

### Claude · 2026-09-05 18:38

Enable QoS on the router to cap his port or prioritize your device.

### Millard · 2026-09-05 18:38

how do i enable Qos on the router?

### Claude · 2026-09-05 18:38

Log into the router's admin page (usually 192.168.1.1 or 192.168.0.1), find QoS or Bandwidth Control under Advanced, enable it, set your total line speed, then either prioritize your device's MAC/IP or cap his.

### Millard · 2026-09-05 18:39

i cant log in to routers admin page

### Claude · 2026-09-05 18:39

Then you don't control the router — talk to whoever does, or run your own router behind the modem.

### Millard · 2026-09-05 18:39

i mean with the ip you sent

### Claude · 2026-09-05 18:39

Run `ipconfig` in Command Prompt — the "Default Gateway" address is your router's real IP.

### Millard · 2026-09-05 18:40

when i run that command a window opens and then just quickly closes

### Claude · 2026-09-05 18:40

Open Command Prompt first (search "cmd", press Enter), then type `ipconfig` inside that window.

### Millard · 2026-09-05 18:41

C:\Users\kmeln>ipconfig  
Windows IP Configuration  
Ethernet adapter Ethernet:  
Connection-specific DNS Suffix . :  
IPv6 Address. . . . . . . . . . . : 2806:2f0:6401:fff8:b567:24c9:11a0:1e3a  
IPv6 Address. . . . . . . . . . . : fda2:8eea:92f0:6a00:12e7:8952:5cfb:8cf3  
Temporary IPv6 Address. . . . . . : 2806:2f0:6401:fff8:c9ad:78:7069:af2a  
Temporary IPv6 Address. . . . . . : fda2:8eea:92f0:6a00:55d:efe2:f498:c99c  
Link-local IPv6 Address . . . . . : fe80::f90e:438d:84ff:10ca%11  
IPv4 Address. . . . . . . . . . . : 192.168.100.121  
Subnet Mask . . . . . . . . . . . : 255.255.255.0  
Default Gateway . . . . . . . . . : fe80::1%11  
192.168.100.1  
Wireless LAN adapter Local Area Connection *8:  
Media State . . . . . . . . . . . : Media disconnected  
Connection-specific DNS Suffix . :  
Wireless LAN adapter Local Area Connection* 10:  
Media State . . . . . . . . . . . : Media disconnected  
Connection-specific DNS Suffix . :  
Wireless LAN adapter Wi-Fi:  
Media State . . . . . . . . . . . : Media disconnected  
Connection-specific DNS Suffix . :  
C:\Users\kmeln>

### Claude · 2026-09-05 18:41

Go to http://192.168.100.1 in your browser.

### Millard · 2026-09-05 18:53

could i test if this is happening without logging into the ip modem thing online?

### Claude · 2026-09-05 18:53

Yes — run a speed test while his cable is plugged in, then again with it unplugged, and compare.

### Millard · 2026-09-05 18:53

if i switch my cable to the port he is using would that work?

### Claude · 2026-09-05 18:53

No — all ports share the same internet connection, so the port makes no difference.

### Millard · 2026-09-05 18:53

but can he cap the internet on certain inputs?

### Claude · 2026-09-05 18:53

Only if he can log into the router — then yes, he could throttle your port specifically.

### Millard · 2026-09-05 18:54

i know when i unplug his cable it makes my internet faster, why is that?

### Claude · 2026-09-05 18:54

Because his device stops pulling bandwidth from the shared line the moment it's disconnected.

### Millard · 2026-09-05 18:54

if i plug in my cable into his and it is fatser what does that mean?

### Claude · 2026-09-05 18:54

That your cable or your port is bad — swap one at a time to find which.

### Millard · 2026-09-05 18:55

what if all other ports are bad except his?

### Claude · 2026-09-05 18:55

Then either the modem's other ports are dead, or someone configured that port as the only unthrottled one.

### Millard · 2026-09-05 18:56

what would the login be?

### Claude · 2026-09-05 18:56

Try `telecomadmin` / `admtelecom`, or `admin` / `admin`.

### Millard · 2026-09-05 18:56

and apss?

### Claude · 2026-09-05 18:56

Those are the passwords: `admtelecom` for telecomadmin, `admin` for admin.

### Millard · 2026-09-05 18:56

no they didnt work

### Claude · 2026-09-05 18:57

Then the password was changed from default — get it from whoever set up the modem (ISP or landlord), or factory-reset it (knocks everyone offline and wipes the config).

### Millard · 2026-09-05 18:57

how do i factory reset it?

### Claude · 2026-09-05 18:57

Physical button: with the modem powered on, press the pinhole "Reset" on the back for ~10 seconds until the lights blink.

But before you do — that's a Huawei fiber ONT, not a normal router. A reset wipes the ISP's fiber config (GPON/PPPoE), and it usually won't reconnect until the ISP re-provisions it. You'd likely knock the whole line offline — you and the neighbor — with no way to fix it yourself.

### Millard · 2026-09-05 18:59

how can i get into the site to see if the ports have been throttled?

### Claude · 2026-09-05 18:59

You already have the two things you need to try: the address (http://192.168.100.1) and the default logins, which didn't work. There's no other trick to get in — no cable swap, no port change, and no "see the settings without logging in" gets you past a password that's been changed. Login is the only door.

So realistically your options are:

Get the real password from whoever set the modem up — the ISP (their name is on the modem or your bill) or the landlord. On ISP-provided Huawei ONTs the `telecomadmin` account often has a unique password printed on a sticker on the modem itself, so check the label.

Or stop trying to fix the shared modem and put your own router behind it — your traffic sits on your own device that the neighbor can't see or throttle, and you control its QoS. That sidesteps the login problem entirely.

One thing worth saying plainly: the picture where every port is dead except his, and your speed jumps when you unplug him, is also just what normal bandwidth sharing looks like. You've confirmed he's a heavy user; you haven't actually confirmed anyone throttled a port. Don't factory-reset chasing a setting that may not exist — the reset risks the whole line.

### Millard · 2026-09-05 19:00

so if he has that he can see my traffic?

### Claude · 2026-09-05 19:00

Short answer: not really, and not from what you've described.

If he's just another device plugged into the same modem, he cannot see the contents of your traffic. Modern sites use HTTPS, so even on a shared connection he can't read your messages, passwords, or what's on your screen.

What someone *could* see, and only if they have the admin login to the modem, is coarse info: which devices are connected, their IP/MAC addresses, and rough traffic volume per device. That's it — not the actual content. And that requires the password you've established you don't have.

The person who actually controls your traffic is whoever holds that admin login — likely the ISP or whoever set the modem up. Not a neighbor on another port, unless he's the one who set it up.

If privacy is the worry, your own router behind the modem fixes it: your devices sit on their own private network that nobody else on the modem can see into.

### Millard · 2026-09-05 19:01

if i call telmex could they give the login info?

### Claude · 2026-09-05 19:01

Maybe — but expect friction, and it depends on whose account it is.

If the Telmex account is in your name, call 800 123 2222, verify your identity, and ask for the admin credentials or ask them to reset them remotely. They can push config to the ONT from their end.

The catch: Telmex support usually won't hand over the `telecomadmin`-level password. They tend to either keep it, or make changes for you remotely rather than giving you full access. You can ask them directly to enable QoS or prioritize your device — that's a reasonable request they can sometimes action without giving you the login.

If the account is *not* in your name — it's the landlord's or a housemate's — Telmex won't give you anything; they'll only talk to the account holder. In that case go to whoever's name is on the bill.

One thing to have ready: the answer to "why." "My internet is slow and I want to manage bandwidth" gets further than anything about a neighbor's port, which invites questions you don't want.
