"""
Main MapPlot class for creating interactive geographical visualizations.
"""

import json
import numpy as np
from typing import Union, List, Dict, Optional, Tuple
from datetime import datetime
import base64
from pathlib import Path


class MapPlot:
    """
    Create interactive web-based geographical visualizations.

    Supports:
    - Scatter/Shape plots
    - Contour plots
    - Filled contour plots
    - Vector fields
    - Stream fields
    - Time-series data with animation
    - Multiple variables with switching capability
    """

    def __init__(self, title: str = "Map Visualization", center: Tuple[float, float] = None, zoom: int = 4):
        """
        Initialize MapPlot instance.

        Args:
            title: Title for the visualization
            center: (lat, lon) center point for the map. If None, auto-calculated from data
            zoom: Initial zoom level (1-18)
        """
        self.title = title
        self.center = center
        self.zoom = zoom
        self.variables = {}

    def add_variable(self,
                     name: str,
                     lon: np.ndarray,
                     lat: np.ndarray,
                     data: np.ndarray,
                     plot_type: str = 'filled_contour',
                     timestamps: Optional[List[datetime]] = None,
                     u_component: Optional[np.ndarray] = None,
                     v_component: Optional[np.ndarray] = None,
                     colormap: str = 'viridis',
                     levels: int = 10,
                     vmin: Optional[float] = None,
                     vmax: Optional[float] = None,
                     units: str = ''):
        """
        Add a variable to the visualization.

        Args:
            name: Variable name
            lon: 2D array of longitudes
            lat: 2D array of latitudes
            data: 2D array (for single time) or 3D array (time, lat, lon) for time-series
            plot_type: Type of visualization - 'scatter', 'contour', 'filled_contour',
                      'vector', 'stream'
            timestamps: List of datetime objects if data is 3D
            u_component: U (eastward) component for vector/stream fields (same shape as data)
            v_component: V (northward) component for vector/stream fields (same shape as data)
            colormap: Color scheme ('viridis', 'plasma', 'jet', 'rainbow', 'cool', 'hot')
            levels: Number of contour levels
            vmin: Minimum value for color scale (auto if None)
            vmax: Maximum value for color scale (auto if None)
            units: Units for the variable
        """

        # Validate inputs
        if lon.shape != lat.shape:
            raise ValueError("lon and lat must have the same shape")

        # Handle 2D vs 3D data
        if data.ndim == 2:
            if data.shape != lon.shape:
                raise ValueError("2D data must match lon/lat shape")
            data = data[np.newaxis, ...]  # Add time dimension
            timestamps = timestamps or [datetime.now()]
        elif data.ndim == 3:
            if data.shape[1:] != lon.shape:
                raise ValueError("3D data shape[1:] must match lon/lat shape")
            if timestamps is None:
                timestamps = [datetime.now()] * data.shape[0]
        else:
            raise ValueError("data must be 2D or 3D array")

        if len(timestamps) != data.shape[0]:
            raise ValueError("Number of timestamps must match first dimension of data")

        # Handle vector fields
        if plot_type in ['vector', 'stream']:
            if u_component is None or v_component is None:
                raise ValueError(f"{plot_type} requires both u_component and v_component")
            if u_component.shape != data.shape or v_component.shape != data.shape:
                raise ValueError("u_component and v_component must match data shape")

        # Calculate value range
        if vmin is None:
            vmin = float(np.nanmin(data))
        if vmax is None:
            vmax = float(np.nanmax(data))

        # Store variable data
        self.variables[name] = {
            'lon': lon.tolist(),
            'lat': lat.tolist(),
            'data': data.tolist(),
            'plot_type': plot_type,
            'timestamps': [ts.isoformat() for ts in timestamps],
            'u_component': u_component.tolist() if u_component is not None else None,
            'v_component': v_component.tolist() if v_component is not None else None,
            'colormap': colormap,
            'levels': levels,
            'vmin': vmin,
            'vmax': vmax,
            'units': units,
            'shape': list(data.shape)
        }

        # Auto-calculate center if not set
        if self.center is None:
            self.center = (float(np.nanmean(lat)), float(np.nanmean(lon)))

    def _generate_html(self) -> str:
        """Generate standalone HTML file content."""

        # Read template
        template_path = Path(__file__).parent.parent / 'templates' / 'map_template.html'
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()

        # Prepare data
        data_json = json.dumps({
            'title': self.title,
            'center': self.center,
            'zoom': self.zoom,
            'variables': self.variables
        })

        # Replace placeholders
        html = template.replace('{{DATA_JSON}}', data_json)
        html = html.replace('{{TITLE}}', self.title)

        return html

    def save_html(self, filename: str = 'map_visualization.html'):
        """
        Save visualization as standalone HTML file.

        Args:
            filename: Output filename
        """
        html = self._generate_html()

        output_path = Path(filename)
        output_path.write_text(html, encoding='utf-8')
        print(f"Saved visualization to {output_path.absolute()}")

        return str(output_path.absolute())

    def show(self, port: int = 5000, debug: bool = False):
        """
        Launch web server to display visualization.

        Args:
            port: Port number for the server
            debug: Enable debug mode
        """
        from .server import run_server
        run_server(self, port=port, debug=debug)

    def _repr_html_(self):
        """For Jupyter notebook integration."""
        return self._generate_html()
