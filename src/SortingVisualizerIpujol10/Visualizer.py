"""Main Visualizer Module"""

import random


class Visualizer:
    """Main visualizer class"""

    def __init__(self) -> None:
        length = 10
        initial: list[int] = [x + 1 for x in range(length)]
        self.data: list[int] = []
        for _ in range(length):
            num = random.choice(initial)
            self.data.append(num)
            initial.remove(num)

        print(self.data)
