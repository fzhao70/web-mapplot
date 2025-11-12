#!/usr/bin/env python3
"""
Quick demo of web_mapplot library
Generates a comprehensive example showing all features
"""

import numpy as np
from datetime import datetime, timedelta
from web_mapplot import MapPlot

print("=" * 60)
print("Web MapPlot - Comprehensive Demo")
print("=" * 60)
print()

# Create spatial grid covering North America
print("Creating spatial grid...")
lon = np.linspace(-130, -60, 60)
lat = np.linspace(20, 55, 50)
lon2d, lat2d = np.meshgrid(lon, lat)

# Create time-series data (12 time steps)
print("Generating time-series data...")
num_timesteps = 12
timestamps = [datetime(2024, 1, 1, 0) + timedelta(hours=i*3) for i in range(num_timesteps)]

# ===== Temperature Field (3D with time) =====
print("  - Temperature field (filled contour, animated)")
temperature_3d = np.zeros((num_timesteps, lat.size, lon.size))
for t in range(num_timesteps):
    phase = t * np.pi / 6
    temperature_3d[t] = 18 + 15 * np.sin(lon2d / 10 + phase) * np.cos(lat2d / 10)

# ===== Pressure Field (2D, static) =====
print("  - Pressure field (contour, static)")
pressure = 1013 + 20 * np.sin(lon2d / 15) * np.cos(lat2d / 12)

# ===== Wind Field (3D with time) =====
print("  - Wind field (vector and stream)")
u_wind = np.zeros((num_timesteps, lat.size, lon.size))
v_wind = np.zeros((num_timesteps, lat.size, lon.size))
for t in range(num_timesteps):
    phase = t * np.pi / 6
    u_wind[t] = 10 + 8 * np.cos(lon2d / 10 + phase) * np.sin(lat2d / 8)
    v_wind[t] = 6 + 5 * np.sin(lon2d / 8) * np.cos(lat2d / 10 + phase)

wind_speed = np.sqrt(u_wind**2 + v_wind**2)

# ===== Precipitation Field (3D with time) =====
print("  - Precipitation field (filled contour, animated)")
precipitation = np.zeros((num_timesteps, lat.size, lon.size))
for t in range(num_timesteps):
    # Create moving precipitation pattern
    precipitation[t] = np.maximum(0,
        8 * np.sin(lon2d / 12 + t * 0.6) * np.cos(lat2d / 10) +
        np.random.random((lat.size, lon.size)) * 3
    )

# ===== Create MapPlot Visualization =====
print()
print("Creating visualization...")
mp = MapPlot(title="Web MapPlot - Full Feature Demo")

# Add all variables
print("  - Adding Temperature variable")
mp.add_variable(
    name='Temperature',
    lon=lon2d,
    lat=lat2d,
    data=temperature_3d,
    plot_type='filled_contour',
    timestamps=timestamps,
    colormap='jet',
    levels=18,
    units='°C'
)

print("  - Adding Pressure variable")
mp.add_variable(
    name='Pressure',
    lon=lon2d,
    lat=lat2d,
    data=pressure,
    plot_type='contour',
    colormap='cool',
    levels=15,
    units='hPa'
)

print("  - Adding Wind (Vector) variable")
mp.add_variable(
    name='Wind (Vectors)',
    lon=lon2d,
    lat=lat2d,
    data=wind_speed,
    plot_type='vector',
    timestamps=timestamps,
    u_component=u_wind,
    v_component=v_wind,
    colormap='viridis',
    units='m/s'
)

print("  - Adding Wind (Stream) variable")
mp.add_variable(
    name='Wind (Streamlines)',
    lon=lon2d,
    lat=lat2d,
    data=wind_speed,
    plot_type='stream',
    timestamps=timestamps,
    u_component=u_wind,
    v_component=v_wind,
    colormap='plasma',
    units='m/s'
)

print("  - Adding Precipitation variable")
mp.add_variable(
    name='Precipitation',
    lon=lon2d,
    lat=lat2d,
    data=precipitation,
    plot_type='filled_contour',
    timestamps=timestamps,
    colormap='rainbow',
    levels=12,
    vmin=0,
    vmax=15,
    units='mm/h'
)

# Save the visualization
print()
print("Saving visualization...")
output_file = mp.save_html('demo_output.html')

print()
print("=" * 60)
print("SUCCESS! Demo visualization created.")
print("=" * 60)
print()
print(f"Output file: {output_file}")
print()
print("Features included in this demo:")
print("  ✓ 5 different variables")
print("  ✓ Multiple plot types (filled contour, contour, vector, stream)")
print("  ✓ Time-series animation (12 time steps)")
print("  ✓ Variable switching capability")
print("  ✓ Interactive controls and colorbar")
print()
print("Open the file in your web browser to explore:")
print("  - Switch between variables using the dropdown")
print("  - Use time controls to animate data")
print("  - Pan and zoom the map")
print("  - Adjust opacity and visualization settings")
print()
print("To run the web server instead:")
print("  python demo.py --server")
print()

# Optional: Launch server if requested
import sys
if '--server' in sys.argv:
    print("Launching web server on http://localhost:5000")
    print("Press Ctrl+C to stop")
    mp.show(port=5000, debug=False)
