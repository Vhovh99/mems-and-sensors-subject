# IMU register driver — held for later laboratories

**This is not Laboratory 1 material.** It was written for Lab 1 and then deliberately
moved: in the first offering the students do not yet have the microcontroller
experience the semester plan assumes as entry background, so Lab 1 runs with no
compilation at all (see `lab-01/`).

Keep this. It is the natural fit for the point in the semester where students begin
authoring firmware.

| File | What it is | Where it belongs |
|---|---|---|
| `imu.h` | Register map and scaling constants, every datasheet value left as `0xFF` TODO | The lab where students first fill in a driver header from a datasheet |
| `imu.c` | Complete, working I²C register driver — burst read, read-modify-write, two's-complement assembly, scaling | Reference implementation. Read it in an earlier lab, write your own version later |
| `main_lab1.c` | Probe → configure → log 200 CSV samples, refuses to print data if the probe fails | Template for any acquisition lab |

## Suggested placement

- **Lab 3** (accelerometer/gyro characterisation) — students fill in `imu.h` only, with
  `imu.c` supplied and read aloud in the pre-lab. First contact with a build.
- **Lab 7** (robust analog and digital integration) — students write their own
  equivalent of `imu.c`, with this one available as the reference to compare against.
- **Lab 8** (capstone) — the plan requires students to submit source files; this is the
  shape those files should take.

The one design decision worth preserving: `main_lab1.c` **refuses to print measurement
data when the device probe fails.** Reporting numbers you cannot attribute to a known
device is exactly the failure this course is about.
