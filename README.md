# SpaceInvaders

This is a project to demonstrate the understaning of the Python programming language and OOP principles. 

In separate files we have a radar signal and an invader signal. 

The Python app takes input from those text files, and returns possible locations of the invaders. 

### Example of invaders:

~~~~
--o-----o--
---o---o---
--ooooooo--
-oo-ooo-oo-
ooooooooooo
o-ooooooo-o
o-o-----o-o
---oo-oo---
~~~~

~~~~
---oo---
--oooo--
-oooooo-
oo-oo-oo
oooooooo
--o--o--
-o-oo-o-
o-o--o-o
~~~~


### Example radar sample:
~~~~
----o--oo----o--ooo--ooo--o------o---oo-o----oo---o--o---------o----o------o-------------o--o--o--o-
--o-o-----oooooooo-oooooo---o---o----o------ooo-o---o--o----o------o--o---ooo-----o--oo-o------o----
--o--------oo-ooo-oo-oo-oo-----O------------ooooo-----oo----o------o---o--o--o-o-o------o----o-o-o--
-------o--oooooo--o-oo-o--o-o-----oo--o-o-oo--o-oo-oo-o--------o-----o------o-ooooo---o--o--o-------
------o---o-ooo-ooo----o-----oo-------o---oo-ooooo-o------o----o--------o-oo--ooo-oo-------------o-o
-o--o-----o-o---o-ooooo-o-------oo---o---------o-----o-oo-----------oo----ooooooo-ooo-oo------------
o-------------ooooo-o--o--o--o-------o--o-oo-oo-o-o-o----oo------------o--oooo--ooo-o----o-----o--o-
--o-------------------------oo---------oo-o-o--ooo----oo----o--o--o----o--o-o-----o-o------o-o------
-------------------o----------o------o--o------o--------o--------o--oo-o-----oo-oo---o--o---o-----oo
----------o----------o---o--------------o--o----o--o-o------------oo------o--o-o---o-----o----------
------o----o-o---o-----o-o---o-----oo-o--------o---------------------------------o-o-o--o-----------
---------------o-------o-----o-------o-------------------o-----o---------o-o-------------o-------oo-
-o--o-------------o-o-----o--o--o--oo-------------o----ooo----o-------------o----------oo----o---o-o
-o--o-------------o----oo------o--o-------o--o-----o-----o----o-----o--o----o--oo-----------o-------
-o-----oo-------o------o----o----------o--o----o-----o-----o-------o-----------o---o-o--oooooo-----o
-o--------o-----o-----o---------oo----oo---o-o---------o---o--oooo-oo--o-------o------oo--oo--o-----
------------o---------o---------o----oooo-------------oo-oo-----ooo-oo-----o-------o-oo-oooooooo---o
----------------------o------------oooooooo---o-----o-------o--oooooo-o------------o-o-ooooooo-o----
------------o------o---o---o-------oo-oo--o--o---------o--o-o-o-ooooo-o--------------oo-o----o-oo-o-
---o-o----------oo-------oo----o----oooooooo-------o----o-o-o-o-----o-o-----o----------ooo-oo--o---o
-o-o---------o-o---------------o--o--o--ooo---ooo-------o------oo-oo------------o--------o--o-o--o--
-------oo---------------------------o-oo----------o------o-o-------o-----o----o-----o-oo-o-----o---o
---o--------o-----o-------o-oo-----oo--oo-o----oo----------o--o---oo------oo----o-----o-------o-----
---o--ooo-o---------o-o----o------------o---------o----o--o-------o----o--------o----------------oo-
---o------o----------------o----o------o------o---oo-----------o-------------o----------oo---------o
--oo---------------o--o------o---o-----o--o-------------o------o-------o-----o-----o----o------o--o-
-o-------o----------o-o-o-------o-----o--o-o-----------o-oo-----------o------o---------o-----o-o----
----------o----o-------o----o--o------o------------o---o---------------oo----o-----ooo--------------
----o--------oo----o-o----o--o------ooo----o-oooo---o--o-oo--------o-oo-----o-o---o-o--o-----oo-----
------o--------o-ooooo----o---o--o-----o---------------o-o-------o-----o----------------------------
o-------oo----o--oooooo-o---o--o------oooo----------o-oo-------o---o----------o------oo-------------
-o---o----------o--oo-oo-o---o-----o-o-----------------------oo--o------o------o--------------------
-----oo-o-o-o---ooooooooo----o----o--------o--o---oo---o------------o----------o-o---o------o-o--oo-
------o------o---ooo-o---------------------------o--o---o---o----o--o-------o-----o------o----o----o
-------o----------ooo-o-----o----o---o--o-oo--o--o-o--o------o--o-oo---ooo------------------------o-
-o-------o------o-o--ooo--o---o---oo-----o----o-------------o----o-ooo-o------o--o-o------o-o-------
---oo--o---o-o---------o---o--------------o--o-----o-------o-----o--o---o-oo--------o----o----o-----
o------o----oo-o-----------oo--o---o--------o-o------o-------o-o------o-oo---------o-----oo---------
----o--o---o-o-----------o---o------------o-------o----o--o--o--o-o---------------o-----------------
-------oo--o-o-----o-----o----o-o--o----------------------o-------o------o----oo----ooo---------o---
o-----oo-------------------o--o-----o-----------o------o-------o----o-----------o----------------o--
--o---o-------o------------o--------------------o----o--o-------------oo---o---------oo--------o----
--o--------o---------o------------o------o-------o------------o-------o---o---------ooooo-----------
------o--------------o-o-o---------o---o-------o--o-----o-------o-o----------o-----oo-ooo----------o
--o---------------o----o--oo-------------o---------o-------------------oo---------oo-o-ooo----------
-o-----------o------ooo----o----------------ooo-----o--------o--o---o-----------o-o-oooooo--------oo
-o---o-------o---o-oooo-----o-------------------o----oo-----------------o--o--------o--o------o--o--
-------o---o------oooooo--o----ooo--o--------o-------o----------------------------oo-oo-o--o--------
o--oo------o-----oo--o-oo------------oo--o------o--o-------------oo----o------------oooo-o------oo--
-----o----------ooooooooo--------------oo--------------oo-----o-----o-o--o------o----------o----o---
~~~~

### Example of one Output location

```python 
[0.909, array([[0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0],
       [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0],
       [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1],
       [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
       [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
       [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0]]), 13, 60]
```

0.909 is the expected accuracy score based on a comparison function between arrays from the invader signal and a sub-matrix of the radar signal. 

The array is a numpy array containing the possible location. (13,60) are the possible coordinates (rows,cols) in the radar sample.

## Classes

For this project I developed 3 main classes, and a helper class. 

## TextInput 

This is a helper class to get the signal as well as rows and cols from a text file. 

In a hypothetical scenario where we would like to add another input method, we can make a new class (and possibly a superclass). 

As a result, we have a helper class that is separate from other classes, has one purpose, is extendable and does not intervene in any way with the main classes.

## SpaceSignal

This class represents a space signal, which can be representated by a numpy array, as well as rows and columns of the array for convenience.

Although we could have made different classes for SpaceInvaders and Radar, both can be represented from this main class, as they have the exact same characteristics. 

In a scenario where something was to change in SpaceInvaders or Aliens, we can easily develop separate classes that inherit from the main class.

### Methods

```python 
def make_array(seq: str, list_len: int) → numpy.array
```

This is a static method to be used in the initialization. There, we develop a numpy array from the row string input from TextInput.


## SimilarityFunction (Abstract Class)

This is an abstract class to develop classes that compare two signals, i.e. two numpy arrays.

### Methods
```python
def similarity_comparison(self, invader_signal: numpy.array, radar_signal: numpy.array) -> float
```

Every class that inherits from the Abstract class, can implement this method differently. 

As such, if in the future we decide that there is a better way to compare the two signals, we can easily develop a new class without having to worry about any conflicts with other classes.

To demonstrate this, I developed two classes, SimpleEquality and InvaderEquality that both inherit from the abstract class and get a similarity value in a slightly different way.

```python 
class SimpleEquality(SimilarityFunction)
"""Checks how many elements in the same location of two arrays are the same and returns a score"""
```
```python 
class InvaderEquality(SimilarityFunction)
"""Checks how many times both arrays have a "1" in the same location of the array. formula: bothAB / sumA"""
```

## LocationFinder

The LocationFinder class finds the possible locations of the invaders and returns them in a list of lists. 

To achieve this, we need to use the other 2 classes (SpaceSignal and SimilarityFunction), to get an alien signal, a radar signal and a similarity function. 
Then the objective is to traverse the matrix and compare sub-matrices of the main radar signal to the alien signal. Then get the best signals based on a predefined *accuracy* from the user. 

As such, we can develop different LocationFinders with different projected accuracies.

The object gets an invader signal, a radar signal, and a similarity function and returns a list of locations based on the accuracy score.

### Methods

```python
def central_locations(self) -> list 
    """Finds possible locations with the full invader array, while traversing the radar array. """
```
This is the main method that traverses the array in the matrix. It compares the whole alien signal starting from the beginning of the radar matrix and traversing through the end of it.
Every time it calculates the score, the radar sub-matrix and the starting location and insets it in a list. In the end, it filters the list based on the *accuracy* score.

```python
def edges(self) -> list
```

This function is for the edge cases (note: starting with the full rows of the invader signal). 

It traverses the edges of the radar array, starting from col 1 up to col n-1. 
It then inserts new invader array rows in each iteration up to n-1 invader rows. 

It does this for 4 times, each time rotating the signal and invader matrices by 90 degrees. 

It then finds the correct coordinates of the returned radar signal and it rotates the sub-matrix again to return it in its standard position.

To find the correct coordinates and to return the signal matrix, we use two sub-functions inside the main edges function.

```python
def rotate_signal(signal: array, n) -> array
""" Rotates signal n times, n: number of current rotations """

def correct_coordinates(num_inversions: int, coordinate: int, radar_rows: int,
                                radar_cols: int, invader_cols: int) -> (int, int)
 """ Develops the right coordinates when rotating the invader and radar arrays by 90 degrees each time."""
```

## Example

*main.py* provides an example usage. 

We can get an invader from TextInput and a signal from TextInput and develop them through the SpaceSignal class. 

We also get a SimilarityFunction and a LocationFinder. Then we use the LocationFinder to get the possible locations.

```python
invader_1 = TextInput('Invaders/AntInvader.txt')
radar_input = TextInput('Radars/RadarSample.txt')

ant = SpaceSignal(invader_1.rows, invader_1.cols, invader_1.row_signal)
amazing_radar = SpaceSignal(radar_input.rows, radar_input.cols, radar_input.row_signal)

simple_similarity_fn = SimpleEquality()
simple_accuracy = 0.75
simple_location_finder = LocationFinder(ant, amazing_radar, simple_similarity_fn, simple_accuracy)

find_ant = simple_location_finder.find_possible_locations()
print(find_ant)
```
