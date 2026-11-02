# Mobile hotspot connection failing on laptop

| | |
|---|---|
| Date | 2026-09-03 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-3928c8ce` |
| Links | [Original](https://claude.ai/chat/3928c8ce-91be-45bd-90b8-ed840af4d237) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-09-03_mobile-hotspot-connection-failing-on-laptop_3928c8ce.html) |

**Summary:** Troubleshoots a Windows mobile hotspot stuck on obtaining IP via ICS and static IP fixes, then checking modem bandwidth use by a housemate.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting; Practical & personal > Phones, WhatsApp, Facebook and social media accounts

**Index terms:** mobile hotspot; Internet Connection Sharing; IP address; Motorola; Totalplay; bandwidth monitoring

[← Catalog home](../README.md)

---

### Millard · 2026-09-03 22:07

my mobile hotspot was working fine before on my laptop so that i could connect my phone to it but now my phone cant connect and just stays on obtaining ip before stopping trying to connect

### Claude · 2026-09-03 22:07

Assuming Windows laptop — the hotspot's DHCP (Internet Connection Sharing) has died. Fixes in order:

1. Toggle the hotspot off, wait 10 seconds, toggle on. Then forget the network on your phone and reconnect.
2. Restart the ICS service: Win+R → `services.msc` → **Internet Connection Sharing (ICS)** → right-click → Restart. If it's set to Disabled or Manual, set Startup type to Automatic first.
3. Re-share the connection: Control Panel → Network Connections → right-click your internet adapter (Wi-Fi or Ethernet) → Properties → Sharing tab → untick "Allow other network users to connect", OK, then re-tick it and pick the hotspot adapter (Local Area Connection\* something).
4. If still stuck, elevated Command Prompt:

```
netsh winsock reset
netsh int ip reset
ipconfig /flushdns
```

then reboot.  
5. Last resort: Device Manager → View → Show hidden devices → uninstall **Microsoft Wi-Fi Direct Virtual Adapter** entries, then Scan for hardware changes.

Third-party VPN or antivirus with a network filter driver is the usual thing that breaks this after it was previously working — disable it before testing if you have one.

### Millard · 2026-09-03 22:10

Restart the ICS service: Win+R → `services.msc` → Internet Connection Sharing (ICS) → right-click → Restart. If it's set to Disabled or Manual, set Startup type to Automatic first.

i did this and now it sayd connected with no internet access?

### Claude · 2026-09-03 22:10

That's progress — DHCP is working now, so it's NAT/routing, not the hotspot itself.

1. Check the laptop actually has internet right now. Open a page on it. If it doesn't, nothing downstream will.
2. Re-do the sharing binding, since restarting ICS often drops it: Control Panel → Network and Sharing Center → Change adapter settings → right-click the adapter that has your internet → Properties → Sharing → untick the box, OK → reopen → tick it → in the dropdown pick the hotspot adapter → OK. Then toggle the hotspot off/on.
3. Forget the network on the phone and rejoin, so it pulls a fresh gateway and DNS.
4. If it's still no-internet, set DNS manually on the phone's Wi-Fi (static/advanced): 8.8.8.8 and 1.1.1.1. If that fixes it, ICS's DNS proxy is the problem.
5. Elevated Command Prompt, then reboot:

```
netsh int ip reset
netsh winsock reset
ipconfig /flushdns
```

One thing that will block this permanently: if the laptop's own internet is a cellular/USB-tethered connection, some carriers and some Windows builds refuse to share it onward. Was the laptop on Wi-Fi or Ethernet when this used to work?

### Millard · 2026-09-03 22:10

i mean i am talking to you so it obviously does have internet

### Claude · 2026-09-03 22:10

Fair. Then it's the NAT binding — the laptop routes for itself but isn't forwarding for the hotspot.

Do this in order:

1. Control Panel → Network and Sharing Center → Change adapter settings → right-click the adapter carrying your internet → Properties → Sharing tab. Untick "Allow other network users to connect", OK. Reopen, tick it, select the hotspot adapter in the dropdown, OK. Toggle the hotspot off and on.
2. Forget the network on the phone, rejoin.
3. If still no internet, set the phone's Wi-Fi DNS manually to 8.8.8.8 / 1.1.1.1.
4. If that fixes it, ICS's DNS proxy is broken — restart the "DNS Client" service on the laptop.

If the sharing dropdown has no hotspot adapter listed, the virtual adapter is stale: Device Manager → View → Show hidden devices → uninstall Microsoft Wi-Fi Direct Virtual Adapter entries → Scan for hardware changes → restart hotspot.

### Millard · 2026-09-03 22:15

there is no network and sharing

### Claude · 2026-09-03 22:15

Two things:

**Adapter list** (the old Network and Sharing Center is hidden in Win11): Win+R → type `ncpa.cpl` → Enter. That's the same window. Right-click your Wi-Fi adapter → Properties → Sharing tab.

Or: Advanced network settings → **More network adapter options**.

**But first**, click the `>` arrow on the Mobile hotspot row. On that page check:  
- **Share my Internet connection from** = Wi-Fi  
- **Share over** = Wi-Fi

If "Share from" is set to Ethernet, that's your no-internet — Ethernet has no connection. Set it to Wi-Fi, toggle the hotspot off and back on, then forget/rejoin on the phone.

### Claude · 2026-09-03 22:16

Correction to my last message — your internet is on **Ethernet**, not Wi-Fi. The Wi-Fi adapter is not connected.

1. In the Mobile hotspot settings page, set **Share my Internet connection from** = **Ethernet**. Share over = Wi-Fi.
2. In this adapter window, right-click **Ethernet** → Properties → **Sharing** tab → untick "Allow other network users to connect", OK. Reopen it, tick it, and in the dropdown select **Local Area Connection\* 10**. OK.
3. Toggle the hotspot off and on, forget the network on the phone, rejoin.

If the Sharing tab is missing on Ethernet, tell me.

### Millard · 2026-09-03 22:17

thats how it always has been

### Claude · 2026-09-03 22:17

Settings are correct. Do step 2 then — the ICS binding is what's broken.

In `ncpa.cpl`: right-click **Ethernet** → Properties → **Sharing** tab → untick "Allow other network users to connect", OK. Reopen, tick it, select **Local Area Connection\* 10** in the dropdown, OK.

Then toggle the hotspot off and on, forget the network on the phone, rejoin.

### Claude · 2026-09-03 22:18

There it is — "Home networking connection" says **Select a private network connection**. Nothing is bound. That's your no-internet.

Open that dropdown and pick **Local Area Connection\* 10**, then OK.

If the dropdown is empty or Local Area Connection\* 10 isn't in it: untick the top box, OK, then reopen and tick it again — the list repopulates.

### Millard · 2026-09-04 01:04

it was working but the same problem happened again, how did we fix it?

### Claude · 2026-09-04 01:04

Two things: restarting the **Internet Connection Sharing (ICS)** service (`services.msc`), and then setting **Home networking connection** to **Local Area Connection\* 10** in Ethernet → Properties → Sharing (`ncpa.cpl`) — it had reset to "Select a private network connection."

Check that dropdown first; it drops the binding on reboot or when the virtual adapter number changes. If the adapter is now Local Area Connection\* 11 or similar, that's why — rebind to whatever the current one is.

### Millard · 2026-09-04 01:06

that option is not showing

### Claude · 2026-09-04 01:06

The dropdown is gone because only one other adapter exists — the hotspot's virtual adapter isn't up, so there's nothing to bind to.

Turn the Mobile hotspot **off**, then **on**, then reopen this Sharing tab. The dropdown should reappear with Local Area Connection\* something.

If it doesn't: `ncpa.cpl` — check whether a "Local Area Connection\* N" entry exists at all. If it's missing, Device Manager → View → Show hidden devices → Network adapters → uninstall **Microsoft Wi-Fi Direct Virtual Adapter** entries → Scan for hardware changes → turn the hotspot on again.

### Claude · 2026-09-04 01:06

Bound correctly now. Click OK, then forget the network on your phone and rejoin.

### Millard · 2026-09-04 01:08

did that and still says no internet access

### Claude · 2026-09-04 01:08

Do these in order, stopping when it works:

1. Untick the top box, OK. Reopen, tick it, confirm the dropdown shows Local Area Connection\* 10, OK. Toggle the hotspot off and on. Rejoin on the phone.
2. Restart the ICS service again in `services.msc` (this is what fixed it last time), then toggle the hotspot.
3. Set the phone's Wi-Fi DNS manually to 8.8.8.8 / 1.1.1.1 and see if pages load. If they do, it's ICS's DNS proxy, not routing.
4. Reboot the laptop, then re-check the Sharing binding before turning the hotspot on.

The fact that it keeps breaking points at either a VPN/antivirus network filter driver or the virtual adapter renumbering. What VPN or security software is on the laptop?

### Millard · 2026-09-04 03:02

what do i do it is still happening saying ocnnected with no internet even though the computer has internetg

### Claude · 2026-09-04 03:02

First, confirm it's actually dead rather than just the warning icon. On the phone, turn mobile data **off**, then open a website. If pages load, it's only Android's connectivity check failing and you can ignore it.

If pages really don't load:

1. On the phone, check the Wi-Fi IP address. It should be **192.168.137.x**. If it's anything else, ICS isn't the one handing out addresses.
2. Set the phone's Wi-Fi DNS manually to 8.8.8.8 and 1.1.1.1 (Advanced → IP settings → Static, gateway 192.168.137.1). If pages load after that, it's ICS's DNS proxy.
3. Turn off any third-party antivirus or VPN completely and retest. Windows Defender Firewall too, temporarily.
4. If none of that works: Settings → Network & internet → Advanced network settings → **Network reset**. Reboot, then set the hotspot up fresh. This clears the stale ICS state that keeps coming back.

Tell me what IP the phone gets and whether static DNS changes anything — that splits routing from DNS and I'll stop guessing.

### Millard · 2026-09-04 03:03

mobile data is off idiot i said that it says connected to wifif but no access

### Claude · 2026-09-04 03:03

Then run the two checks and tell me the results:

1. On the phone, Wi-Fi → tap the network → what IP address does it show?
2. On the phone, set that Wi-Fi to Static: IP 192.168.137.50, gateway 192.168.137.1, DNS 8.8.8.8 and 1.1.1.1. Does a website load?

Without those two answers I'm guessing between routing and DNS, and I've been guessing for six messages.

### Millard · 2026-09-04 03:04

IP 192.168.137.25 is what it shows

### Claude · 2026-09-04 03:04

Good — ICS is handing out addresses, so DHCP and the gateway are fine. The break is downstream of that.

Now set the phone's Wi-Fi to Static: IP 192.168.137.50, gateway 192.168.137.1, DNS 8.8.8.8 and 1.1.1.1. Then open a website.

That one test tells us whether it's DNS or routing, and the fix differs completely.

### Millard · 2026-09-04 03:05

how do i do that?

### Claude · 2026-09-04 03:05

On Android:

1. Settings → Network & internet → Internet
2. Tap the gear/pencil icon next to your hotspot network (or long-press the network → Modify network)
3. Expand **Advanced options**
4. IP settings: change **DHCP** to **Static**
5. Fill in:  
   - IP address: `192.168.137.50`  
   - Gateway: `192.168.137.1`  
   - Network prefix length: `24`  
   - DNS 1: `8.8.8.8`  
   - DNS 2: `1.1.1.1`
6. Save, then open a website.

On iPhone: Settings → Wi-Fi → tap the ⓘ next to the network → Configure IP → Manual → same IP, subnet mask `255.255.255.0`, router `192.168.137.1`. Then back out, tap Configure DNS → Manual → add 8.8.8.8 and 1.1.1.1.

### Millard · 2026-09-04 03:06

thre is no internet in network and internet, dont guess

### Claude · 2026-09-04 03:06

Then tell me the phone: Android or iPhone, and which brand — Samsung, Xiaomi, Pixel, something else. The menu path differs per manufacturer and I'm not going to invent one.

### Millard · 2026-09-04 03:06

android motorola

### Claude · 2026-09-04 03:06

On Motorola:

1. Settings → **Network & internet** → **Wi-Fi**
2. Tap the **gear icon** to the right of your connected hotspot network (not the network name itself)
3. Scroll down and tap **Advanced options** to expand it
4. **IP settings**: tap it, change **DHCP** → **Static**
5. Fill in:  
   - IP address: `192.168.137.50`  
   - Gateway: `192.168.137.1`  
   - Network prefix length: `24`  
   - DNS 1: `8.8.8.8`  
   - DNS 2: `1.1.1.1`
6. Tap **Save**, then open a website

If there's no gear icon, long-press the network name and choose **Modify network** — Advanced options is in there.

### Millard · 2026-09-04 03:07

i cant tap the gear if i do it just takes me to the same netowrk thing

### Claude · 2026-09-04 03:07

That screen it takes you to is the right one — the static IP settings are on it, you just have to scroll.

On that network detail page, scroll to the bottom. Look for **Advanced** or **Advanced options** and tap to expand. **IP settings** is inside, currently set to DHCP. Change it to Static.

If you scroll to the bottom and there's genuinely no Advanced section, tell me what options that page does show and I'll work from that.

### Millard · 2026-09-04 03:08

no such advanced or advanced options appears...

### Claude · 2026-09-04 03:08

Read me what that page does show — the option names top to bottom. I'll work from that.

Meanwhile, a faster route that skips the phone entirely: on the laptop, open `services.msc` and restart these three, in this order:

1. **Internet Connection Sharing (ICS)**
2. **Windows Firewall** (or Windows Defender Firewall)
3. **WLAN AutoConfig**

Then toggle the hotspot off and on. That combination clears the ICS NAT/DNS proxy state, which is what keeps dying on you.

### Millard · 2026-09-04 03:08

signal strength frequency security network usage privacy auto connect add device under netowrk details it lists wifi type ips ect but i cant click on anything there

### Claude · 2026-09-04 03:09

Two possibilities: that page has a **pencil/edit icon** at the top right, or you have to **forget the network first** — Motorola only exposes Advanced options when you're entering the password on a fresh connection.

Try the forget route:  
1. Forget the network  
2. Tap it to reconnect — the password box appears  
3. **Advanced options** is on that password screen, below the password field. Expand it, set IP settings to Static, fill in the values, then connect.

If that still doesn't show it, drop the phone side. Do the three service restarts on the laptop instead — ICS, Windows Defender Firewall, WLAN AutoConfig, in that order — then toggle the hotspot off and on and reconnect the phone normally.

### Millard · 2026-09-04 03:09

ok now i am in advanced options

### Claude · 2026-09-04 03:09

Tap **IP settings**, change **DHCP** to **Static**, then enter:

* IP address: `192.168.137.50`
* Gateway: `192.168.137.1`
* Network prefix length: `24`
* DNS 1: `8.8.8.8`
* DNS 2: `1.1.1.1`

Connect, then open a website and tell me if it loads.

### Millard · 2026-09-04 03:11

yes

### Claude · 2026-09-04 03:11

Then it's DNS, not routing. ICS's DNS proxy is dead — the phone was getting 192.168.137.1 as its DNS server and nothing was answering.

You can leave the phone on static and it will keep working. To fix it properly on the laptop so DHCP clients work again:

1. `services.msc` → restart **DNS Client**, then **Internet Connection Sharing (ICS)** — in that order.
2. Toggle the hotspot off and on.
3. Set the phone back to DHCP and test.

If it breaks again, it's a third-party firewall or antivirus blocking port 53 on the hotspot adapter. What security software is on the laptop?

### Millard · 2026-09-04 03:12

i cant restart dns client as it is greyed out

### Claude · 2026-09-04 03:12

That's normal — DNS Client can't be restarted from the Services window on Windows 10/11. Skip it.

Elevated Command Prompt (right-click Start → Terminal (Admin)):

```
net stop dnscache
net start dnscache
net stop sharedaccess
net start sharedaccess
```

Then toggle the hotspot off and on, set the phone back to DHCP, and test.

If `net stop dnscache` refuses, just do the sharedaccess pair — that's ICS itself and it's the one that matters.

### Millard · 2026-09-04 03:12

terminal or spower shell?

### Claude · 2026-09-04 03:12

Either. Terminal is just a wrapper around PowerShell — those `net` commands work the same in both.

### Millard · 2026-09-04 03:13

the commands do i enter all at once?

### Claude · 2026-09-04 03:13

One at a time, Enter after each. Wait for each to finish before the next.

### Millard · 2026-09-04 03:14

ok i entered the commands

### Claude · 2026-09-04 03:14

ICS restarted cleanly (dnscache refusing is expected).

Now:  
1. Check `ncpa.cpl` → Ethernet → Properties → Sharing — confirm Home networking connection still shows Local Area Connection\* 10. Restarting ICS sometimes clears it.  
2. Toggle the hotspot off and on.  
3. Set the phone back to DHCP and test.

### Millard · 2026-09-04 03:15

all it says now is wifi

### Claude · 2026-09-04 03:15

Wrong — it rebound to the physical Wi-Fi adapter, which isn't connected to anything. That's why the phone gets nothing.

Open that dropdown and select **Local Area Connection\* 10** instead, then OK.

If Local Area Connection\* 10 isn't in the list, the virtual adapter is down: toggle the hotspot off and on, then reopen this and pick it.

### Millard · 2026-09-04 03:15

i really need you to stop dicking around be thorough and fix this without guessing

### Claude · 2026-09-04 03:15

Fair. Here's what's actually established versus what I've been guessing at.

**Proven:** ICS assigns addresses (phone got 192.168.137.25). Routing works — static config with public DNS loads pages. So the break is DNS only: the phone gets 192.168.137.1 as its DNS server and ICS's DNS proxy isn't answering on it.

**Not established:** why the proxy dies, and why the sharing binding keeps reverting. I've been proposing fixes for both without evidence. That stops here.

Run these in the elevated PowerShell you already have open and paste the output:

```
Get-NetIPAddress -InterfaceAlias "Local Area Connection* 10"
```

```
Get-NetTCPConnection -LocalPort 53 -ErrorAction SilentlyContinue; Get-Process -Id (Get-NetUDPEndpoint -LocalPort 53).OwningProcess -ErrorAction SilentlyContinue | Select-Object Name,Id
```

```
Get-NetFirewallProfile | Select-Object Name,Enabled
```

```
Get-MpComputerStatus | Select-Object AMRunningMode
```

```
Get-NetAdapter | Select-Object Name,InterfaceDescription,Status
```

That tells me: whether the virtual adapter holds 192.168.137.1, what process owns port 53 (if anything), whether a third-party firewall replaced Defender, and the current adapter names so the binding stops being a moving target.

Two answers I still need from you, because no command gives them:

1. What VPN or antivirus is installed, if any.
2. Did this break after a Windows update, or after installing something.

Set the phone back to static for now so you have a working connection while we diagnose.

### Millard · 2026-09-04 03:16

IPAddress : fe80::4cbf:10c9:bcc5:182f%7  
InterfaceIndex : 7  
InterfaceAlias : Local Area Connection *10  
AddressFamily : IPv6  
Type : Unicast  
PrefixLength : 64  
PrefixOrigin : WellKnown  
SuffixOrigin : Link  
AddressState : Preferred  
ValidLifetime : Infinite ([TimeSpan]::MaxValue)  
PreferredLifetime : Infinite ([TimeSpan]::MaxValue)  
SkipAsSource : False  
PolicyStore : ActiveStore  
IPAddress : 169.254.199.117  
InterfaceIndex : 7  
InterfaceAlias : Local Area Connection* 10  
AddressFamily : IPv4  
Type : Unicast  
PrefixLength : 16  
PrefixOrigin : WellKnown  
SuffixOrigin : Link  
AddressState : Preferred  
ValidLifetime : Infinite ([TimeSpan]::MaxValue)  
PreferredLifetime : Infinite ([TimeSpan]::MaxValue)  
SkipAsSource : False  
PolicyStore : ActiveStore

### Claude · 2026-09-04 03:16

That's the answer. The virtual adapter has **169.254.199.117** — an APIPA self-assigned address, meaning ICS never applied 192.168.137.1 to it. The hotspot has no gateway, no DNS server, no NAT.

Cause: the binding is currently pointing at **Wi-Fi** instead of Local Area Connection\* 10, exactly as your last screenshot showed. ICS is sharing Ethernet to an adapter that isn't the hotspot, so the hotspot adapter got nothing.

Fix, in order:

1. `ncpa.cpl` → Ethernet → Properties → Sharing → untick "Allow other network users to connect" → OK.
2. Toggle the Mobile hotspot **off**.
3. Toggle the Mobile hotspot **on**. This recreates the virtual adapter.
4. Reopen Ethernet → Properties → Sharing → tick the box → in the dropdown select **Local Area Connection\* 10** (or whatever number it now shows — read it from `ncpa.cpl` first) → OK.
5. Back in PowerShell, run `Get-NetIPAddress -InterfaceAlias "Local Area Connection* 10"` again.

It must show **192.168.137.1**. If it does, set the phone back to DHCP and it will work. If it still shows 169.254.x.x, the binding didn't take and I'll need the rest of those command outputs.

### Millard · 2026-09-04 03:18

IPAddress : fe80::4cbf:10c9:bcc5:182f%7  
InterfaceIndex : 7  
InterfaceAlias : Local Area Connection *10  
AddressFamily : IPv6  
Type : Unicast  
PrefixLength : 64  
PrefixOrigin : WellKnown  
SuffixOrigin : Link  
AddressState : Preferred  
ValidLifetime : Infinite ([TimeSpan]::MaxValue)  
PreferredLifetime : Infinite ([TimeSpan]::MaxValue)  
SkipAsSource : False  
PolicyStore : ActiveStore  
IPAddress : 192.168.137.1  
InterfaceIndex : 7  
InterfaceAlias : Local Area Connection* 10  
AddressFamily : IPv4  
Type : Unicast  
PrefixLength : 24  
PrefixOrigin : Manual  
SuffixOrigin : Manual  
AddressState : Preferred  
ValidLifetime : Infinite ([TimeSpan]::MaxValue)  
PreferredLifetime : Infinite ([TimeSpan]::MaxValue)  
SkipAsSource : False  
PolicyStore : ActiveStore  
PS C:\WINDOWS\system32>

### Claude · 2026-09-04 03:18

192.168.137.1 is there. Set the phone back to DHCP and connect.

### Millard · 2026-09-04 03:20

it works for my phone but on my girlfriends phone it doesnt

### Claude · 2026-09-04 03:20

Check what her phone shows: does it get a 192.168.137.x address, or does it sit on "obtaining IP"?

* **No IP / obtaining IP**: forget the network on her phone and rejoin. If still nothing, her phone may be on 5GHz-only while the hotspot is 2.4GHz, or MAC randomization is tripping it — turn off "Use randomized MAC" for that network in her Wi-Fi settings.
* **Gets 192.168.137.x but no internet**: same DNS problem you had. Set her DNS to 8.8.8.8 / 1.1.1.1.

Which is it?

### Millard · 2026-09-04 03:22

can i see how much bandwidth is beeing used off the modem in our house? someone moved in and put another ethernet cable in and now the internet has gone down dramticaly and i feel they might be crypto mining or something

### Claude · 2026-09-04 03:22

Yes — your Totalplay router's admin page. Open a browser on the laptop and go to `http://192.168.1.1` (Totalplay's default; the login is usually printed on the router itself). Look for **Device List**, **Connected Devices**, or **Traffic Statistics**. Most Totalplay units show connected clients and per-device up/down totals.

What you'll actually get varies by model — some ISP routers only list devices, not bandwidth per device. If yours doesn't show traffic stats, alternatives:

* **GlassWire** or **NetLimiter** on your own laptop shows your traffic only, not theirs. Not useful here.
* **Wireshark** on the laptop won't see their traffic either — it's a switched network, you only see your own.
* Best practical check: unplug their cable for a minute and see if your speed jumps. That answers it without any tooling.

Crypto mining is a bad fit for the symptom, though. GPU mining uses almost no bandwidth — a few KB/s. Something that tanks a whole household connection is more likely torrenting, cloud backup, 4K streaming, or a security camera uploading constantly.

Before you go down this road: is this a housemate whose internet you share by arrangement, or someone who plugged in without asking? That changes what's reasonable to do about it.
