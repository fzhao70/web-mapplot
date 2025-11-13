"""
Example: Voronoi Diagram

This example demonstrates Voronoi diagrams, which partition space based on
nearest neighbor regions - useful for service areas and influence zones.
"""

import numpy as np
from web_mapplot import MapPlot

# Create a moderate resolution dataset
lon = np.linspace(-125, -65, 40)
lat = np.linspace(25, 50, 32)
lon2d, lat2d = np.meshgrid(lon, lat)

# Create data representing service quality or accessibility
# This could represent coverage areas, service territories, etc.
service_quality = 50 + 30 * np.sin((lon2d + 95) / 20) * np.cos((lat2d - 37.5) / 12)

# Add some regional variations
service_quality += 10 * np.sin((lon2d + 80) / 15)
service_quality += 10 * np.cos((lat2d - 35) / 8)

# Create map plot
mp = MapPlot(title='Voronoi Diagram - Service Coverage Quality')

# Add Voronoi diagram
mp.add_variable(
    name='Service Quality',
    lon=lon2d,
    lat=lat2d,
    data=service_quality,
    plot_type='voronoi',
    colormap='viridis',
    units='score'
)

# Save visualization
output_file = mp.save_html('output_voronoi.html')

print("Voronoi diagram created successfully!")
print(f"Output saved to: {output_file}")
print("\nVoronoi diagrams are useful for:")
print("- Showing nearest-neighbor regions")
print("- Service area boundaries")
print("- Territory assignment")
print("- Coverage zones for facilities, stores, or services")
print("- Natural neighbor interpolation")
print("\nEach polygon represents the area closest to each data point!")
