"""Simple night sky visualizer using matplotlib.

Reads star data from a CSV file and produces a sky chart image.
"""
from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path
from typing import List

import matplotlib.pyplot as plt


@dataclass
class Star:
    """Information about a star."""
    name: str
    ra_deg: float  # Right ascension in degrees
    dec_deg: float  # Declination in degrees
    mag: float  # Apparent magnitude


THEMES = {
    "dark": {"bg": "black", "fg": "white"},
    "light": {"bg": "#f2f2f2", "fg": "#111111"},
}


def read_stars(path: Path) -> List[Star]:
    """Load stars from a CSV file."""
    stars: List[Star] = []
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            stars.append(
                Star(
                    name=row["name"],
                    ra_deg=float(row["ra_deg"]),
                    dec_deg=float(row["dec_deg"]),
                    mag=float(row["mag"]),
                )
            )
    return stars


def plot_sky(stars: List[Star], theme: str, show_labels: bool, output: Path) -> None:
    """Render the given stars using matplotlib."""
    style = THEMES.get(theme, THEMES["dark"])

    fig, ax = plt.subplots(figsize=(10, 6), facecolor=style["bg"])
    ax.set_facecolor(style["bg"])
    ax.invert_xaxis()  # Sky charts usually have RA increasing to the left

    ra = [s.ra_deg for s in stars]
    dec = [s.dec_deg for s in stars]
    sizes = [max(1, 10 - s.mag * 2) ** 2 for s in stars]

    ax.scatter(ra, dec, s=sizes, c=style["fg"], alpha=0.8)

    if show_labels:
        for s in stars:
            ax.text(s.ra_deg, s.dec_deg, s.name, color=style["fg"], fontsize=8)

    ax.set_xlabel("Right Ascension (deg)")
    ax.set_ylabel("Declination (deg)")
    ax.set_title("Night Sky")
    ax.grid(color=style["fg"], alpha=0.2)

    fig.savefig(output, dpi=150, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data",
        default=Path("data/stars.csv"),
        type=Path,
        help="Path to star catalogue CSV",
    )
    parser.add_argument(
        "--theme",
        default="dark",
        choices=sorted(THEMES),
        help="Colour theme for the chart",
    )
    parser.add_argument(
        "--show-labels",
        action="store_true",
        help="Draw star names next to their positions",
    )
    parser.add_argument(
        "--output",
        default=Path("night_sky.png"),
        type=Path,
        help="File to save the generated image",
    )

    args = parser.parse_args()

    stars = read_stars(args.data)
    plot_sky(stars, args.theme, args.show_labels, args.output)


if __name__ == "__main__":
    main()
