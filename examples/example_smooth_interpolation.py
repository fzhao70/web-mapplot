"""
Example: Smooth Time Interpolation

This example demonstrates smooth interpolation between animation frames.
When enabled, data values are blended between time steps for more fluid
animations. Compare with and without interpolation to see the difference.
"""

import numpy as np
from datetime import datetime, timedelta
from web_mapplot import MapPlot

# Create dataset with relatively few time steps to make interpolation visible
lon = np.linspace(-130, -60, 60)
lat = np.linspace(25, 50, 48)
lon2d, lat2d = np.meshgrid(lon, lat)

# Create 6 time steps (fewer steps make interpolation more noticeable)
num_timesteps = 6
timestamps = [datetime(2024, 1, 1) + timedelta(hours=i*4) for i in range(num_timesteps)]

# Temperature with significant changes between frames
temp_data = []
for t in range(num_timesteps):
    phase = t * 2 * np.pi / num_timesteps  # Complete cycle
    temp = 20 + 15 * np.sin((lon2d + 95) / 15 + phase) * np.cos((lat2d - 37.5) / 10)
    # Add wave pattern that moves
    temp += 5 * np.sin((lon2d + 95) / 10 + phase * 2)
    temp_data.append(temp)
temp_data = np.array(temp_data)

print("=" * 70)
print("SMOOTH TIME INTERPOLATION EXAMPLES")
print("=" * 70)

# 1. WITHOUT interpolation (default)
print("\n1. Creating animation WITHOUT interpolation...")
mp_no_interp = MapPlot(
    title='Temperature Animation - WITHOUT Interpolation (Discrete Frames)',
    interpolate_frames=False  # Default
)
mp_no_interp.add_variable(
    name='Temperature',
    lon=lon2d,
    lat=lat2d,
    data=temp_data,
    timestamps=timestamps,
    plot_type='filled_contour',
    colormap='jet',
    units='°C',
    levels=15
)
mp_no_interp.save_html('output_no_interpolation.html')
print("   ✓ Standard animation - jumps between frames")

# 2. WITH interpolation
print("\n2. Creating animation WITH interpolation...")
mp_with_interp = MapPlot(
    title='Temperature Animation - WITH Smooth Interpolation',
    interpolate_frames=True  # Enable smooth blending
)
mp_with_interp.add_variable(
    name='Temperature',
    lon=lon2d,
    lat=lat2d,
    data=temp_data,
    timestamps=timestamps,
    plot_type='filled_contour',
    colormap='jet',
    units='°C',
    levels=15
)
mp_with_interp.save_html('output_with_interpolation.html')
print("   ✓ Smooth animation - blends between frames")

print("\n" + "=" * 70)
print("INTERPOLATION COMPARISON")
print("=" * 70)
print("\n🎬 WITHOUT Interpolation (output_no_interpolation.html):")
print("   • Discrete jumps between time steps")
print("   • Exact data values shown")
print("   • Can appear jerky with few time steps")
print("   • Faster rendering")
print("   • Best for: Scientific accuracy, sparse data")
print("\n✨ WITH Interpolation (output_with_interpolation.html):")
print("   • Smooth transitions between frames")
print("   • Values blended linearly")
print("   • More fluid appearance")
print("   • Slightly slower rendering")
print("   • Best for: Presentations, smooth phenomena")
print("\n⚡ WHEN TO USE INTERPOLATION:")
print("   ✓ Presentation mode - smoother looks better")
print("   ✓ Few time steps - fills in gaps")
print("   ✓ Continuous phenomena - temperature, pressure")
print("   ✓ Visualization focus - emphasize patterns")
print("\n🔬 WHEN TO SKIP INTERPOLATION:")
print("   ✓ Scientific analysis - need exact values")
print("   ✓ Many time steps - already smooth")
print("   ✓ Discrete events - rain/no-rain states")
print("   ✓ Performance critical - large datasets")
print("\n💡 TECHNICAL DETAILS:")
print("   • Linear interpolation: v = v1*(1-t) + v2*t")
print("   • Interpolates between current and next frame")
print("   • NaN values preserved (not interpolated)")
print("   • Works with all plot types")
print("   • No extra data storage required")
print("\n🎯 BEST PRACTICES:")
print("   • Use with 5-10 time steps for best effect")
print("   • Combine with slower animation speed")
print("   • Test both modes to see difference")
print("   • Consider your audience (science vs. presentation)")
print("\n" + "=" * 70)
print("Compare the two HTML files side-by-side!")
print("Play animations at same speed to see the difference.")
print("=" * 70)
