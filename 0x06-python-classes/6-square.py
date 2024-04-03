#!/usr/bin/python3
"""
Module: 6-square
"""


class Square:
    """
    Defines a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the Square instance.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0 or any element of position is less than 0.

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The position of the square.

        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If any element of value is less than 0.

        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the '#' character.

        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
