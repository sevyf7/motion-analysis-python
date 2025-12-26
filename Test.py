import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 300)

x = 3*np.cos(t)
y = 2*np.sin(t)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Position: Trajectory of the Particle")
plt.axis("equal")
plt.grid(True)
plt.show()
