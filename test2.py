import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 300)

# Position
x = 3*np.cos(t)
y = 2*np.sin(t)

# Velocity (numerical derivative)
vx = np.gradient(x, t)
vy = np.gradient(y, t)

# Acceleration (numerical derivative of velocity)
ax = np.gradient(vx, t)
ay = np.gradient(vy, t)

# 1) Trajectory
plt.figure()
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Position: Trajectory")
plt.axis("equal")
plt.grid(True)

# 2) Velocity vectors along the path
plt.figure()
plt.plot(x, y)
plt.quiver(x[::20], y[::20], vx[::20], vy[::20], scale=30)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Velocity Vectors (tangent to the path)")
plt.axis("equal")
plt.grid(True)

# 3) Acceleration vectors along the path
plt.figure()
plt.plot(x, y)
plt.quiver(x[::20], y[::20], ax[::20], ay[::20], scale=200)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Acceleration Vectors")
plt.axis("equal")
plt.grid(True)

plt.show()
