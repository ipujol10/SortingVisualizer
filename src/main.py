"""Main entry point for the visualizer"""

from SortingVisualizerIpujol10.Visualizer import Visualizer  # type: ignore


def main() -> None:
    """Visualizer"""
    with Visualizer() as v:
        v.mainloop()


if __name__ == "__main__":
    main()
