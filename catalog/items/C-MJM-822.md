# PC crash cause diagnosis

| | |
|---|---|
| Date | 2026-10-29 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-822` |
| Links | [Original](https://claude.ai/chat/40d199d3-d9b5-4cbc-aa80-f71ca0a487ec) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/822-2026-10-29-pc-crash-cause-diagnosis.html) |

**Summary:** Diagnosing a Windows bugcheck 0xA crash with Reliability Monitor and WinDbg, and whether a new RAM stick with XMP or Firefox caused it.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting

**Index terms:** bugcheck 0x0000000A; WinDbg; Reliability Monitor; minidump; XMP; Windows Memory Diagnostic; MemTest86; RAM

[← Catalog home](../Master_catalog.md)

---

### Millard · 2026-10-29 15:43

I just had a "device ran into a problem" error and my PC restarted. How can I find out what caused the problem?

### Claude · 2026-10-29 15:43

Thursday, October 29, 2026, [time unavailable]

Read the stop code and the crash dump Windows saved at the moment of the crash.

**1. Stop code (2 minutes)**

* Press Win+R, type `perfmon /rel`, press Enter. This opens Reliability Monitor.
* Click today's column (red X), then double-click **"Shut down unexpectedly"** in the lower pane.
* Under **Problem signature**, the line **BCCode** is the stop code (e.g. `9f`, `d1`, `124`). The **Files that help describe the problem** list shows the dump file path, usually `C:\Windows\Minidump\[date]-01.dmp`.

**2. The responsible driver (the actual cause)**

* Install **WinDbg** from the Microsoft Store.
* Open it, then go to **File → Start debugging → Open dump file** and select the `.dmp` file from step 1.
* In the command box at the bottom, type `!analyze -v` and press Enter.
* Read three lines: **BUGCHECK\_CODE**, **MODULE\_NAME**, and **IMAGE\_NAME**. IMAGE\_NAME names the driver that crashed, such as `nvlddmkm.sys` (Nvidia GPU) or `rtwlane.sys` (Realtek Wi-Fi).

**If no .dmp file exists:** Event Viewer still has the stop code. Press Win+R, type `eventvwr.msc`, then go to **Windows Logs → System** and look for Event ID **1001** with source **BugCheck**. Event ID **41** (Kernel-Power) only records that the restart was unexpected; it does not show a cause.

`ntoskrnl.exe` or `hal.dll` as IMAGE\_NAME usually means the faulting component isn't identifiable from one dump. Stop code `124` (WHEA) points to hardware such as the CPU, RAM, or overclock/XMP settings, not a driver.

### Millard · 2026-10-29 15:45

[image attached — not included in export]

Don't give me general directions. Here is what I see. Tell me exactly what to do .

[File attached: 1793288696040\_image.png — contents not included in export]

### Claude · 2026-10-29 15:45

Click **View technical details** on the second row, **Windows stopped working**, at 10/29/2026 9:41 AM.

My earlier instruction to open "Shut down unexpectedly" was wrong. That entry doesn't hold the stop code; "Windows stopped working" does.

In the window that opens, screenshot it or copy two things:

* The **BCCode** line under Problem signature.
* The file paths listed under **Files that help describe the problem**.

### Millard · 2026-10-29 15:46

Description
The computer has rebooted from a bugcheck. The bugcheck was: 0x0000000a (0x00000000000000dd, 0x0000000000000002, 0x0000000000000000, 0xfffff8077e0b982e). A dump was saved in: C:\WINDOWS\Minidump\102926-12437-01.dmp. Report Id: 8b92142d-7dde-4c54-849d-21061ed4eb00.

### Claude · 2026-10-29 15:46

**Stop code 0x0A = IRQL\_NOT\_LESS\_OR\_EQUAL.** A kernel driver tried to read memory address `0xdd` while running at a level where that is forbidden.

**What this says now:**

* `0xdd` is a null pointer plus a small offset, which is typical of a driver code bug. It is not typical of random memory corruption.
* Driver bug: Likely. Bad RAM: Unlikely. One crash isn't enough to rule RAM out.
* Missing evidence: which driver owns the crashing instruction (`0xfffff8077e0b982e`). Only the dump file shows that.

**Do this exactly:**

1. Open the **Microsoft Store**, search **WinDbg**, and install the one published by **Microsoft Corporation**.
2. Click **Start**, type **WinDbg**, right-click it, and choose **Run as administrator**. The Minidump folder is locked to admins.
3. Click the **File** tab, then **Start debugging**, then **Open dump file**, then **Browse**.
4. In the **File name** box, paste `C:\WINDOWS\Minidump\102926-12437-01.dmp` and click **Open**.
5. Wait until the bottom-left shows `0: kd>` and the status bar stops saying it's loading. The first run takes 1–3 minutes to download symbols.
6. Click in the command box at the bottom, type `!analyze -v`, and press Enter.
7. Copy everything from **BUGCHECK\_CODE** down to the end of the output and paste it here.

### Millard · 2026-10-29 15:49

[image attached — not included in export]

Your instructions don't match what I see

[File attached: 1793288931861\_image.png — contents not included in export]

### Claude · 2026-10-29 15:49

Click the blue **File** tab in the top-left corner, just left of **Home**, then send me a screenshot of what opens.

I described the File screen without having seen it in your version (1.2610), so I won't guess its labels again.

### Millard · 2026-10-29 15:49

What the fuck do you think I just gave you? You can see that the file tab is already selected

### Claude · 2026-10-29 15:49

The **File** tab isn't selected; **Home** is. File is colored blue all the time, the same way Office apps do it. The active tab is **Home**: it's in bold blue text, and its buttons (Break, Go, Step Out, and so on) fill the ribbon.

When File is actually opened, the whole window changes to a page with a list of options down the left side, and the Command, Locals and Threads panes disappear.

Click the blue **File** box once. If the window doesn't change to that page, send a screenshot of what it does show.

### Millard · 2026-10-29 15:51

[image attached — not included in export]

my bad
OK, I did thru #5, now what?

[File attached: 1793289085024\_image.png — contents not included in export]

### Claude · 2026-10-29 15:51

Click the blue underlined **!analyze -v** link in the Command window. You can also type `!analyze -v` in the box right of **4: kd>** and press Enter.

While it runs, the box on the left shows **\*BUSY\***; when it changes back to **4: kd>**, it's done.

Then:

1. Click anywhere in the large white output area.
2. Press **Ctrl+A**, then **Ctrl+C**.
3. Paste the result here.

### Millard · 2026-10-29 15:52

[document attached — not included in export]

Attached file: unnamed

```
ExtensionGallery settings after reading 'SOFTWARE\Microsoft\Debug Engine' registry:
ExtensionGallery ExtensionRepository: Implicit


*******************************************************************************
*                                                                             *
*      MCP Server Bridge Attached (enabled , not running, not connected)      *
*                                                                             *
*******************************************************************************


************* Preparing the environment for Debugger Extensions Gallery repositories **************
   ExtensionRepository : Implicit
   UseExperimentalFeatureForNugetShare : true
   AllowNugetExeUpdate : true
   NonInteractiveNuget : true
   AllowNugetMSCredentialProviderInstall : true
   AllowParallelInitializationOfLocalRepositories : true

   -- Configuring repositories
      ----> Repository : LocalInstalled, Enabled: true
      ----> Repository : UserExtensions, Enabled: true

>>>>>>>>>>>>> Preparing the environment for Debugger Extensions Gallery repositories completed, duration 0.000 seconds

************* Waiting for Debugger Extensions Gallery to Initialize **************

>>>>>>>>>>>>> Waiting for Debugger Extensions Gallery to Initialize completed, duration 0.062 seconds
   ----> Repository : UserExtensions, Enabled: true, Packages count: 0
   ----> Repository : LocalInstalled, Enabled: true, Packages count: 46

Microsoft (R) Windows Debugger Version 10.0.29661.1004 AMD64
Copyright (c) Microsoft Corporation. All rights reserved.


Loading Dump File [C:\WINDOWS\Minidump\102926-12437-01.dmp]
Mini Kernel Dump File: Only registers and stack trace are available

WARNING: TriageDumpDataExtArray.HeaderSize is 0
WARNING: Failed to read dump data exension data
Symbol search path is: srv*
Executable search path is: 
Windows 10 Kernel Version 26100 MP (8 procs) Free x64
Product: WinNt, suite: TerminalServer SingleUserTS Personal
Kernel base = 0xfffff807`7da00000 PsLoadedModuleList = 0xfffff807`7e8f54c0
Debug session time: Thu Oct 29 09:40:52.723 2026 (UTC - 6:00)
System Uptime: 2 days 18:00:24.709
Loading Kernel Symbols
...............................................................
................................................................
................................................................
.....................
Loading User Symbols
PEB is paged out (Peb.Ldr = 0000006c`f0a3e018).  Type ".hh dbgerr001" for details
Loading unloaded module list
.................................
ReadVirtual() failed in GetXStateConfiguration() first read attempt (error == 0.)
For analysis of this file, run !analyze -v
nt!KeBugCheckEx:
fffff807`7defd660 48894c2408      mov     qword ptr [rsp+8],rcx ss:0018:fffff500`e2296b70=000000000000000a
4: kd> !analyze -v
Loading Kernel Symbols
...............................................................
................................................................
................................................................
.....................
Loading User Symbols
PEB is paged out (Peb.Ldr = 0000006c`f0a3e018).  Type ".hh dbgerr001" for details
Loading unloaded module list
.................................
*******************************************************************************
*                                                                             *
*                        Bugcheck Analysis                                    *
*                                                                             *
*******************************************************************************

IRQL_NOT_LESS_OR_EQUAL (a)
An attempt was made to access a pageable (or completely invalid) address at an
interrupt request level (IRQL) that is too high.  This is usually
caused by drivers using improper addresses.
If a kernel debugger is available get the stack backtrace.
Arguments:
Arg1: 00000000000000dd, memory referenced
Arg2: 0000000000000002, IRQL
Arg3: 0000000000000000, bitfield :
	bit 0 : value 0 = read operation, 1 = write operation
	bit 3 : value 0 = not an execute operation, 1 = execute operation (only on chips which support this level of status)
Arg4: fffff8077e0b982e, address which referenced memory

Debugging Details:
------------------


KEY_VALUES_STRING: 1

    Key  : Analysis.CPU.mSec
    Value: 1500

    Key  : Analysis.Elapsed.mSec
    Value: 2954

    Key  : Analysis.IO.Other.Mb
    Value: 3

    Key  : Analysis.IO.Read.Mb
    Value: 1

    Key  : Analysis.IO.Write.Mb
    Value: 25

    Key  : Analysis.Init.CPU.mSec
    Value: 609

    Key  : Analysis.Init.Elapsed.mSec
    Value: 75128

    Key  : Analysis.Memory.CommitPeak.Mb
    Value: 86

    Key  : Analysis.Version.DbgEng
    Value: 10.0.29661.1004

    Key  : Analysis.Version.Description
    Value: 10.2608.26.1 amd64fre

    Key  : Analysis.Version.Ext
    Value: 1.2608.26.1

    Key  : Bugcheck.Code.LegacyAPI
    Value: 0xa

    Key  : Bugcheck.Code.TargetModel
    Value: 0xa

    Key  : Dump.Attributes.AsUlong
    Value: 0x21008

    Key  : Dump.Attributes.DiagDataWrittenToHeader
    Value: 1

    Key  : Dump.Attributes.ErrorCode
    Value: 0x0

    Key  : Dump.Attributes.KernelGeneratedTriageDump
    Value: 1

    Key  : Dump.Attributes.LastLine
    Value: Dump completed successfully.

    Key  : Dump.Attributes.ProgressPercentage
    Value: 0

    Key  : Failure.Bucket
    Value: AV_nt!SwapContext

    Key  : Failure.Exception.IP.Address
    Value: 0xfffff8077e0b982e

    Key  : Failure.Exception.IP.Module
    Value: nt

    Key  : Failure.Exception.IP.Offset
    Value: 0x6b982e

    Key  : Failure.Hash
    Value: {47b746a3-60bf-1f5a-5fa5-88903b6a3204}

    Key  : Faulting.IP.Type
    Value: Paged


BUGCHECK_CODE:  a

BUGCHECK_P1: dd

BUGCHECK_P2: 2

BUGCHECK_P3: 0

BUGCHECK_P4: fffff8077e0b982e

FILE_IN_CAB:  102926-12437-01.dmp

DUMP_FILE_ATTRIBUTES: 0x21008
  Kernel Generated Triage Dump

FAULTING_THREAD:  ffff908d948bb080

READ_ADDRESS: fffff8077e9c54d8: Unable to get MiVisibleState
 00000000000000dd 

BLACKBOXBSD: 1 (!blackboxbsd)


BLACKBOXPNP: 1 (!blackboxpnp)


BLACKBOXWINLOGON: 1 (!blackboxwinlogon) (!blackboxwinlogonnotify)


CUSTOMER_CRASH_COUNT:  1

PROCESS_NAME:  Speedtest.exe

IP_IN_PAGED_CODE: 
nt!SwapContext+e
fffff807`7e0b982e 807e7100        cmp     byte ptr [rsi+71h],0

STACK_TEXT:  
fffff500`e2296b68 fffff807`7e0c58e9     : 00000000`0000000a 00000000`000000dd 00000000`00000002 00000000`00000000 : nt!KeBugCheckEx
fffff500`e2296b70 fffff807`7e0c0ba8     : 00000001`00000048 00000000`00000004 00000000`c0000102 ffff2738`f04f2200 : nt!KiBugCheckDispatch+0x69
fffff500`e2296cb0 fffff807`7e0b982e     : 00000000`00000001 00000400`00000000 00000000`00000000 00000000`00000000 : nt!KiPageFault+0x468
fffff500`e2296e40 fffff807`7e0b97b6     : 00000000`00000000 00000000`00000000 fffff807`7e815a40 fffff807`7dc57aaf : nt!SwapContext+0xe
fffff500`e2296e80 fffff807`7dd55888     : 00000000`00000047 fffff807`0b4c0180 00000000`00000000 fffff807`0b4ca2a8 : nt!KiSwapContext+0x76
fffff500`e2296fc0 fffff807`7dc0e205     : 00000000`00000000 00000000`00000000 ffff908d`948bb080 fffff807`0b4c0180 : nt!KiSwapThread+0x248
fffff500`e2297030 fffff807`7dc0d738     : 00000000`00000000 fffff807`0b4c0180 00000000`00000000 00000000`00000000 : nt!KiCommitThreadWait+0x225
fffff500`e22970d0 fffff807`7e269135     : 00000000`00200001 00000000`000000ff 00000000`00000002 00000000`00000000 : nt!KeWaitForMultipleObjects+0x628
fffff500`e22971d0 fffff807`7e39e51a     : 00000000`00001bb0 00000000`00000000 00000000`00000001 00000000`00000000 : nt!ObWaitForMultipleObjects+0x345
fffff500`e22976e0 fffff807`7e0c4f55     : ffff2738`f04f3b08 00000000`00001bb0 ffff908d`948bb080 0000006c`f42ae2f8 : nt!NtWaitForMultipleObjects+0x11a
fffff500`e2297970 00007ff9`be9028a4     : 00000000`00000000 00000000`00000000 00000000`00000000 00000000`00000000 : nt!KiSystemServiceCopyEnd+0x25
0000006c`f42ae2d8 00000000`00000000     : 00000000`00000000 00000000`00000000 00000000`00000000 00000000`00000000 : 0x00007ff9`be9028a4


SYMBOL_NAME:  nt!SwapContext+e

MODULE_NAME: nt

IMAGE_NAME:  ntkrnlmp.exe

IMAGE_VERSION:  10.0.26100.9711

STACK_COMMAND: .process /r /p 0xffff908d8a6020c0; .thread /r /p 0xffff908d948bb080 ; kb

BUCKET_ID_FUNC_OFFSET:  e

FAILURE_BUCKET_ID:  AV_nt!SwapContext

OSPLATFORM_TYPE:  x64

OSNAME:  Windows 10

FAILURE_ID_HASH:  {47b746a3-60bf-1f5a-5fa5-88903b6a3204}

Followup:     MachineOwner
---------
```

[File attached: unnamed — contents not included in export]

### Claude · 2026-10-29 15:52

**Result:** the dump doesn't name a culprit. The crash happened inside Windows' own code that switches between running tasks, and none of your add-on drivers appear in the crash trace.

**What the dump shows:**

* Windows tried to switch to a task whose internal record pointed to address `0x6c`, which is garbage. That code then read `0x6c + 0x71 = 0xdd`, the address in your stop code. Something had corrupted that record before this moment.
* **Speedtest.exe** was the running program. Its task was simply waiting, so it was the victim, not the cause.
* Uptime was 2 days 18 hours, and this is the first crash recorded in this dump.

**Grading:**

* A bug in Windows' task switching itself: Highly unlikely. It's among the most heavily exercised code in Windows.
* A driver corrupted Windows memory: Likely. The network driver is the leading suspect, because Speedtest was hammering it when the crash hit.
* Hardware instability (RAM, or an XMP/EXPO memory profile, overclock or undervolt): Likely.
* Missing evidence: hardware error records, and whether the crash repeats.

**Check 1: hardware errors (no risk)**

1. Press Win+R, type `eventvwr.msc`, press Enter.
2. In the left pane, expand **Windows Logs** and click **System**.
3. In the right pane under **Actions**, click **Filter Current Log...**
4. Open the **Event sources** dropdown, tick **WHEA-Logger**, and click **OK**.
5. Report the **Number of events** shown at the top of the middle pane. If it's above 0, send a screenshot of the most recent one.

**Check 2: reproduce**

1. Save your work. FYI: close MetaTrader first if it's running live trades.
2. Run Speedtest 5 times back to back.
3. If it crashes, repeat the WinDbg steps on the newest file in `C:\WINDOWS\Minidump` and paste the output.

If it crashes again, the network driver becomes Highly likely. If there are WHEA-Logger events and no repeat crash, hardware moves up.

### Millard · 2026-10-29 15:53

I wanted to make sure that the new RAM stick I installed isn't the culprit. And I also wonder about Firefox. Any indications that either was involved ?

### Claude · 2026-10-29 15:53

**New RAM stick:** the dump neither implicates nor clears it. Your stick is a Likely suspect anyway: a crash from corrupted Windows memory shortly after adding RAM is consistent with a faulty stick, or with a stick that doesn't run stably alongside your existing one.

Correction to my earlier Check 1: ordinary desktop RAM doesn't report its own errors, so zero WHEA-Logger events would not clear the RAM.

**Firefox:** there's no indication it was involved; this is Highly unlikely. The only program in the dump is Speedtest.exe. A minidump records only the task that crashed, so it shows no sign of Firefox either way. Firefox also can't crash Windows directly; it could only set off a bug in a driver such as the graphics driver, and no driver appears in the crash trace.

**To test the RAM:**

1. Download **MemTest86** (free edition): https://www.memtest86.com/download.htm. It needs a USB stick, which will be wiped.
2. Boot from the USB and let it run the default 4 passes. One error means a RAM fault.
3. If it passes with both sticks, shut down and remove the old stick. Run 4 passes on the new stick alone, then swap and test the old stick alone.

Missing facts that change the odds:

* Is the new stick the same brand, model, speed and timings as the old one?
* Is XMP/EXPO turned on in the BIOS?

### Millard · 2026-10-29 15:54

different brand, XMP on

### Claude · 2026-10-29 15:54

Different brands with XMP on makes the RAM the leading suspect: Likely, and higher than the network driver.

XMP pushes both sticks to one speed and timing profile, read from one of them, and the other brand's stick may not run stably at those settings. That kind of instability produces exactly this sort of random memory corruption. Proof requires a test.

**Do this, in order:**

1. Run MemTest86 for 4 passes with XMP still on, so it tests exactly the setup that crashed.
2. **Errors found:** turn XMP off, run 4 passes again, and report the result. To give you the exact BIOS steps for turning XMP off, I need your motherboard model or a photo of the BIOS screen.
3. **No errors:** test each stick alone with XMP on, as in my previous message.

### Millard · 2026-10-29 15:56

[image attached — not included in export]

What's the difference between this tool which I've used before and MemTest86

[File attached: 1793289325862\_image.png — contents not included in export]

### Claude · 2026-10-29 15:56

Both test RAM after a restart, outside of Windows. The difference is how hard they push it.

**Windows Memory Diagnostic**

* Its default mode, **Standard**, is a light test.
* Its heaviest mode, **Extended**, adds more patterns but is still less stressful than MemTest86.
* It's weaker at catching instability that only shows up under heavy load, which is the kind mismatched sticks on XMP typically cause.

**MemTest86**

* It runs more test types, including a "hammer" test that stresses neighboring memory cells, and makes several passes.
* It's the more sensitive tool for marginal instability.

**What a result means for you:**

* **Fail on either tool:** the RAM is bad or unstable. Highly likely.
* **Pass on Windows Memory Diagnostic:** weak evidence. Mismatched-XMP instability can still slip through.
* **Pass on MemTest86 (4 passes):** much stronger, though not absolute.

**If you use Windows Memory Diagnostic now:**

1. Click **Open**, then **Restart now and check for problems**.
2. When the blue test screen appears, press **F1**.
3. Use the arrow keys to select **Extended**, then press **F10** to start.

### Millard · 2026-10-29 15:57

If I run the Windows Memory Diagnostic against both sticks installed and get no errors, do I need to go further ?

### Claude · 2026-10-29 15:57

Yes. A clean Windows Memory Diagnostic run is weak evidence against exactly the kind of fault your setup is prone to: mismatched brands on XMP that are only unstable under heavy load.

The next step after a clean run is MemTest86, 4 passes with both sticks installed and XMP on.

### Millard · 2026-10-29 15:57

You're very confusing. I already told you X and P is on

### Claude · 2026-10-29 15:57

That was unclear on my part. "XMP on" wasn't an instruction to change anything; it means leave XMP as it is now, so the test checks the same setup that crashed.

Next step if the Windows test is clean: run MemTest86 for 4 passes with both sticks in and the BIOS left alone.

### Millard · 2026-10-29 15:58

Well then why would I run the window test at all ?

### Claude · 2026-10-29 15:58

You don't need to. Its only advantages are that it's already installed and needs no USB stick. If it found errors, that would save you the MemTest86 setup, but a clean result changes nothing because you'd still have to run MemTest86.

Going straight to MemTest86 skips a step that can't clear the RAM anyway.

### Millard · 2026-10-29 15:59

What if I just wait see if I have another error and if I do turn XMP off and wait and see if I have another error ?

### Claude · 2026-10-29 15:59

That works as a test, but it's slow and leaves you exposed while you wait.

**Time cost:** you've had one crash in about 3 days, so the crash rate is barely known.

* Step 1 (waiting for a second crash) could take days or weeks.
* Step 2 needs a long crash-free stretch to mean anything. If crashes were coming about every 3 days, you'd need about 9 crash-free days with XMP off to be 95% sure the change fixed it. If they're rarer, you'd need longer.
* MemTest86 gives an answer in hours.

**Risk while waiting:** unstable RAM doesn't only crash the PC. It can silently corrupt files as they're being saved, which includes your code, CSVs and MetaTrader data. A crash can also hit while MetaTrader is running live trades.

**What it can't separate:** if crashes continue after XMP is off, waiting can't tell a faulty stick from a driver. MemTest86 on each stick alone can.

### Millard · 2026-10-29 16:00

Exactly, hours I don't want to spend on debugging this

### Claude · 2026-10-29 16:00

MemTest86 takes hours of machine time, not your time. Setup is about 15 minutes: download it, write the USB, boot from it. Then it runs on its own overnight and you read one screen in the morning.

If you don't want even that, the least-effort move is to turn XMP off now and get on with your work. That takes about 5 minutes in the BIOS and removes the leading suspect.

* **Cost:** somewhat slower RAM. In most work the difference is a few percent and you're unlikely to notice it.
* **Downside:** you won't know whether XMP was the cause unless crashes continue.

For exact BIOS steps, I need your motherboard model.

### Millard · 2026-10-29 16:00

If I had one crash every three weeks, I wouldn't worry about it

### Claude · 2026-10-29 16:01

That's a reasonable threshold if crashes are the only cost.

Two things bear on it:

* **The crash may be the visible part of a bigger problem.** If the cause is RAM instability, the same fault can corrupt files without crashing anything, so you wouldn't see it happen. Have you considered whether a crash every three weeks is acceptable if it comes with occasional silent corruption of your code or data files?
* **Your actual crash rate may already be about that.** Your Reliability Monitor screenshot covers 10/10 to 10/29 and shows only this one Windows crash. When did you install the new stick? If it was before 10/10, you're at about one crash in 3 weeks or more.
