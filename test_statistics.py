"""
Unit tests for the statistics module.

Tests the variance and standard deviation functions with typical values,
non-integer values, and edge cases.
"""

from unittest import TestCase
from statistics import variance, stdev


class StatisticsTest(TestCase):

    def test_variance_typical_values(self):
        """Test variance with typical values."""
        self.assertAlmostEqual(0.0, variance([10.0, 10.0, 10.0, 10.0, 10.0]), places=7)
        self.assertAlmostEqual(2.0, variance([1, 2, 3, 4, 5]), places=7)
        self.assertAlmostEqual(8.0, variance([10, 2, 8, 4, 6]), places=7)

    def test_variance_non_integers(self):
        """Test variance with decimal values."""
        self.assertAlmostEqual(4.0, variance([0.1, 4.1]), places=7)
        self.assertAlmostEqual(8.0, variance([0.1, 4.1, 4.1, 8.1]), places=7)

    def test_stdev(self):
        """Test standard deviation calculation."""
        self.assertEqual(0.0, stdev([10.0]))
        self.assertAlmostEqual(2.0, stdev([1, 5]), places=7)
        self.assertAlmostEqual(stdev([0, 0.5, 1, 1.5, 2]), sqrt(0.5), places=7)


if __name__ == '__main__':
    import unittest
    unittest.main(verbosity=1)
