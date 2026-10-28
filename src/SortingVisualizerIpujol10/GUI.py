"""GUI module"""

from __future__ import annotations

from abc import ABC, abstractmethod
import tkinter as tk
from typing import TYPE_CHECKING

from SortingVisualizerIpujol10.Utils import Screens

if TYPE_CHECKING:
    from SortingVisualizerIpujol10.Visualizer import Visualizer


class MyScreen(ABC, tk.Frame):
    """Interface for screens"""

    def __init__(self, parent: tk.Frame, controller: Visualizer) -> None:
        self.width: int = 1000
        self.height: int = 500

        tk.Frame.__init__(self, master=parent, width=self.width, height=self.height)
        self.controller: Visualizer = controller

    @abstractmethod
    def setSettings(self) -> None:
        """Set settings when needed"""

    @abstractmethod
    def getSelection(self) -> str:
        """Get function selected in settings"""


class MainVisualizer(MyScreen):
    """Main Visualizer Screen"""

    def __init__(self, parent: tk.Frame, controller: Visualizer) -> None:
        MyScreen.__init__(self, parent, controller)

        size: int = len(self.controller.data)
        d_width: int = self.width // size
        d_height: int = self.height // size

        self._canvas: tk.Canvas = tk.Canvas(self, width=self.width, height=self.height)
        self._canvas.pack(side="top", fill="both")
        self._coordinates: list[tuple[int, int, int, int]] = [(0, 0, 0, 0) for _ in range(size)]
        for i, h in enumerate(self.controller.data):
            coords: tuple[int, int, int, int] = (
                i * d_width,
                self.height - h * d_height,
                (i + 1) * d_width,
                self.height,
            )
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

        controls: tk.Frame = tk.Frame(self)
        controls.pack(side="bottom", fill="x")
        controls.columnconfigure(0, weight=1)
        controls.columnconfigure(1, weight=1)
        controls.columnconfigure(2, weight=1)
        controls.rowconfigure(0, weight=1)

        self._sorting_type_var: tk.StringVar = tk.StringVar(self, value="Test", name="sorting_type_var")
        self._start_stop_button_var: tk.StringVar = tk.StringVar(self, value="Start", name="start_stop_button_var")
        tk.Label(
            controls,
            textvariable=self._sorting_type_var,
        ).grid(row=0, column=0)
        tk.Button(
            controls,
            textvariable=self._start_stop_button_var,
            command=lambda: print("Start"),
        ).grid(row=0, column=1)
        tk.Button(
            controls,
            text="Restart",
            command=lambda: print("Restart"),
        ).grid(column=2, row=0)

        self._draw()

    def _swap(self, i: int, j: int) -> None:
        a: int = self.controller.data[i]
        b: int = self.controller.data[j]
        coord_a: tuple[int, ...] = self._coordinates[a - 1]
        coord_b: tuple[int, ...] = self._coordinates[b - 1]
        xa0: int = coord_b[0]
        xa1: int = coord_b[2]
        xb0: int = coord_a[0]
        xb1: int = coord_a[2]
        self._coordinates[a - 1] = (xa0, coord_a[1], xa1, coord_a[3])
        self._coordinates[b - 1] = (xb0, coord_b[1], xb1, coord_b[3])

    def _draw(self) -> None:
        for h in self.controller.data:
            self._canvas.delete(str(h))
            self._canvas.create_rectangle(*self._coordinates[h - 1], fill="green", tags=str(h))

    def setSettings(self) -> None:
        self.controller.menubar.entryconfigure("Settings", state="active")
        self._sorting_type_var.set(self.controller.getSelection())

    def getSelection(self) -> str:
        raise ValueError("Function called on the wrong class")


class Settings(MyScreen):
    """Settings screen"""

    def __init__(self, parent: tk.Frame, controller: Visualizer) -> None:
        MyScreen.__init__(self, parent, controller)

        tk.Button(
            self,
            text="Visualizer",
            command=lambda: self.controller.showScreen(Screens.VISUALIZER),
        ).pack(side="top", pady=15)

        self._frame: tk.Frame = tk.Frame(self)
        self._frame.pack(fill="y", expand=True)
        self._selection: tk.IntVar = tk.IntVar(self, 0)
        self._values: list[str] = [f"Label {i+1}" for i in range(10)]
        self._radios: list[tk.Radiobutton] = []
        self._drawOptions()

        tk.Button(
            self,
            text="Refresh",
            command=self._drawOptions,
        ).pack(pady=15)

        location: tk.Frame = tk.Frame(self)
        location.pack(side="bottom", fill="x", expand=True)
        tk.Label(location, text="Location: ").pack(side="left")
        self._location_var: tk.StringVar = tk.StringVar(self, value="")
        tk.Label(
            location,
            textvariable=self._location_var,
            relief="sunken",
        ).pack()
        tk.Button(location, text="Select").pack(side="right")

    def setSettings(self) -> None:
        self.controller.menubar.entryconfigure("Settings", state="disabled")

    def _drawOptions(self) -> None:
        for radio in self._radios:
            radio.destroy()
        self._radios.clear()
        self._selection.set(0)
        for i, val in enumerate(self._values):
            radio: tk.Radiobutton = tk.Radiobutton(
                self._frame,
                text=val,
                variable=self._selection,
                value=i,
            )
            radio.pack(anchor="w")
            self._radios.append(radio)

    def getSelection(self) -> str:
        return self._values[self._selection.get()]
