from numpy import array, sum
from abc import ABC, abstractmethod


class SimilarityFunction(ABC):
    """Other formulas for distances: https://docs.eyesopen.com/toolkits/python/graphsimtk/measure.html"""

    @abstractmethod
    def similarity_comparison(self, invader_signal: array, radar_signal: array) -> float:
        pass


class SimpleEquality(SimilarityFunction):
    def similarity_comparison(self, invader_signal: array, radar_signal: array) -> float:
        return sum(invader_signal == radar_signal) / invader_signal.size


class InvaderEquality(SimilarityFunction):
    def similarity_comparison(self, invader_signal: array, radar_signal: array) -> float:
        """ formula: bothAB / sumA """
        total = 0
        for i in range(invader_signal.shape[0]):
            for j in range(invader_signal.shape[1]):
                if invader_signal[i][j] > 0 and invader_signal[i][j] == radar_signal[i][j]:
                    total += 1
        return total / invader_signal.sum()
