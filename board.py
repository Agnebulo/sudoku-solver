class SudokuBoard:
    def __init__(self, grid):
        self._grid = grid  # encapsulation

    def get_grid(self):
        return self._grid

    def print_board(self):
        for row in self._grid:
            print(" ".join(str(num) for num in row))