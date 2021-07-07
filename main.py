import similarity_function
from input import TextInput
from spacesignal import SpaceSignal
from location_finder import LocationFinder


invader_1 = TextInput('Invaders/AntInvader.txt')
invader_2 = TextInput('Invaders/JellyInvader.txt')
radar_input = TextInput('Radars/RadarSample.txt')

ant = SpaceSignal(invader_1.rows, invader_1.cols, invader_1.row_signal)
jellyfish = SpaceSignal(invader_2.rows, invader_2.cols, invader_2.row_signal)
amazing_radar = SpaceSignal(radar_input.rows, radar_input.cols, radar_input.row_signal)

simple_similarity_fn = similarity_function.SimpleEquality()
simple_location_finder = LocationFinder(0.75)

better_similarity_fn = similarity_function.InvaderEquality()
better_location_finder = LocationFinder(0.85)

find_ant = simple_location_finder.find_all_cases(ant, amazing_radar, simple_similarity_fn)
find_jelly = better_location_finder.find_all_cases(jellyfish, amazing_radar, better_similarity_fn)

print(find_ant)
print('----------------------------------------------------------------------')
print(find_jelly)

# TODO: 1. write tests 2. write documentation 3. (possible) video
""" 
When testing, test for:
- normal circumstances
- empty arrays 
- arrays < invader arrays
- corrupt input files
- edges should be at least 50% 
- edges up down left right
- 100% accuracy
- 0% accuracy
"""
