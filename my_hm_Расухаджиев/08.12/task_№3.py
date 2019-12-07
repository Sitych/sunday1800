x = int(input())
if x <= -12:
    y = -1*(x**2)
elif -12< x <0:
    y = x**4
elif x>=0:
    y = x-2
print(y)