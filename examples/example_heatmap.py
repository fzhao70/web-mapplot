"""
Example: Heatmap with Clustering

This example demonstrates the heatmap plot type, which uses intensity-based
clustering to show data density and patterns.
"""

import numpy as np
from web_mapplot import MapPlot

# Create dataset focusing on population density or similar data
lon = np.linspace(-125, -65, 150)
lat = np.linspace(25, 50, 120)
lon2d, lat2d = np.meshgrid(lon, lat)

# Create data with several "hotspots" (e.g., cities)
density = np.zeros_like(lon2d)

# Add hotspots at major city locations
cities = [
    (-118, 34, 50),   # Los Angeles
    (-122, 37, 45),   # San Francisco
    (-87, 42, 40),    # Chicago
    (-74, 41, 55),    # New York
    (-95, 30, 35),    # Houston
]

for city_lon, city_lat, intensity in cities:
    dist = np.sqrt((lon2d - city_lon)**2 + (lat2d - city_lat)**2)
    density += intensity * np.exp(-dist**2 / 20)

# Add some random background
density += np.random.exponential(2, density.shape)

# Create map plot
mp = MapPlot(title='Heatmap Visualization - Population Density')

# Add heatmap
mp.add_variable(
    name='Density',
    lon=lon2d,
    lat=lat2d,
    data=density,
    plot_type='heatmap',
    colormap='hot',
    units='units'
)

# Save visualization
output_file = mp.save_html('output_heatmap.html')

print("Heatmap created successfully!")
print(f"Output saved to: {output_file}")
print("\nHeatmaps are useful for:")
print("- Visualizing density and clustering patterns")
print("- Showing hotspots and concentration areas")
print("- Population density, crime statistics, disease spread")
print("- Smooth, continuous representation of point data")
print("\nThe heatmap automatically adjusts intensity based on zoom level!")
