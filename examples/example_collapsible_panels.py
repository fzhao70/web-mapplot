"""
Example: Collapsible Control Panels

This example demonstrates the collapsible control panels feature which helps
save screen space and provides a cleaner interface. Perfect for dashboards
with many controls or for mobile/tablet viewing.
"""

import numpy as np
from datetime import datetime, timedelta
from web_mapplot import MapPlot

# Create dataset with multiple variables
lon = np.linspace(-130, -60, 80)
lat = np.linspace(25, 50, 64)
lon2d, lat2d = np.meshgrid(lon, lat)

# Time series data
num_timesteps = 10
timestamps = [datetime(2024, 1, 1) + timedelta(hours=i*6) for i in range(num_timesteps)]

# Temperature (3D)
temp_data = []
for t in range(num_timesteps):
    phase = t * np.pi / 5
    temp = 15 + 15 * np.sin((lon2d + 95) / 15 + phase) * np.cos((lat2d - 37.5) / 10)
    temp_data.append(temp)
temp_data = np.array(temp_data)

# Pressure (3D)
pressure_data = []
for t in range(num_timesteps):
    phase = t * np.pi / 5
    pressure = 1013 + 10 * np.cos((lon2d + 90) / 20 + phase) * np.sin((lat2d - 35) / 12)
    pressure_data.append(pressure)
pressure_data = np.array(pressure_data)

# Wind components (3D)
u_wind_data = []
v_wind_data = []
for t in range(num_timesteps):
    phase = t * np.pi / 5
    u_wind = 5 * np.sin((lon2d + 100) / 25 + phase)
    v_wind = 5 * np.cos((lat2d - 40) / 15 + phase)
    u_wind_data.append(u_wind)
    v_wind_data.append(v_wind)
u_wind_data = np.array(u_wind_data)
v_wind_data = np.array(v_wind_data)
wind_speed = np.sqrt(u_wind_data**2 + v_wind_data**2)

# Create map plot
mp = MapPlot(title='Collapsible Panels Demo - Multi-Variable Dashboard')

# Add multiple variables
mp.add_variable(
    name='Temperature',
    lon=lon2d,
    lat=lat2d,
    data=temp_data,
    timestamps=timestamps,
    plot_type='filled_contour',
    colormap='jet',
    units='°C'
)

mp.add_variable(
    name='Pressure',
    lon=lon2d,
    lat=lat2d,
    data=pressure_data,
    timestamps=timestamps,
    plot_type='contour',
    colormap='viridis',
    units='hPa'
)

mp.add_variable(
    name='Wind',
    lon=lon2d,
    lat=lat2d,
    data=wind_speed,
    timestamps=timestamps,
    u_component=u_wind_data,
    v_component=v_wind_data,
    plot_type='vector',
    colormap='cool',
    units='m/s',
    vector_scale=1.5
)

# Save visualization
output_file = mp.save_html('output_collapsible_panels.html')

print("=" * 70)
print("COLLAPSIBLE CONTROL PANELS")
print("=" * 70)
print(f"\nOutput saved to: {output_file}")
print("\n🎛️  COLLAPSIBLE PANELS FEATURES:")
print("\n✨ All control sections are now collapsible:")
print("   1. Variable Selection")
print("   2. Layer Visibility")
print("   3. Time Control")
print("   4. Visualization Settings")
print("\n📱 HOW TO USE:")
print("   • Click any section header to collapse/expand")
print("   • Arrow indicator shows current state (▼ = expanded, ▶ = collapsed)")
print("   • Smooth animations when collapsing/expanding")
print("   • Settings persist during your session")
print("\n💡 BENEFITS:")
print("   ✓ Save screen space - collapse unused sections")
print("   ✓ Cleaner interface - focus on what you need")
print("   ✓ Mobile-friendly - better for smaller screens")
print("   ✓ Organized layout - group related controls")
print("   ✓ Easy navigation - find controls quickly")
print("\n🎯 PERFECT FOR:")
print("   • Dashboards with many controls")
print("   • Mobile and tablet viewing")
print("   • Presentations - minimize distractions")
print("   • Multi-variable visualizations")
print("   • Complex workflows with many options")
print("\n⚙️  CUSTOMIZATION:")
print("   • All sections expand by default")
print("   • Click headers to collapse as needed")
print("   • Hover effect shows clickable areas")
print("   • Smooth CSS transitions (0.3s)")
print("\n" + "=" * 70)
print("Open the HTML file and try collapsing different panels!")
print("Notice how much cleaner the interface becomes.")
print("=" * 70)
