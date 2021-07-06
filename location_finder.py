from dataclasses import dataclass
from spacesignal import SpaceSignal
import similarity_function


@dataclass
class LocationFinder:
    accuracy: float

    def find_possible_locations(self, invader: SpaceSignal, radar: SpaceSignal,
                                similarity: similarity_function) -> list:
        equality_lst = []
        for i in range(0, radar.rows - invader.rows + 1):
            for j in range(0, radar.cols - invader.cols + 1):
                equality_lst.append(
                    [similarity.similarity_comparison(invader.signal,
                                                      radar.signal[i:i + invader.rows, j:j + invader.cols]),
                     radar.signal[i:i + invader.rows, j:j + invader.cols], i, j])
        filtered_list = filter(lambda x: x[0] >= self.accuracy, equality_lst)
        return sorted(filtered_list, key=lambda k: k[0], reverse=True)
