from dataclasses import dataclass
from numpy import array


@dataclass
class SpaceSignal:
    rows: int
    cols: int
    signal: array

    def __init__(self, rows, cols, row_signal):
        self.rows = rows
        self.cols = cols
        self.signal = self.make_array(row_signal, self.cols)

    @staticmethod
    def make_array(seq: str, list_len: int) -> array:
        lst = [0 if char == '-' else 1 for char in seq]
        divided_list = [lst[i:i + list_len] for i in range(0, len(lst), list_len)]
        return array(divided_list)
