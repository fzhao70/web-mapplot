"""
Example: Hexbin Plot for Large Point Datasets

This example demonstrates the hexbin plot type, which is ideal for visualizing
large point datasets by aggregating points into hexagonal bins.
"""

import numpy as np
from web_mapplot import MapPlot

# Create a large dataset with many points
lon = np.linspace(-130, -60, 100)
lat = np.linspace(20, 55, 80)
lon2d, lat2d = np.meshgrid(lon, lat)

# Create temperature data with random variations
# This simulates station data or scattered observations
np.random.seed(42)
temp = 15 + 15 * np.sin((lon2d + 95) / 15) * np.cos((lat2d - 37.5) / 10)
temp += np.random.normal(0, 2, temp.shape)  # Add noise

# Create map plot
mp = MapPlot(title='Hexbin Visualization - Temperature Observations')

# Add hexbin plot
mp.add_variable(
    name='Temperature',
    lon=lon2d,
    lat=lat2d,
    data=temp,
    plot_type='hexbin',
    colormap='jet',
    units='°C'
)

# Save visualization
output_file = mp.save_html('output_hexbin.html')

print("Hexbin plot created successfully!")
print(f"Output saved to: {output_file}")
print("\nHexbin plots are useful for:")
print("- Visualizing large numbers of scattered observations")
print("- Reducing visual clutter from overlapping points")
print("- Showing spatial density and average values")
print("- Station data, weather observations, sensor networks")
print("\nTry zooming in to see individual hexagonal bins!")
