import unittest
from board import SudokuBoard
from solver_tracker import BacktrackingSolver

class TestSolver(unittest.TestCase):

    def test_solver(self):
        grid = [
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ]

        board = SudokuBoard(grid)
        solver = BacktrackingSolver()

        result = solver.solve(board)

        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main()