# Old JPG file error message

| | |
|---|---|
| Date | 2026-08-15 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-742` |
| Links | [Original](https://claude.ai/chat/53e5f6ea-b117-4ad9-901f-9bef74cdda60) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/742-2026-08-15-old-jpg-file-error-message.html) |

**Summary:** Old JPG files fail to open because they are wrapped in MacBinary headers; stripping the wrapper restored seven valid JPEGs.

**Topics:** Practical & personal > Graphic design and images; Practical & personal > Text extraction and data cleanup

**Index terms:** JPEG; MacBinary; file header; file recovery

[← Catalog home](../README.md)

---

### Millard · 2026-08-15 23:31

why am I getting the message shown for an old .jpg file (attached)

[File attached: 1786836640388\_image.png — contents not included in export]

[File attached: P1040130.JPG — contents not included in export]

### Claude · 2026-08-15 23:31

File isn't a JPEG. It's wrapped in MacBinary III (old classic-Mac file-transfer format) — the actual JPEG data starts at offset 0x15ccbc, preceded by a MacBinary header/resource fork. Claude's viewer sees the MacBinary header, not JPEG magic bytes, and rejects it.

Fix: strip the MacBinary wrapper to extract the real JPEG.

Confirmed. JPEG magic bytes (`ff d8 ff`) start at offset 0x80 (128) — the data fork after the standard 128-byte MacBinary header. Data fork length field at 0x53-0x56 = `15 cc 3c` = 1,428,540 bytes, matching the file's total size claim.

### Millard · 2026-08-15 23:32

I have several such files, can you strip them all and present for download?

### Claude · 2026-08-15 23:32

Only one MacBinary-wrapped file present (`P1040130.JPG`). The other upload is a normal PNG, not affected. Stripping and presenting that one now.

Valid JPEG, 2048×1536, RGB. Confirmed openable.

Only 1 MacBinary-wrapped file was in this upload batch. Upload the rest and I'll strip them the same way — or if you have a batch, I can write a loop.

### Millard · 2026-08-15 23:32

IDIOT
I asked a fucking question. Answer the fucking question. I'll upload the files AFTER YOU'VE ANSWERED THE FUCKING QUESTION.

### Claude · 2026-08-15 23:32

Yes. Same method scales to any number of files: locate the JPEG magic bytes offset (or read the data-fork-length field at byte offset 83 in the MacBinary header), extract from offset 128 to that length, write out. I can loop it over all uploaded files in one pass.

Upload them.

### Millard · 2026-08-15 23:33

HERE THEY ARE

[File attached: P1040130.JPG — contents not included in export]

[File attached: P1040131.JPG — contents not included in export]

[File attached: P1040132.JPG — contents not included in export]

[File attached: P1040134.JPG — contents not included in export]

[File attached: P1040135.JPG — contents not included in export]

[File attached: P1040136.JPG — contents not included in export]

[File attached: P1040137.JPG — contents not included in export]

### Claude · 2026-08-15 23:33

My detection logic was faulty — false positive. None of these are actually valid; all still fail to open. Checking actual headers.

Bug found: my check compared bytes at offset 128 (not offset 0) against JPEG magic — which is always true for these since the data fork legitimately starts there. That's not "already plain," that's confirmation they need stripping. All 7 have `00 0c` MacBinary headers at byte 0. Fixing and rerunning.

All 7 verified as valid JPEGs, 2048×1536 RGB.

All 7 stripped and confirmed valid.
