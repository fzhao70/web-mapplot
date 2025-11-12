# Web MapPlot

A Python library for creating interactive web-based geographical visualizations with support for multiple plot types, time-series data, and variable switching.

## Features

- 🗺️ **Interactive base maps** using Leaflet.js
- 📊 **Multiple visualization types**:
  - Scatter plots
  - Contour plots
  - Filled contour plots
  - Vector fields
  - Stream fields
- ⏱️ **Time-series support** with animation controls
- 🔄 **Variable switching** - visualize multiple fields in one plot
- 📁 **Dual output modes**:
  - Standalone HTML files
  - Interactive web server
- 🎨 **Multiple color schemes** (viridis, plasma, jet, rainbow, cool, hot)
- 🎯 **Easy Python interface**

## Installation

```bash
pip install -r requirements.txt
```

### Requirements

- numpy
- flask (optional, for web server mode)

## Quick Start

### Basic Usage

```python
import numpy as np
from web_mapplot import MapPlot

# Create grid
lon = np.linspace(-120, -70, 50)
lat = np.linspace(25, 50, 40)
lon2d, lat2d = np.meshgrid(lon, lat)

# Generate data
temperature = 20 + 10 * np.sin(lon2d / 10) * np.cos(lat2d / 10)

# Create visualization
mp = MapPlot(title="Temperature Map")
mp.add_variable(
    name='Temperature',
    lon=lon2d,
    lat=lat2d,
    data=temperature,
    plot_type='filled_contour',
    colormap='jet',
    units='°C'
)

# Save as HTML
mp.save_html('temperature_map.html')
```

### Time-Series Data

```python
from datetime import datetime, timedelta

# Create 3D data (time, lat, lon)
num_timesteps = 10
timestamps = [datetime(2024, 1, 1) + timedelta(hours=i*6)
              for i in range(num_timesteps)]

temperature_3d = np.zeros((num_timesteps, 50, 40))
for t in range(num_timesteps):
    phase = t * np.pi / 5
    temperature_3d[t] = 15 + 15 * np.sin(lon2d / 8 + phase) * np.cos(lat2d / 8)

mp = MapPlot(title="Temperature Animation")
mp.add_variable(
    name='Temperature',
    lon=lon2d,
    lat=lat2d,
    data=temperature_3d,
    timestamps=timestamps,
    plot_type='filled_contour',
    colormap='hot',
    units='°C'
)

mp.save_html('animated_temperature.html')
```

### Vector Fields

```python
# Generate wind components
u = 5 + 10 * np.sin(lon2d / 5) * np.cos(lat2d / 5)  # eastward
v = 3 + 8 * np.cos(lon2d / 5) * np.sin(lat2d / 5)   # northward
wind_speed = np.sqrt(u**2 + v**2)

mp = MapPlot(title="Wind Field")
mp.add_variable(
    name='Wind Velocity',
    lon=lon2d,
    lat=lat2d,
    data=wind_speed,
    plot_type='vector',  # or 'stream' for streamlines
    u_component=u,
    v_component=v,
    colormap='viridis',
    units='m/s'
)

mp.save_html('wind_field.html')
```

### Multiple Variables

```python
mp = MapPlot(title="Multi-Variable Visualization")

# Add temperature
mp.add_variable(
    name='Temperature',
    lon=lon2d,
    lat=lat2d,
    data=temperature_data,
    plot_type='filled_contour',
    colormap='jet',
    units='°C'
)

# Add pressure
mp.add_variable(
    name='Pressure',
    lon=lon2d,
    lat=lat2d,
    data=pressure_data,
    plot_type='contour',
    colormap='cool',
    units='hPa'
)

# Users can switch between variables in the web interface
mp.save_html('multi_variable.html')
```

### Custom Color Scale Ranges

Control the color scale range with `vmin` and `vmax`:

```python
# Auto-range (default) - uses data min/max
mp.add_variable(
    name='Temperature',
    lon=lon2d,
    lat=lat2d,
    data=temperature,
    plot_type='filled_contour',
    colormap='jet',
    units='°C'
    # vmin=None, vmax=None (default)
)

# Fixed range - useful for comparing multiple datasets
mp.add_variable(
    name='Temperature (Fixed Scale)',
    lon=lon2d,
    lat=lat2d,
    data=temperature,
    plot_type='filled_contour',
    colormap='jet',
    vmin=0,      # Fixed minimum
    vmax=40,     # Fixed maximum
    units='°C'
)

# Symmetric range - useful for anomaly plots
mp.add_variable(
    name='Temperature Anomaly',
    lon=lon2d,
    lat=lat2d,
    data=temperature - 20,
    plot_type='filled_contour',
    colormap='cool',
    vmin=-15,    # Symmetric around zero
    vmax=15,
    units='°C'
)
```

### Web Server Mode

```python
# Launch interactive web server instead of saving file
mp.show(port=5000, debug=False)
# Open http://localhost:5000 in your browser
```

## API Reference

### MapPlot Class

#### `__init__(title, center, zoom)`

Initialize a MapPlot instance.

**Parameters:**
- `title` (str): Title for the visualization
- `center` (tuple): (lat, lon) center point. If None, auto-calculated from data
- `zoom` (int): Initial zoom level (1-18)

#### `add_variable(name, lon, lat, data, **kwargs)`

Add a variable to visualize.

**Parameters:**
- `name` (str): Variable name
- `lon` (ndarray): 2D array of longitudes
- `lat` (ndarray): 2D array of latitudes
- `data` (ndarray): 2D array or 3D array (time, lat, lon)
- `plot_type` (str): Visualization type
  - `'scatter'`: Scatter plot
  - `'contour'`: Contour lines
  - `'filled_contour'`: Filled contours (default)
  - `'vector'`: Vector arrows
  - `'stream'`: Streamlines
- `timestamps` (list): List of datetime objects (required for 3D data)
- `u_component` (ndarray): U component for vector/stream (required for vector plots)
- `v_component` (ndarray): V component for vector/stream (required for vector plots)
- `colormap` (str): Color scheme
  - `'viridis'`, `'plasma'`, `'jet'`, `'rainbow'`, `'cool'`, `'hot'`
- `levels` (int): Number of contour levels (default: 10)
- `vmin` (float): Minimum value for color scale (auto if None)
- `vmax` (float): Maximum value for color scale (auto if None)
- `units` (str): Units for the variable

#### `save_html(filename)`

Save visualization as standalone HTML file.

**Parameters:**
- `filename` (str): Output filename (default: 'map_visualization.html')

**Returns:**
- Absolute path to saved file

#### `show(port, debug)`

Launch web server to display visualization.

**Parameters:**
- `port` (int): Port number (default: 5000)
- `debug` (bool): Enable debug mode (default: False)

## Data Format

### 2D Fields

For single time step data:

```python
lon = 2D array of shape (nlat, nlon)
lat = 2D array of shape (nlat, nlon)
data = 2D array of shape (nlat, nlon)
```

### 3D Fields (Time Series)

For time-varying data:

```python
lon = 2D array of shape (nlat, nlon)
lat = 2D array of shape (nlat, nlon)
data = 3D array of shape (ntime, nlat, nlon)
timestamps = list of datetime objects of length ntime
```

### Vector Fields

For vector or stream fields:

```python
u_component = same shape as data (eastward component)
v_component = same shape as data (northward component)
data = magnitude (or any scalar field for coloring)
```

## Interactive Features

The generated web interface includes:

- **Pan and zoom** on the map
- **Variable selection** dropdown to switch between fields
- **Time controls** for animated data:
  - Play/Pause animation
  - Step forward/backward
  - Time slider
  - Adjustable animation speed
- **Opacity control** for visualization layer
- **Color bar** showing value range
- **Interactive tooltips** on hover
- **Reset view** button

## Examples

See the `examples/` directory for complete working examples:

- `example_basic.py` - Simple filled contour plot
- `example_timeseries.py` - Animated time-series data
- `example_vector_field.py` - Wind velocity vectors
- `example_multiple_variables.py` - Multiple variables with switching
- `example_custom_range.py` - Custom vmin/vmax color scale ranges
- `example_webserver.py` - Using web server mode

Run any example:

```bash
cd examples
python example_basic.py
```

## Browser Compatibility

The generated visualizations work in all modern browsers:
- Chrome/Edge (recommended)
- Firefox
- Safari

## Performance Tips

1. **Subsample large datasets**: For very high-resolution data, consider downsampling for better performance
2. **Limit time steps**: For animations, 10-50 time steps provide good balance between detail and performance
3. **Use appropriate plot types**: Filled contours render faster than scatter plots for dense data
4. **Vector field density**: Vector and stream plots automatically subsample for performance

## Troubleshooting

### Module not found error

Make sure you're running examples from the `examples/` directory or adjust the path:

```python
import sys
sys.path.insert(0, '/path/to/web-mapplot')
from web_mapplot import MapPlot
```

### Data shape mismatch

Ensure lon, lat, and data arrays have compatible shapes:
- lon and lat must have identical shapes
- 2D data must match lon/lat shape
- 3D data shape[1:] must match lon/lat shape

### Web server not accessible

If using `mp.show()`, make sure the port is not already in use:

```python
mp.show(port=8080)  # Try different port
```

## License

MIT License - see LICENSE file

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.
