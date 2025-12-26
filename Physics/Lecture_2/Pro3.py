import numpy as np
import matplotlib.pyplot as plt

#EDIT:  # Find the turning point where velocity is zero (direction change)
        # Draw and label the tangent line at the direction-change point on the position graph
        # Mark and label the direction-change point on the velocity graph (v = 0)
        # Define functions
        
# ----------------------------
# Define functions
# ----------------------------
def x(t):
    return 3*t**2 - 4*t + 2

def v(t):
    return 6*t - 4

def a(t):
    return 6 + 0*t

# Time array for smooth curves
t = np.linspace(0, 10, 500)

# ----------------------------
# Points you want labeled
# ----------------------------
points_t = np.array([1, 3, 5, 7])

# ----------------------------
# Turning point (direction change)
# v(t) = 0 → 6t - 4 = 0 → t = 2/3
# ----------------------------
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
        xytext=(t0 + 0.2, x0 + 10),
        arrowprops=dict(arrowstyle="->")
    )

# --- Direction change point (VERY clear) ---
plt.scatter(t_turn, x_turn, color="red", s=120, zorder=5)

# Tangent line (horizontal because v = 0)
t_tangent = np.linspace(t_turn - 1, t_turn + 1, 50)
x_tangent = x_turn + 0*(t_tangent - t_turn)
plt.plot(t_tangent, x_tangent, linestyle="--", color="red")

plt.annotate(
    f"Direction changes\nv = 0 at t = {t_turn:.2f} s",
    xy=(t_turn, x_turn),
    xytext=(2.0, 40),
    arrowprops=dict(arrowstyle="->", lw=2),
    fontsize=12,
    color="red"
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
        xytext=(t0 + 0.2, v0 + 5),
        arrowprops=dict(arrowstyle="->")
    )

# Mark v = 0 clearly
plt.scatter(t_turn, 0, color="red", s=120, zorder=5)

plt.annotate(
    f"v = 0 at t = {t_turn:.2f} s",
    xy=(t_turn, 0),
    xytext=(2.0, 8),
    arrowprops=dict(arrowstyle="->", lw=2),
    fontsize=12,
    color="red"
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
        xytext=(t0 + 0.2, a0 + 0.5),
        arrowprops=dict(arrowstyle="->")
    )

plt.show()
