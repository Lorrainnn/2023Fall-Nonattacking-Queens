# queens.py
#
# ICS 33 Fall 2023
# Project 0: History of Modern
#
# A module containing tools that could assist in solving variants of the
# well-known "n-queens" problem.  Note that we're only implementing one part
# of the problem: immutably managing the "state" of the board (i.e., which
# queens are arranged in which cells).  The rest of the problem -- determining
# a valid solution for it -- is not our focus here.
#
# Your goal is to complete the QueensState class described below, though
# you'll need to build it incrementally, as well as test it incrementally by
# writing unit tests in test_queens.py.  Make sure you've read the project
# write-up before you proceed, as it will explain the requirements around
# following (and documenting) an incremental process of solving this problem.
#
# DO NOT MODIFY THE Position NAMEDTUPLE OR THE PROVIDED EXCEPTION CLASSES.

from collections import namedtuple
from typing import Self



Position = namedtuple('Position', ['row', 'column'])

# Ordinarily, we would write docstrings within classes or their methods.
# Since a namedtuple builds those classes and methods for us, we instead
# add the documentation by hand afterward.
Position.__doc__ = 'A position on a chessboard, specified by zero-based row and column numbers.'
Position.row.__doc__ = 'A zero-based row number'
Position.column.__doc__ = 'A zero-based column number'



class DuplicateQueenError(Exception):
    """An exception indicating an attempt to add a queen where one is already present."""

    def __init__(self, position: Position):
        """Initializes the exception, given a position where the duplicate queen exists."""
        self._position = position


    def __str__(self) -> str:
        return f'duplicate queen in row {self._position.row} column {self._position.column}'



class MissingQueenError(Exception):
    """An exception indicating an attempt to remove a queen where one is not present."""

    def __init__(self, position: Position):
        """Initializes the exception, given a position where a queen is missing."""
        self._position = position


    def __str__(self) -> str:
        return f'missing queen in row {self._position.row} column {self._position.column}'



class QueensState:
    """Immutably represents the state of a chessboard being used to assist in
    solving the n-queens problem."""

    def __init__(self, rows: int, columns: int):
        """Initializes the chessboard to have the given numbers of rows and columns,
        with no queens occupying any of its cells."""
        self.initial_chessboard = Position(rows,columns)
        self.chessboard = []
        for i in range(rows):
            row = []
            for j in range(columns):
                row.append('.')
            self.chessboard.append(row)


    def queen_count(self) -> int:
        """Returns the number of queens on the chessboard."""
        count = 0
        for i in range(self.initial_chessboard.row):
            for j in range(self.initial_chessboard.column):
                if self.chessboard[i][j] != '.':
                    count += 1
        return count


    def queens(self) -> list[Position]:
        """Returns a list of the positions in which queens appear on the chessboard,
        arranged in no particular order."""
        list_position = []
        for i in range(self.initial_chessboard.row):
            for j in range(self.initial_chessboard.column):
                if self.chessboard[i][j] != '.':
                    list_position.append(Position(i, j))
        return list_position


    def has_queen(self, position: Position) -> bool:
        """Returns True if a queen occupies the given position on the chessboard, or
        False otherwise."""
        if self.chessboard[position.row][position.column] != '.':
            return True
        else:
            return False



    def any_queens_unsafe(self) -> bool:
        """Returns True if any queens on the chessboard are unsafe (i.e., they can
        be captured by at least one other queen on the chessboard), or False otherwise."""
        All_queen = self.queens()
        for queen in All_queen:
            for c in range(self.initial_chessboard.column):
                """Horizontally check"""
                if c!= queen.column and self.has_queen(Position(queen.row, c)):
                    return True
            for r in range(self.initial_chessboard.row):
                """Vertically check"""
                if r != queen.row and self.has_queen(Position(r, queen.column)) is True:
                    return True

            for r in range(self.initial_chessboard.row):
                for c in range(self.initial_chessboard.column):
                    """Diagonally check"""
                    if c!= queen.column and r != queen.row and ((r + c) == (queen.row + queen.column) or (r - c) == (queen.row - queen.column)):
                        if self.has_queen(Position(r, c)) is True:
                            return True
        return False


    def with_queens_added(self, positions: list[Position]) -> Self:
        """Builds a new QueensState with queens added in the given positions.
        Raises a DuplicateQueenException when there is already a queen in at
        least one of the given positions."""
        for pos in positions:
            if pos.row >= self.initial_chessboard.row or pos.column >= self.initial_chessboard.column:
                raise IndexError
            if not self.has_queen(pos):
                self.chessboard[pos.row][pos.column] = 'Q'
            else:
                raise DuplicateQueenError(Position(pos.row, pos.column))
        return self


    def with_queens_removed(self, positions: list[Position]) -> Self:
        """Builds a new QueensState with queens removed from the given positions.
        Raises a MissingQueenException when there is no queen in at least one of
        the given positions."""
        for pos in positions:
            if pos.row >= self.initial_chessboard.row or pos.column >= self.initial_chessboard.column:
                raise IndexError
            if self.has_queen(pos):
                self.chessboard[pos.row][pos.column] = '.'
            else:
                raise MissingQueenError(Position(pos.row,pos.column))
        return self

