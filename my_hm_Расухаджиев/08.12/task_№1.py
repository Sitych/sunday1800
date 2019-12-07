x1 = int()
y1 = int()
x2 = int()
y2 = int()
def distance(x1, y1, x2, y2):
    return ((x2-x1)**2+(y2-y1))**0.5
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
print(distance(x1, y1, x2, y2))