"""
Setup script for web_mapplot package
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / 'README.md'
long_description = readme_file.read_text(encoding='utf-8') if readme_file.exists() else ''

setup(
    name='web-mapplot',
    version='2.0.0',
    author='Web MapPlot Contributors',
    author_email='',
    description='Interactive web-based geographical visualizations with advanced features',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/web-mapplot',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['templates/*.html'],
    },
    install_requires=[
        'numpy>=1.20.0',
        'flask>=2.0.0',
    ],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'black>=21.0',
        ],
    },
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Scientific/Engineering :: GIS',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    keywords='visualization, maps, geospatial, plotting, contour, vector-field, heatmap, leaflet, interactive',
    project_urls={
        'Documentation': 'https://github.com/yourusername/web-mapplot#readme',
        'Source': 'https://github.com/yourusername/web-mapplot',
        'Tracker': 'https://github.com/yourusername/web-mapplot/issues',
    },
)
