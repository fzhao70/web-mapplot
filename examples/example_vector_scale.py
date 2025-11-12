"""
Example demonstrating vector scale control
Shows how to set vector scale in Python and adjust it in the UI
"""

import numpy as np
from datetime import datetime
import sys
sys.path.insert(0, '..')

from web_mapplot import MapPlot

# Create spatial grid
lon = np.linspace(-100, -80, 40)
lat = np.linspace(30, 45, 35)
lon2d, lat2d = np.meshgrid(lon, lat)

# Generate wind data with different magnitudes
# Weak wind
u_weak = 2 + 3 * np.sin(lon2d / 5) * np.cos(lat2d / 5)
v_weak = 1 + 2 * np.cos(lon2d / 5) * np.sin(lat2d / 5)
wind_speed_weak = np.sqrt(u_weak**2 + v_weak**2)

# Strong wind
u_strong = 15 + 20 * np.sin(lon2d / 5) * np.cos(lat2d / 5)
v_strong = 10 + 15 * np.cos(lon2d / 5) * np.sin(lat2d / 5)
wind_speed_strong = np.sqrt(u_strong**2 + v_strong**2)

# Create MapPlot instance
mp = MapPlot(title="Vector Scale Control Example")

# Add weak wind with larger vector_scale (to make arrows visible)
mp.add_variable(
    name='Weak Wind',
    lon=lon2d,
    lat=lat2d,
    data=wind_speed_weak,
    plot_type='vector',
    u_component=u_weak,
    v_component=v_weak,
    vector_scale=3.0,  # Amplify weak vectors for visibility
    colormap='viridis',
    units='m/s'
)

# Add strong wind with default vector_scale
mp.add_variable(
    name='Strong Wind',
    lon=lon2d,
    lat=lat2d,
    data=wind_speed_strong,
    plot_type='vector',
    u_component=u_strong,
    v_component=v_strong,
    vector_scale=1.0,  # Default scale
    colormap='plasma',
    units='m/s'
)

# Add strong wind as streamlines with reduced scale
mp.add_variable(
    name='Strong Wind (Stream)',
    lon=lon2d,
    lat=lat2d,
    data=wind_speed_strong,
    plot_type='stream',
    u_component=u_strong,
    v_component=v_strong,
    vector_scale=0.5,  # Reduce for cleaner streamlines
    colormap='plasma',
    units='m/s'
)

# Save as standalone HTML
mp.save_html('output_vector_scale.html')

print("\nVector scale example created! Open output_vector_scale.html")
print("\nFeatures demonstrated:")
print("  1. Python API: Set initial vector_scale for each variable")
print("     - Weak Wind: vector_scale=3.0 (amplified for visibility)")
print("     - Strong Wind: vector_scale=1.0 (default)")
print("     - Streamlines: vector_scale=0.5 (reduced for clarity)")
print("\n  2. Interactive UI: Adjust vector scale dynamically")
print("     - Vector Scale slider appears when vector/stream layers are visible")
print("     - Slider range: 0.1x to 5.0x")
print("     - Affects ALL visible vector/stream layers in real-time")
print("\nTry it:")
print("  - Toggle different wind layers on/off")
print("  - Adjust the Vector Scale slider to see arrows change size")
print("  - Combine vector layers and adjust scale for best visualization")
