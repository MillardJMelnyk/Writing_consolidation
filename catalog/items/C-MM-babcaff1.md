# Nginx sites-available and sites-enabled symlinks

| | |
|---|---|
| Date | 2025-12-26 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-babcaff1` |
| Links | [Original](https://claude.ai/chat/babcaff1-3828-4cb5-abb6-904c49a0a2c6) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2025-12-26_nginx-sites-available-and-sites-enabled-symlinks_babcaff1.html) |

**Summary:** How nginx sites-available and sites-enabled symlinks work and the need to reload nginx after editing configs.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting; Practical & personal > Software tools and open-source projects

**Index terms:** nginx; sites-available; sites-enabled; symbolic link; server configuration

[← Catalog home](../Master_catalog.md)

---

### Millard · 2025-12-26 16:33

so if i update site-available symbolic links to sites-enables in nginx nginx will use the conf from sites-available and update enabled?

### Claude · 2025-12-26 16:34

Not quite! Let me clarify how this works:

When you create a symbolic link from `sites-enabled` **pointing to** a file in `sites-available`, nginx reads the configuration from `sites-available` through that symlink.

Here's the key point: **nginx only reads configs from `sites-enabled`**. The symlink is just a pointer, so when nginx reads `sites-enabled/mysite`, it's actually reading the content from `sites-available/mysite`.

This means:  
- If you **edit** the file in `sites-available`, the changes are automatically reflected in `sites-enabled` (because the symlink points to the same file)  
- But you still need to **reload/restart nginx** for it to pick up the changes: `sudo nginx -t && sudo nginx -s reload`

The typical workflow is:  
1. Edit your config in `sites-available/mysite`  
2. The symlink in `sites-enabled/mysite` automatically "sees" these changes  
3. Test and reload nginx to apply: `sudo nginx -t && sudo nginx -s reload`

You don't need to recreate or update the symlink itself unless you're enabling/disabling a site. The symlink is just a one-time setup that says "hey nginx, use this config file."

Does that clear things up?
