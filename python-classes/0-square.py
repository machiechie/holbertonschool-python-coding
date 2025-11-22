#!/usr/bin/python3
"""0-square module
Defines a class Square with a private size attribute.
"""

class Square:
"""Represents a square with a private size attribute."""

def __init__(self, size):
    """Initialize a new Square instance.

    Args:
        size (int): The size of the square.
    """
    self.__size = size
