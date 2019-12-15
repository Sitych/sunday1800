class Box:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def cubes(self):
        for i in range(0,9999):
            if ((self.a*self.b*self.c)-(8*i))<8:
                return i
figure = Box(int(input()), int(input()), int(input()))
print(figure.cubes())