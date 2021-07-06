import similarity_function
from input import TextInput
from spacesignal import SpaceSignal
from location_finder import LocationFinder


invader_1 = TextInput('Invaders/AntInvader.txt')
invader_2 = TextInput('Invaders/JellyInvader.txt')
radar_input = TextInput('Radars/RadarSample.txt')

ant = SpaceSignal(8, 11, invader_1.signal)
jellyfish = SpaceSignal(8, 8, invader_2.signal)
amazing_radar = SpaceSignal(50, 100, radar_input.signal)

simple_similarity_fn = similarity_function.SimpleEquality()
simple_location_finder = LocationFinder(0.75)

better_similarity_fn = similarity_function.InvaderEquality()
better_location_finder = LocationFinder(0.85)

find_ant = simple_location_finder.find_possible_locations(ant, amazing_radar, simple_similarity_fn)
find_jelly = better_location_finder.find_possible_locations(jellyfish, amazing_radar, better_similarity_fn)

print(find_ant)
print('----------------------------------------------------------------------')
print(find_jelly)

# TODO: 1. edge cases 2. write tests 3. write documentation 4. (possible) improve code 5. (possible) video
""" 
When testing, test for:
- normal circumstances
- empty arrays 
- arrays < invader arrays
- corrupt input files
- edges should be at least 50% 
- 100% accuracy
- 0% accuracy
"""
