"""
Example: Auto-Refresh for Real-Time Data

This example demonstrates the auto-refresh feature, which automatically reloads
the page at a specified interval. This is useful for:
- Real-time monitoring dashboards
- Live weather data
- Sensor networks with frequent updates
- IoT data streams

Note: In production, you would typically regenerate the HTML file with updated
data from your data source before each refresh.
"""

import numpy as np
from datetime import datetime
from web_mapplot import MapPlot

# Create a dataset - in real use, this would come from a live data source
lon = np.linspace(-130, -60, 60)
lat = np.linspace(25, 50, 48)
lon2d, lat2d = np.meshgrid(lon, lat)

# Simulate real-time data (in production, fetch from API/database/sensor)
# Add current time to make changes visible
current_time = datetime.now()
time_offset = current_time.hour + current_time.minute / 60.0

# Temperature with time-based variation to show updates
temp = 20 + 10 * np.sin((lon2d + 95 + time_offset * 5) / 15) * np.cos((lat2d - 37.5) / 10)

# Create map plot with auto-refresh enabled
# The page will automatically reload every 30 seconds
mp = MapPlot(
    title=f'Real-Time Temperature Monitoring - Updated: {current_time.strftime("%H:%M:%S")}',
    auto_refresh=30  # Refresh every 30 seconds
)

# Add temperature data
mp.add_variable(
    name='Temperature',
    lon=lon2d,
    lat=lat2d,
    data=temp,
    plot_type='filled_contour',
    colormap='jet',
    units='°C'
)

# Save visualization
output_file = mp.save_html('output_auto_refresh.html')

print("=" * 70)
print("AUTO-REFRESH DEMONSTRATION")
print("=" * 70)
print(f"\nOutput saved to: {output_file}")
print(f"Current time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"\n🔄 AUTO-REFRESH SETTINGS:")
print("   - Interval: 30 seconds")
print("   - Visual indicator with countdown in header")
print("   - Automatic page reload")
print("\n📊 REAL-TIME MONITORING USE CASES:")
print("   - Weather station data updates")
print("   - Sensor network monitoring")
print("   - Traffic flow visualization")
print("   - Environmental monitoring (air quality, water levels)")
print("   - IoT device dashboards")
print("\n💡 PRODUCTION SETUP:")
print("   In a real deployment, you would:")
print("   1. Set up a web server (Flask/FastAPI)")
print("   2. Regenerate HTML with fresh data before each refresh")
print("   3. Use a background job to fetch data from APIs/databases")
print("   4. Consider WebSocket connections for instant updates")
print("\n🔧 EXAMPLE WORKFLOW:")
print("   # Pseudo-code for production")
print("   while True:")
print("       data = fetch_from_api()  # Get latest data")
print("       mp = MapPlot(auto_refresh=30)")
print("       mp.add_variable(..., data=data)")
print("       mp.save_html('output.html')  # Overwrite with new data")
print("       time.sleep(30)  # Wait for refresh interval")
print("\n⚙️  ADJUSTING REFRESH INTERVAL:")
print("   - Short intervals (5-10s): High-frequency updates")
print("   - Medium intervals (30-60s): Balanced monitoring")
print("   - Long intervals (5-10min): Periodic snapshots")
print("\n" + "=" * 70)
print("Open the HTML file to see auto-refresh in action!")
print("Watch the countdown timer in the header.")
print("=" * 70)
