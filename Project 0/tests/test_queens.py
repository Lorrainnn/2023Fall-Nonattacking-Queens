# test_queens.py
#
# ICS 33 Fall 2023
# Project 0: History of Modern
#
# Unit tests for the QueensState class in "queens.py".
#
# Docstrings are not required in your unit tests, though each test does need to have
# a name that clearly indicates its purpose.  Notice, for example, that the provided
# test method is named "test_zero_queen_count_initially" instead of something generic
# like "test_queen_count", since it doesn't entirely test the "queen_count" method,
# but instead focuses on just one aspect of how it behaves.  You'll want to do likewise.

from queens import QueensState, Position
import unittest



class TestQueensState(unittest.TestCase):
    def test_queen_count_is_zero_initially(self):
        state = QueensState(8, 8)
        self.assertEqual(state.queen_count(), 0)

    def test_chessboard_is_initialized(self):
        state = QueensState(3, 2)
        self.assertEqual(state.chessboard, [['.','.'],['.','.'],['.','.']])

    def test_return_queen_position_is_empty_initially(self):
        state = QueensState(8, 8)
        self.assertEqual(state.queens(), [])

    def test_has_queen_function_in_empty_chessboard(self):
        state = QueensState(4, 4)
        self.assertFalse(state.has_queen(Position(1,1)))

    def test_add_queen_successfully(self):
        state = QueensState(4, 4)
        state.with_queens_added([Position(1,1),Position(2,3)])
        self.assertTrue(state.has_queen(Position(1, 1)))
        self.assertTrue(state.has_queen(Position(2, 3)))

    def test_add_queen_unsuccessfully(self):
        state = QueensState(3, 3)
        try:
            state.with_queens_added([Position(1,1),Position(1,1)])
        except Exception as e:
            self.assertEqual(str(e),'duplicate queen in row 1 column 1')

    def test_add_queen_beyond_map(self):
        state = QueensState(3, 3)
        try:
            state.with_queens_added([Position(22, 33)])
        except:
            self.assertRaises(IndexError)



    def test_remove_queen_successfully(self):
        state = QueensState(5, 5)
        state.with_queens_added([Position(1, 1), Position(2, 3)])
        self.assertTrue(state.has_queen(Position(1, 1)))
        self.assertTrue(state.has_queen(Position(2, 3)))
        state.with_queens_removed([Position(1, 1), Position(2, 3)])
        self.assertFalse(state.has_queen(Position(1, 1)))
        self.assertFalse(state.has_queen(Position(2, 3)))

    def test_remove_queen_unsuccessfully(self):
        state = QueensState(5, 5)
        try:
            state.with_queens_removed([Position(1, 1)])
        except Exception as e:
            self.assertEqual(e.__str__(),"missing queen in row 1 column 1")

    def test_remove_queen_beyond_map(self):
        state = QueensState(5, 5)
        try:
            state.with_queens_removed([Position(22, 33)])
        except:
            self.assertRaises(IndexError)



    def test_queen_return_list(self):
        state = QueensState(5, 5)
        state.with_queens_added([Position(1, 1), Position(1, 3)])
        self.assertEqual(state.queens(),[Position(1, 1), Position(1, 3)])

    def test_count_multi_number_queens(self):
        state = QueensState(3, 3)
        state.with_queens_added([Position(0, 0), Position(1,2)])
        self.assertEqual(state.queen_count(), 2)

    def test_any_queen_unsafe_SAFE_with_no_queen(self):
        state = QueensState(8, 3)
        self.assertFalse(state.any_queens_unsafe())

    def test_any_queen_unsafe_SAFE_with_queens(self):
        state = QueensState(3, 3)
        state.with_queens_added([Position(0,0),Position(2,1)])
        self.assertFalse(state.any_queens_unsafe())

    def test_any_queen_unsafe_UNSAFE_Horizontally(self):
        state = QueensState(3, 3)
        state.with_queens_added([Position(0, 0), Position(0, 1)])
        self.assertTrue(state.any_queens_unsafe())

    def test_any_queen_unsafe_UNSAFE_Vertically(self):
        state = QueensState(3, 3)
        state.with_queens_added([Position(0, 0), Position(1, 0)])
        self.assertTrue(state.any_queens_unsafe())

    def test_any_queen_unsafe_UNSAFE_PositiveDiagonal(self):
        state = QueensState(3, 3)
        state.with_queens_added([Position(1,1), Position(0,2)])
        self.assertTrue(state.any_queens_unsafe())

    def test_any_queen_unsafe_UNSAFE_NegativeDiagonal(self):
        state = QueensState(3, 3)
        state.with_queens_added([Position(1,1), Position(2, 0)])
        self.assertTrue(state.any_queens_unsafe())


if __name__ == '__main__':
    unittest.main()
