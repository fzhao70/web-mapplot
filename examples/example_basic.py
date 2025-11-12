"""
Basic example: Creating a simple filled contour plot
"""

import numpy as np
from datetime import datetime
import sys
sys.path.insert(0, '..')

from web_mapplot import MapPlot

# Create sample data - temperature over a grid
lon = np.linspace(-120, -70, 50)
lat = np.linspace(25, 50, 40)
lon2d, lat2d = np.meshgrid(lon, lat)

# Generate synthetic temperature data
temperature = 20 + 10 * np.sin(lon2d / 10) * np.cos(lat2d / 10)

# Create MapPlot instance
mp = MapPlot(title="Temperature Map - Basic Example")

# Add variable
mp.add_variable(
    name='Temperature',
    lon=lon2d,
    lat=lat2d,
    data=temperature,
    plot_type='filled_contour',
    colormap='jet',
    levels=15,
    units='°C'
)

# Save as standalone HTML
mp.save_html('output_basic.html')

print("Basic example created! Open output_basic.html in your browser.")
