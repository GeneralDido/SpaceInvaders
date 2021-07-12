import unittest
from input import TextInput


class TestTextInput(unittest.TestCase):

    def test_get_correct_input(self):
        invader = TextInput('tests/Invaders/InvaderSimple.txt')
        rows = invader.rows
        cols = invader.cols
        row_signal = invader.row_signal

        self.assertEqual(rows, 2)
        self.assertEqual(cols, 3)
        self.assertEqual(row_signal, '-o--o-')


if __name__ == '__main__':
    unittest.main()
