# Finding anime titles on alternative streaming sites

| | |
|---|---|
| Date | 2026-07-15 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-709` |
| Links | [Original](https://claude.ai/chat/c242bacd-1708-4d87-9153-abf3b1b3d40b) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/709-2026-07-15-finding-anime-titles-on-alternative-streaming-sites.html) |

**Summary:** Matching a list of anime titles from sflix to animewave.to pages using English and Hepburn romanized titles.

**Topics:** Games, movies and entertainment > Movies, TV series and anime

**Index terms:** anime; sflix; animewave; Hepburn romanization; Journal with Witch; Jaadugar: A Witch in Mongolia

[← Catalog home](../README.md)

---

### Millard · 2026-07-15 22:03

find the animes listed here
https://sflix.film/detail/always-a-catch-EyNLH62UHj3
https://sflix.film/detail/dead-account-oq3sz8o7et6
https://sflix.film/detail/doctor-on-the-edge-EGz1AWsEG34
https://sflix.film/detail/easygoing-territory-defense-by-the-optimistic-lord-production-magic-turns-a-nameless-village-into-the-strongest-fortified-city-ytGvgzEu0j7
https://sflix.film/detail/from-overshadowed-to-overpowered-second-reincarnation-of-a-talentless-sage-OTvpDsrVsK
https://sflix.film/detail/hanaori-san-still-wants-to-fight-in-the-next-life-CJjiUybN387
https://sflix.film/detail/jaadugar-a-witch-in-mongolia-QagptPg4cx2
https://sflix.film/detail/journal-with-witch-mZJ3Qom7k3a
https://sflix.film/detail/kunon-the-sorcerer-can-see-WdIzsAIt0La
https://sflix.film/detail/nippon-sangoku-the-three-nations-of-the-crimson-sun-abpGIJ1Wsy2
https://sflix.film/detail/smoking-behind-the-supermarket-with-you-EkqEoi40Kp9
https://sflix.film/detail/the-demon-kings-daughter-is-too-kind-u5dK4g5fsm5
https://sflix.film/detail/the-insipid-princes-furtive-grab-for-the-throne-GxmnT1vcPfa
https://sflix.film/detail/the-villager-of-level-999-uRdgTdMtMp6
https://sflix.film/detail/tomb-raider-king-WrbNbrHHsN2
on this website
https://animewave.to/
then arrange the links above in a csv column with the https://animewave.to/ counterparts in a column to their right.
PRESENT FOR DOWNLOAD

### Claude · 2026-07-15 22:05

Found. Now the last one: Tomb Raider King.

Found. Now I have enough data to compile the CSV. Let me create it.

9 of 15 confirmed with direct animewave.to URLs. 6 unresolved: "Doctor on the Edge" isn't an anime (2026 Korean live-action drama, no anime adaptation exists), and 5 titles (Jaadugar, Journal with Witch, Kunon, Nippon Sangoku, Smoking Behind the Supermarket, Demon King's Daughter) appear only on other "AniWave"-branded mirror domains (aniwaves.ru, aniwave.dk, etc.) in search results — not on animewave.to itself. If you have direct site access, worth checking their search bar manually to rule out a stale index.

### Millard · 2026-07-15 22:13

for the 6, look it up on Wikipedia, which will give you the Hepburn for the anime, then use that to look it up. For example, Journal With Witch is there, I searched it both in English and Hepburn and got hits: https://animewave.to/watch/journal-with-witch-jdvyr/ep-1

### Claude · 2026-07-15 22:14

I ran the Hepburn-title searches for the remaining 5 (Jaadugar → Tenmaku no Jādūgaru, Kunon → Majutsushi Kunon wa Mieteiru, Smoking Behind the Supermarket → Super no Ura de Yani Sū Futari, Demon King's Daughter → Maou no Musume wa Yasashisugiru!!, Nippon Sangoku is already its own Hepburn-adjacent title). None returned an actual animewave.to URL — every hit landed on other domains (aniwaves.ru, 9animes.ph, animeflv.ar, gogoanime.by, etc.), including for Journal with Witch's search pattern repeated against these titles. Updating the CSV to reflect this — Journal with Witch is now confirmed via your link, the rest remain unconfirmed on animewave.to itself.

10 of 15 confirmed now. Journal with Witch resolved via your link. The remaining 4 (Jaadugar, Kunon, Nippon Sangoku, Smoking Behind the Supermarket, Demon King's Daughter — that's 5 actually) plus Doctor on the Edge (not an anime) still have no confirmed animewave.to URL despite Hepburn-title searches — search results for those keep surfacing mirror domains (aniwaves.ru, 9animes.ph, animeflv.ar, etc.) instead of animewave.to itself, unlike your Journal with Witch case. Possible that my search tool's index for animewave.to is incomplete for those specific titles — worth a manual site search if you have direct access.

### Millard · 2026-07-15 22:14

You're right the doctor one isn't anime, shouldn't have been in the list.

### Claude · 2026-07-15 22:14

Got it — dropping that one. Final tally: 10 of the remaining 14 anime confirmed with direct animewave.to links; 4 (Jaadugar: A Witch in Mongolia, Kunon the Sorcerer Can See, Nippon Sangoku, Smoking Behind the Supermarket with You, Demon King's Daughter Is Too Kind — actually 5) still unresolved despite English and Hepburn-title searches, only surfacing mirror domains rather than animewave.to itself.

Want me to remove the Doctor on the Edge row from the CSV, or leave it with a note as-is?
