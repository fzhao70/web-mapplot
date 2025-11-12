"""
Setup script for web_mapplot package
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / 'README.md'
long_description = readme_file.read_text() if readme_file.exists() else ''

setup(
    name='web_mapplot',
    version='1.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='Interactive web-based geographical visualizations',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/web-mapplot',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'web_mapplot': ['../templates/*.html'],
    },
    install_requires=[
        'numpy>=1.20.0',
        'flask>=2.0.0',
    ],
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Visualization',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='visualization, maps, geospatial, plotting, contour, vector-field',
)
