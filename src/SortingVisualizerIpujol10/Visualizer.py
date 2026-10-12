"""Main Visualizer Module"""

from __future__ import annotations

from types import TracebackType
import random
import tkinter as tk


class Visualizer(tk.Tk):
    """Main visualizer class"""

    def __init__(self) -> None:
        tk.Tk.__init__(self)
        self.is_root_alive: bool = True
        self.data: list[int]
        self._generateInitialRandomSample(10)

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
