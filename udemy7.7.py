#Example

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point x={self.x}, y={self.y}'
p = Point(3, 4)
print(p)

class Road():
    def __init__(self, lenght):
        self.lenght = lenght

    def __len__(self):
        return self.lenght

    def __str__(self):
        return f'A road of lenght:{self.lenght}'

    def __del__(self):
        print(f'The road has been destroyed')

r = Road(100)
len(r)
print(r)
