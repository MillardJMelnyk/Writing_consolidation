# Setting up local AI document indexing with Big RAG

| | |
|---|---|
| Date | 2026-04-13 |
| Type | AI chat |
| Source | AI chat (MM account) |
| By | Millard & Claude |
| Catalog ID | `C-MM-7cc03e67` |
| Links | [Original](https://claude.ai/chat/7cc03e67-b88e-4ce7-a01e-10ddb697c6d1) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20M.M%20export%20chats%20on%202026-10-31/chats/2026-04-13_setting-up-local-ai-document-indexing-with-big-rag_7cc03e67.html) |

**Summary:** Setting up automatic local indexing of documents across drives with Big RAG, Pandoc conversion scripts, AnythingLLM and Ollama.

**Topics:** AI chatbots and working with Claude > Local LLMs and AI document search

**Index terms:** Big RAG; Pandoc; AnythingLLM; Ollama; PowerShell; OneNote; document indexing

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-04-13 16:14

I need help setting up a self-indexing local AI document search system. Here's my situation and what's already been decided:  
My hardware: Intel i7-9700K, 32GB RAM, RTX 2060 Super (8GB VRAM), 9TB storage across multiple drives (D:, E:, F:). A GPU upgrade (likely RTX 3090 24GB) is coming soon.  
Already installed and working: Ollama v0.20.5 (with llama3.1:8b, qwen2.5:14b, and nomic-embed-text models), AnythingLLM Desktop v1.12.0 configured to use Ollama, LM Studio, Python 3.13, Node.js 22.  
My documents: Thousands of research files across multiple drives in DOCX, TXT, PPTX, Excel, PDF, and a large OneNote notebook collection. I need the AI to crawl my drives and index everything automatically — not drag-and-drop file by file.  
The plan we arrived at: Use LM Studio's Big RAG plugin to recursively crawl and index my drives. Big RAG doesn't support DOCX/PPTX/Excel natively, so the workaround is to bulk convert Office files to Markdown using Pandoc first, then let Big RAG crawl everything. OneNote notebooks will be exported to DOCX via a PowerShell/COM script, then also converted to Markdown.  
What I need help with now:

1. Install Pandoc if I don't already have it
2. Set up bulk conversion of DOCX, PPTX, and Excel to Markdown across my drive structure
3. Export OneNote notebooks to DOCX via PowerShell
4. Install and configure Big RAG plugin in LM Studio
5. Point Big RAG at my drives and start the indexing crawl  
   Start by checking whether I have Pandoc installed.

### Claude · 2026-04-13 16:15

Here's the full walkthrough. Since I can't execute commands on your Windows machine, I'll give you everything ready to run.

**Step 1 — Check for Pandoc**

Open PowerShell and run:

```
pandoc --version
```

If it returns a version, you're set. If not, install it:

```
winget install --id JohnMacFarlane.Pandoc -e
```

Then close and reopen PowerShell and verify with `pandoc --version`.

---

**Step 2 — Bulk convert Office files to Markdown**

Save this as `Convert-ToMarkdown.ps1` somewhere convenient. It recursively finds DOCX, PPTX, and XLSX/XLS files across your drives, converts them to `.md` files placed right next to the originals (so Big RAG finds them during its crawl).

```
#Requires -Version 5.1
# Convert-ToMarkdown.ps1
# Bulk-converts DOCX, PPTX, and Excel files to Markdown via Pandoc.
# Excel goes through an intermediate HTML step since Pandoc can't read .xlsx directly.

param(
    [string[]]$Drives = @("D:\", "E:\", "F:\"),
    [switch]$WhatIf
)

$extensions = @("*.docx", "*.pptx", "*.xlsx", "*.xls")

# Excel needs a helper: export each sheet to HTML via COM, then pandoc HTML→MD
function Convert-ExcelToMarkdown {
    param([string]$Path, [string]$OutMd, [bool]$DryRun)

    $excel = $null
    try {
        $excel = New-Object -ComObject Excel.Application
        $excel.Visible = $false
        $excel.DisplayAlerts = $false
        $wb = $excel.Workbooks.Open($Path)
        $tmpHtml = [IO.Path]::ChangeExtension($Path, ".tmp.html")
        # Save as HTML (xlHtml = 44)
        $wb.SaveAs($tmpHtml, 44)
        $wb.Close($false)

        if (-not $DryRun) {
            & pandoc $tmpHtml -f html -t markdown -o $OutMd --wrap=none 2>&1
        }
        Remove-Item $tmpHtml -ErrorAction SilentlyContinue
        # Excel also creates a _files folder
        $filesDir = [IO.Path]::ChangeExtension($Path, ".tmp_files")
        if (Test-Path $filesDir) { Remove-Item $filesDir -Recurse -Force -ErrorAction SilentlyContinue }
    }
    catch {
        Write-Warning "Excel COM failed for $Path : $_"
    }
    finally {
        if ($excel) {
            $excel.Quit()
            [System.Runtime.InteropServices.Marshal]::ReleaseComObject($excel) | Out-Null
        }
    }
}

$total = 0; $converted = 0; $failed = 0

foreach ($drive in $Drives) {
    Write-Host "`n=== Scanning $drive ===" -ForegroundColor Cyan
    foreach ($ext in $extensions) {
        Get-ChildItem -Path $drive -Filter $ext -Recurse -File -ErrorAction SilentlyContinue |
        ForEach-Object {
            $total++
            $src = $_.FullName
            $md  = [IO.Path]::ChangeExtension($src, ".md")

            # Skip if .md already exists and is newer than source
            if ((Test-Path $md) -and ((Get-Item $md).LastWriteTime -ge $_.LastWriteTime)) {
                Write-Host "  SKIP (up-to-date): $src" -ForegroundColor DarkGray
                return
            }

            if ($WhatIf) {
                Write-Host "  WOULD CONVERT: $src" -ForegroundColor Yellow
                return
            }

            Write-Host "  Converting: $src" -ForegroundColor Green
            try {
                if ($_.Extension -match '\.xlsx?$') {
                    Convert-ExcelToMarkdown -Path $src -OutMd $md -DryRun $false
                } else {
                    & pandoc $src -t markdown -o $md --wrap=none 2>&1
                }

                if (Test-Path $md) { $converted++ }
                else { $failed++; Write-Warning "No output produced for $src" }
            }
            catch {
                $failed++
                Write-Warning "Failed: $src — $_"
            }
        }
    }
}

Write-Host "`n=== Done ===" -ForegroundColor Cyan
Write-Host "Total found: $total | Converted: $converted | Failed: $failed"
```

**Usage:**

```
# Dry run first — see what it would convert without touching anything
.\Convert-ToMarkdown.ps1 -WhatIf

# Actually convert
.\Convert-ToMarkdown.ps1

# Specific drives only
.\Convert-ToMarkdown.ps1 -Drives @("D:\", "E:\")
```

Key behaviors: it skips files that already have an up-to-date `.md` next to them, so you can re-run it after adding new files. Excel conversion uses the COM automation (requires Office installed) to go through HTML as an intermediate.

---

**Step 3 — Export OneNote notebooks to DOCX**

OneNote's COM API is notoriously brittle, but this approach works with the desktop OneNote app (not the UWP/Store version). Save as `Export-OneNote.ps1`:

```
#Requires -Version 5.1
# Export-OneNote.ps1
# Exports all OneNote sections to DOCX, then converts to Markdown.

param(
    [string]$OutputRoot = "D:\OneNote-Export"
)

# OneNote COM requires the desktop (Office) version, not the Windows Store app
try {
    $onenote = New-Object -ComObject OneNote.Application
} catch {
    Write-Error "Could not start OneNote COM. Ensure the desktop Office version of OneNote is installed."
    exit 1
}

[xml]$hierarchy = $null
$onenote.GetHierarchy("", [Microsoft.Office.Interop.OneNote.HierarchyScope]::hsPages, [ref]$hierarchy)

if (-not $hierarchy) {
    # Fallback: get as string first
    [string]$xml = ""
    $onenote.GetHierarchy("", 3, [ref]$xml)  # 3 = hsPages
    [xml]$hierarchy = $xml
}

$ns = @{ one = "http://schemas.microsoft.com/office/onenote/2013/onenote" }

$notebooks = $hierarchy | Select-Xml -XPath "//one:Notebook" -Namespace $ns

if (-not $notebooks) {
    Write-Warning "No notebooks found. Check that OneNote desktop is open with notebooks synced."
    exit 1
}

New-Item -ItemType Directory -Path $OutputRoot -Force | Out-Null
$count = 0

foreach ($nb in $notebooks) {
    $nbName = $nb.Node.name
    Write-Host "Notebook: $nbName" -ForegroundColor Cyan

    $sections = $nb.Node | Select-Xml -XPath ".//one:Section" -Namespace $ns
    foreach ($sec in $sections) {
        $secName = $sec.Node.name
        $secId   = $sec.Node.ID
        $safeName = ($nbName + "_" + $secName) -replace '[\\/:*?"<>|]', '_'
        $outDocx = Join-Path $OutputRoot "$safeName.docx"

        Write-Host "  Exporting section: $secName -> $outDocx"
        try {
            # pfWord = 5
            $onenote.Publish($secId, $outDocx, 5, "")
            $count++
        } catch {
            Write-Warning "  Failed to export $secName : $_"
        }
    }
}

Write-Host "`nExported $count sections to $OutputRoot" -ForegroundColor Green
Write-Host "Now converting exported DOCX files to Markdown..."

Get-ChildItem -Path $OutputRoot -Filter "*.docx" | ForEach-Object {
    $md = [IO.Path]::ChangeExtension($_.FullName, ".md")
    & pandoc $_.FullName -t markdown -o $md --wrap=none
    Write-Host "  -> $md"
}

Write-Host "Done. Markdown files are in $OutputRoot" -ForegroundColor Green
```

**Usage:**

```
# Make sure OneNote desktop is open first
.\Export-OneNote.ps1 -OutputRoot "D:\OneNote-Export"
```

This exports each OneNote section as a `.docx`, then immediately converts each to `.md`. You can change the output path to wherever you want Big RAG to crawl.

---

**Step 4 & 5 — Big RAG in LM Studio**

Open LM Studio, go to the **Plugins** tab (or **Discover** → search "Big RAG"). Install the Big RAG plugin. Once installed:

1. Open Big RAG's settings panel within LM Studio.
2. Set the **embedding model** — select `nomic-embed-text` (you already have it in Ollama, but Big RAG uses LM Studio's own model loader, so you may need to download it again through LM Studio's model search: search `nomic-embed-text` and pull it).
3. Under **Directories to index**, add your drive roots:  
   - `D:\`  
   - `E:\`  
   - `F:\`  
   - `D:\OneNote-Export` (or wherever you put the OneNote exports)
4. In file type filters, make sure `.md`, `.txt`, and `.pdf` are enabled. You can disable `.docx`/`.pptx`/`.xlsx` since you've already converted them (or leave them — Big RAG will just skip what it can't parse).
5. Hit **Start Indexing** and let it crawl. First run on 9TB will take a while — hours, potentially overnight depending on file count.

After indexing completes, any query you run through LM Studio's chat with Big RAG active will search your local document index and pull relevant chunks into context before the LLM responds.

---

**Recommended execution order:**

1. `pandoc --version` → install if missing
2. Run `Convert-ToMarkdown.ps1 -WhatIf` to preview
3. Run `Convert-ToMarkdown.ps1` for real
4. Run `Export-OneNote.ps1`
5. Set up Big RAG and start the crawl

Let me know what `pandoc --version` returns and we'll go from there.
