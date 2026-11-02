# WhatsApp desktop MP4 upload issue

| | |
|---|---|
| Date | 2025-12-17 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-474` |
| Links | [Original](https://claude.ai/chat/14448436-b92a-435d-b490-78c138016634) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/474-2025-12-17-whatsapp-desktop-mp4-upload-issue.html) |

**Summary:** Troubleshoots WhatsApp Desktop rejecting MP4 videos due to codecs and creates an FFmpeg batch script to convert videos.

**Topics:** Practical & personal > Phones, WhatsApp, Facebook and social media accounts; Practical & personal > Windows, Linux and PC hardware troubleshooting; Practical & personal > Software tools and open-source projects

**Index terms:** WhatsApp Desktop; FFmpeg; H.264; HEVC; VLC media player; video codec

[← Catalog home](../README.md)

---

### Millard · 2025-12-17 00:49

whatsapp desktop for Windows recently had an update. Now I can't upload .MP4 videos, says the format isn't supported.

### Claude · 2025-12-17 00:49

**Issue: MP4 codec incompatibility, not container format rejection.**

WhatsApp accepts MP4 *containers* but rejects specific video/audio codecs inside them.

**Required codecs (as of Dec 2024):**

* Video: H.264 or MPEG-4 only
* Audio: AAC or AC3 only

**Your MP4 likely uses:**

* HEVC (H.265), VP9, or AV1 video codec, OR
* Unsupported audio codec

**Diagnostic:**

1. Get codec info with MediaInfo (free tool) or VLC: `Tools > Codec Information`
2. Check video codec line - if it says HEVC, H.265, VP9, AV1 → that's the problem

**Solution:**
Re-encode with FFmpeg (free, command-line):

```
ffmpeg -i input.mp4 -c:v libx264 -c:a aac -strict experimental output.mp4
```

**Alternative cause:**
Recent WhatsApp Desktop update (Dec 9, 2024) switched from native UWP to Chromium-based app. If this coincides with your problem, try:

1. Uninstall WhatsApp Desktop completely
2. Delete `%AppData%\WhatsApp` folder
3. Reinstall from whatsapp.com/download

Does the video work on WhatsApp mobile? If yes, the file is fine - reinstall desktop app.

### Millard · 2025-12-17 16:30

what's a more common format that won't have the problem? I've got VLC media player, which I believe has format conversion features.
Here's the current codec info (image attached).

[File attached: 1765989032433\_image.png — contents not included in export]

### Claude · 2025-12-17 16:30

**Problem confirmed: AV1 video codec.**

Stream 1 shows `AOMedia's AV1 Video (av01)` - WhatsApp rejects this.

**Convert in VLC:**

1. `Media > Convert/Save` (or Ctrl+R)
2. Click `Add`, select your video, click `Convert/Save`
3. Under Profile, select: **`Video - H.264 + MP3 (MP4)`**
4. Click `Start`

**Alternative profile if first doesn't work:**

* Select `Video - H.264 + AAC (MP4)` instead

Both produce H.264 video, which WhatsApp accepts. The AAC profile matches your current audio codec exactly, but MP3 also works.

Done. Test the output file in WhatsApp Desktop.

### Millard · 2025-12-17 16:38

I did as instructed. There was no "AAC" profile in the list. It converted the vid, but about 3 seconds of the video at the start was blacked out, and about 2 seconds of audio at the end was silent. Everything else was fine and in sync.

### Claude · 2025-12-17 16:38

**VLC's converter has known bugs with AV1 sources.**

**Better option - FFmpeg (more reliable):**

1. Download: https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip
2. Extract anywhere, open Command Prompt in that folder
3. Run:

```
ffmpeg.exe -i "C:\path\to\your\video.mp4" -c:v libx264 -c:a aac -preset fast output.mp4
```

Replace `C:\path\to\your\video.mp4` with your actual file path.

**Or try VLC again with different settings:**

1. `Media > Convert/Save`
2. Add file, click `Convert/Save`
3. Click the wrench icon next to Profile dropdown
4. Select `Video - H.264 + MP3 (MP4)`, then click wrench to edit it
5. In `Encapsulation` tab, verify `MP4/MOV` is selected
6. In `Video codec` tab, check `Keep original video track` is **unchecked**
7. Save profile, convert again

FFmpeg will give cleaner results. The corruption you saw is VLC struggling with AV1 decoding during conversion.

### Millard · 2025-12-17 16:47

The installation zip file contains a folder, ffmpeg-8.0.1-essentials\_build. Where on my PC do I put this?

### Claude · 2025-12-17 16:47

**Anywhere. FFmpeg is portable - no installation needed.**

Simplest:

1. Put folder on Desktop
2. Open Command Prompt
3. Navigate: `cd C:\Users\YourUsername\Desktop\ffmpeg-8.0.1-essentials_build\bin`
4. Run the command from there

Or just drag your video file into the `bin` subfolder, then:

```
cd C:\Users\YourUsername\Desktop\ffmpeg-8.0.1-essentials_build\bin
ffmpeg.exe -i input.mp4 -c:v libx264 -c:a aac -preset fast output.mp4
```

Replace `input.mp4` with your actual filename.

Output file appears in same `bin` folder.

### Millard · 2025-12-17 16:54

OK, I put the folder here: D:\Programs\ffmpeg-8.0.1-essentials\_build
Write me a script that will ask for the path/file to be converted (by double quotes added by script) output to a file with "WHATSAPP" appended to the name just before the extension period, saved in the folder D:\Programs\ffmpeg-8.0.1-essentials\_build\converted.

### Claude · 2025-12-17 16:55

**Usage:**

1. Download the script above
2. Place it in `D:\Programs\ffmpeg-8.0.1-essentials_build\`
3. Double-click `whatsapp_convert.bat`
4. Paste or type the full path to your video (quotes optional - script adds them)
5. Press Enter

Output appears in `D:\Programs\ffmpeg-8.0.1-essentials_build\converted\` with `_WHATSAPP` before the extension.

Example: `myvideo.mp4` becomes `myvideo_WHATSAPP.mp4`
