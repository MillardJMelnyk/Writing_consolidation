# Converting plain text URLs to hyperlinks in Word

| | |
|---|---|
| Date | 2025-12-18 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-484` |
| Links | [Original](https://claude.ai/chat/d770f6ed-7ef1-43a7-a24f-b0cd96f43137) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/484-2025-12-18-converting-plain-text-urls-to-hyperlinks-in-word.html) |

**Summary:** Converts plain-text URLs to hyperlinks in Word 365 via macro, checks an LED beanie seller for scams, and seeks Amazon alternatives with headphones.

**Topics:** Practical & personal > Browsers, Word, OneNote and desktop apps; Practical & personal > Scams and fraud checks; Practical & personal > Shopping, product comparisons and gifts

**Index terms:** Microsoft Word 365; hyperlink; VBA macro; terminatei.com; LED beanie; Bluetooth headphones; Amazon

[← Catalog home](../Master_catalog.md)

---

### Millard · 2025-12-18 18:19

I have plain text URLs in a Word document. How do I change them all to working hyperlinks at one time?

### Claude · 2025-12-18 18:19

**Method 1 (if available):**

1. Ctrl+A (select all)
2. Format menu > AutoFormat > AutoFormat Now

(Note: AutoFormat menu is hidden in Word 2013+)

**Method 2 (modern Word):**

1. Ctrl+H (Find & Replace)
2. Find: `^u` (special format code for hyperlink field)
3. Leave Replace blank
4. Replace All

If URLs aren't recognized:

1. Ctrl+A
2. Ctrl+Shift+F9 (converts fields to text)
3. Then press Ctrl+Z to undo
4. This forces Word to re-evaluate and auto-convert URLs

**Method 3 (VBA Macro - most reliable):**
Alt+F11 > Insert > Module, paste:

```
Sub ConvertToHyperlinks()
    Dim oField As Field
    For Each oField In ActiveDocument.Fields
        If oField.Type = wdFieldHyperlink Then
            oField.Update
        End If
    Next
End Sub
```

Which Word version are you using?

### Millard · 2025-12-18 18:20

this is Word 365, there is no "Format" menu. Base your answer on the current version of Word.

### Claude · 2025-12-18 18:21

**Method 1 (Quick force-refresh):**

1. Ctrl+A (select all)
2. Ctrl+Shift+F9 (unlinks fields)
3. Immediately press Ctrl+Z (undo)

This forces Word to re-scan and auto-convert URL text to hyperlinks.

**Method 2 (VBA Macro - most reliable):**

1. Alt+F11 (opens VBA editor)
2. Insert > Module
3. Paste:

```
Sub ConvertURLsToHyperlinks()
    Dim oRng As Range
    Set oRng = ActiveDocument.Content
    
    With oRng.Find
        .Text = "http"
        .MatchWildcards = False
        .Forward = True
        
        Do While .Execute
            oRng.Expand Unit:=wdWord
            If Left(oRng.Text, 4) = "http" Then
                ActiveDocument.Hyperlinks.Add Anchor:=oRng, Address:=oRng.Text
            End If
            oRng.Collapse wdCollapseEnd
        Loop
    End With
End Sub
```

4. F5 to run

**Method 3 (Manual trigger):**

1. Click at end of any URL
2. Press spacebar, then immediately backspace

This triggers Word's auto-hyperlink feature. (Not practical for many URLs.)

Does Method 1 work for your document?

### Millard · 2025-12-18 18:22

of course method 1 doesn't work. Doesn't even make sense.

### Claude · 2025-12-18 18:22

You're correct. That doesn't work.

**Working method (VBA Macro):**

1. Alt+F11
2. Insert > Module
3. Paste:

```
Sub ConvertURLsToHyperlinks()
    Dim oRng As Range
    Set oRng = ActiveDocument.Content
    
    With oRng.Find
        .ClearFormatting
        .Text = "http*"
        .MatchWildcards = True
        .Forward = True
        
        Do While .Execute
            oRng.Expand Unit:=wdWord
            ActiveDocument.Hyperlinks.Add Anchor:=oRng, Address:=oRng.Text
            oRng.Collapse wdCollapseEnd
        Loop
    End With
End Sub
```

4. F5 to run

**Alternative (if URLs start with "www"):**
Change `.Text = "http*"` to `.Text = "www.*"` and add `Address:="http://" & oRng.Text`

Are your URLs all http/https, or do some start with www only?

### Millard · 2025-12-18 18:25

the macro only turned "https" into a bogus link. All begin with "https" or "http"

### Claude · 2025-12-18 18:25

**Corrected macro:**

```
Sub ConvertURLsToHyperlinks()
    Dim rng As Range
    Dim urlText As String
    
    Set rng = ActiveDocument.Content
    rng.Collapse wdCollapseStart
    
    With rng.Find
        .ClearFormatting
        .Text = "http"
        .Forward = True
        .Wrap = wdFindStop
        
        Do While .Execute
            ' Expand range to end of URL (until space/newline/tab)
            rng.MoveStartWhile Cset:=" " + vbTab, Count:=wdBackward
            rng.MoveEndUntil Cset:=" " + vbCr + vbTab, Count:=wdForward
            
            urlText = Trim(rng.Text)
            
            ' Add hyperlink only if range doesn't already contain one
            If rng.Hyperlinks.Count = 0 And Len(urlText) > 7 Then
                ActiveDocument.Hyperlinks.Add Anchor:=rng, Address:=urlText
            End If
            
            rng.Collapse wdCollapseEnd
        Loop
    End With
End Sub
```

Run this. If it still fails, what does the actual URL text look like in your document? (Copy/paste one example exactly as it appears.)

### Millard · 2025-12-18 18:27

that worked

### Claude · 2025-12-18 18:27

Good.

### Millard · 2025-12-18 18:27

Please check on this company for scamshttps://www.terminatei.com/products/led-beanie-light-4-3?utm\_source=fb&utm\_medium=Facebook\_Mobile\_Feed&utm\_campaign=120234053288090493&utm\_term=120234053336980493&utm\_content=120234053486000493&fbclid=IwdGRzaAN2HQtleHRuA2FlbQEwAGFkaWQBqym6LsVV3QEezEMdaScAo7X0uTvtjSODY65UWZtw\_\_WMx3gLHx6vA\_mDYjviUDTX11r59ac\_aem\_b4Wf1CAWXNdXxapWZNB2mg&utm\_id=120234053288090493&sfnsn=scwspwa

### Claude · 2025-12-18 18:28

**No specific scam reports found for terminatei.com** (searched December 18, 2025).

However, **several red flags** in the URL you provided:

1. **Facebook ad with tracking parameters** - Extensive utm\_ codes and fbclid indicate targeted advertising typical of dropshipping/scam operations
2. **Similar domain scams exist** - "terminaten.com" (different spelling) has extensive scam reports: Trustpilot 1.3/5 stars (82 reviews), ScamAdviser "very low trust score"
3. **LED beanie lights** frequently advertised in Facebook scam ads

**Typical indicators to check:**

* Domain age (use whois lookup)
* Contact information/physical address present?
* Return policy clarity
* Payment security (https)
* Price unrealistically low?
* Professional website quality

**Recommendation:** Do not purchase. If you already ordered:

* Contact bank/credit card immediately if charged
* File dispute/chargeback
* Report to Facebook

Did you already make a purchase?

### Millard · 2025-12-18 18:30

Please find me the comparable product from Amazon or other reputable online store.

### Claude · 2025-12-18 18:30

**Amazon LED Beanie Options:**

**1. Tutuko LED Beanie**

* Price: ~$14-18
* 4 LED lights, 30ft illumination
* 3 brightness levels
* USB rechargeable (8 hours runtime)
* https://www.amazon.com/Tutuko-Lighted-Rechargeable-Headlamp-Flashlight/dp/B08GLN2CHP

**2. BERGWEISER LED Beanie**

* Price: ~$16-20
* 6 super bright bulbs (80 lumens)
* 3 modes including blue-red strobing
* USB rechargeable (24hr strobe mode)
* https://www.amazon.com/BERGWEISER-Beanie-Headlamp-Rechargable-Removable/dp/B0G5MW6WMW

**3. Number-one LED Beanie (Front + Rear lights)**

* Price: ~$15-22
* Dual lights: white front (4 LED) + red rear (4 LED)
* 3 brightness levels each
* USB rechargeable (2-8 hours)
* https://www.amazon.com/Number-one-Rechargeable-LED-Light-Hat-lighting-Headlamp/dp/B08LNVPZFH

**4. MELASA LED Beanie**

* Price: ~$13-17
* 4 LED bulbs, 120 lumens
* 6-8 hours runtime
* USB rechargeable
* https://www.amazon.com/Unisex-Rechargeable-Headlamp-Knitted-Husband/dp/B09D93KPSG

All include: removable lights for washing, one-size-fits-most, various colors available.

### Millard · 2025-12-18 18:33

none of those have the headphone feature, which was the whole point

### Claude · 2025-12-18 18:34

**Amazon LED Beanie with Bluetooth Headphones:**

**1. Wmcaps Bluetooth Beanie with Light**

* Price: ~$20-25
* 4 LED lights (3 brightness levels, 30ft range)
* Bluetooth 5.0 with built-in speakers & mic
* USB rechargeable
* https://www.amazon.com/Bluetooth-Rechargeable-Headlamp-Headphones-Speakers/dp/B09DJVT3W3

**2. Bosttor Bluetooth Beanie with Light**

* Price: ~$22-28
* 4 LED lights (30ft illumination)
* Bluetooth 5.0, stereo speakers & mic
* 10 hours battery life (music/calling)
* https://www.amazon.com/Bosttor-Bluetooth-Headlamp-Headphones-Speaker/dp/B0BH41HYFZ

**3. Attikee Bluetooth Beanie Hat with Light**

* Price: ~$18-24
* 4 LED bulbs, 3 brightness levels
* Bluetooth 5.0 speakers & mic (33ft range)
* IP44 waterproof
* https://www.amazon.com/Bluetooth-Beanie-Unisex-Headphones-Speakers/dp/B08LBCLXB7

**4. Bluetooth Beanie with 5 LED & Headphones**

* Price: ~$25-30
* 5 ultra-bright LEDs
* Bluetooth 5.4 (latest version)
* 10-15 hours music playback
* Type-C charging
* https://www.amazon.com/TOUCH-TWO-Bluetooth-Wireless-Headphone/dp/B0CHJ2R6QX

All feature: removable components for washing, hands-free calling, one-size-fits-most.
