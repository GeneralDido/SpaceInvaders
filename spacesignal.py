from dataclasses import dataclass
from numpy import array, rot90


@dataclass
class SpaceSignal:
    """ Space signal is used to represent a signal, in a numpy array.
    Can be used by both aliens and radars. """

    rows: int
    cols: int
    signal: array

    def __init__(self, rows, cols, row_signal):
        self.rows = rows
        self.cols = cols
        self.signal = self.make_array(row_signal, self.cols)

    @staticmethod
    def make_array(seq: str, list_len: int) -> array:
        """ Develop the signal (numpy array) from string input. """

        lst = [0 if char == '-' else 1 for char in seq]
        divided_list = [lst[i:i + list_len] for i in range(0, len(lst), list_len)]
        return array(divided_list)

    def rotate_signal(self):
        """ Rotate the signal by 90 degrees. """

        self.signal = rot90(self.signal)
        return self
