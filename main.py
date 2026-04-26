from board import SudokuBoard
from backtracking_solver import BacktrackingSolver
from file_manager import FileManager


def main():
    file_manager = FileManager()

    grid = file_manager.read_from_file("input.txt")

    board = SudokuBoard(grid)

    solver = BacktrackingSolver()
    solved = solver.solve(board)

    print("Solved Sudoku:")
    board.print_board()

    file_manager.write_to_file("output.txt", solved)


if __name__ == "__main__":
    main()