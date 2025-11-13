"""
Example: Isosurface Rendering for 3D-like Effects

This example demonstrates isosurface rendering, which creates a 3D appearance
using multiple contour layers with varying opacity.
"""

import numpy as np
from web_mapplot import MapPlot

# Create dataset with interesting topography
lon = np.linspace(-125, -65, 100)
lat = np.linspace(25, 50, 80)
lon2d, lat2d = np.meshgrid(lon, lat)

# Create elevation-like data with multiple peaks and valleys
elevation = np.zeros_like(lon2d)

# Add multiple "mountains"
peaks = [
    (-105, 40, 3000, 10),  # Rocky Mountains
    (-120, 47, 2500, 8),   # Cascades
    (-110, 44, 2800, 9),   # Yellowstone
    (-82, 36, 2000, 7),    # Appalachians
]

for peak_lon, peak_lat, height, spread in peaks:
    dist = np.sqrt((lon2d - peak_lon)**2 + (lat2d - peak_lat)**2)
    elevation += height * np.exp(-dist**2 / (2 * spread**2))

# Add some rolling hills
elevation += 200 * np.sin((lon2d + 90) / 8) * np.cos((lat2d - 35) / 6)

# Create map plot
mp = MapPlot(title='Isosurface Visualization - Elevation Profile')

# Add isosurface plot
mp.add_variable(
    name='Elevation',
    lon=lon2d,
    lat=lat2d,
    data=elevation,
    plot_type='isosurface',
    colormap='rainbow',
    units='meters'
)

# Save visualization
output_file = mp.save_html('output_isosurface.html')

print("Isosurface visualization created successfully!")
print(f"Output saved to: {output_file}")
print("\nIsosurface rendering features:")
print("- Creates 3D appearance with layered contours")
print("- Multiple opacity levels simulate depth")
print("- Great for elevation, atmospheric layers, or depth data")
print("- Gives visual impression of terrain or surface structure")
print("\nAdjust the opacity slider to enhance the 3D effect!")
