#!/usr/bin/python3
"""
import from the base class
"""
from models.base import Base

"""
class rectangle that inherits from Base
"""


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
        Initializes a Rectangle instance.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
                     Default is 0.
            y (int): The y-coordinate of the rectangle's position.
                     Default is 0.
            id: The ID of the rectangle. Default is None.

        Returns:
            None
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): The new value for the width.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format("width"))
        if value <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.__width = value
        if value is None:
            raise TypeError("{} must be an integer".format("width"))

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): The new value for the height.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format("height"))
        if value <= 0:
            raise ValueError("{} must be > 0".format("height"))
        self.__height = value

    @property
    def x(self):
        """
        Getter method for the x attribute.

        Returns:
            int: The x-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x attribute.

        Args:
            value (int): The new value for the x-coordinate.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format("x"))
        if value < 0:
            raise ValueError("{} must be >= 0".format("x"))
        self.__x = value

    @property
    def y(self):
        """
        Getter method for the y attribute.

        Returns:
            int: The y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y attribute.

        Args:
            value (int): The new value for the y-coordinate.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format("y"))
        if value < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__y = value

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        print the rectangle with the character #
        """
        for _ in range(self.__y):
            print()
        for i in range(self.height):
            for _ in range(self.__x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """
        returns a string representation of the rectangle
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -"\
               f" {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        updates the attributes of the rectangle
        if *args exist and is not empty: **kwargs must be skipped
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        if len(args) > 1:
            self.id = args[0]
        if len(args) > 2:
            self.__width = args[1]
        if len(args) > 3:
            self.__height = args[3]
        if len(args) > 4:
            self.__x = args[4]
        if len(args) > 5:
            self.__y = args[5]

    def to_dictionary(self):
        """
        returns the dictionary representation of the rectangle
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
