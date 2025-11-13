"""
Example: All Plot Types Showcase

This comprehensive example demonstrates all available plot types in a single
visualization with layer overlay capability.
"""

import numpy as np
from web_mapplot import MapPlot

# Create dataset
lon = np.linspace(-130, -60, 60)
lat = np.linspace(25, 50, 48)
lon2d, lat2d = np.meshgrid(lon, lat)

# Temperature data
temp = 15 + 15 * np.sin((lon2d + 95) / 15) * np.cos((lat2d - 37.5) / 10)

# Pressure data
pressure = 1013 + 10 * np.cos((lon2d + 90) / 20) * np.sin((lat2d - 35) / 12)

# Wind components
u_wind = 5 * np.sin((lon2d + 100) / 25)
v_wind = 5 * np.cos((lat2d - 40) / 15)

# Precipitation data
precip = 50 + 30 * np.exp(-((lon2d + 95)**2 + (lat2d - 37.5)**2) / 500)

# Density data for hexbin
density = temp + np.random.normal(0, 3, temp.shape)

# Create map plot
mp = MapPlot(title='Complete Plot Types Showcase')

# 1. Filled Contour
mp.add_variable(
    name='Temperature (Filled)',
    lon=lon2d,
    lat=lat2d,
    data=temp,
    plot_type='filled_contour',
    colormap='jet',
    units='°C'
)

# 2. Contour Lines
mp.add_variable(
    name='Pressure (Contours)',
    lon=lon2d,
    lat=lat2d,
    data=pressure,
    plot_type='contour',
    colormap='viridis',
    units='hPa',
    levels=15
)

# 3. Vector Field
mp.add_variable(
    name='Wind (Vectors)',
    lon=lon2d,
    lat=lat2d,
    data=np.sqrt(u_wind**2 + v_wind**2),
    u_component=u_wind,
    v_component=v_wind,
    plot_type='vector',
    colormap='cool',
    units='m/s',
    vector_scale=1.5
)

# 4. Scatter Plot
mp.add_variable(
    name='Observations (Scatter)',
    lon=lon2d[::4, ::4],  # Subsample for scatter
    lat=lat2d[::4, ::4],
    data=temp[::4, ::4],
    plot_type='scatter',
    colormap='hot',
    units='°C'
)

# 5. Hexbin
mp.add_variable(
    name='Density (Hexbin)',
    lon=lon2d,
    lat=lat2d,
    data=density,
    plot_type='hexbin',
    colormap='plasma',
    units='units'
)

# 6. Heatmap
mp.add_variable(
    name='Precipitation (Heatmap)',
    lon=lon2d,
    lat=lat2d,
    data=precip,
    plot_type='heatmap',
    colormap='hot',
    units='mm'
)

# 7. Voronoi
mp.add_variable(
    name='Regions (Voronoi)',
    lon=lon2d[::3, ::3],  # Subsample for Voronoi
    lat=lat2d[::3, ::3],
    data=temp[::3, ::3],
    plot_type='voronoi',
    colormap='rainbow',
    units='°C'
)

# 8. Isosurface
mp.add_variable(
    name='Elevation (Isosurface)',
    lon=lon2d,
    lat=lat2d,
    data=precip,
    plot_type='isosurface',
    colormap='rainbow',
    units='m'
)

# Save visualization
output_file = mp.save_html('output_all_plot_types.html')

print("=" * 70)
print("ALL PLOT TYPES SHOWCASE")
print("=" * 70)
print(f"\nOutput saved to: {output_file}")
print("\n📊 AVAILABLE PLOT TYPES:")
print("\n1. FILLED_CONTOUR - Smooth colored regions showing data values")
print("2. CONTOUR - Contour lines without fill")
print("3. VECTOR - Arrow fields showing direction and magnitude")
print("4. SCATTER - Individual colored points")
print("5. HEXBIN - Hexagonal binning for large point datasets")
print("6. HEATMAP - Intensity-based clustering visualization")
print("7. VORONOI - Nearest-neighbor region partitioning")
print("8. ISOSURFACE - 3D-like layered rendering")
print("\n💡 INTERACTION TIPS:")
print("- Use Layer Visibility to toggle different plot types")
print("- Try overlaying multiple layers (e.g., Temperature + Wind)")
print("- Adjust opacity for better layer blending")
print("- Switch between variables using the dropdown")
print("- Try dark mode for a different aesthetic")
print("- Use the search box to jump to specific locations")
print("\n" + "=" * 70)
