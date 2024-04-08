#!/usr/bin/python3
""" Task 7, Change Represenation """

class Rectangle:
    """Defines a rectangle."""
    
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize width, height, and increment number_of_instances."""
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width, validate type and value."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height, validate type and value."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter or 0 if width or height is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return printable representation using `print_symbol`."""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join([symbol * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return string representation to recreate the rectangle."""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """Print a message upon instance deletion and decrement number_of_instances."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
