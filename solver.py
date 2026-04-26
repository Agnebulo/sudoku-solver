from abc import ABC, abstractmethod

class SudokuSolver(ABC):

    @abstractmethod
    def solve(self, board):
        pass