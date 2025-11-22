#!/usr/bin/python3
"""
4-square Module

"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size (side length) of the square (private).
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the new square. Defaults to 0.
        """
        self.size = size  # Calls the property setter

    @property
    def size(self):
        """
        Retrieves the size of the square. (The Getter method)

        Returns:
            int: The value of the private size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation. (The Setter method)

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the current area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square to stdout using the character '#'.

        If the size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
