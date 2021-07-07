from dataclasses import dataclass
from spacesignal import SpaceSignal
import similarity_function


@dataclass
class LocationFinder:
    accuracy: float

    def central_locations(self, invader: SpaceSignal, radar: SpaceSignal,
                          similarity: similarity_function) -> list:
        equality_lst = []
        for i in range(0, radar.rows - invader.rows + 1):
            for j in range(0, radar.cols - invader.cols + 1):
                equality_lst.append(
                    [similarity.similarity_comparison(
                        invader.signal,
                        radar.signal[i:i + invader.rows, j:j + invader.cols]),
                        radar.signal[i:i + invader.rows, j:j + invader.cols], i, j])
        filtered_list = filter(lambda x: x[0] >= self.accuracy, equality_lst)
        return sorted(filtered_list, key=lambda k: k[0], reverse=True)

    def edges_left(self, invader: SpaceSignal, radar: SpaceSignal, similarity: similarity_function) -> list:
        edge_list_left = []
        for _ in range(4):
            rows = invader.rows
            for i in range(0, invader.rows - 1):
                edge_cols_left = 1
                for _ in range(0, invader.cols - 1):
                    if edge_cols_left <= invader.cols:
                        edge_list_left.append(
                            [similarity.similarity_comparison(
                                invader.signal[rows - 1:invader.rows, -edge_cols_left:],
                                radar.signal[0:i + 1, :edge_cols_left]),
                                radar.signal[0:i + 1, :edge_cols_left],
                                invader.signal[rows - 1:invader.rows, -edge_cols_left:]])
                        edge_cols_left += 1
                rows -= 1
            invader.inverse_signal()
            radar.inverse_signal()
        filtered_list = filter(lambda x: x[0] >= self.accuracy and x[1].size >= invader.signal.size/2, edge_list_left)
        return sorted(filtered_list, key=lambda k: k[0], reverse=True)

    def edges_right(self, invader: SpaceSignal, radar: SpaceSignal, similarity: similarity_function) -> list:
        edge_list_right = []
        for _ in range(4):
            rows = invader.rows
            for i in range(0, invader.rows - 1):
                edge_cols_right = invader.cols
                for _ in range(0, invader.cols - 1):
                    if edge_cols_right > 0:
                        edge_list_right.append(
                            [similarity.similarity_comparison(
                                invader.signal[rows - 1:invader.rows, :edge_cols_right - 1],
                                radar.signal[0:i + 1, radar.cols - edge_cols_right + 1:]),
                                radar.signal[0:i + 1, radar.cols - edge_cols_right + 1:],
                                invader.signal[rows - 1:invader.rows, :edge_cols_right - 1]])
                    edge_cols_right -= 1
                rows -= 1
            invader.inverse_signal()
            radar.inverse_signal()
        filtered_list = filter(lambda x: x[0] >= self.accuracy and x[1].size >= invader.signal.size/2, edge_list_right)
        return sorted(filtered_list, key=lambda k: k[0], reverse=True)

    def edges_center(self, invader: SpaceSignal, radar: SpaceSignal, similarity: similarity_function) -> list:
        edge_list_center = []
        for _ in range(4):
            rows_up = invader.rows
            for i in range(0, invader.rows - 1):
                for j in range(0, radar.cols - invader.cols + 1):
                    edge_list_center.append(
                        [similarity.similarity_comparison(
                            invader.signal[rows_up - 1:invader.rows, :],
                            radar.signal[0:i + 1, j:j + invader.cols]),
                            radar.signal[0:i + 1, j:j + invader.cols],
                            invader.signal[rows_up - 1:invader.rows, :]])
                rows_up -= 1
            invader.inverse_signal()
            radar.inverse_signal()
        filtered_list = filter(lambda x: x[0] >= self.accuracy and x[1].size >= invader.signal.size/2, edge_list_center)
        return sorted(filtered_list, key=lambda k: k[0], reverse=True)

    def find_all_cases(self, invader: SpaceSignal, radar: SpaceSignal, similarity: similarity_function) -> list:

        edges_list = [
            # self.central_locations(invader, radar, similarity),
                      self.edges_left(invader, radar, similarity),
                      self.edges_center(invader, radar, similarity),
                      self.edges_right(invader, radar, similarity)
                      ]
        return edges_list
