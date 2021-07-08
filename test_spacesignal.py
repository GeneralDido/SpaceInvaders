import unittest
from input import TextInput
from spacesignal import SpaceSignal
import numpy as np  # pragma: no cover


class TestSpaceSignal(unittest.TestCase):

    def test_make_array(self):
        invader_input = TextInput('tests/Invaders/InvaderSimple.txt')
        invader = SpaceSignal(invader_input.rows, invader_input.cols, invader_input.row_signal)

        np.testing.assert_array_equal(invader.signal, np.array([[0, 1, 0], [0, 1, 0]]))

        invader.rotate_signal()
        np.testing.assert_array_equal(invader.signal, np.array([[0, 0], [1, 1], [0, 0]]))


unittest.main()
