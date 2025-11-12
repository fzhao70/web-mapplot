"""
Example demonstrating layer overlay capability
Multiple variables can be displayed simultaneously on the map
"""

import numpy as np
from datetime import datetime, timedelta
import sys
sys.path.insert(0, '..')

from web_mapplot import MapPlot

# Create spatial grid
lon = np.linspace(-120, -70, 50)
lat = np.linspace(25, 50, 40)
lon2d, lat2d = np.meshgrid(lon, lat)

# Generate different types of data that look good overlaid
# Temperature (filled contour - background layer)
temperature = 20 + 10 * np.sin(lon2d / 10) * np.cos(lat2d / 10)

# Pressure (contour lines - can overlay on temperature)
pressure = 1013 + 20 * np.sin(lon2d / 15) * np.cos(lat2d / 12)

# Wind (vector field - can overlay on both)
u_wind = 10 + 8 * np.cos(lon2d / 10) * np.sin(lat2d / 8)
v_wind = 6 + 5 * np.sin(lon2d / 8) * np.cos(lat2d / 10)
wind_speed = np.sqrt(u_wind**2 + v_wind**2)

# Create MapPlot instance
mp = MapPlot(title="Layer Overlay Example")

# Add temperature as filled contour (good as background)
mp.add_variable(
    name='Temperature',
    lon=lon2d,
    lat=lat2d,
    data=temperature,
    plot_type='filled_contour',
    colormap='hot',
    levels=15,
    units='°C'
)

# Add pressure as contour lines (overlay well on temperature)
mp.add_variable(
    name='Pressure',
    lon=lon2d,
    lat=lat2d,
    data=pressure,
    plot_type='contour',
    colormap='cool',
    levels=12,
    units='hPa'
)

# Add wind vectors (overlay on everything)
mp.add_variable(
    name='Wind',
    lon=lon2d,
    lat=lat2d,
    data=wind_speed,
    plot_type='vector',
    u_component=u_wind,
    v_component=v_wind,
    colormap='viridis',
    units='m/s'
)

# Save as standalone HTML
mp.save_html('output_layer_overlay.html')

print("\nLayer overlay example created! Open output_layer_overlay.html")
print("\nIn the web interface:")
print("  1. Use the 'Layer Visibility' section to toggle layers on/off")
print("  2. Check multiple layers to see them overlaid")
print("  3. Try overlaying:")
print("     - Temperature (filled) + Pressure (lines)")
print("     - Temperature (filled) + Wind (vectors)")
print("     - All three layers together!")
print("  4. Use 'Show All' / 'Hide All' buttons for quick control")
print("  5. Adjust opacity to see through overlaid layers")
