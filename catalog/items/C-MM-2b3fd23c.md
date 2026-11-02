# Spanish document review help

| | |
|---|---|
| Date | 2026-08-25 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-2b3fd23c` |
| Links | [Original](https://claude.ai/chat/2b3fd23c-e442-4d24-a0fb-3ae91350ed65) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-08-25_spanish-document-review-help_2b3fd23c.html) |

**Summary:** Reviews a Spanish rental application form, flagging tenant sections and references, then covers secured credit cards for temporary residents and Mercado Libre installments.

**Topics:** Practical & personal > Living in Mexico: rentals, contracts and landlords; Practical & personal > Spanish translation and Mexican Spanish; Practical & personal > Money transfers, payments, banking and taxes; Practical & personal > Scams and fraud checks

**Index terms:** rental application; Duna Language; secured credit card; temporary residency; Mercado Libre; meses sin intereses

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-08-25 20:11

can you check this and tell me what i need to fiill out, it is in spanish and my spanish isnt very good

### Millard · 2026-08-25 20:11

can you check this and tell me what i need to fiill out, it is in spanish and my spanish isnt very good

### Claude · 2026-08-25 20:12

Only the tenant section and the three references. The guarantor block is already filled in and the owner block isn't yours.

**Your details (Datos del arrendatario):**  
- Full name  
- Nationality  
- Phone / email  
- CURP / RFC (Mexican tax + population IDs)  
- INE number / NUE — if you're not Mexican, passport and residency card (FM/temporary or permanent resident) numbers go here instead  
- Company where you work / job title  
- Time at the job, company phone, documents you're presenting  
- Company address  
- Net monthly income  
- Previous landlord + phone  
- Reason for moving

**Three personal references:** name, phone, relationship to you, and any comments.

**Documents you have to hand in with it:**  
- Proof of income, last 3 months (payslips or bank statements)  
- Official ID (INE or passport)  
- The completed form  
- Billing details (datos de facturación — name, RFC, tax address, CFDI use)  
- Proof of address, if it's a commercial space

Blank lines for date and real-estate agent at the top are usually filled by the agency, not you.

### Millard · 2026-08-25 20:13

documents you're presenting

what documents i am presenting?

### Claude · 2026-08-25 20:13

The ones you hand over with the form: proof of income for the last 3 months (payslips or bank statements) and official ID (passport, and residency card if you have one). You write in that box what you're actually giving them — e.g. "Pasaporte, estados de cuenta 3 meses."

### Millard · 2026-08-25 20:14

does this document seem standard or suspicious/

### Claude · 2026-08-25 20:14

Standard. It's a normal Mexican rental application: form code and revision date in the header, a real company (SBI Pólizas, a Querétaro policy/lease-guarantee outfit) with address and phone, and exactly the fields Mexican landlords always ask for — CURP, RFC, INE, income, guarantor, references.

Two things worth noting, neither suspicious in itself:

Someone else's complete personal data is already on the form you were sent — CURP, RFC, INE number, salary, home address. Sloppy on their part, not a scam signal, but it tells you your data will be handled the same way.

The bank details section is for the *owner* to fill in, not you. If anyone asks you to deposit before a signed contract exists, that's where a scam would live. Legit process: you submit this, they verify, you sign the contract, then you pay.

### Millard · 2026-08-25 20:14

?

### Claude · 2026-08-25 20:14

What's the question?

### Millard · 2026-08-25 20:14

double check and make sure there is nothing off about the document, be thorough

### Claude · 2026-08-25 20:15

I dug through the file itself and checked the company. Nothing off.

**Technical inspection of the .docx**  
- No macros, no embedded objects, no DDE/field codes — nothing that could execute anything.  
- No hidden text, no tracked changes, no comments hiding content.  
- Exactly one external link in the whole file: sbipolizas.com in the footer. No trackers, no remote-template hooks.  
- Four images (logos), all legitimate image files.  
- Metadata: created by "Ivonne Montero," last saved by "office32," last printed July 2021 — a real office template that's been reused for years, not something generated fresh to target you. (The creation timestamp reads as today because it got re-saved on upload.)

**Content checks**  
- SBI is real — sbipolizas.com, and their listed services are exactly what this form supports: tenant background checks, credit bureau search, employment and personal reference verification, contract drafting. Their Facebook page lists them in Corregidora, Querétaro, matching the footer address.  
- The guarantor's CURP passes the official check-digit algorithm, and her RFC is consistent with it. Real person, real data — not fabricated filler.  
- Form fields are the standard Mexican set. Nothing unusual is being asked of you.

**Two things to be aware of, neither a red flag**

Someone else's full identity data — CURP, RFC, INE, salary, home address — is sitting in the copy they sent you. That's the agency's sloppiness, and it tells you your data gets handled the same loose way.

The bank details line is for the *owner* to fill in. Nobody should be asking you to transfer money on the strength of this form. Sequence is: submit, they run the background check, you sign the contract, then you pay.

### Millard · 2026-08-25 20:19

i cant find a record of duna english's physical address, do i need it for this form?

### Claude · 2026-08-25 20:19

Yes — "Domicilio de la empresa" is a required tenant field. They call the employer to verify, so the address matters less than the phone, but leave it blank and they'll bounce it back.

Ask HR or whoever signs your payslips; the address should also be printed on your recibo de nómina if you get one. If Duna English operates online with no office, write that in the box ("Empresa remota, sin domicilio físico") plus whatever address is on their tax invoices.

### Millard · 2026-08-25 20:22

this is the address is it legitimate and connected to Duna Language?

### Claude · 2026-08-25 20:22

The address is real. "LG" is the standard Spanish abbreviation for *Lugar* — used for hamlets that don't have street names. Baños de Vilo is a small rural settlement in the municipality of Periana, Málaga, known for its old sulphurous thermal pool, about 3 km outside the town. 29710 is the correct postcode. So it geocodes, and it's a residential/rural address, not an office building.

Duna Language is also real: operating since 2021, paying regular teachers $14/hour, doing 1-to-1 English tutoring for Chinese families. It has a Glassdoor page and a website at dunalanguage.ca.

What I can't confirm is the link between the two. Nothing public ties that Periana address to Duna Language — no company registry entry, no listing, nothing on their own site. The company's footprint is scattered: a .ca domain, a Facebook page registered to Dublin, and now a Spanish home address. That pattern is normal for a one-person remote outfit run from wherever the owner lives, and it's not evidence of anything wrong. But it means if the rental agency tries to verify your employer, they'll find the same thin trail I did.

Two practical points: use whatever address appears on your actual pay documents, since that's what has to match if they check. And expect the agency to lean harder on your bank statements than on the employer, because a foreign micro-employer isn't something they can call and confirm.

### Millard · 2026-08-25 20:29

is the previous owner part needed?

### Claude · 2026-08-25 20:29

Previous *landlord*, not owner — "arrendador anterior" means whoever you last rented from. They call to ask whether you paid on time and left the place in good shape.

If you've rented before, fill it in; skipping it looks like you're hiding a bad reference. If you've never rented in Mexico, put your last landlord abroad, or write "primer arrendamiento en México" if there isn't one. Blank with no explanation is what gets questioned.

### Millard · 2026-08-25 20:30

in the document does it say it is compulsory or not compulsory, i dont want your opinion, i want the language used in the document

### Claude · 2026-08-25 20:30

The document says nothing. No "obligatorio," no "opcional," no asterisks, no note about required fields anywhere in it — just field labels followed by blank space. The only list marked as requirements is "Requisitos inquilino," which covers documents to attach, not form fields.

### Millard · 2026-08-25 21:50

can i open up a credit card here in mexico with remporary, going on permananent, residency?

### Claude · 2026-08-25 21:50

Yes, but not a normal unsecured card from a big bank — not on temporary residency with no Mexican credit history and a foreign employer.

< cite index="39-1">Banks generally want permanent residency for credit cards; with temporary residency it's case-by-case, plus proof of address under 3 months old and three months of income backed by CFDI invoices.</cite> That last part is the wall for you: your income comes from Spain, so there's no CFDI and no Mexican payroll. Your file looks empty to their system.

What actually works:

**Secured card (tarjeta garantizada).** You deposit money, they give you a card with that limit. Banorte, Banamex and HSBC all do it. Approval is near-automatic because the bank risks nothing — residency card, passport, proof of address, CURP, done.

**Department store card.** Liverpool and Coppel approve foreigners far more loosely than banks. Slow, low limits, but it registers in Buró de Crédito.

Either way you're building the credit history you don't have yet. Six to twelve months of on-time payments and the unsecured cards open up — by which time you may have permanent residency anyway, which removes the main objection.

Get your RFC from SAT if you haven't. Several banks won't process a credit application without one.

### Millard · 2026-08-25 21:52

does the secured card work with payment plans like on mercado libre?

### Claude · 2026-08-25 21:52

Yes. A secured card is a real credit card on the Visa or Mastercard rails — Mercado Libre reads the BIN, not whether you deposited collateral. < cite index="50-1">MSI promotions run across every processing network operating in the country,</cite> so it shows up in checkout like any other card.

Two limits that bite in practice. Your credit line equals your deposit, and an MSI purchase blocks the *whole* amount against that line immediately, not the monthly installment — a $12,000 phone at 12 MSI eats $12,000 of a $15,000 limit until you pay it down. And issuer-specific promos (18 MSI on the Mercado Pago card, Amex-only deals) won't apply to you; you get the generic bank-card MSI offers only.

There's also < cite index="49-1">Mercado Pago's Línea de Crédito, which lets you buy in installments with no card at all,</cite> and it approves off your Mercado Libre activity rather than your credit history — often easier for a new arrival. But < cite index="49-1">its installments carry interest, with an average CAT around 128%.</cite> Not a substitute for MSI on a real card.
