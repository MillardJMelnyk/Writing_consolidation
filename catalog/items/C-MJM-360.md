# Cheapest email setup for custom domain

| | |
|---|---|
| Date | 2025-11-26 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-360` |
| Links | [Original](https://claude.ai/chat/5562be10-3429-4fab-bb34-1882bd056767) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/360-2025-11-26-cheapest-email-setup-for-custom-domain.html) |

**Summary:** Finds the cheapest way to set up email for the reloveution.org domain, confirming Zoho Mail Free works with it.

**Topics:** Practical & personal > Software tools and open-source projects; Writing, Substack and publishing > ReLOVEution Substack and glossary

**Index terms:** reloveution.org; Zoho Mail; Cloudflare Email Routing; custom domain email; MX record

[← Catalog home](../Master_catalog.md)

---

### Millard · 2025-11-26 12:37

I have a domain reloveution.org. I need to set up an email for it. What's the cheapest way to do this?

### Claude · 2025-11-26 12:37

**Cheapest options, ranked:**

1. **Free: Email forwarding only**

   * **Cloudflare Email Routing** – Free. Forwards incoming mail to an existing address (e.g., Gmail). To *send* as your domain, configure Gmail's "Send mail as" feature using a free SMTP relay or your ISP's SMTP.
   * **ImprovMX** or **ForwardEmail.net** – Similar free forwarding services.
2. **Free: Full mailbox**

   * **Zoho Mail Free** – Free for up to 5 users, 5GB/user. Full send/receive with webmail and IMAP. Requires adding MX/SPF/DKIM records.
3. **Paid (if free options don't meet needs):**

   * **Zoho Mail Lite** – ~$1/user/month
   * **MXroute** – ~$45/year for unlimited domains/mailboxes (good if you have multiple domains)
   * **Porkbun** – ~$24/year if you transfer/register domain there (bundled email)

**Recommendation for lowest cost with full functionality:** Zoho Mail Free.

**Recommendation for zero cost, minimal setup:** Cloudflare Email Routing (if you only need to receive and can work around sending).

Do you need full send/receive capability, or is forwarding sufficient?

### Millard · 2025-11-26 12:39

Zoho Mail Free works under my current domain?

### Claude · 2025-11-26 12:39

Yes. Zoho Mail Free works with any domain you own, regardless of registrar. You verify ownership by adding a TXT record, then configure MX, SPF, and DKIM records at wherever your DNS is hosted.
