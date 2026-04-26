from solver import SudokuSolver

class BacktrackingSolver(SudokuSolver):

    def solve(self, board):
        grid = board.get_grid()
        self._solve(grid)
        return grid

    def _solve(self, grid):
        empty = self._find_empty(grid)
        if not empty:
            return True

        row, col = empty

        for num in range(1, 10):
            if self._is_valid(grid, num, row, col):
                grid[row][col] = num

                if self._solve(grid):
                    return True

                grid[row][col] = 0

        return False

    def _find_empty(self, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return (i, j)
        return None

    def _is_valid(self, grid, num, row, col):
        # row
        if num in grid[row]:
            return False

        # column
        for i in range(9):
            if grid[i][col] == num:
                return False

        # box
        box_x = col // 3
        box_y = row // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if grid[i][j] == num:
                    return False

        return True