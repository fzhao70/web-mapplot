"""
Example showing custom vmin/vmax ranges for color scaling
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

# Generate temperature data with range ~10-30°C
temperature = 20 + 10 * np.sin(lon2d / 10) * np.cos(lat2d / 10)

print("Data range:", np.min(temperature), "to", np.max(temperature))

# Create MapPlot instance
mp = MapPlot(title="Custom vmin/vmax Example")

# Example 1: Auto-range (vmin=None, vmax=None) - DEFAULT
# Color scale uses actual data range
mp.add_variable(
    name='Auto Range',
    lon=lon2d,
    lat=lat2d,
    data=temperature,
    plot_type='filled_contour',
    colormap='jet',
    units='°C'
    # vmin and vmax not specified, will use data min/max
)

# Example 2: Fixed range (vmin=0, vmax=40)
# Useful for comparing multiple datasets on the same scale
mp.add_variable(
    name='Fixed Range (0-40)',
    lon=lon2d,
    lat=lat2d,
    data=temperature,
    plot_type='filled_contour',
    colormap='jet',
    vmin=0,      # Fixed minimum
    vmax=40,     # Fixed maximum
    units='°C'
)

# Example 3: Symmetric range around zero
# Useful for anomaly plots
mp.add_variable(
    name='Symmetric Range (-15 to 15)',
    lon=lon2d,
    lat=lat2d,
    data=temperature - 20,  # Convert to anomalies
    plot_type='filled_contour',
    colormap='cool',
    vmin=-15,
    vmax=15,
    units='°C anomaly'
)

# Example 4: Clipping extreme values
# Show only values between 15-25, clip outliers
mp.add_variable(
    name='Clipped Range (15-25)',
    lon=lon2d,
    lat=lat2d,
    data=temperature,
    plot_type='filled_contour',
    colormap='viridis',
    vmin=15,
    vmax=25,
    units='°C'
)

# Save as standalone HTML
mp.save_html('output_custom_range.html')

print("\nCustom range example created! Open output_custom_range.html")
print("\nCompare the different variables:")
print("  1. Auto Range - uses actual data min/max")
print("  2. Fixed Range - uses 0-40°C regardless of data")
print("  3. Symmetric Range - centered on zero for anomalies")
print("  4. Clipped Range - focuses on 15-25°C range")
