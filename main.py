from similarity_function import SimpleEquality, InvaderEquality
from input import TextInput
from spacesignal import SpaceSignal
from location_finder import LocationFinder

""" 
This is a simple demonstration of how the program works. 
We first get the row input from a text file for both invaders and radar. 
Then we develop the radar signal (numpy array) and choose a similarity function to use.
Finally we build a location finder using the previous classes + an expected accuracy score.
We use the location finder to find the possible locations in the radar.
"""

invader_1 = TextInput('Invaders/AntInvader.txt')
invader_2 = TextInput('Invaders/JellyInvader.txt')
radar_input = TextInput('Radars/RadarSample.txt')

ant = SpaceSignal(invader_1.rows, invader_1.cols, invader_1.row_signal)
jellyfish = SpaceSignal(invader_2.rows, invader_2.cols, invader_2.row_signal)
amazing_radar = SpaceSignal(radar_input.rows, radar_input.cols, radar_input.row_signal)

simple_similarity_fn = SimpleEquality()
simple_accuracy = 0.75
simple_location_finder = LocationFinder(ant, amazing_radar, simple_similarity_fn, simple_accuracy)

better_similarity_fn = InvaderEquality()
better_accuracy = 0.85
better_location_finder = LocationFinder(jellyfish, amazing_radar, better_similarity_fn, better_accuracy)

find_ant = simple_location_finder.find_possible_locations()
find_jelly = better_location_finder.find_possible_locations()

print(find_ant)
print('----------------------------------------------------------------------')
print(find_jelly)
