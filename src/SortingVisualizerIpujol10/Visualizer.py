"""Main Visualizer Module"""

from __future__ import annotations

from types import TracebackType
import random
import tkinter as tk
from SortingVisualizerIpujol10.GUI import MyScreen, MainVisualizer
from SortingVisualizerIpujol10.Utils import Screens


class Visualizer(tk.Tk):
    """Main visualizer class"""

    def __init__(self) -> None:
        tk.Tk.__init__(self)
        self.is_root_alive: bool = True
        self.data: list[int]
        self._generateInitialRandomSample(10)

        self.title("Sorting Visualizer")
        self.mainframe: tk.Frame = tk.Frame(self)
        self.mainframe.grid(column=0, row=0, sticky="nsew")
        self._current_frame: tk.Frame
        self._frames: dict[Screens, MyScreen] = {}
        for i, f in enumerate((MainVisualizer,)):
            frame = f(parent=self.mainframe, controller=self)
            self._frames[Screens(i)] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.showScreen(Screens.VISUALIZER)
        self.is_root_alive = True

        self.resizable(width=False, height=False)

        self.menubar: tk.Menu = tk.Menu(self)
        file = tk.Menu(self)
        file.add_command(label="Test1", command=lambda: print("test1"))
        file.add_command(label="Test2", command=lambda: print("test2"))
        self.menubar.add_cascade(menu=file, label="File")
        self.menubar.add_command(label="Settings", underline=0)
        self.configure(menu=self.menubar)

    def __enter__(self) -> Visualizer:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.destroy()

    def destroy(self) -> None:
        self.is_root_alive = False
        self.quit()

    def _generateInitialRandomSample(self, size: int) -> None:
        initial: list[int] = [x + 1 for x in range(size)]
        self.data = []
        for _ in range(size):
            num = random.choice(initial)
            self.data.append(num)
            initial.remove(num)

    def showScreen(self, screen: Screens) -> None:
        """Show a screen"""
        self._current_frame = self._frames[screen]
        self._current_frame.tkraise()  # type: ignore
