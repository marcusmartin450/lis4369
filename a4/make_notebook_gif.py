#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Execute a notebook, export partial HTML after each code cell, screenshot with headless browser,
and stitch into an animated GIF.
"""

import os
import asyncio
from pathlib import Path
from copy import deepcopy

from nbformat import read
from nbclient import NotebookClient
from nbconvert import HTMLExporter

from PIL import Image
import imageio.v2 as imageio  # not strictly necessary, but handy if you change formats later

# ------------ CONFIG ------------
NB_PATH = Path("a4.ipynb")         # the notebook to execute
KERNEL_NAME = None                 # None = use notebook's kernel; or e.g. "your_env_name"
OUT_DIR = Path("gif_frames")       # temp folder for frames
GIF_PATH = Path("a4_run.gif")      # final GIF path
FPS = 2                            # frames per second
VIEWPORT_WIDTH = 1200              # px width of browser viewport
SCROLL_MARGIN = 50                 # extra bottom margin to avoid clipping
HTML_THEME = "light"               # "light" or "dark"
# ---------------------------------

DARK_SCROLLBAR_CSS = """
::-webkit-scrollbar { width: 12px; height: 12px; }
::-webkit-scrollbar-thumb { background: #888; border-radius: 6px; }
::-webkit-scrollbar-track { background: #222; }
"""

# --- Headless HTML -> PNG via pyppeteer ---
async def html_to_png_async(html_str: str, png_path: Path, width: int):
    from pyppeteer import launch
    browser = await launch(
        headless=True,
        args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-gpu"],
    )
    try:
        page = await browser.newPage()
        await page.setViewport({"width": width, "height": 10})  # temp height
        await page.setContent(html_str, waitUntil=["load", "domcontentloaded", "networkidle0"])
        full_h = await page.evaluate("() => document.documentElement.scrollHeight")
        await page.setViewport({"width": width, "height": int(full_h) + SCROLL_MARGIN})
        await page.addStyleTag(content=DARK_SCROLLBAR_CSS)
        await page.screenshot({"path": str(png_path), "fullPage": True})
    finally:
        await browser.close()

def html_to_png(html_str: str, png_path: Path, width: int):
    # Windows fix: ensure a compatible event loop policy for asyncio
    try:
        import sys
        if sys.platform.startswith("win"):
            import asyncio as _asyncio
            _asyncio.set_event_loop_policy(_asyncio.WindowsSelectorEventLoopPolicy())  # type: ignore[attr-defined]
    except Exception:
        pass
    asyncio.run(html_to_png_async(html_str, png_path, width))

def nb_to_html_string(nb_node) -> str:
    exporter = HTMLExporter()
    exporter.exclude_input = False
    exporter.exclude_input_prompt = True
    exporter.exclude_output_prompt = True
    exporter.theme = HTML_THEME
    body, _ = exporter.from_notebook_node(nb_node)
    return body

def notebook_to_gif(nb_path: Path = NB_PATH,
                    kernel_name: str | None = KERNEL_NAME,
                    out_dir: Path = OUT_DIR,
                    gif_path: Path = GIF_PATH,
                    fps: int = FPS,
                    width: int = VIEWPORT_WIDTH):
    if not nb_path.exists():
        raise FileNotFoundError(nb_path)

    out_dir.mkdir(parents=True, exist_ok=True)

    # Read notebook
    with nb_path.open("r", encoding="utf-8") as f:
        nb = read(f, as_version=4)

    # Execute (populates outputs in-place)
    client = NotebookClient(nb, timeout=600, kernel_name=kernel_name, allow_errors=True)
    client.execute()

    # Build frames: capture after each *code* cell
    frame_paths = []
    frame_idx = 0
    for i, cell in enumerate(nb.cells):
        if cell.cell_type != "code":
            continue
        partial = deepcopy(nb)
        partial.cells = deepcopy(nb.cells[: i + 1])  # cells up to current
        html_str = nb_to_html_string(partial)
        png_path = out_dir / f"frame_{frame_idx:03d}.png"
        html_to_png(html_str, png_path, width)
        frame_paths.append(png_path)
        frame_idx += 1
        print(f"Captured {png_path.name}")

    if not frame_paths:
        raise RuntimeError("No frames captured — are there code cells?")

    # Assemble GIF
    images = [Image.open(p) for p in frame_paths]
    duration_ms = int(1000 / max(1, fps))
    images[0].save(
        gif_path,
        save_all=True,
        append_images=images[1:],
        duration=duration_ms,
        loop=0,
        optimize=False,
        disposal=2,
    )
    print(f"GIF written to: {gif_path.resolve()}")

    # Optional cleanup: uncomment if you want to remove PNG frames
    # for p in frame_paths: p.unlink()

if __name__ == "__main__":
    notebook_to_gif()
