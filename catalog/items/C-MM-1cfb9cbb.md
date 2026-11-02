# Osiris open source intelligence overview

| | |
|---|---|
| Date | 2026-09-11 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-1cfb9cbb` |
| Links | [Original](https://claude.ai/chat/1cfb9cbb-5ef7-4b70-8265-2fa939b0ee8b) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-09-11_osiris-open-source-intelligence-overview_1cfb9cbb.html) |

**Summary:** Overview of the Osiris OSINT dashboard on GitHub, a free Palantir-style live map, noting a Solana pump.fun token attached to the project.

**Topics:** Practical & personal > Software tools and open-source projects; Practical & personal > Scams and fraud checks

**Index terms:** Osiris; open-source intelligence; GitHub; Palantir; pump.fun; Solana

[← Catalog home](../README.md)

---

### Millard · 2026-09-11 08:40

I saw a post about "Osiris open source intelligence". What's the scoop on this?

### Claude · 2026-09-11 08:41

Two different things carry that name — the one in circulating posts is simplifaisoul/osiris on GitHub, a free OSINT dashboard that mashes live flight tracking, vessels, CCTV feeds, earthquakes, conflict-zone mapping, and news into one WebGL map, pitched as a Palantir alternative.

The mechanics: it pulls only free public APIs and does all the heavy rendering client-side in your browser, so the backend runs off a laptop in Docker and costs the dev nothing to host. There's a live hosted version, or you clone and npm run dev locally.

Two things worth knowing before you touch it:

* The repo title has a Solana pump.fun token address stapled to it. There's a coin attached to this project, which explains a chunk of the promotion volume.
* It includes a "Market AI overview" feature — treat that as decoration, not signal.

Separately, the CIA's Open Source Enterprise runs an unrelated classified-adjacent platform also called Osiris. Different animal entirely.
