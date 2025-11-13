"""
Example: Demonstrating Advanced UI Features

This example showcases all the fancy new UI features:
- Dark mode toggle
- Glassmorphism panels
- Search/geocoding
- Fullscreen mode
- Floating mini-map
"""

import numpy as np
from datetime import datetime, timedelta
from web_mapplot import MapPlot

# Create a global dataset
lon = np.linspace(-180, 180, 120)
lat = np.linspace(-60, 75, 80)
lon2d, lat2d = np.meshgrid(lon, lat)

# Create time-series temperature data
num_timesteps = 8
temp_data = []
timestamps = []

for t in range(num_timesteps):
    # Simulate seasonal temperature variations
    season_offset = np.cos(2 * np.pi * t / num_timesteps)
    temp = 15 + 20 * np.cos(np.radians(lat2d)) * season_offset
    temp += 5 * np.sin(np.radians(lon2d / 2))
    temp_data.append(temp)
    timestamps.append(datetime(2024, 1, 1) + timedelta(days=t*45))

temp_data = np.array(temp_data)

# Create map plot
mp = MapPlot(title='Advanced Features Demo - Global Temperature')

# Add temperature variable
mp.add_variable(
    name='Temperature',
    lon=lon2d,
    lat=lat2d,
    data=temp_data,
    timestamps=timestamps,
    plot_type='filled_contour',
    colormap='jet',
    units='°C'
)

# Save visualization
output_file = mp.save_html('output_advanced_features.html')

print("=" * 70)
print("Advanced Features Demo Created!")
print("=" * 70)
print(f"\nOutput file: {output_file}")
print("\n🎨 NEW UI FEATURES TO TRY:")
print("\n1. 🌙 DARK MODE TOGGLE")
print("   - Click the moon/sun icon in the top-right header")
print("   - Switches between light and dark themes")
print("   - Preference saved in browser")
print("\n2. ✨ GLASSMORPHISM EFFECT")
print("   - Notice the frosted glass appearance of the control panel")
print("   - Semi-transparent with blur effect")
print("   - Modern, clean aesthetic")
print("\n3. 🔍 SEARCH/GEOCODING")
print("   - Use the search box at top-left of the map")
print("   - Try searching: 'London', 'Tokyo', 'New York'")
print("   - Automatically flies to the location")
print("\n4. ⛶ FULLSCREEN MODE")
print("   - Click the fullscreen icon in the header")
print("   - Immersive viewing experience")
print("   - Press ESC to exit")
print("\n5. 🗺️  MINI-MAP")
print("   - Small overview map in top-right corner")
print("   - Shows your current view location")
print("   - Can be collapsed/expanded")
print("\n6. 🎯 OTHER FEATURES")
print("   - Base map selection (OSM, Topo, Satellite, Light, Dark)")
print("   - Layer overlay capability")
print("   - Time-series animation")
print("   - Opacity control")
print("\n" + "=" * 70)
print("Enjoy exploring all the new features!")
print("=" * 70)
