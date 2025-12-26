import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# Define functions
# ----------------------------
def x(t):
    return 3*t**2 - 4*t + 2

def v(t):
    return 6*t - 4

def a(t):
    return 6 + 0*t

# Time array
t = np.linspace(0, 10, 500)

# Points to label
points_t = np.array([1, 3, 5, 7])

# Turning time (direction change)
t_turn = 2 / 3
x_turn = x(t_turn)

# ============================
# Position vs Time
# ============================
plt.figure()
plt.plot(t, x(t))
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlabel("Time (s)")
plt.ylabel("x position (m)")
plt.title("Position vs Time")
plt.grid(True)

# Regular labeled points
points_x = x(points_t)
plt.scatter(points_t, points_x)

for t0, x0 in zip(points_t, points_x):
    plt.annotate(
        f"({t0}, {x0:.1f})",
        xy=(t0, x0),
        xytext=(t0 + 0.25, x0 + 10),
        arrowprops=dict(arrowstyle="->")
    )

# Turning point marker
plt.scatter(t_turn, x_turn, color="red", s=120, zorder=5)

# Vertical event line at direction change (asymptote-style marker)
plt.axvline(t_turn, color="red", linestyle="--", linewidth=2)

# Label placed above plot (won't collide with data)
plt.text(
    t_turn, 1.02,
    f"direction change\nv=0 at t={t_turn:.2f}s",
    color="red",
    ha="center",
    va="bottom",
    transform=plt.gca().get_xaxis_transform()
)

# ============================
# Velocity vs Time
# ============================
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
        xytext=(t0 + 0.25, v0 + 5),
        arrowprops=dict(arrowstyle="->")
    )

# Mark v=0 crossing time with vertical line
plt.scatter(t_turn, 0, color="red", s=120, zorder=5)
plt.axvline(t_turn, color="red", linestyle="--", linewidth=2)

plt.text(
    t_turn, 1.02,
    f"v=0 at t={t_turn:.2f}s",
    color="red",
    ha="center",
    va="bottom",
    transform=plt.gca().get_xaxis_transform()
)

# ============================
# Acceleration vs Time
# ============================
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
        xytext=(t0 + 0.25, a0 + 0.3),
        arrowprops=dict(arrowstyle="->")
    )

# Optional: also show the same event line on acceleration
plt.axvline(t_turn, color="red", linestyle="--", linewidth=2)
plt.text(
    t_turn, 1.02,
    f"t={t_turn:.2f}s",
    color="red",
    ha="center",
    va="bottom",
    transform=plt.gca().get_xaxis_transform()
)

plt.show()
