import unittest
from similarity_function import SimpleEquality, InvaderEquality
from numpy import array


class TestSimilarityFunction(unittest.TestCase):

    def test_simple_equality(self):
        simple_equality = SimpleEquality()
        self.assertEqual(simple_equality.similarity_comparison(array([[0, 1], [1, 0]]), array([[0, 1], [1, 0]])), 1.0)
        self.assertEqual(simple_equality.similarity_comparison(array([[0, 1], [1, 0]]), array([[1, 1], [1, 0]])), 0.75)

    def test_invader_equality(self):
        invader_equality = InvaderEquality()
        self.assertEqual(invader_equality.similarity_comparison(array([[0, 1], [1, 0]]), array([[0, 1], [1, 0]])), 1.0)
        self.assertEqual(invader_equality.similarity_comparison(array([[0, 1], [1, 0]]), array([[1, 1], [1, 0]])), 1.0)


unittest.main()
