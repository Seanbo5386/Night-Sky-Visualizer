# Night-Sky-Visualizer

A simple Python tool for rendering a customizable star chart. It uses a small
catalogue of bright stars and matplotlib to generate a PNG image.

## Features
- Dark and light themes
- Star size scaled by magnitude
- Optional star name labels
- Outputs to a PNG file

## Quick start
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Generate a chart with default settings:
   ```bash
   python night_sky.py --output my_sky.png
   ```
3. Additional options:
   - `--theme dark|light`
   - `--show-labels` to draw star names
   - `--data` to use a different CSV catalogue

The default catalogue in `data/stars.csv` lists some of the brightest stars in
the sky.
