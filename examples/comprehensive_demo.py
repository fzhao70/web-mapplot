"""
COMPREHENSIVE EXAMPLE - Showcasing All Major Features

This example demonstrates nearly all features of the Web MapPlot library
in a single, comprehensive visualization. Perfect for understanding the
full capabilities of the library.

Features Demonstrated:
✓ Custom projection (EPSG4326)
✓ Auto-refresh (30 seconds)
✓ Smooth time interpolation
✓ Multiple plot types (8 different types)
✓ Time-series animation
✓ Multiple variables with layer overlay
✓ Vector fields with custom scaling
✓ Custom color scales (vmin/vmax)
✓ All color schemes
✓ Layer visibility controls
✓ Dark mode support
✓ Collapsible panels
✓ Location search
✓ Fullscreen mode
✓ Floating mini-map
✓ Base map selection
✓ Interactive tooltips
"""

import numpy as np
from datetime import datetime, timedelta
from web_mapplot import MapPlot

print("=" * 80)
print("COMPREHENSIVE WEB MAPPLOT DEMONSTRATION")
print("Showcasing ALL Major Features")
print("=" * 80)

# ==============================================================================
# DATA PREPARATION
# ==============================================================================

print("\n📊 Generating comprehensive dataset...")

# Create a global grid for various visualizations
lon_global = np.linspace(-180, 180, 120)
lat_global = np.linspace(-60, 75, 100)
lon2d, lat2d = np.meshgrid(lon_global, lat_global)

# Regional grid for detailed visualizations
lon_regional = np.linspace(-130, -60, 80)
lat_regional = np.linspace(25, 50, 64)
lon2d_regional, lat2d_regional = np.meshgrid(lon_regional, lat_regional)

# Time series setup (10 time steps)
num_timesteps = 10
timestamps = [datetime(2024, 1, 1) + timedelta(hours=i*6) for i in range(num_timesteps)]

print(f"   ✓ Created global grid: {lon2d.shape}")
print(f"   ✓ Created regional grid: {lon2d_regional.shape}")
print(f"   ✓ Time steps: {num_timesteps}")

# ==============================================================================
# VARIABLE 1: Global Temperature (Filled Contour + Time Series)
# ==============================================================================

print("\n🌡️  Variable 1: Global Temperature (Filled Contour)")
print("   Features: Time-series, smooth interpolation, custom range")

temp_global_data = []
for t in range(num_timesteps):
    phase = t * 2 * np.pi / num_timesteps
    # Latitude-based temperature with seasonal variation
    temp = 15 + 20 * np.cos(np.radians(lat2d)) + 5 * np.sin(phase)
    # Add longitude variation
    temp += 5 * np.sin(np.radians(lon2d / 2) + phase)
    temp_global_data.append(temp)
temp_global_data = np.array(temp_global_data)

# ==============================================================================
# VARIABLE 2: Regional Pressure (Contour Lines)
# ==============================================================================

print("\n🔵 Variable 2: Regional Pressure (Contour)")
print("   Features: Static, overlay with other layers")

pressure = 1013 + 10 * np.cos((lon2d_regional + 90) / 20) * np.sin((lat2d_regional - 35) / 12)
pressure += 5 * np.sin((lon2d_regional + 95) / 15)

# ==============================================================================
# VARIABLE 3: Regional Wind Velocity (Vector Field)
# ==============================================================================

print("\n💨 Variable 3: Wind Vectors")
print("   Features: Time-series, vector scaling, color by magnitude")

u_wind_data = []
v_wind_data = []
for t in range(num_timesteps):
    phase = t * 2 * np.pi / num_timesteps
    u_wind = 8 * np.sin((lon2d_regional + 100) / 25 + phase)
    v_wind = 8 * np.cos((lat2d_regional - 40) / 15 + phase)
    u_wind_data.append(u_wind)
    v_wind_data.append(v_wind)
u_wind_data = np.array(u_wind_data)
v_wind_data = np.array(v_wind_data)
wind_speed = np.sqrt(u_wind_data**2 + v_wind_data**2)

# ==============================================================================
# VARIABLE 4: Precipitation (Hexbin)
# ==============================================================================

print("\n🌧️  Variable 4: Precipitation (Hexbin)")
print("   Features: Aggregated visualization, large point dataset")

# Subsample for hexbin
precip_hex = 50 + 30 * np.exp(-((lon2d_regional + 95)**2 + (lat2d_regional - 37.5)**2) / 500)
precip_hex += np.random.normal(0, 5, precip_hex.shape)

# ==============================================================================
# VARIABLE 5: Population Density (Heatmap)
# ==============================================================================

print("\n👥 Variable 5: Population Density (Heatmap)")
print("   Features: Clustering, intensity visualization")

# Create hotspots for major cities
density = np.zeros_like(lon2d_regional)
cities = [
    (-118, 34, 50),   # Los Angeles
    (-122, 37, 45),   # San Francisco
    (-87, 42, 40),    # Chicago
    (-74, 41, 55),    # New York
]
for city_lon, city_lat, intensity in cities:
    dist = np.sqrt((lon2d_regional - city_lon)**2 + (lat2d_regional - city_lat)**2)
    density += intensity * np.exp(-dist**2 / 20)
density += np.random.exponential(1, density.shape)

# ==============================================================================
# VARIABLE 6: Service Coverage (Voronoi)
# ==============================================================================

print("\n📡 Variable 6: Service Coverage (Voronoi)")
print("   Features: Nearest-neighbor partitioning")

# Subsample for cleaner Voronoi
service_quality = 50 + 30 * np.sin((lon2d_regional + 95) / 20) * np.cos((lat2d_regional - 37.5) / 12)

# ==============================================================================
# VARIABLE 7: Elevation (Isosurface 3D)
# ==============================================================================

print("\n⛰️  Variable 7: Terrain Elevation (Isosurface)")
print("   Features: 3D-like rendering, multi-layer visualization")

elevation = np.zeros_like(lon2d_regional)
peaks = [
    (-105, 40, 3000, 10),  # Rocky Mountains
    (-120, 47, 2500, 8),   # Cascades
]
for peak_lon, peak_lat, height, spread in peaks:
    dist = np.sqrt((lon2d_regional - peak_lon)**2 + (lat2d_regional - peak_lat)**2)
    elevation += height * np.exp(-dist**2 / (2 * spread**2))
elevation += 200 * np.sin((lon2d_regional + 90) / 8) * np.cos((lat2d_regional - 35) / 6)

# ==============================================================================
# VARIABLE 8: Weather Stations (Colored Scatter)
# ==============================================================================

print("\n📍 Variable 8: Weather Stations (Scatter)")
print("   Features: Point data, color by value")

# Subsample for scatter plot
stations_temp = 20 + 10 * np.sin((lon2d_regional + 95) / 15) * np.cos((lat2d_regional - 37.5) / 10)

# ==============================================================================
# CREATE COMPREHENSIVE VISUALIZATION
# ==============================================================================

print("\n🎨 Creating comprehensive MapPlot visualization...")
print("   Features enabled:")
print("   ✓ Custom projection (EPSG4326 - Scientific)")
print("   ✓ Auto-refresh (30 seconds)")
print("   ✓ Smooth time interpolation")
print("   ✓ 8 different plot types")
print("   ✓ Multiple overlayable layers")

mp = MapPlot(
    title=f"🌍 Comprehensive Web MapPlot Demo - Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
    projection="EPSG4326",      # Equirectangular projection (scientific)
    auto_refresh=30,             # Auto-refresh every 30 seconds
    interpolate_frames=True,     # Smooth animation transitions
    center=(40, -95),            # Center on USA
    zoom=4
)

# Add all variables
print("\n📦 Adding all variables...")

# 1. Global Temperature (Time-series, filled contour)
mp.add_variable(
    name='🌡️ Global Temperature',
    lon=lon2d,
    lat=lat2d,
    data=temp_global_data,
    timestamps=timestamps,
    plot_type='filled_contour',
    colormap='jet',
    vmin=-10,
    vmax=40,
    levels=20,
    units='°C'
)
print("   ✓ Global Temperature (filled_contour, jet, time-series)")

# 2. Regional Pressure (Static, contour lines)
mp.add_variable(
    name='🔵 Pressure',
    lon=lon2d_regional,
    lat=lat2d_regional,
    data=pressure,
    plot_type='contour',
    colormap='viridis',
    levels=15,
    units='hPa'
)
print("   ✓ Pressure (contour, viridis)")

# 3. Wind Vectors (Time-series, custom scale)
mp.add_variable(
    name='💨 Wind Velocity',
    lon=lon2d_regional,
    lat=lat2d_regional,
    data=wind_speed,
    timestamps=timestamps,
    u_component=u_wind_data,
    v_component=v_wind_data,
    plot_type='vector',
    colormap='cool',
    vector_scale=1.5,
    units='m/s'
)
print("   ✓ Wind Velocity (vector, cool, scaled)")

# 4. Precipitation (Hexbin)
mp.add_variable(
    name='🌧️ Precipitation',
    lon=lon2d_regional,
    lat=lat2d_regional,
    data=precip_hex,
    plot_type='hexbin',
    colormap='plasma',
    units='mm'
)
print("   ✓ Precipitation (hexbin, plasma)")

# 5. Population Density (Heatmap)
mp.add_variable(
    name='👥 Population Density',
    lon=lon2d_regional,
    lat=lat2d_regional,
    data=density,
    plot_type='heatmap',
    colormap='hot',
    units='people/km²'
)
print("   ✓ Population Density (heatmap, hot)")

# 6. Service Coverage (Voronoi)
mp.add_variable(
    name='📡 Service Coverage',
    lon=lon2d_regional[::3, ::3],  # Subsample
    lat=lat2d_regional[::3, ::3],
    data=service_quality[::3, ::3],
    plot_type='voronoi',
    colormap='rainbow',
    units='quality score'
)
print("   ✓ Service Coverage (voronoi, rainbow)")

# 7. Elevation (Isosurface)
mp.add_variable(
    name='⛰️ Terrain Elevation',
    lon=lon2d_regional,
    lat=lat2d_regional,
    data=elevation,
    plot_type='isosurface',
    colormap='rainbow',
    units='meters'
)
print("   ✓ Terrain Elevation (isosurface, rainbow)")

# 8. Weather Stations (Scatter)
mp.add_variable(
    name='📍 Weather Stations',
    lon=lon2d_regional[::4, ::4],  # Subsample
    lat=lat2d_regional[::4, ::4],
    data=stations_temp[::4, ::4],
    plot_type='scatter',
    colormap='hot',
    units='°C'
)
print("   ✓ Weather Stations (scatter, hot)")

# Save the comprehensive visualization
print("\n💾 Saving comprehensive visualization...")
output_file = mp.save_html('comprehensive_demo.html')

# ==============================================================================
# SUCCESS MESSAGE
# ==============================================================================

print("\n" + "=" * 80)
print("✅ COMPREHENSIVE DEMONSTRATION CREATED SUCCESSFULLY!")
print("=" * 80)
print(f"\n📂 Output file: {output_file}")
print("\n🎯 FEATURES DEMONSTRATED:")
print("\n  📊 Plot Types (8):")
print("     1. Filled Contour - Global temperature")
print("     2. Contour Lines - Regional pressure")
print("     3. Vector Field - Wind velocity")
print("     4. Hexbin - Precipitation aggregation")
print("     5. Heatmap - Population density")
print("     6. Voronoi - Service coverage")
print("     7. Isosurface - 3D terrain elevation")
print("     8. Scatter - Weather stations")
print("\n  🎨 Visual Features:")
print("     • 6 different colormaps (jet, viridis, cool, plasma, hot, rainbow)")
print("     • Custom color ranges (vmin/vmax)")
print("     • Time-series animation with 10 frames")
print("     • Smooth frame interpolation")
print("     • Vector field scaling")
print("     • Multiple contour levels")
print("\n  🚀 Advanced Features:")
print("     • Custom projection (EPSG4326 - Equirectangular)")
print("     • Auto-refresh (30 seconds)")
print("     • Layer overlay system (toggle 8 layers)")
print("     • Collapsible control panels")
print("     • Dark mode support")
print("     • Location search/geocoding")
print("     • Fullscreen mode")
print("     • Floating mini-map")
print("     • Base map selection (5 options)")
print("     • Interactive tooltips")
print("\n  💡 Try These Interactions:")
print("     1. Click section headers to collapse/expand panels")
print("     2. Toggle layer visibility to overlay multiple datasets")
print("     3. Play the animation to see smooth interpolation")
print("     4. Search for locations (e.g., 'Los Angeles', 'Chicago')")
print("     5. Toggle dark mode (moon icon in header)")
print("     6. Enter fullscreen mode for immersive viewing")
print("     7. Adjust vector scale slider")
print("     8. Switch between different base maps")
print("     9. Adjust opacity to blend layers")
print("     10. Use mini-map for navigation overview")
print("\n  📈 Data Highlights:")
print("     • Global data: 120×100 grid (12,000 points)")
print("     • Regional data: 80×64 grid (5,120 points)")
print("     • Time steps: 10 frames × 6 hours = 60 hours")
print("     • Total variables: 8 different fields")
print("     • Projection: EPSG4326 (Scientific)")
print("\n  ⚡ Performance:")
print("     • Auto-refresh: Updates every 30 seconds")
print("     • Smooth animations: Linear interpolation")
print("     • Responsive UI: Collapsible panels save space")
print("     • Multi-layer: 8 independent visualization layers")
print("\n" + "=" * 80)
print("🌐 Open comprehensive_demo.html in your browser to explore!")
print("=" * 80)
