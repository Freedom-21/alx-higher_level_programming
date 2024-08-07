#!/usr/bin/python3
"""Task 1, Defining a Real Rectangle"""

class Rectangle:
    """Class Rectangle that defines a rectangle by its width and height.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        """

    def __init__(self, width=0, height=0):

        """Initialize a new Rectangle"""

        self.width = width
        self.height = height

    @property
    def width(self):

        """Get the width of the rectangle."""

        return self.__width

    @width.setter
    def width(self, value):

        """Set the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.

        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""

        return self.__height

    @height.setter
    def height(self, value):

        """Set the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.

        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
