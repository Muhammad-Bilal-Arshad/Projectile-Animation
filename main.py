import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
g = 9.81  # Acceleration due to gravity (m/s^2)
v0 = 15.0  # Initial velocity (m/s)
theta = 30.0  # Launch angle (degrees)
dt = 0.01  # Time step (s)

# Convert angle to radians
theta = np.radians(theta)

# Initial conditions
x0, y0 = 0.0, 0.0
vx0 = v0 * np.cos(theta)
vy0 = v0 * np.sin(theta)

# Time array
t_max = 2 * vy0 / g  # Time of flight
t_values = np.arange(0, t_max, dt)

# Calculate projectile motion
x_values = x0 + vx0 * t_values
y_values = y0 + vy0 * t_values - 0.5 * g * t_values ** 2

# Calculate range and maximum height
range_ = x_values[-1]
max_height = np.max(y_values)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, np.max(x_values) * 1.1)
ax.set_ylim(0, np.max(y_values) * 1.1)
ax.set_xlabel("Horizontal Distance (m)", fontsize=14)
ax.set_ylabel("Vertical Distance (m)", fontsize=14)
ax.set_title("Projectile Motion Animation", fontsize=16)

line, = ax.plot([], [], 'o-', lw=2, markersize=6, color='tab:blue')
range_text = ax.text(0.75, 0.95, "", transform=ax.transAxes, fontsize=12, color='tab:green')
height_text = ax.text(0.75, 0.90, "", transform=ax.transAxes, fontsize=12, color='tab:orange')

def init():
    line.set_data([], [])
    range_text.set_text("")
    height_text.set_text("")
    return line, range_text, height_text

def animate(i):
    line.set_data(x_values[:i], y_values[:i])
    range_text.set_text(f"Range: {x_values[i]:.2f} m")
    height_text.set_text(f"Max Height: {y_values[i]:.2f} m")
    return line, range_text, height_text

ani = FuncAnimation(fig, animate, frames=len(t_values), init_func=init, blit=True, interval=dt * 1000)

plt.tight_layout()
plt.show()
