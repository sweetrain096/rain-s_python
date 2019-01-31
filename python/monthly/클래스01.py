class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x
    def sety(self, y):
        self.y = y
    def get(self):
        return self.x, self.y
    def move(self, dx, dy):
        self.dx = dx
        self.dy = dy
        return self.x + self.dx, self.y + self.dy


p1 = Point(3, 3)
print(p1.get())

p1.setx(5)
p1.sety(7)
print(p1.get())

print(p1.move(2, 1))