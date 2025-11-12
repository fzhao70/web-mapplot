"""
Flask web server for serving MapPlot visualizations.
"""

from flask import Flask, render_template_string, jsonify
import json


def run_server(mapplot_instance, port=5000, debug=False):
    """
    Run Flask server to display MapPlot visualization.

    Args:
        mapplot_instance: MapPlot instance to visualize
        port: Port number
        debug: Enable debug mode
    """
    app = Flask(__name__)

    @app.route('/')
    def index():
        html = mapplot_instance._generate_html()
        return render_template_string(html)

    @app.route('/api/data')
    def get_data():
        return jsonify({
            'title': mapplot_instance.title,
            'center': mapplot_instance.center,
            'zoom': mapplot_instance.zoom,
            'variables': mapplot_instance.variables
        })

    print(f"Starting server on http://localhost:{port}")
    print("Press Ctrl+C to stop the server")
    app.run(host='0.0.0.0', port=port, debug=debug)
