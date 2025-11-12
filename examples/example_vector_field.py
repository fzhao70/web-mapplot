"""
Vector field example: Wind velocity visualization
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

# Generate synthetic wind data
# U component (eastward wind)
u = 5 + 10 * np.sin(lon2d / 5) * np.cos(lat2d / 5)
# V component (northward wind)
v = 3 + 8 * np.cos(lon2d / 5) * np.sin(lat2d / 5)

# Calculate wind speed (magnitude)
wind_speed = np.sqrt(u**2 + v**2)

# Create MapPlot instance
mp = MapPlot(title="Wind Vector Field Example")

# Add vector field
mp.add_variable(
    name='Wind Velocity',
    lon=lon2d,
    lat=lat2d,
    data=wind_speed,
    plot_type='vector',
    u_component=u,
    v_component=v,
    colormap='viridis',
    units='m/s'
)

# Save as standalone HTML
mp.save_html('output_vector.html')

print("Vector field example created! Open output_vector.html in your browser.")
