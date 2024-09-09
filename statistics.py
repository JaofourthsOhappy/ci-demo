"""
Module for statistical calculations.

This module includes functions to calculate the average, variance,
and standard deviation of a list of numeric values.
"""

import math  # Import the math module for sqrt


def average(data):
    """Calculate the average of a list of numeric values.

    Raise ValueError if the list is empty.

    :param data: List of numeric values.
    :return: The average of the values.
    """
    if len(data) == 0:
        raise ValueError("List must contain at least one value")
    return sum(data) / len(data)


def variance(data):
    """Calculate the population variance of a list of numbers.

    The variance is the sum of squared differences between data values
    and their mean, divided by the number of items in the list.

    :param data: List of numbers for which variance will be computed.
           Must contain at least one element.
    :return: Population variance of values in data list.
    :raises ValueError: If the data parameter is empty.
    """
    n = len(data)
    if n == 0:
        raise ValueError("List must contain at least one value")
    avg = average(data)
    return sum([(x - avg) ** 2 for x in data]) / n


def stdev(data):
    """Calculate the standard deviation of a list of values.

    Uses the square root of the variance.

    :param data: List of numeric values.
    :return: Standard deviation of the values.
    """
    return math.sqrt(variance(data))
