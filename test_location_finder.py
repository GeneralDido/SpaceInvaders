import unittest
from input import TextInput
from spacesignal import SpaceSignal
from location_finder import LocationFinder
from similarity_function import SimpleEquality
import numpy as np  # pragma: no cover


class TestLocationFinder(unittest.TestCase):

    def test_central_locations(self):
        invader_input = TextInput('tests/Invaders/InvaderSimple.txt')
        invader = SpaceSignal(invader_input.rows, invader_input.cols, invader_input.row_signal)
        radar_input = TextInput('tests/Radars/RadarSimple.txt')
        radar = SpaceSignal(radar_input.rows, radar_input.cols, radar_input.row_signal)
        similarity_fn = SimpleEquality()

        location_finder = LocationFinder(invader, radar, similarity_fn, 1.0)
        find_location = location_finder.central_locations()

        self.assertEqual(find_location[0][0], 1.0)
        np.testing.assert_array_equal(find_location[0][1], np.array([[0, 1, 0], [0, 1, 0]]))
        self.assertEqual(find_location[0][2], 0)  # alien array starts at row 0
        self.assertEqual(find_location[0][3], 0)  # alien array starts at col 0

    def test_no_alien_signal(self):
        invader_input = TextInput('tests/Invaders/InvaderSimple.txt')
        invader = SpaceSignal(invader_input.rows, invader_input.cols, invader_input.row_signal)
        radar_input = TextInput('tests/Radars/Radar_no_signal.txt')
        radar = SpaceSignal(radar_input.rows, radar_input.cols, radar_input.row_signal)
        similarity_fn = SimpleEquality()

        location_finder = LocationFinder(invader, radar, similarity_fn, 1.0)
        find_location = location_finder.find_possible_locations()

        self.assertEqual(find_location, [[], []])

    def test_edges_center(self):
        similarity_fn = SimpleEquality()
        invader_input = TextInput('tests/Invaders/Invader2x2.txt')
        invader = SpaceSignal(invader_input.rows, invader_input.cols, invader_input.row_signal)
        radar_input = TextInput('tests/Radars/RadarUpDownLeftRight.txt')
        radar = SpaceSignal(radar_input.rows, radar_input.cols, radar_input.row_signal)
        location_finder = LocationFinder(invader, radar, similarity_fn, 1.0)
        find_central_locations = location_finder.edges()

        self.assertEqual(find_central_locations[0][0], 1)
        np.testing.assert_array_equal(find_central_locations[0][1], np.array([[1, 1]]))
        self.assertEqual(find_central_locations[0][2], 0)
        self.assertEqual(find_central_locations[0][3], 1)

        self.assertEqual(find_central_locations[1][0], 1)
        np.testing.assert_array_equal(find_central_locations[1][1], np.array([[1], [1]]))
        self.assertEqual(find_central_locations[1][2], 1)
        self.assertEqual(find_central_locations[1][3], 3)

        self.assertEqual(find_central_locations[2][0], 1)
        np.testing.assert_array_equal(find_central_locations[2][1], np.array([[1, 1]]))
        self.assertEqual(find_central_locations[2][2], 3)
        self.assertEqual(find_central_locations[2][3], 1)

        self.assertEqual(find_central_locations[3][0], 1)
        np.testing.assert_array_equal(find_central_locations[3][1], np.array([[1], [1]]))
        self.assertEqual(find_central_locations[3][2], 1)
        self.assertEqual(find_central_locations[3][3], 0)


if __name__ == '__main__':
    unittest.main()
