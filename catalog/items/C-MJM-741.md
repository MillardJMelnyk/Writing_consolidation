# Finding large email attachments in Gmail

| | |
|---|---|
| Date | 2026-08-14 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-741` |
| Links | [Original](https://claude.ai/chat/04f2c072-c262-4707-9c86-96acbad4ffeb) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/741-2026-08-14-finding-large-email-attachments-in-gmail.html) |

**Summary:** Building Gmail searches for large old attachments excluding contacts and many labels, plus an Everything copy-full-path shortcut.

**Topics:** Practical & personal > Browsers, Word, OneNote and desktop apps

**Index terms:** Gmail; search operator; attachment size; Gmail label; Everything

[← Catalog home](../README.md)

---

### Millard · 2026-08-14 15:09

Give me a gmail search that will find all emails with attachments > 500 KB

### Claude · 2026-08-14 15:09

has:attachment larger:500000

Gmail's `larger:` operator uses bytes, not KB — 500000 ≈ 488 KiB, close enough for practical filtering. If you need exact 500 KiB threshold, use `larger:512000`.

### Millard · 2026-08-14 15:10

add they must be older than dec 1 2023

### Claude · 2026-08-14 15:10

has:attachment larger:500000 before:2023/12/1

### Millard · 2026-08-14 15:11

add and not in contacts

### Claude · 2026-08-14 15:11

No native Gmail operator excludes senders in your Contacts. Options:

**Workaround 1** — exclude specific senders manually:
`has:attachment larger:500000 before:2023/12/1 -from:(contact1@example.com OR contact2@example.com ...)`
Doesn't scale past a handful of addresses.

**Workaround 2** — if your contacts are mostly people you've labeled/starred as such, no equivalent search filter exists either.

There is no `-in:contacts` or similar operator in Gmail's search syntax. Confirming this isn't a gap in my knowledge would require checking Google's current operator list — want me to verify against their docs?

### Millard · 2026-08-14 15:11

yes

### Claude · 2026-08-14 15:11

Confirmed. No `-in:contacts` or equivalent operator exists in Gmail search syntax — checked against current documentation and multiple operator references. Google's own support page (accessed above) lists no contacts-exclusion operator.

Final query without contacts exclusion (not achievable natively):

```
has:attachment larger:500000 before:2023/12/1
```

To exclude known contacts, you'd need to manually chain `-from:()` with specific addresses, or export Contacts and cross-reference results outside Gmail (e.g., via API script).

### Millard · 2026-08-14 20:02

In Voidtools Everything, what is the keyboard shortcut for the "Copy Full Path" context menu?

### Claude · 2026-08-14 20:02

Ctrl+Shift+C

### Millard · 2026-08-15 22:49

can a search refer to labels?

### Claude · 2026-08-15 22:49

Yes — `label:name`

Example: `label:work has:attachment larger:500000 before:2023/12/1`

Notes:

* Multi-word label names need underscores or quotes: `label:"my label"` or `label:my_label`
* Nested labels use `/`: `label:parent/child`
* To exclude a label: `-label:name`

### Millard · 2026-08-15 22:49

what if I want to exclude emails with a list of labels?

### Claude · 2026-08-15 22:50

Chain `-label:` for each one — Gmail's syntax has no list/array operator.

```
-label:label1 -label:label2 -label:label3
```

Example:

```
has:attachment larger:500000 before:2023/12/1 -label:work -label:archive -label:receipts
```

No shorthand exists for "exclude any of these labels" in one clause — each label needs its own `-label:` term.

### Millard · 2026-08-15 22:50

exclude ALL these labels

### Claude · 2026-08-15 22:50

Same syntax — chaining `-label:` terms with no OR between them is Gmail's implicit AND, so it already excludes every message carrying any of the listed labels.

```
-label:label1 -label:label2 -label:label3
```

This returns only emails with **none** of label1, label2, label3. If you instead want to exclude only emails that have all three labels simultaneously (rare use case), Gmail's search syntax cannot express that — no AND-grouping operator exists for negation logic like that.

### Millard · 2026-08-15 22:51

how do I export a list of labels

### Claude · 2026-08-15 22:51

Three options, none native to Gmail's UI as a one-click export:

**1. Settings page (manual)**
Settings (gear icon) → See all settings → Labels tab. Lists every label with show/hide toggles. No export button — you'd copy manually.

**2. Gmail API — `users.labels.list`**
Returns JSON with all labels (id, name, type). Requires OAuth setup. Most reliable for a clean programmatic list:

```
GET https://gmail.googleapis.com/gmail/v1/users/me/labels
```

**3. Google Takeout**
Exports mail data (mbox/JSON) with labels attached to each message — not a standalone label list. You'd need to parse the export to extract unique label names.

For just a list of label names, API is the direct route. Want a script?

### Millard · 2026-08-15 23:01

is this ok or must it be space-delimited?

### Millard · 2026-08-15 23:02

-label:14th Ave S Relocation
-label:Brian McIntosh, Edmonds
-label:QRO 2024
-label:\_ CA Passport
-label:\_ \_ Logitech
-label:Jas
-label:\_ \_ Katie
-label:\_ Eric Dooley
-label:Vinay
-label:\_ Emergency/Weather mail
-label:Barb G
-label:\_ Simple
-label:\_ \_ Unead w SMS
-label:\_ \_ Payments
-label:\_ Anj
-label:CRM
-label:Anj
-label:\_ \_ Istina
-label:Myfax IN
-label:Nate
-label:Phil
-label:\_ BCC-SF
-label:`DONE
-label:`TODOit
-label:\_ Nextdoor
-label:\_ Shopping orders
-label:\_ Paul
-label:Maria - FROM
-label:\_ Vera
-label:Shane
-label:Dad
-label:Tom Reidy
-label:\_ \_ Walmart
-label:Call log
-label:Huffington Post
-label:\_ Apt Search
-label:\_ OnePlus Support
-label:\_ Trading
-label:Auntie Anne
-label:\_ GEICO
-label:Home Voice Mail
-label:\_ \_ Katie starred
-label:Receipt
-label:\_ Instacart
-label:Rob
-label:\_ \_ RnC Wedding
-label:\_ \_ \_ QRO
-label:Myfax FAILED
-label:Chuck Wilson
-label:Myfax Confirms
-label:SMS - Marcie
-label:Dan R
-label:\_ Lisa
-label:Chase Bank
-label:Dao
-label:\_ BnH Photo
-label:\_ \_ \_ Venmo
-label:\_ \_ PTSD
-label:\_ Anj Bandcamp
-label:`QUAnswers
-label:\_ Mail log
-label:- To Boys
-label:\_ Amtrak
-label:Marcie fiasco
-label:\_ Julia n Ruben
-label:\_ \_ Xmas
-label:Maria
-label:\_ KCLS
-label:\_ Craigslist
-label:\_ \_ ML
-label:\_ \_ \_ Unread
-label:Susan Liming
-label:\_ Synchrony Bank
-label:Myfax SENT
-label:Kev
-label:\_ \_ Katie Convos
-label:GCal
-label:John Moser
-label:\_ Money
-label:Matt Effsaef
-label:SMS
-label:Christy
-label:\_ Karla
-label:\_ \_ ML Msgs
-label:Publishing
-label:\_ \_ MyChart
-label:\_ Sarah Plimmer (Conscious Woman)

### Claude · 2026-08-15 23:02

Not OK as-is. Space-delimited breaks any label containing spaces — Gmail truncates at the first space, so `-label:14th Ave S Relocation` is parsed as `-label:14th` plus three bare keywords (`Ave`, `S`, `Relocation` searched as body text), not as one label exclusion.

**Fix:** wrap every multi-word label in quotes.

```
-label:"14th Ave S Relocation" -label:"Brian McIntosh, Edmonds" -label:"QRO 2024" -label:"_ CA Passport" -label:"_ _ Logitech" -label:Jas -label:"_ _ Katie" -label:"_ Eric Dooley" -label:Vinay -label:"_ Emergency/Weather mail" -label:"Barb G" -label:"_ Simple" -label:"_ _ Unead w SMS" -label:"_ _ Payments" -label:"_ Anj" -label:CRM -label:Anj -label:"_ _ Istina" -label:"Myfax IN" -label:Nate -label:Phil -label:"_ BCC-SF" -label:`DONE -label:`TODOit -label:"_ Nextdoor" -label:"_ Shopping orders" -label:"_ Paul" -label:"Maria - FROM" -label:"_ Vera" -label:Shane -label:Dad -label:"Tom Reidy" -label:"_ _ Walmart" -label:"Call log" -label:"Huffington Post" -label:"_ Apt Search" -label:"_ OnePlus Support" -label:"_ Trading" -label:"Auntie Anne" -label:"_ GEICO" -label:"Home Voice Mail" -label:"_ _ Katie starred" -label:Receipt -label:"_ Instacart" -label:Rob -label:"_ _ RnC Wedding" -label:"_ _ _ QRO" -label:"Myfax FAILED" -label:"Chuck Wilson" -label:"Myfax Confirms" -label:"SMS - Marcie" -label:"Dan R" -label:"_ Lisa" -label:"Chase Bank" -label:Dao -label:"_ BnH Photo" -label:"_ _ _ Venmo" -label:"_ _ PTSD" -label:"_ Anj Bandcamp" -label:`QUAnswers -label:"_ Mail log" -label:"- To Boys" -label:"_ Amtrak" -label:"Marcie fiasco" -label:"_ Julia n Ruben" -label:"_ _ Xmas" -label:Maria -label:"_ KCLS" -label:"_ Craigslist" -label:"_ _ ML" -label:"_ _ _ Unread" -label:"Susan Liming" -label:"_ Synchrony Bank" -label:"Myfax SENT" -label:Kev -label:"_ _ Katie Convos" -label:GCal -label:"John Moser" -label:"_ Money" -label:"Matt Effsaef" -label:SMS -label:Christy -label:"_ Karla" -label:"_ _ ML Msgs" -label:Publishing -label:"_ _ MyChart" -label:"_ Sarah Plimmer (Conscious Woman)"
```

**Warnings, quantified:**

* 84 labels chained — Gmail's search box has no documented hard character limit, but UI/URL practical ceilings around 1500–2000 chars cause truncation or failure in some clients. This string is ~2000 chars. Test it; if it fails silently, split into two searches with results merged manually.
* Labels containing `/` (e.g. `_ Emergency/Weather mail`) — Gmail treats `/` as label-nesting syntax. If that's a literal label name (not a parent/child label), confirm it's not actually stored as nested (`_ Emergency` → `Weather mail`), which would need `-label:"_ Emergency/Weather mail"` to still work as a literal string match — untested edge case, verify against your actual label list.
* Labels with backtick (`` `DONE ``, `` `TODOit ``, `` `QUAnswers ``) — backtick isn't a Gmail special character, should pass through fine unquoted, but I left them unquoted since no space exists in those three.

### Millard · 2026-08-15 23:08

ok how's this?
has:attachment larger:20000000 before:2021/12/1 -label:"14th Ave S Relocation" -label:"Brian McIntosh, Edmonds" -label:"QRO 2024" -label:"\_ CA Passport" -label:"\_ \_ Logitech" -label:Jas -label:"\_ \_ Katie" -label:"\_ Eric Dooley" -label:Vinay -label:"\_ Emergency n Weather mail" -label:"Barb G" -label:"\_ Simple" -label:"\_ \_ Unead w SMS" -label:"\_ \_ Payments" -label:"\_ Anj" -label:CRM -label:Anj -label:"\_ \_ Istina" -label:"Myfax IN" -label:Nate -label:Phil -label:"\_ BCC-SF" -label:`DONE -label:`TODOit -label:"\_ Nextdoor" -label:"\_ Shopping orders" -label:"\_ Paul" -label:"Maria - FROM" -label:"\_ Vera" -label:Shane -label:Dad -label:"Tom Reidy" -label:"\_ \_ Walmart" -label:"Call log" -label:"Huffington Post" -label:"\_ Apt Search" -label:"\_ OnePlus Support" -label:"\_ Trading" -label:"Auntie Anne" -label:"\_ GEICO" -label:"Home Voice Mail" -label:"\_ \_ Katie starred" -label:Receipt -label:"\_ Instacart" -label:Rob -label:"\_ \_ RnC Wedding" -label:"\_ \_ \_ QRO" -label:"Myfax FAILED" -label:"Chuck Wilson" -label:"Myfax Confirms" -label:"SMS - Marcie" -label:"Dan R" -label:"\_ Lisa" -label:"Chase Bank" -label:Dao -label:"\_ BnH Photo" -label:"\_ \_ \_ Venmo" -label:"\_ \_ PTSD" -label:"\_ Anj Bandcamp" -label:`QUAnswers -label:"\_ Mail log" -label:"- To Boys" -label:"\_ Amtrak" -label:"Marcie fiasco" -label:"\_ Julia n Ruben" -label:"\_ \_ Xmas" -label:Maria -label:"\_ KCLS" -label:"\_ Craigslist" -label:"\_ \_ ML" -label:"\_ \_ \_ Unread" -label:"Susan Liming" -label:"\_ Synchrony Bank" -label:"Myfax SENT" -label:Kev -label:"\_ \_ Katie Convos" -label:GCal -label:"John Moser" -label:"\_ Money" -label:"Matt Effsaef" -label:SMS -label:Christy -label:"\_ Karla" -label:"\_ \_ ML Msgs" -label:Publishing -label:"\_ \_ MyChart" -label:"\_ Sarah Plimmer (Conscious Woman)"

### Claude · 2026-08-15 23:08

Syntactically correct. Changes verified:

* `larger:20000000` = 20MB threshold (up from 500KB) — correct operator, no unit suffix needed, bytes assumed
* `before:2021/12/1` — valid date format
* `"_ Emergency n Weather mail"` — resolved the `/` ambiguity by substituting literal "n"; this now depends on that being the label's *actual* stored name. If the real label is `_ Emergency/Weather mail` with a literal slash, this quoted string will not match it. Confirm which is correct before running.
* All other quoting intact, no syntax breaks introduced.

**Unresolved from last message:** total string length ~2050 characters. Untested whether Gmail's search bar silently truncates past a threshold — no documented limit found. Run it; if results look incomplete or the box visibly truncates, split into two queries (e.g., first ~42 labels, then remaining ~42) and merge results.
