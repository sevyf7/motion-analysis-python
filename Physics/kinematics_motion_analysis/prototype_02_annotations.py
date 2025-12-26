import numpy as np
import matplotlib.pyplot as plt

# Define functions
def x(t):
    return 3*t**2 - 4*t + 2

def v(t):
    return 6*t - 4

def a(t):
    return 6 + 0*t

# Time array for smooth curves
t = np.linspace(0, 10, 500)

# POINTS CONTROL (EDIT THIS)

points_t = np.array([0,5])      # ← just change numbers here
# points_t = np.linspace(0, 10, 5)     # alternative: evenly spaced points
# points_t = np.arange(0, 11, 2)       # alternative: every 2 seconds


# Position vs Time
plt.figure()
plt.plot(t, x(t))
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlabel("Time (s)")
plt.ylabel("x position (m)")
plt.title("Position vs Time")
plt.grid(True)

points_x = x(points_t)
plt.scatter(points_t, points_x)

for t0, x0 in zip(points_t, points_x):
    plt.annotate(
        f"({t0}, {x0:.1f})",
        xy=(t0, x0),
        xytext=(t0 + 0.2, x0 + 10),
        arrowprops=dict(arrowstyle="->")
    )


# Velocity vs Time
plt.figure()
plt.plot(t, v(t))
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity vs Time")
plt.grid(True)

points_v = v(points_t)
plt.scatter(points_t, points_v)

for t0, v0 in zip(points_t, points_v):
    plt.annotate(
        f"({t0}, {v0:.1f})",
        xy=(t0, v0),
        xytext=(t0 + 0.2, v0 + 5),
        arrowprops=dict(arrowstyle="->")
    )

# Acceleration vs Time
plt.figure()
plt.plot(t, a(t))
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s²)")
plt.title("Acceleration vs Time")
plt.grid(True)

points_a = a(points_t)
plt.scatter(points_t, points_a)

for t0, a0 in zip(points_t, points_a):
    plt.annotate(
        f"({t0}, {a0:.1f})",
        xy=(t0, a0),
        xytext=(t0 + 0.2, a0 + 0.5),
        arrowprops=dict(arrowstyle="->")
    )

plt.show()
