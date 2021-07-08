from numpy import array, sum
from abc import ABC, abstractmethod


class SimilarityFunction(ABC):
    """ Functions to return a possible score from 0.0 to 1.0
    Other formulas for distances: https://docs.eyesopen.com/toolkits/python/graphsimtk/measure.html"""

    @abstractmethod
    def similarity_comparison(self, invader_signal: array, radar_signal: array) -> float:
        raise NotImplementedError


class SimpleEquality(SimilarityFunction):
    """ Checks how many elements in the same location of two arrays are the same and gets a score"""
    def similarity_comparison(self, invader_signal: array, radar_signal: array) -> float:
        return round(sum(invader_signal == radar_signal) / invader_signal.size, 3)


class InvaderEquality(SimilarityFunction):
    def similarity_comparison(self, invader_signal: array, radar_signal: array) -> float:
        """ Checks how many times both arrays have a "1" in the same location of the array. formula: bothAB / sumA """
        total = 0
        for i in range(radar_signal.shape[0]):
            for j in range(radar_signal.shape[1]):
                if invader_signal[i][j] > 0 and invader_signal[i][j] == radar_signal[i][j]:
                    total += 1
        return round(total / invader_signal.sum(), 3) if total != 0 else 0.0
