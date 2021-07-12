from spacesignal import SpaceSignal
from similarity_function import SimilarityFunction
from numpy import array, rot90


class LocationFinder:
    """ LocationFinder calculates possible locations using signals from a space invader and the radar,
    a similarity function and an expected accuracy score."""

    invader: SpaceSignal
    radar: SpaceSignal
    similarity: SimilarityFunction
    accuracy: float

    def __init__(self, invader: SpaceSignal, radar: SpaceSignal, similarity: SimilarityFunction, accuracy: float):
        if invader.signal.size > radar.signal.size:
            raise ValueError(f"Invader signal array should be the same size or smaller than the radar signal array.")
        else:
            self.invader = invader
            self.radar = radar
        self.similarity = similarity
        if accuracy <= 0.0 or accuracy > 1.0:
            raise ValueError(f"accuracy should be between 0.0 and 1.0 but received {accuracy} instead.")
        else:
            self.accuracy = accuracy

    def central_locations(self) -> list:
        """ Finds possible locations with the full invader array, while traversing the radar array. """

        equality_lst = []
        for i in range(0, self.radar.rows - self.invader.rows + 1):
            for j in range(0, self.radar.cols - self.invader.cols + 1):
                equality_lst.append(
                    [self.similarity.similarity_comparison(
                        self.invader.signal,
                        self.radar.signal[i:i + self.invader.rows, j:j + self.invader.cols]),
                        self.radar.signal[i:i + self.invader.rows, j:j + self.invader.cols], i, j])
        filtered_list = filter(lambda x: x[0] >= self.accuracy, equality_lst)
        return sorted(filtered_list, key=lambda k: k[0], reverse=True)

    def edges(self) -> list:
        """Traverses the edges of the radar array, starting from col 1 up to col n-1.
        Inserts new invader array rows in each iteration up to n-1 invader rows.
         We do this 4 times, each time rotating the two matrices by 90 degrees.
         Coordinates of returned radar signal start from the edge."""

        def rotate_signal(signal: array, n) -> array:
            """ Rotates signal n times, n: number of current rotations """

            for _ in range(n):
                signal = rot90(signal)
            return signal

        def correct_coordinates(num_inversions: int, coordinate: int, radar_rows: int,
                                radar_cols: int, invader_cols: int) -> (int, int):
            """ Develops the right coordinates when rotating the invader and radar arrays by 90 degrees each time."""

            if num_inversions == 0:
                return 0, coordinate
            elif num_inversions == 1:
                return coordinate, radar_cols - 1
            elif num_inversions == 2:
                return radar_rows - 1, abs(radar_cols - coordinate - invader_cols)
            else:
                return coordinate, 0

        edge_list = []
        for num_rotations in range(4):
            rows = self.invader.rows
            for i in range(0, self.invader.rows - 1):
                for j in range(0, self.radar.cols - self.invader.cols + 1):
                    coordinates = correct_coordinates(
                        num_rotations, j, self.radar.rows, self.radar.cols, self.invader.cols)
                    rotated_signal = rotate_signal(
                        self.radar.signal[0:i + 1, j:j + self.invader.cols], 4 - num_rotations)
                    edge_list.append(
                        [self.similarity.similarity_comparison(
                            self.invader.signal[rows - 1:self.invader.rows, :],
                            self.radar.signal[0:i + 1, j:j + self.invader.cols]),
                            rotated_signal,
                            coordinates[0],
                            coordinates[1]])
                rows -= 1
            self.invader.signal = rotate_signal(self.invader.signal, 1)
            self.radar.signal = rotate_signal(self.radar.signal, 1)
        filtered_list = filter(lambda x: x[0] >= self.accuracy and x[1].size >= self.invader.signal.size/2, edge_list)
        return sorted(filtered_list, key=lambda k: k[0], reverse=True)

    def find_possible_locations(self) -> list:
        """ Returns possible locations in a list of lists. """

        possible_locations = [
            self.central_locations(),
            self.edges()
        ]
        return possible_locations
