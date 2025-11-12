"""
Web server example: Launch interactive server instead of saving HTML
"""

import numpy as np
from datetime import datetime, timedelta
import sys
sys.path.insert(0, '..')

from web_mapplot import MapPlot

# Create spatial grid
lon = np.linspace(-110, -70, 50)
lat = np.linspace(25, 50, 40)
lon2d, lat2d = np.meshgrid(lon, lat)

# Create time-series data
num_timesteps = 12
timestamps = [datetime(2024, 1, 1) + timedelta(hours=i*2) for i in range(num_timesteps)]

# Generate evolving data
data_3d = np.zeros((num_timesteps, lat.size, lon.size))
for t in range(num_timesteps):
    phase = t * np.pi / 6
    data_3d[t] = 25 + 20 * np.sin(lon2d / 10 + phase) * np.cos(lat2d / 10 - phase)

# Create MapPlot instance
mp = MapPlot(title="Interactive Web Server Example")

# Add variable
mp.add_variable(
    name='Sea Surface Temperature',
    lon=lon2d,
    lat=lat2d,
    data=data_3d,
    plot_type='filled_contour',
    timestamps=timestamps,
    colormap='hot',
    levels=20,
    units='°C'
)

# Launch web server (will run on http://localhost:5000)
print("Starting web server...")
print("Open http://localhost:5000 in your browser")
print("Press Ctrl+C to stop")

mp.show(port=5000, debug=False)
