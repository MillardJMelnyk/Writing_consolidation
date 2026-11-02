# Python script crashed VS Code

| | |
|---|---|
| Date | 2026-02-17 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-660` |
| Links | [Original](https://claude.ai/chat/fd33cbb8-eee3-4ec3-b340-291ca2e78a1b) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/660-2026-02-17-python-script-crashed-vs-code.html) |

**Summary:** Recovering from a Python script out-of-memory crash of VS Code that left Windows tasklist hanging, and a batch file to clear it.

**Topics:** Practical & personal > Windows, Linux and PC hardware troubleshooting

**Index terms:** Visual Studio Code; out of memory; tasklist; PowerShell; batch file

[← Catalog home](../README.md)

---

### Millard · 2026-02-17 20:37

I ran a Python script that crashed VS Code. what should I do now?

[File attached: 1771360655340\_image.png — contents not included in export]

### Claude · 2026-02-17 20:37

Tuesday, February 17, 2026, 11:45 AM CST

OOM = Out Of Memory. The renderer process was killed by the OS memory manager.

**Immediate:**

* Do NOT reopen until you address the memory issue — it will crash again.

**Diagnose first:**

* What does the script do that's memory-intensive? (large dataset, loop with no cleanup, etc.)
* How much RAM does your machine have, and what was usage at crash time?

**Fix options (in order):**

1. **Add memory limits** to the script itself — process data in chunks, not all at once.
2. **Run the script in a terminal** (not inside VS Code's integrated terminal) to isolate VS Code's renderer from the process.
3. **Increase VS Code memory limit** — launch with `--max-memory=<MB>` flag if the script output/rendering is what's consuming memory.
4. **Kill background extensions** — some extensions (Pylance, etc.) balloon memory on large files.

What does the script do?

### Millard · 2026-02-17 20:38

I'm fixing the script. What do I do now? Just close it?

### Claude · 2026-02-17 20:38

Yes, click **Close**. Don't reopen until the fix is ready.

### Millard · 2026-02-17 20:38

that's ridiculous. I need to be in VS Code to implement the fix.

### Claude · 2026-02-17 20:38

Click **Reopen**.

### Millard · 2026-02-17 20:38

too late, already closed

### Claude · 2026-02-17 20:38

Open VS Code normally — Start menu, taskbar, or `code .` in terminal.

### Millard · 2026-02-17 20:40

OK, this happened last time VS Code crashed. It screws up Windows. "tasklist" in a command prompt window just hangs. There's gotta be an easier way to clear it without restarting Windows

### Claude · 2026-02-17 20:40

When `tasklist` hangs, it's typically blocked on an unresponsive process handle. Try these without restarting:

**PowerShell (often bypasses the hang):**

```
Get-Process | Where-Object {$_.Responding -eq $false}
```

Then kill the offenders:

```
Stop-Process -Name "Code" -Force
Stop-Process -Name "python" -Force
```

**If PowerShell also hangs on Get-Process:**

* Open Task Manager (`Ctrl+Shift+Esc`) — it uses a different API and usually still works
* Look for `Code.exe` or `python.exe` processes showing "Not Responding" or high memory
* End them from there

**Root cause:** The OOM-killed process likely left zombie handles. Killing the hung Code/python processes clears it.

Does PowerShell's `Get-Process` respond, or does it also hang?

### Millard · 2026-02-17 20:41

it shows me
Handles NPM(K) PM(K) WS(K) CPU(s) Id SI ProcessName
------- ------ ----- ----- ------ -- -- -----------
1727 73 168692 74720 3.56 23344 1 SystemSettings
give me the command

### Claude · 2026-02-17 20:41

```
Stop-Process -Id 23344 -Force
```

### Millard · 2026-02-17 20:42

it got rid of it, but tasklist still hangs

### Claude · 2026-02-17 20:42

Run this to find any remaining stuck ones:

```
Get-Process | Where-Object {$_.Responding -eq $false}
```

### Millard · 2026-02-17 20:43

PS C:\WINDOWS\system32> Get-Process | Where-Object {$\_.Responding -eq $false}
PS C:\WINDOWS\system32>

### Claude · 2026-02-17 20:43

No unresponsive processes. The `tasklist` hang is likely a WMI issue. Try:

```
tasklist /FI "STATUS eq RUNNING"
```

Does that hang too?

### Millard · 2026-02-17 20:43

yes

### Claude · 2026-02-17 20:43

Restart the WMI service:

```
Stop-Service winmgmt -Force
Start-Service winmgmt
```

Then test `tasklist` again.

### Millard · 2026-02-17 20:44

now it works

### Claude · 2026-02-17 20:44

Good. Open VS Code and fix the script.

### Millard · 2026-02-17 20:44

write me a .bat file that will clear this if it happens again

### Claude · 2026-02-17 20:45

Run it as Administrator.

### Millard · 2026-02-17 20:52

is this the code you just gave me?Attached file: unnamed

```
#!/usr/bin/env python3
"""
TEMA/KC Pattern Analyzer
L0: PL slope dynamics (SL-agnostic)
L1: Shape detection (crosses/pivots via spread delta)
L2: Pattern detection (frequency analysis of shape sequences)

Input: CSV from MT5 with Time, OHLC, TEMA, KC_Upper, KC_Middle, KC_Lower
Output: Bar-by-bar L0/L1 data, then L2 pattern catalog
"""

import pandas as pd
import numpy as np
import sys
import argparse
import time
from collections import defaultdict
from typing import Tuple, Optional


# ---------------------------------------------------------------------------
# Progress tracking
# ---------------------------------------------------------------------------

class ProgressTracker:
    """
    Single-line overwriting progress display.
    Call tick() each iteration (or tick(n) for batches).
    Call done() when finished.
    Prints at most once every `interval` seconds to reduce I/O overhead.
    """

    def __init__(self, label: str, total: int, interval: float = 2.0):
        self.label    = label
        self.total    = total
        self.interval = interval
        self.completed = 0
        self.start    = time.monotonic()
        self.last_print = 0.0  # force first print after first tick

    @staticmethod
    def _fmt_seconds(s: float) -> str:
        s = int(s)
        h, rem = divmod(s, 3600)
        m, sec = divmod(rem, 60)
        return f"{h:02d}:{m:02d}:{sec:02d}"

    def tick(self, n: int = 1) -> None:
        self.completed += n
        now = time.monotonic()
        if now - self.last_print < self.interval:
            return
        self.last_print = now
        elapsed = now - self.start

        pct = self.completed / self.total * 100 if self.total > 0 else 0.0
        elapsed_str = self._fmt_seconds(elapsed)

        if elapsed > 0 and self.completed > 0:
            rate = self.completed / elapsed
            remaining = (self.total - self.completed) / rate
            eta_str = self._fmt_seconds(remaining)
        else:
            eta_str = "--:--:--"

        line = (f"\r{self.label}: {self.completed:,} / {self.total:,} "
                f"({pct:.1f}%) | {elapsed_str} elapsed | ETA: {eta_str} remaining   ")
        print(line, end='', flush=True)

    def done(self) -> None:
        elapsed = time.monotonic() - self.start
        elapsed_str = self._fmt_seconds(elapsed)
        line = (f"\r{self.label}: {self.total:,} / {self.total:,} "
                f"(100.0%) | {elapsed_str} elapsed | done                          ")
        print(line, flush=True)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def round_to_point(value: float, point: float = 0.001) -> float:
    """Round to nearest point (0.001 for USDJPY)."""
    return round(value / point) * point


def calculate_spreads(tema: float, kc_upper: float, kc_middle: float, kc_lower: float, point: float) -> dict:
    """Calculate spreads from TEMA to each KC line, rounded to point."""
    return {
        'spread_upper':  round_to_point(tema - kc_upper,  point),
        'spread_middle': round_to_point(tema - kc_middle, point),
        'spread_lower':  round_to_point(tema - kc_lower,  point)
    }


def determine_active_line(spreads: dict) -> Tuple[str, str]:
    abs_spreads = {
        'U': abs(spreads['spread_upper']),
        'M': abs(spreads['spread_middle']),
        'L': abs(spreads['spread_lower'])
    }
    active = min(abs_spreads, key=abs_spreads.get)
    return active, active


def calculate_spread_delta_state(spread_curr: float, spread_prev: float) -> str:
    if spread_curr == 0 and spread_prev == 0:
        return 'SD0'
    if spread_prev != 0 and spread_curr != 0:
        if (spread_curr > 0) != (spread_prev > 0):
            return 'SDX'
    elif spread_prev == 0 or spread_curr == 0:
        if spread_prev != 0 or spread_curr != 0:
            return 'SDX'
    delta = abs(spread_curr) - abs(spread_prev)
    if delta > 0:
        return 'SD+'
    elif delta < 0:
        return 'SD-'
    else:
        return 'SD0'


def calculate_l0_state(slope_delta: float) -> int:
    if slope_delta > 0:
        return 1
    elif slope_delta < 0:
        return -1
    else:
        return 0


# ---------------------------------------------------------------------------
# Passes
# ---------------------------------------------------------------------------

def pass1_raw_calculations(df: pd.DataFrame, point: float = 0.001) -> pd.DataFrame:
    n = len(df)
    prog = ProgressTracker("Pass 1 (spreads/zones)", n)
    results = []
    for i, row in df.iterrows():
        spreads = calculate_spreads(
            row['TEMA'], row['KC_Upper'], row['KC_Middle'], row['KC_Lower'], point
        )
        active_line, zone = determine_active_line(spreads)
        results.append({
            'bar_index':     i,
            'time':          row['Time'],
            'close':         row['Close'],
            'tema':          row['TEMA'],
            'kc_upper':      row['KC_Upper'],
            'kc_middle':     row['KC_Middle'],
            'kc_lower':      row['KC_Lower'],
            'spread_upper':  spreads['spread_upper'],
            'spread_middle': spreads['spread_middle'],
            'spread_lower':  spreads['spread_lower'],
            'active_line':   active_line,
            'zone':          zone
        })
        prog.tick()
    prog.done()
    return pd.DataFrame(results)


def pass2_l1_calculation(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['L1_state']         = None
    df['zone_switch']      = 'N'
    df['active_spread']    = None
    df['active_spread_prev'] = None

    n = len(df)
    prog = ProgressTracker("Pass 2 (L1 states)  ", n - 1)
    for i in range(1, n):
        curr = df.iloc[i]
        prev = df.iloc[i - 1]
        al = curr['active_line']
        spread_key = {'U': 'spread_upper', 'M': 'spread_middle', 'L': 'spread_lower'}[al]
        spread_curr = curr[spread_key]
        spread_prev = prev[spread_key]
        l1_state    = calculate_spread_delta_state(spread_curr, spread_prev)
        zone_switch = 'Y' if curr['active_line'] != prev['active_line'] else 'N'
        df.at[i, 'L1_state']          = l1_state
        df.at[i, 'zone_switch']       = zone_switch
        df.at[i, 'active_spread']     = spread_curr
        df.at[i, 'active_spread_prev'] = spread_prev
        prog.tick()
    prog.done()
    return df


def pass3_l0_calculation(df: pd.DataFrame, point: float = 0.001) -> pd.DataFrame:
    df = df.copy()
    df['slope_1']    = None
    df['slope_2']    = None
    df['slope_delta'] = None
    df['L0_state']   = None

    n = len(df)
    prog = ProgressTracker("Pass 3 (L0 states)  ", n - 2)
    for i in range(2, n):
        tema_n  = df.iloc[i]['tema']
        tema_n1 = df.iloc[i - 1]['tema']
        tema_n2 = df.iloc[i - 2]['tema']
        slope_1     = round_to_point(tema_n1 - tema_n2, point)
        slope_2     = round_to_point(tema_n  - tema_n1, point)
        slope_delta = round_to_point(slope_2 - slope_1, point)
        df.at[i, 'slope_1']    = slope_1
        df.at[i, 'slope_2']    = slope_2
        df.at[i, 'slope_delta'] = slope_delta
        df.at[i, 'L0_state']   = calculate_l0_state(slope_delta)
        prog.tick()
    prog.done()
    return df


def pass4_symbol_encoding(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['symbol'] = None

    n = len(df)
    prog = ProgressTracker("Pass 4 (symbols)    ", n - 2)
    for i in range(2, n):
        row = df.iloc[i]
        if pd.isna(row['L0_state']) or pd.isna(row['L1_state']):
            prog.tick()
            continue
        symbol = (f"L0:{int(row['L0_state']):+d}"
                  f"|L1:{row['L1_state']}"
                  f"|ZS:{row['zone_switch']}"
                  f"|Z:{row['zone']}")
        df.at[i, 'symbol'] = symbol
        prog.tick()
    prog.done()
    return df


def pass5_pattern_mining(df: pd.DataFrame, min_length: int = 2, min_frequency: int = 2) -> dict:
    valid_mask = df['symbol'].notna()
    valid_df   = df[valid_mask].copy()
    symbols    = valid_df['symbol'].tolist()
    indices    = valid_df.index.tolist()
    n          = len(symbols)

    if n < min_length:
        return {}

    total_iters = sum(n - l + 1 for l in range(min_length, n + 1))
    print(f"Pass 5: {n:,} symbols → {total_iters:,} total iterations per sub-pass")

    TICK_BATCH = 500

    # ------------------------------------------------------------------
    # Sub-pass A: count only, no instance storage
    # ------------------------------------------------------------------
    counts     = defaultdict(int)
    prog       = ProgressTracker("Pass 5a (count)     ", total_iters)
    tick_accum = 0

    for length in range(min_length, n + 1):
        for start in range(n - length + 1):
            counts[tuple(symbols[start:start + length])] += 1
            tick_accum += 1
            if tick_accum >= TICK_BATCH:
                prog.tick(tick_accum)
                tick_accum = 0

    if tick_accum:
        prog.tick(tick_accum)
    prog.done()

    # Keep only patterns that meet the frequency threshold
    qualifying = {p for p, c in counts.items() if c >= min_frequency}
    del counts  # release memory before sub-pass B
    print(f"  {len(qualifying):,} patterns qualify (freq >= {min_frequency})")

    # ------------------------------------------------------------------
    # Sub-pass B: record instances only for qualifying patterns
    # ------------------------------------------------------------------
    pattern_data = {p: {'count': 0, 'instances': []} for p in qualifying}
    prog         = ProgressTracker("Pass 5b (instances) ", total_iters)
    tick_accum   = 0

    for length in range(min_length, n + 1):
        for start in range(n - length + 1):
            pattern = tuple(symbols[start:start + length])
            if pattern in qualifying:
                pattern_data[pattern]['count'] += 1
                pattern_data[pattern]['instances'].append(
                    (indices[start], indices[start + length - 1])
                )
            tick_accum += 1
            if tick_accum >= TICK_BATCH:
                prog.tick(tick_accum)
                tick_accum = 0

    if tick_accum:
        prog.tick(tick_accum)
    prog.done()

    return pattern_data


# ---------------------------------------------------------------------------
# Export helpers (unchanged)
# ---------------------------------------------------------------------------

def export_l1_output(df: pd.DataFrame, output_path: str) -> None:
    output_cols = [
        'bar_index', 'time', 'close', 'tema',
        'spread_upper', 'spread_middle', 'spread_lower',
        'active_line', 'zone', 'zone_switch',
        'L1_state', 'active_spread',
        'slope_1', 'slope_2', 'slope_delta', 'L0_state',
        'symbol'
    ]
    existing_cols = [c for c in output_cols if c in df.columns]
    df[existing_cols].to_csv(output_path, index=False, encoding='utf-8')
    print(f"Exported L1 data: {len(df)} rows to {output_path}")


def export_l2_patterns(patterns: dict, output_path: str) -> None:
    rows = [
        {
            'pattern_length': len(pattern),
            'frequency':      data['count'],
            'pattern':        ' -> '.join(pattern)
        }
        for pattern, data in sorted(patterns.items(), key=lambda x: -x[1]['count'])
    ]
    pd.DataFrame(rows).to_csv(output_path, index=False, encoding='utf-8')
    print(f"Exported L2 patterns: {len(rows)} patterns to {output_path}")


def export_visualization_csv(df: pd.DataFrame, patterns: dict, output_path: str,
                              min_length: int = 4, min_frequency: int = 2,
                              filter_mode: str = 'AND') -> None:
    colors = ['BLUE', 'RED', 'GREEN', 'MAGENTA', 'CYAN',
              'ORANGE', 'PURPLE', 'YELLOW', 'LIME', 'MAROON']

    filtered_patterns = []
    for pattern, data in patterns.items():
        meets_length = len(pattern) >= min_length
        meets_freq   = data['count'] >= min_frequency
        include = (meets_length and meets_freq) if filter_mode == 'AND' else (meets_length or meets_freq)
        if include:
            filtered_patterns.append((pattern, data))

    if not filtered_patterns:
        print(f"No patterns meet criteria: length>={min_length}, freq>={min_frequency}, mode={filter_mode}")
        pd.DataFrame(columns=['pattern_type', 'start_time', 'end_time',
                               'high_price', 'low_price', 'color', 'description']
                     ).to_csv(output_path, index=False, encoding='utf-8')
        return

    print(f"Found {len(filtered_patterns)} patterns meeting criteria")
    filtered_patterns.sort(key=lambda x: -x[1]['count'])

    rows = []
    for pattern_idx, (pattern, data) in enumerate(filtered_patterns):
        color       = colors[pattern_idx % len(colors)]
        frequency   = data['count']
        pattern_len = len(pattern)
        for inst_idx, (start_bar, end_bar) in enumerate(data['instances']):
            try:
                start_row     = df.loc[start_bar]
                end_row       = df.loc[end_bar]
                pattern_slice = df.loc[start_bar:end_bar]
                if 'high' in pattern_slice.columns and 'low' in pattern_slice.columns:
                    high_price = pattern_slice['high'].max()
                    low_price  = pattern_slice['low'].min()
                else:
                    high_price = pattern_slice['close'].max()
                    low_price  = pattern_slice['close'].min()
                price_range = max(high_price - low_price, 0.001)
                high_price += price_range * 0.1
                low_price  -= price_range * 0.1
                rows.append({
                    'pattern_type': f"P{pattern_idx+1}_L{pattern_len}",
                    'start_time':   start_row['time'],
                    'end_time':     end_row['time'],
                    'high_price':   round(high_price, 6),
                    'low_price':    round(low_price,  6),
                    'color':        color,
                    'description':  f"P{pattern_idx+1} L={pattern_len} F={frequency} #{inst_idx+1}"
                })
            except Exception as e:
                print(f"Error processing instance {start_bar}-{end_bar}: {e}")

    pd.DataFrame(rows).to_csv(output_path, index=False, encoding='utf-8')
    print(f"Exported {len(rows)} shading blocks for {len(filtered_patterns)} patterns to {output_path}")


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------

def run_analysis(input_path: str, output_dir: str = None, point: float = 0.001,
                 min_length: int = 4, min_frequency: int = 2,
                 filter_mode: str = 'AND') -> Tuple[pd.DataFrame, dict]:
    if output_dir is None:
        output_dir = '.'

    print(f"Loading {input_path}...")
    try:
        df = pd.read_csv(input_path, encoding='utf-16')
    except Exception:
        df = pd.read_csv(input_path, encoding='utf-8')
    print(f"Loaded {len(df):,} bars")

    df = pass1_raw_calculations(df, point)
    df = pass2_l1_calculation(df)
    df = pass3_l0_calculation(df, point)
    df = pass4_symbol_encoding(df)

    valid_symbols = df['symbol'].notna().sum()
    print(f"Generated {valid_symbols:,} symbols")

    patterns = pass5_pattern_mining(df, min_length=2, min_frequency=2)
    print(f"Found {len(patterns):,} significant patterns")

    base_name = input_path.replace('.csv', '')
    export_l1_output(df,       f"{base_name}_L1_output.csv")
    export_l2_patterns(patterns, f"{base_name}_L2_catalog.csv")
    export_visualization_csv(df, patterns, f"{base_name}_patterns.csv",
                             min_length=min_length, min_frequency=min_frequency,
                             filter_mode=filter_mode)
    return df, patterns


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='TEMA/KC Pattern Analyzer',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python tema_kc_pattern_analyzer.py data.csv
  python tema_kc_pattern_analyzer.py data.csv -l 5 -f 3 -m AND
  python tema_kc_pattern_analyzer.py data.csv 0.01 -l 4 -m OR
        """
    )
    parser.add_argument('input_file', nargs='?',
                        default='TEMA_KC_Data_USDJPY.a_CURRENT.csv',
                        help='Input CSV file from MT5')
    parser.add_argument('point', nargs='?', type=float, default=0.001,
                        help='Point size for rounding (default: 0.001)')
    parser.add_argument('-l', type=int, default=4,
                        help='Minimum pattern length (default: 4)')
    parser.add_argument('-f', type=int, default=2,
                        help='Minimum pattern frequency (default: 2)')
    parser.add_argument('-m', choices=['AND', 'OR'], default='AND',
                        help='Filter mode: AND or OR (default: AND)')

    args = parser.parse_args()
    print(f"Point size: {args.point}")
    print(f"Filter: length>={args.l}, freq>={args.f}, mode={args.m}")

    MT5_COMMON_FILES = r"C:\Users\Millard\AppData\Roaming\MetaQuotes\Terminal\Common\Files"

    df, patterns = run_analysis(
        MT5_COMMON_FILES + "\\" + args.input_file,
        point=args.point,
        min_length=args.l,
        min_frequency=args.f,
        filter_mode=args.m
    )

    print("\nAnalysis complete!")

    if patterns:
        print("\nTop 10 most frequent patterns:")
        for pattern, data in sorted(patterns.items(), key=lambda x: -x[1]['count'])[:10]:
            print(f"  {data['count']}x (L={len(pattern)}): {' -> '.join(pattern)}")


if __name__ == "__main__":
    main()
```

[File attached: unnamed — contents not included in export]

### Claude · 2026-02-17 20:52

No. This is your TEMA/KC Pattern Analyzer. I haven't seen or written this code before.
