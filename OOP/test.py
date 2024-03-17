# class Rectangle:
#     '''Docstring text here'''
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
#
#     def perimeter(self):
#         return 2 * (self.width + self.length)
#
#
# obj1 = Rectangle(3, 5)
# print(obj1.perimeter())
# print(Rectangle.perimeter(obj1))


# class Shape:
#     def __init__(self, color):
#         self.color = color
#
#
#     def say_hi(self):
#         print(f'I am a shape with {self.color} color')
#
#
# class Quadrangle(Shape):
#     pass
#
#
# s1 = Shape('red')
# s1.say_hi()
# q1 = Quadrangle('blue')
# q1.say_hi()

# class Shape:
#     def __init__(self, color):
#         self.color = color
#
#     def say_hi(self):
#         print(f'Iam a shape with {self.color} color')
#
# class Quadrangle(Shape):
#     def __init__(self, a, b, c, d, color):
#         super().__init__(color)
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#     def say_hi(self):
#         print(f'Iam a quadrangle with {self.color} color')
#
# s1 = Shape('red')
# s1.say_hi()
# q1 = Quadrangle('blue')
# q1.say_hi()


class Shape:
    def __init__(self, color):
        self.color = color
    def say_hi(self):
        print(f'Iam a shape with {self.color} color')
class Quadrangle(Shape):
    def __init__(self, a, b, c, d, color):
        super().__init__(color)
        self.a, self.b, self.c, self.d = a, b, c, d
    def say_hi(self):
        print(f'Iam a quadrangle with {self.color} color')
class Triangle(Shape):
    pass
class Rectangle(Quadrangle):
    def __init__(self, a, b, color):
        Shape.__init__(self, color)
        self.a = a
        self.b = b
s1 = Shape('red')
s1.say_hi()
q1 = Quadrangle(4, 2, 1, 6, 'blue')
q1.say_hi()
r1 = Rectangle(1, 5, 'black')
r1.say_hi()
t1 = Triangle('green')
t1.say_hi()




print(isinstance(q1, Shape))      #Output: True
print(isinstance(q1, Quadrangle))  #Output: True
print(isinstance(q1, object))    #Output: True
print(isinstance(5, int))        #Output: True
print(isinstance(5, object))        #Output: True

print(issubclass(Shape, object))    #Output: True
print(issubclass(Quadrangle, Shape))  #Output: True
print(issubclass(Shape, Quadrangle))   #Output: False
print(issubclass(int, object))       #Output: True
print(issubclass(bool, int))        #Output: True


class Left:
    def call(self):
        print("Left")

class Right:
    def call(self):
        print("Right")

class Bottom(Left, Right):
    pass


obj = Bottom()
obj.call()