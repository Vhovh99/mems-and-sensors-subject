#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reference analysis for a Laboratory 2 capture — for the INSTRUCTOR.

Students do this in a spreadsheet; that is the point of the exercise, and it is
outcomes Lab2.2 to Lab2.4. This script exists so that you can check a team's
numbers in ten seconds at the bench, and so that you can fill in the soft row of
the answer key (the LPF2 ratio) from your own part.

    ./analyse_capture.py baseline_0x40.csv
    ./analyse_capture.py baseline_0x40.csv filtered_0x42.csv     # compare two
    ./analyse_capture.py sweep_*.csv                             # tabulate a sweep

Reads the CSV the capture firmware emits, including its `#` comment lines, and
reports exactly the quantities the handout asks students to produce.
"""
import sys, math, glob, re

SENS_UG_PER_LSB = {0: 61, 1: 488, 2: 122, 3: 244}     # FS_XL code -> µg/LSB
ODR_HZ = {1: 12.5, 2: 26, 3: 52, 4: 104, 5: 208, 6: 416}


def read(path):
    """-> (ctrl1 or None, [(t_ms, x, y, z)], reported_rate or None)"""
    ctrl1, rows, rate = None, [], None
    with open(path, encoding="utf-8", errors="replace") as fh:
        for ln in fh:
            ln = ln.strip()
            m = re.search(r"CTRL1_XL=0x([0-9A-Fa-f]{2})", ln)
            if m:
                ctrl1 = int(m.group(1), 16)
            m = re.search(r"achieved_rate=([\d.]+)", ln)
            if m:
                rate = float(m.group(1))
            p = ln.split(",")
            if len(p) == 5 and p[0].isdigit():
                rows.append(tuple(int(v) for v in p[1:5]))
    return ctrl1, rows, rate


def stats(vals):
    n = len(vals)
    mean = sum(vals) / n
    var = sum((v - mean) ** 2 for v in vals) / n         # population, = STDEV.P
    return mean, math.sqrt(var)


def moving_average(vals, N):
    return [sum(vals[i:i + N]) / N for i in range(len(vals) - N + 1)]


def low_pass(vals, alpha):
    out, y = [], vals[0]
    for v in vals:
        y += alpha * (v - y)
        out.append(y)
    return out


def report(path):
    ctrl1, rows, rate = read(path)
    if not rows:
        print(f"{path}: no data rows found")
        return None

    lsb = SENS_UG_PER_LSB[(ctrl1 >> 2) & 3] / 1000.0 if ctrl1 is not None else 0.061
    odr = ODR_HZ.get((ctrl1 >> 4) & 0xF) if ctrl1 is not None else None
    lpf = (ctrl1 >> 1) & 1 if ctrl1 is not None else None

    t = [r[0] for r in rows]
    axes = {ax: [r[i + 1] for r in rows] for i, ax in enumerate("xyz")}

    print(f"\n=== {path} ===")
    if ctrl1 is not None:
        print(f"CTRL1_XL 0x{ctrl1:02X}   ODR {odr} Hz   LSB {lsb:.4f} mg   LPF2 {'on' if lpf else 'off'}")
    print(f"samples {len(rows)}")

    print(f"\n{'axis':<5}{'mean (codes)':>14}{'mean (mg)':>12}"
          f"{'sigma (LSB)':>13}{'sigma (mg)':>12}")
    sig = {}
    for ax, v in axes.items():
        m, s = stats(v)
        sig[ax] = s
        print(f"{ax:<5}{m:>14.1f}{m*lsb:>12.2f}{s:>13.2f}{s*lsb:>12.4f}")

    mx, my, mz = (stats(axes[a])[0] * lsb for a in "xyz")
    print(f"\nmean vector magnitude   {math.hypot(math.hypot(mx, my), mz):.2f} mg"
          f"   (expect ~1000 flat)")
    print(f"zero-g offset X / Y     {mx:+.2f} / {my:+.2f} mg"
          f"   (datasheet +/-10 typ, +/-65 max)")

    s_lsb = sig["x"]
    if s_lsb > 0:
        lost = math.log2(s_lsb)
        print(f"\neffective bits (X)      16 - log2({s_lsb:.2f}) = 16 - {lost:.2f}"
              f" = {16-lost:.2f} bits")
    if odr:
        for dens, tag in ((60, "typ"), (100, "max")):
            pred = dens * math.sqrt(odr / 2) / 1000
            print(f"predicted sigma ({tag:>3})    {pred:.4f} mg"
                  f"   -> measured/predicted = {sig['x']*lsb/pred:.2f}")
        got = sig["x"] * lsb / math.sqrt(odr / 2) * 1000
        print(f"YOUR PART's density     {got:.0f} ug/rtHz   (from the X axis)")

    if len(t) >= 2 and t[-1] > t[0]:
        mean_int = (t[-1] - t[0]) / (len(t) - 1)
        print(f"\nmean interval           {mean_int:.4f} ms -> {1000/mean_int:.2f} Hz")
        if rate:
            print(f"firmware reported       {rate:.2f} Hz")
        if odr:
            err = (1000 / mean_int - odr) / odr * 100
            print(f"vs ODR {odr} Hz           {err:+.2f} %")
            drift = (t[-1] - t[0]) / 1000 - len(t) / odr
            print(f"drift over the capture  {drift:+.2f} s if you assume 1/ODR spacing")

    print("\nfiltering the X axis:")
    raw_s = sig["x"] * lsb
    print(f"  {'raw':<24}{raw_s:.4f} mg")
    for N in (2, 4, 8, 16):
        s = stats(moving_average(axes["x"], N))[1] * lsb
        print(f"  {'moving average N=%-2d' % N:<24}{s:.4f} mg"
              f"   reduction {raw_s/s:.2f}x   (sqrt{N} = {math.sqrt(N):.2f})"
              f"   delay {(N-1)/2/(odr or 1)*1000:.1f} ms" if odr else
              f"  {'moving average N=%-2d' % N:<24}{s:.4f} mg   reduction {raw_s/s:.2f}x")
    for a in (0.25, 0.125):
        s = stats(low_pass(axes["x"], a))[1] * lsb
        print(f"  {'low-pass alpha=%-8s' % a:<24}{s:.4f} mg   reduction {raw_s/s:.2f}x")

    return {"path": path, "ctrl1": ctrl1, "odr": odr, "lpf": lpf,
            "sigma_mg": sig["x"] * lsb, "rate": rate}


def main(paths):
    if not paths:
        print(__doc__)
        return
    out = [r for r in (report(p) for p in paths) if r]

    # Only a genuine sweep — two captures at the SAME rate are an LPF2 pair, and
    # the "ratio to previous row" column would misdescribe them as a doubling.
    sweep = sorted([r for r in out if r["odr"]], key=lambda r: r["odr"])
    if len({r["odr"] for r in sweep}) > 1:
        print("\n\n=== sweep summary — this is the students' stage 3 table ===")
        print(f"{'ODR':>5}{'LPF2':>6}{'BW':>7}{'sigma (mg)':>12}"
              f"{'ratio':>8}{'achieved (Hz)':>15}")
        prev = None
        for r in sweep:
            ratio = f"{r['sigma_mg']/prev:.3f}" if prev else "-"
            print(f"{r['odr']:>5}{'on' if r['lpf'] else 'off':>6}{r['odr']/2:>7.1f}"
                  f"{r['sigma_mg']:>12.4f}{ratio:>8}"
                  f"{(r['rate'] or float('nan')):>15.2f}")
            prev = r["sigma_mg"]
        print("\nthe ratio column should sit near sqrt(2) = 1.414 for each doubling")

    pair = [r for r in out if r["lpf"] is not None]
    offs = [r for r in pair if not r["lpf"]]
    ons  = [r for r in pair if r["lpf"]]
    if offs and ons:
        a, b = offs[0]["sigma_mg"], ons[0]["sigma_mg"]
        print(f"\n=== LPF2 off vs on ===  {a:.4f} -> {b:.4f} mg   ratio {a/b:.3f}")
        print("Put this ratio in instructor-notes.md, 'the one soft number in this lab'.")


if __name__ == "__main__":
    args = []
    for a in sys.argv[1:]:
        args.extend(sorted(glob.glob(a)) or [a])
    main(args)
