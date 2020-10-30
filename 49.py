class Shape(object):
    def __init__(self):
        pass

    def Area(self):
        return 0

class Square(Shape):
    def __init__(self, length = 0):
        Shape.__init__(self)
        self.length = length

    def Area(self):
        return (self.length * self.length)

print(Square(5).Area())






