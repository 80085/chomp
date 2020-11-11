import itertools
import unittest

from chomp.board import Board


class BoardTest(unittest.TestCase):

    def test_board_created_with_all_available_actions(self):
        rows = 3
        cols = 4
        self.assertEqual(
            list(itertools.product(range(rows), range(cols))),
            Board(rows, cols).available_actions()
        )

    def test_pick_removes_cell(self):
        board = Board(2, 2)
        self.assertEqual(4, len(board.available_actions()))
        board.pick((1, 1))
        self.assertEqual(3, len(board.available_actions()))
        board.pick((1, 0))
        self.assertEqual(2, len(board.available_actions()))
        board.pick((0, 1))
        self.assertEqual(1, len(board.available_actions()))

    def test_pick_same_cell_throws(self):
        board = Board(2, 2)
        board.pick((1, 1))
        with self.assertRaisesRegex(ValueError, 'Invalid action'):
            board.pick((1, 1))

    def test_pick_shrinks_list_when_whole_row_is_picked(self):
        board = Board(4, 1)
        self.assertEqual(4, len(board._grid))
        board.pick((2, 0))
        self.assertEqual(2, len(board._grid))


if __name__ == '__main__':
    unittest.main()
