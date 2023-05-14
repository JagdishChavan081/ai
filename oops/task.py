# Q-1 Rectangle Class
# Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.
# Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
# author: Jagdish Chavan


class Rectangle:
    """Rectangle class allows user to build a rectangle ith length and width attribute
    Rectangle class includes Premiter() method to calculate perimiter of the rectangle
    & Area method to calculate the area of the rectang with display method to print output
    """

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        Perimeter = 2 * (self.length + self.width)
        return Perimeter

    def area(self):
        area = self.length * self.width
        return area

    def display(self):
        print("The Length of rectangle is", self.length)
        print("The width of rectangle is", self.width)
        print("Perimiter of Rectanggle is:", self.Perimeter())
        print("Area of Rectanggle is: ", self.area())


# input
my_rectangle = Rectangle(3, 4)
my_rectangle.display()
