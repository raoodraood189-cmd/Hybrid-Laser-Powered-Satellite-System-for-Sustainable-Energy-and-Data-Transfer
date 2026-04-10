import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure(figsize=(10, 8), dpi=100)
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('black')
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

ax.set_title("3D Structural Diagram of Laser Power & Data Transfer", color='white', fontsize=16)

u = np.linspace(0, 2 * np.pi, 50)
v = np.linspace(0, np.pi/2, 50)
earth_radius = 50
x_earth = earth_radius * np.outer(np.cos(u), np.sin(v))
y_earth = earth_radius * np.outer(np.sin(u), np.sin(v))
z_earth = -20 * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x_earth, y_earth, z_earth, color='royalblue', alpha=0.5, label='Earth')

sat_height = 500
sat_center = np.array([-50, 50, sat_height])

r_sat_body, h_sat_body = 5, 10
u_sat = np.linspace(0, 2 * np.pi, 20)
h_sat_range = np.linspace(-h_sat_body/2, h_sat_body/2, 10)
x_sat_body = sat_center[0] + r_sat_body * np.outer(np.cos(u_sat), np.ones(np.size(h_sat_range)))
y_sat_body = sat_center[1] + r_sat_body * np.outer(np.sin(u_sat), np.ones(np.size(h_sat_range)))
z_sat_body = sat_center[2] + np.outer(np.ones(np.size(u_sat)), h_sat_range)
ax.plot_surface(x_sat_body, y_sat_body, z_sat_body, color='darkgray')

panel_w, panel_h = 20, 10
ax.plot([sat_center[0]-panel_w, sat_center[0]+panel_w], [sat_center[1], sat_center[1]], [sat_center[2], sat_center[2]], color='deepskyblue', linewidth=3)
ax.text(sat_center[0], sat_center[1], sat_center[2]+r_sat_body+2, "Laser-Enhanced Solar Panels", color='white', fontsize=9, ha='center')

ground_center = np.array([20, -20, 0])

solar_grid_x = np.linspace(0, 20, 5)
solar_grid_y = np.linspace(-30, -10, 5)
solar_X, solar_Y = np.meshgrid(solar_grid_x, solar_grid_y)
solar_Z = np.zeros_like(solar_X)
ax.plot_surface(solar_X, solar_Y, solar_Z, color='mediumblue', alpha=0.6)

r_dish, h_dish = 8, 12
u_dish = np.linspace(0, 2 * np.pi, 20)
h_dish_range = np.linspace(0, h_dish, 10)
x_dish = ground_center[0] + r_dish * np.outer(np.cos(u_dish), np.ones(np.size(h_dish_range)))
y_dish = ground_center[1] + r_dish * np.outer(np.sin(u_dish), np.ones(np.size(h_dish_range)))
z_dish = np.outer(np.ones(np.size(u_dish)), h_dish_range)
ax.plot_surface(x_dish, y_dish, z_dish, color='silver', alpha=0.8)

receiv_power_pt = np.array([5, -20, 0])
ax.plot([sat_center[0], receiv_power_pt[0]], [sat_center[1], receiv_power_pt[1]], [sat_center[2], receiv_power_pt[2]], color='red', linewidth=3, label='Power Laser')
ax.text(receiv_power_pt[0]-10, receiv_power_pt[1], receiv_power_pt[2]+10, "Power Laser 1064 nm", color='red', fontsize=9, ha='right')

receiv_data_pt = ground_center + np.array([0, 0, h_dish])
ax.plot([sat_center[0], receiv_data_pt[0]], [sat_center[1], receiv_data_pt[1]], [sat_center[2], receiv_data_pt[2]], color='lime', linewidth=3, label='Data Laser')
ax.text(receiv_data_pt[0]+10, receiv_data_pt[1], receiv_data_pt[2]+10, "Data Laser 1550 nm", color='lime', fontsize=9, ha='left')

ax.plot([sat_center[0], sat_center[0]], [sat_center[1], sat_center[1]], [0, sat_height], color='white', linestyle='--', linewidth=0.5)
ax.text(sat_center[0], sat_center[1], sat_height/2, "500 km", color='white', ha='center')

ax.text(ground_center[0], ground_center[1], 15, "Ground Station", color='white', fontsize=10, ha='center')
ax.text(ground_center[0], ground_center[1]-15, 0, "Solar & Wind Power Area: 2000 m2", color='white', fontsize=8, ha='center', bbox=dict(facecolor='black', alpha=0.5))
ax.text(0, -25, 0, "Energy Storage", color='white', fontsize=8, ha='center')

plt.legend(loc='upper right', facecolor='black', edgecolor='white', labelcolor='white')
plt.tight_layout()
plt.show()
