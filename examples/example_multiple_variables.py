"""
Multiple variables example: Switch between different fields
"""

import numpy as np
from datetime import datetime, timedelta
import sys
sys.path.insert(0, '..')

from web_mapplot import MapPlot

# Create spatial grid
lon = np.linspace(-125, -65, 55)
lat = np.linspace(25, 50, 45)
lon2d, lat2d = np.meshgrid(lon, lat)

# Create time steps
num_timesteps = 8
timestamps = [datetime(2024, 1, 1, 12) + timedelta(hours=i*3) for i in range(num_timesteps)]

# Generate synthetic meteorological data
# Temperature (3D with time)
temperature = np.zeros((num_timesteps, lat.size, lon.size))
for t in range(num_timesteps):
    phase = t * np.pi / 4
    temperature[t] = 18 + 12 * np.sin(lon2d / 10 + phase) * np.cos(lat2d / 10)

# Pressure (2D - single time)
pressure = 1013 + 15 * np.sin(lon2d / 15) * np.cos(lat2d / 15)

# Wind components
u_wind = np.zeros((num_timesteps, lat.size, lon.size))
v_wind = np.zeros((num_timesteps, lat.size, lon.size))
for t in range(num_timesteps):
    phase = t * np.pi / 4
    u_wind[t] = 8 + 6 * np.cos(lon2d / 8 + phase)
    v_wind[t] = 5 + 4 * np.sin(lat2d / 8 + phase)

wind_speed = np.sqrt(u_wind**2 + v_wind**2)

# Precipitation (3D with time)
precipitation = np.zeros((num_timesteps, lat.size, lon.size))
for t in range(num_timesteps):
    precipitation[t] = np.maximum(0,
        5 * np.sin(lon2d / 12 + t * 0.5) * np.cos(lat2d / 12) +
        np.random.random((lat.size, lon.size)) * 2
    )

# Create MapPlot instance
mp = MapPlot(title="Multi-Variable Meteorological Data")

# Add temperature variable
mp.add_variable(
    name='Temperature',
    lon=lon2d,
    lat=lat2d,
    data=temperature,
    plot_type='filled_contour',
    timestamps=timestamps,
    colormap='jet',
    levels=15,
    units='°C'
)

# Add pressure variable (static)
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

# Add wind velocity as stream field
mp.add_variable(
    name='Wind (Stream)',
    lon=lon2d,
    lat=lat2d,
    data=wind_speed,
    plot_type='stream',
    timestamps=timestamps,
    u_component=u_wind,
    v_component=v_wind,
    colormap='viridis',
    units='m/s'
)

# Add precipitation as filled contour
mp.add_variable(
    name='Precipitation',
    lon=lon2d,
    lat=lat2d,
    data=precipitation,
    plot_type='filled_contour',
    timestamps=timestamps,
    colormap='plasma',
    levels=10,
    units='mm/h'
)

# Save as standalone HTML
mp.save_html('output_multiple_variables.html')

print("Multiple variables example created! Open output_multiple_variables.html in your browser.")
print("Use the variable dropdown to switch between Temperature, Pressure, Wind, and Precipitation.")
