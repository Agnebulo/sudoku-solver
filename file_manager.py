class FileManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FileManager, cls).__new__(cls)
        return cls._instance

    def read_from_file(self, filename):
        grid = []

        with open(filename, "r") as f:
            for line in f:
                if line.strip():
                    row = list(map(int, line.strip().split()))
                    if len(row) != 9:
                        raise ValueError("Each row must have 9 numbers")
                    grid.append(row)

        if len(grid) != 9:
            raise ValueError("Grid must have 9 rows")

        return grid

    def write_to_file(self, filename, grid):
        with open(filename, "w") as f:
            for row in grid:
                f.write(" ".join(map(str, row)) + "\n")