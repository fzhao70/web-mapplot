"""
Example: Custom Projections

This example demonstrates different map projections/coordinate reference systems.
Different projections are better suited for different purposes and regions.
"""

import numpy as np
from web_mapplot import MapPlot

# Create global dataset
lon = np.linspace(-180, 180, 100)
lat = np.linspace(-80, 80, 80)
lon2d, lat2d = np.meshgrid(lon, lat)

# Create temperature data
temp = 15 + 20 * np.cos(np.radians(lat2d))

print("=" * 70)
print("PROJECTION EXAMPLES")
print("=" * 70)

# 1. EPSG:3857 - Web Mercator (Default)
print("\n1. Creating Web Mercator (EPSG:3857) map...")
mp_mercator = MapPlot(
    title="Temperature - Web Mercator Projection (EPSG:3857)",
    projection="EPSG3857"  # Default, used by Google Maps, OSM
)
mp_mercator.add_variable(
    name='Temperature',
    lon=lon2d,
    lat=lat2d,
    data=temp,
    plot_type='filled_contour',
    colormap='jet',
    units='°C'
)
mp_mercator.save_html('output_projection_mercator.html')
print("   ✓ Web Mercator - Standard web map projection")
print("   • Best for: General purpose web maps, navigation")
print("   • Distorts: Area increases toward poles")

# 2. EPSG:4326 - Simple Equirectangular
print("\n2. Creating Equirectangular (EPSG:4326) map...")
mp_equirect = MapPlot(
    title="Temperature - Equirectangular Projection (EPSG:4326)",
    projection="EPSG4326"  # Simple lat/lon grid
)
mp_equirect.add_variable(
    name='Temperature',
    lon=lon2d,
    lat=lat2d,
    data=temp,
    plot_type='filled_contour',
    colormap='jet',
    units='°C'
)
mp_equirect.save_html('output_projection_equirect.html')
print("   ✓ Equirectangular - Simple latitude/longitude grid")
print("   • Best for: Scientific data, simple coordinate systems")
print("   • Distorts: Areas at high latitudes")

# 3. EPSG:3395 - World Mercator
print("\n3. Creating World Mercator (EPSG:3395) map...")
mp_world = MapPlot(
    title="Temperature - World Mercator Projection (EPSG:3395)",
    projection="EPSG3395"
)
mp_world.add_variable(
    name='Temperature',
    lon=lon2d,
    lat=lat2d,
    data=temp,
    plot_type='filled_contour',
    colormap='jet',
    units='°C'
)
mp_world.save_html('output_projection_world.html')
print("   ✓ World Mercator - Alternative Mercator projection")
print("   • Best for: World maps, similar to Web Mercator")
print("   • Distorts: Area increases toward poles")

print("\n" + "=" * 70)
print("PROJECTION COMPARISON")
print("=" * 70)
print("\nAvailable Projections:")
print("  • EPSG3857 (Web Mercator) - Default, most common")
print("  • EPSG4326 (Equirectangular) - Simple lat/lon grid")
print("  • EPSG3395 (World Mercator) - Alternative Mercator")
print("  • Simple - For non-geographic maps")
print("\nChoosing a Projection:")
print("  📍 General web maps → EPSG3857 (Web Mercator)")
print("  🌍 Scientific/climate data → EPSG4326 (Equirectangular)")
print("  🗺️  Navigation/shipping → EPSG3395 (World Mercator)")
print("  📐 Custom coordinates → Simple")
print("\n" + "=" * 70)
print("Open the HTML files to compare projections!")
print("=" * 70)
