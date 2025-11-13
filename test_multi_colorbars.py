"""
Test script for multi-layer colorbars feature.
This creates 3 overlapping layers to test the colorbar display.
"""

import numpy as np
import sys
sys.path.insert(0, '/home/user/web-mapplot')

from web_mapplot import MapPlot

print("Creating test visualization with 3 layers...")

# Create a simple grid
lon = np.linspace(-100, -80, 30)
lat = np.linspace(30, 50, 25)
lon2d, lat2d = np.meshgrid(lon, lat)

# Layer 1: Temperature
temp = 20 + 10 * np.sin(np.radians(lat2d)) * np.cos(np.radians(lon2d))
print("✓ Created temperature layer")

# Layer 2: Pressure
pressure = 1013 + 5 * np.cos(np.radians(lat2d * 2))
print("✓ Created pressure layer")

# Layer 3: Humidity
humidity = 50 + 30 * np.sin(np.radians(lon2d * 2)) * np.sin(np.radians(lat2d))
print("✓ Created humidity layer")

# Create visualization
mp = MapPlot(
    title="Multi-Layer Colorbar Test",
    center=(40, -90),
    zoom=5
)

# Add all layers
mp.add_variable(
    name='Temperature',
    lon=lon2d,
    lat=lat2d,
    data=temp,
    plot_type='filled_contour',
    colormap='jet',
    units='°C'
)

mp.add_variable(
    name='Pressure',
    lon=lon2d,
    lat=lat2d,
    data=pressure,
    plot_type='contour',
    colormap='viridis',
    units='hPa'
)

mp.add_variable(
    name='Humidity',
    lon=lon2d,
    lat=lat2d,
    data=humidity,
    plot_type='filled_contour',
    colormap='plasma',
    units='%'
)

print("✓ Added all 3 variables")

# Save
output_file = mp.save_html('test_multi_colorbars.html')
print(f"\n✅ Success! Saved to {output_file}")
print("\nInstructions:")
print("1. Open test_multi_colorbars.html in your browser")
print("2. You should see 3 colorbars stacked in the bottom-right corner")
print("3. Toggle layer visibility to see colorbars appear/disappear dynamically")
print("4. All visible layers should have their own colorbar displayed")
