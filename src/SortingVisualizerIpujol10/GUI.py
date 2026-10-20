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

        self.canvas: tk.Canvas = tk.Canvas(self, state="normal")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.canvas.create_rectangle(0, 0, 10, 200, fill="red")
