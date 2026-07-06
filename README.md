# US7032353 - Swivel Joint Visualizer

An interactive 3D solid assembly and 2D technical schematic visualizer for the Utility Swivel Joint apparatus (Patent US7032353B2).

This project features a fully self-contained, GPU-independent 3D vector engine built entirely on the HTML5 CPU Canvas. It uses a custom Painter's Algorithm for depth sorting and dynamic solid face clipping, allowing high-fidelity technical diagrams and fluid flow animations directly in the browser.

## Features
- **Dual Engine Render**: Switch seamlessly between a 2D engineering cross-section and a 3D isometric solid assembly.
- **CPU Painter's Algorithm**: Fully opaque 3D objects, dynamic edge fading, and clipping planes calculated entirely on the CPU (no WebGL required).
- **Interactive Cutaway**: View the internal rotating mechanism and fluid channels via an interactive 90-degree cutaway toggle.
- **Export to SVG**: Download a pristine, infinitely scalable vector blueprint of the exact current 3D or 2D viewport.
- **Flow Simulation**: Animated particle tracing to understand the routing of water, gas, wastewater, and electricity through the rotating joints.

## Development

To preview locally:
1. Simply open `index.html` in your browser.
2. (Optional) Run a local HTTP server: `python3 -m http.server 3018`.

## Testing
This repository includes a Playwright script to verify UI integrity.
```bash
# Run tests
python3 test.py
```
