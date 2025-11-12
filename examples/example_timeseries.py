"""
Time-series example: Animated data over time
"""

import numpy as np
from datetime import datetime, timedelta
import sys
sys.path.insert(0, '..')

from web_mapplot import MapPlot

# Create spatial grid
lon = np.linspace(-130, -60, 60)
lat = np.linspace(20, 55, 50)
lon2d, lat2d = np.meshgrid(lon, lat)

# Create time-series data (10 time steps)
num_timesteps = 10
timestamps = [datetime(2024, 1, 1) + timedelta(hours=i*6) for i in range(num_timesteps)]

# Generate synthetic data that evolves over time
temperature_3d = np.zeros((num_timesteps, lat.size, lon.size))
for t in range(num_timesteps):
    # Moving wave pattern
    phase = t * np.pi / 5
    temperature_3d[t] = 15 + 15 * np.sin(lon2d / 8 + phase) * np.cos(lat2d / 8)

# Create MapPlot instance
mp = MapPlot(title="Temperature Animation - Time Series Example")

# Add time-varying variable
mp.add_variable(
    name='Temperature',
    lon=lon2d,
    lat=lat2d,
    data=temperature_3d,
    plot_type='filled_contour',
    timestamps=timestamps,
    colormap='hot',
    levels=20,
    units='°C'
)

# Save as standalone HTML
mp.save_html('output_timeseries.html')

print("Time-series example created! Open output_timeseries.html in your browser.")
print("Use the time controls to animate through the data.")
