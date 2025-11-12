# Quick Start Guide

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Or install the package
pip install -e .
```

## Run the Demo

The fastest way to see the library in action:

```bash
python demo.py
```

This will create `demo_output.html` with all features demonstrated.

## Basic Example (30 seconds)

```python
import numpy as np
from web_mapplot import MapPlot

# 1. Create your data
lon = np.linspace(-120, -70, 50)
lat = np.linspace(25, 50, 40)
lon2d, lat2d = np.meshgrid(lon, lat)
data = 20 + 10 * np.sin(lon2d / 10) * np.cos(lat2d / 10)

# 2. Create the plot
mp = MapPlot(title="My First Map")
mp.add_variable('Temperature', lon2d, lat2d, data,
                plot_type='filled_contour', units='°C')

# 3. Save it
mp.save_html('my_map.html')
```

Open `my_map.html` in your browser!

## Examples

All examples are in the `examples/` directory:

```bash
cd examples

# Basic filled contour
python example_basic.py

# Time-series animation
python example_timeseries.py

# Vector field visualization
python example_vector_field.py

# Multiple variables
python example_multiple_variables.py

# Web server mode
python example_webserver.py
```

## Web Server Mode

Instead of saving HTML files, you can run a web server:

```python
mp.show(port=5000)
```

Then open http://localhost:5000 in your browser.

## Key Features

### Plot Types

- `'scatter'` - Scatter points
- `'contour'` - Contour lines
- `'filled_contour'` - Filled contours (default)
- `'vector'` - Vector arrows
- `'stream'` - Streamlines

### Time-Series Data

For animated data, use 3D arrays:

```python
# data shape: (time_steps, lat, lon)
data_3d = np.zeros((10, 40, 50))  # 10 time steps
timestamps = [datetime(2024, 1, 1) + timedelta(hours=i*6)
              for i in range(10)]

mp.add_variable('Temperature', lon2d, lat2d, data_3d,
                timestamps=timestamps, plot_type='filled_contour')
```

### Vector Fields

For wind or current data:

```python
u = ...  # eastward component
v = ...  # northward component
magnitude = np.sqrt(u**2 + v**2)

mp.add_variable('Wind', lon2d, lat2d, magnitude,
                plot_type='vector', u_component=u, v_component=v)
```

### Multiple Variables

Add multiple variables for easy switching:

```python
mp.add_variable('Temperature', lon2d, lat2d, temp_data, ...)
mp.add_variable('Pressure', lon2d, lat2d, pres_data, ...)
mp.add_variable('Wind', lon2d, lat2d, wind_data, ...)
```

Users can switch between them in the web interface.

## Color Schemes

Available colormaps:
- `'viridis'` (blue to yellow)
- `'plasma'` (purple to yellow)
- `'jet'` (blue to red through rainbow)
- `'rainbow'` (full rainbow)
- `'cool'` (cyan to magenta)
- `'hot'` (black to white through red/yellow)

## Need Help?

- See `README.md` for full documentation
- Check `examples/` for working code
- Run `python demo.py` for a comprehensive demonstration
