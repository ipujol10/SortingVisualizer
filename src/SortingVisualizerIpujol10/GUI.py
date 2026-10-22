"""GUI module"""

from __future__ import annotations

from abc import ABC
import tkinter as tk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from SortingVisualizerIpujol10.Visualizer import Visualizer


class MyScreen(ABC, tk.Frame):
    """Interface for screens"""

    def __init__(self, parent: tk.Frame, controller: Visualizer) -> None:
        tk.Frame.__init__(self, master=parent)
        self.controller: Visualizer = controller


class MainVisualizer(MyScreen):
    """Main Visualizer Screen"""

    def __init__(self, parent: tk.Frame, controller: Visualizer) -> None:
        MyScreen.__init__(self, parent, controller)

        width: int = 1000
        height: int = 500
        size: int = len(self.controller.data)
        d_width: int = width // size
        d_height: int = height // size

        self._canvas: tk.Canvas = tk.Canvas(self, width=width, height=height)
        self._canvas.grid(row=0, column=0, sticky="nsew")
        self._coordinates: list[tuple[int, int, int, int]] = [(0, 0, 0, 0) for _ in range(size)]
        for i, h in enumerate(self.controller.data):
            coords: tuple[int, int, int, int] = (i * d_width, height - h * d_height, (i + 1) * d_width, height)
            self._canvas.create_rectangle(*coords, fill="green", tags=str(h))
            self._coordinates[h - 1] = coords

        coord1 = self._coordinates[0]
        coord10 = self._coordinates[9]
        x00 = coord10[0]
        x01 = coord10[2]
        x10 = coord1[0]
        x11 = coord1[2]
        self._coordinates[0] = (x00, coord1[1], x01, coord1[3])
        self._coordinates[9] = (x10, coord10[1], x11, coord10[3])

        for i, h in enumerate(self.controller.data):
            self._canvas.delete(str(h))
            self._canvas.create_rectangle(*self._coordinates[h - 1], fill="green", tags=str(h))
