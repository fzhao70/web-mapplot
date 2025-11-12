"""
Example demonstrating base map selection
Shows different base maps for geographic context
"""

import numpy as np
from datetime import datetime
import sys
sys.path.insert(0, '..')

from web_mapplot import MapPlot

# Create spatial grid covering a recognizable geographic area
# California coast for clear geographic features
lon = np.linspace(-125, -115, 60)
lat = np.linspace(32, 42, 50)
lon2d, lat2d = np.meshgrid(lon, lat)

# Generate synthetic sea surface temperature
temperature = 15 + 8 * np.sin(lon2d / 5) * np.cos(lat2d / 5) + \
              (lat2d - 37) * 0.5  # Temperature gradient with latitude

# Generate coastal wind pattern
u_wind = 5 + 8 * np.cos(lon2d / 8)
v_wind = -3 + 5 * np.sin(lat2d / 6)
wind_speed = np.sqrt(u_wind**2 + v_wind**2)

# Create MapPlot instance
mp = MapPlot(title="Base Map Selection Demo - California Coast")

# Add sea surface temperature
mp.add_variable(
    name='Sea Surface Temperature',
    lon=lon2d,
    lat=lat2d,
    data=temperature,
    plot_type='filled_contour',
    colormap='hot',
    levels=15,
    units='°C'
)

# Add wind vectors
mp.add_variable(
    name='Surface Wind',
    lon=lon2d,
    lat=lat2d,
    data=wind_speed,
    plot_type='vector',
    u_component=u_wind,
    v_component=v_wind,
    vector_scale=2.0,
    colormap='viridis',
    units='m/s'
)

# Save as standalone HTML
mp.save_html('output_basemap.html')

print("\nBase map selection example created! Open output_basemap.html")
print("\nAvailable base maps in the dropdown:")
print("  1. OpenStreetMap - Default street map with detailed features")
print("     Good for: Urban areas, road networks, general reference")
print()
print("  2. Topographic - Terrain visualization with contours")
print("     Good for: Elevation data, mountainous regions, hiking/outdoor")
print()
print("  3. Satellite - Aerial/satellite imagery")
print("     Good for: Real imagery, land cover, coastal features")
print()
print("  4. Light (CartoDB) - Minimal light background")
print("     Good for: Focus on data, clean presentation, printing")
print()
print("  5. Dark (CartoDB) - Dark theme background")
print("     Good for: Night mode, reducing eye strain, modern aesthetic")
print()
print("Try switching between base maps using the dropdown in the")
print("'Visualization Settings' section to see which works best!")
print()
print("Tip: Try comparing:")
print("  - Topographic map to see terrain features")
print("  - Satellite imagery to see real coastal features")
print("  - Light/Dark maps to reduce visual clutter")
