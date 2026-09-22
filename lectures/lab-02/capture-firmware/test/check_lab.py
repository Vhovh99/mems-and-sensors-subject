# -*- coding: utf-8 -*-
"""Drive the stubbed firmware and check the lab's own conclusions come out."""
import subprocess, statistics as st, math

LSB = 0.061

def capture(cmds, n):
    out = subprocess.run(["./lab2_test"], input="".join(c+"\n" for c in cmds),
                         capture_output=True, text=True).stdout
    rows, rate = [], None
    for l in out.splitlines():
        if l.startswith("# achieved_rate"): rate = float(l.split("=")[1].split()[0])
        p = l.strip().split(",")
        if len(p) == 5 and p[0].isdigit():
            rows.append((int(p[1]), int(p[2]), int(p[3]), int(p[4])))
    return rows[-n:], rate

print("ODR   sigma_x (mg)   predicted 100ug/rtHz x sqrt(ODR/2)   ratio to previous")
prev = None
sig = {}
for code, hz in ((2,26),(3,52),(4,104),(5,208),(6,416)):
    rows, rate = capture([f"odr {code}", "cap 3000"], 3000)
    sx = st.pstdev([r[1] for r in rows]) * LSB
    pred = 100*math.sqrt(hz/2)/1000
    sig[hz] = (sx, rows, rate)
    r = f"{sx/prev:.3f}" if prev else "   -"
    print(f"{hz:>4}   {sx:>8.3f}       {pred:>8.3f}                        {r}")
    prev = sx

print("\nLPF2 off vs on at 104 Hz:")
for lpf in ("off","on"):
    rows,_ = capture(["odr 4", f"lpf {lpf}", "cap 3000"], 3000)
    print(f"  LPF2 {lpf:>3}: sigma_x = {st.pstdev([r[1] for r in rows])*LSB:.3f} mg")

print("\nMoving average on the 416 Hz capture vs sampling natively slower:")
rows = sig[416][1]
xs = [r[1]*LSB for r in rows]
for N, equiv in ((2,208),(4,104),(8,52),(16,26)):
    ma = [sum(xs[i:i+N])/N for i in range(len(xs)-N+1)]
    print(f"  N={N:>2} on 416 Hz -> {st.pstdev(ma):.3f} mg   |   native {equiv:>3} Hz -> {sig[equiv][0]:.3f} mg")

print("\nAchieved rate vs requested (stage 4's point):")
for hz in (26,104,416):
    print(f"  ODR {hz:>3} Hz -> firmware reports {sig[hz][2]:.2f} Hz achieved")
