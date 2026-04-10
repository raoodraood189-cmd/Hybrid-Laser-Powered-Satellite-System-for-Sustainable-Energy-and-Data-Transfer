import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure(figsize=(14, 10), dpi=120)
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('black')
ax.xaxis.pane.set_facecolor((0, 0, 0, 1))
ax.yaxis.pane.set_facecolor((0, 0, 0, 1))
ax.zaxis.pane.set_facecolor((0, 0, 0, 1))
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_xlim(-120, 120)
ax.set_ylim(-120, 120)
ax.set_zlim(-30, 120)
ax.set_title('Satellite Laser & SATCOM Simulation', color='white', fontsize=18, pad=20)

# Star field
rng = np.random.default_rng(42)
stars_x = rng.uniform(-160, 160, 400)
stars_y = rng.uniform(-160, 160, 400)
stars_z = rng.uniform(15, 120, 400)
ax.scatter(stars_x, stars_y, stars_z, color='white', s=2, alpha=0.8)

# Earth horizon and atmosphere gradient
u = np.linspace(0, 2 * np.pi, 120)
v = np.linspace(0, np.pi / 2, 50)
earth_radius = 110
x_earth = earth_radius * np.outer(np.cos(u), np.sin(v))
y_earth = earth_radius * np.outer(np.sin(u), np.sin(v))
z_earth = -30 + 15 * np.outer(np.ones_like(u), np.cos(v))
ax.plot_surface(x_earth, y_earth, z_earth, color='#0b2749', alpha=0.75, linewidth=0, shade=True)

# Ground platform and antenna dish
ground_center = np.array([30, -25, 0])
platform_x = np.linspace(ground_center[0] - 18, ground_center[0] + 18, 2)
platform_y = np.linspace(ground_center[1] - 18, ground_center[1] + 18, 2)
platform_X, platform_Y = np.meshgrid(platform_x, platform_y)
platform_Z = np.full_like(platform_X, 0.5)
ax.plot_surface(platform_X, platform_Y, platform_Z, color='#1a2330', alpha=0.9)

r_dish = 12
u_dish = np.linspace(0, 2 * np.pi, 80)
v_dish = np.linspace(0, np.pi / 2, 30)
x_dish = ground_center[0] + r_dish * np.outer(np.cos(u_dish), np.sin(v_dish))
y_dish = ground_center[1] + r_dish * np.outer(np.sin(u_dish), np.sin(v_dish))
z_dish = 0.5 + 5 * np.outer(np.ones_like(u_dish), np.cos(v_dish))
ax.plot_surface(x_dish, y_dish, z_dish, color='#d4d4d4', alpha=0.95)
ax.plot([ground_center[0], ground_center[0]], [ground_center[1], ground_center[1]], [0.5, 1.5], color='gray', linewidth=4)
ax.plot([ground_center[0], ground_center[0] + 2], [ground_center[1], ground_center[1]], [1.5, 4], color='gray', linewidth=3)
ax.scatter([ground_center[0]], [ground_center[1]], [8], color='black', s=50)
ax.text(ground_center[0], ground_center[1], 11, 'Ground Dish', color='white', fontsize=10, ha='center')

# Airplane
plane_center = np.array([60, 55, 25])
wing_span = 30
body_length = 42
body_x = np.linspace(plane_center[0] - body_length / 2, plane_center[0] + body_length / 2, 5)
body_y = np.full_like(body_x, plane_center[1])
body_z = np.full_like(body_x, plane_center[2])
ax.plot(body_x, body_y, body_z, color='white', linewidth=5)
ax.plot([plane_center[0] - 12, plane_center[0] + 12], [plane_center[1] - 8, plane_center[1] - 8], [plane_center[2], plane_center[2]], color='white', linewidth=6)
ax.plot([plane_center[0] - 12, plane_center[0] + 12], [plane_center[1] + 8, plane_center[1] + 8], [plane_center[2], plane_center[2]], color='white', linewidth=6)
ax.plot([plane_center[0] + 15, plane_center[0] + 20], [plane_center[1], plane_center[1]], [plane_center[2], plane_center[2] + 10], color='white', linewidth=4)
ax.plot([plane_center[0] - 18, plane_center[0] - 15], [plane_center[1], plane_center[1]], [plane_center[2], plane_center[2] + 8], color='white', linewidth=4)
ax.scatter([plane_center[0]], [plane_center[1]], [plane_center[2] + 3], color='white', s=50)
ax.text(plane_center[0] + 18, plane_center[1] + 4, plane_center[2] + 10, 'Aircraft SATCOM', color='cyan', fontsize=10, ha='center')

# Satellite
sat_center = np.array([-45, 20, 95])
body_radius = 5
body_height = 18
theta = np.linspace(0, 2 * np.pi, 40)
z_body = np.linspace(-body_height / 2, body_height / 2, 16)
theta_grid, z_grid = np.meshgrid(theta, z_body)
x_body = sat_center[0] + body_radius * np.cos(theta_grid)
y_body = sat_center[1] + body_radius * np.sin(theta_grid)
z_body = sat_center[2] + z_grid
ax.plot_surface(x_body, y_body, z_body, color='#b2b2b2', alpha=0.95)

# Solar panels
panel_width = 22
panel_height = 6
panel_y = sat_center[1] + 12
ax.plot([sat_center[0] - panel_width / 2, sat_center[0] + panel_width / 2], [panel_y, panel_y], [sat_center[2] + 2, sat_center[2] + 2], color='#1f78b4', linewidth=8)
panel_y2 = sat_center[1] - 12
ax.plot([sat_center[0] - panel_width / 2, sat_center[0] + panel_width / 2], [panel_y2, panel_y2], [sat_center[2] + 2, sat_center[2] + 2], color='#1f78b4', linewidth=8)

ax.text(sat_center[0], sat_center[1], sat_center[2] + 16, 'Laser Satellite', color='white', fontsize=10, ha='center')

# Laser beams with glow effect
dish_target = np.array([ground_center[0], ground_center[1], 8])
plane_target = np.array([plane_center[0], plane_center[1], plane_center[2] + 4])
for alpha, width, color in [(0.12, 12, 'red'), (0.2, 8, 'red')]:
    ax.plot([sat_center[0], dish_target[0]], [sat_center[1], dish_target[1]], [sat_center[2] - 3, dish_target[2]], color=color, linewidth=width, alpha=alpha)
for alpha, width, color in [(0.12, 12, 'lime'), (0.2, 8, 'lime')]:
    ax.plot([sat_center[0], dish_target[0]], [sat_center[1], dish_target[1]], [sat_center[2] + 3, dish_target[2]], color=color, linewidth=width, alpha=alpha)
for alpha, width, color in [(0.12, 12, 'deepskyblue'), (0.2, 8, 'deepskyblue')]:
    ax.plot([sat_center[0], plane_target[0]], [sat_center[1], plane_target[1]], [sat_center[2], plane_target[2]], color=color, linewidth=width, alpha=alpha)

ax.scatter([dish_target[0]], [dish_target[1]], [dish_target[2]], color='yellow', s=60)
ax.text(dish_target[0], dish_target[1] - 8, dish_target[2] + 2, 'Ground Receiver', color='white', fontsize=9, ha='center')

# Annotations
ax.text(sat_center[0] - 8, sat_center[1] + 18, sat_center[2] + 5, 'Energy laser (green)', color='lime', fontsize=9, ha='center')
ax.text(sat_center[0] - 8, sat_center[1] + 14, sat_center[2] - 2, 'Power laser (red)', color='red', fontsize=9, ha='center')
ax.text(plane_center[0] + 24, plane_center[1] + 10, plane_center[2] + 8, 'Data SATCOM link', color='cyan', fontsize=9, ha='center')
ax.text(-110, -110, 115, 'Full simulation of your image', color='white', fontsize=10, ha='left')

plt.tight_layout()
plt.savefig('full_image_simulation.png', dpi=150)
plt.show()

