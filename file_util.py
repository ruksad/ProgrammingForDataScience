from pathlib import Path


def head(filepath: Path, n=5, width=-1):
    """prints width characters of first n lines of filepath"""

    with filepath.open() as f:
        for _ in range(n):
            (print(f.readline(), end="")) if width < 0 else (print(f.readline()[:width]))


if __name__ == '__main__':
    head(Path('sources') / 'co2_mm_mlo.txt')
    print("\n")
    head(Path('sources') / 'co2_mm_mlo.txt', 10, 20)  ## read only 20 chars from every line of the given file
