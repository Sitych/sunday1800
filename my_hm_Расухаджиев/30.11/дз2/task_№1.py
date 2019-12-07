n = int(input())
a = float(0.5)
b = float(0.5)
c = float(0.5)
k = 0
q = 0
pirog = 1
for i in range (0,9999):
    if pirog >= n:
        a = q
        break
    else:
        pirog = pirog * 2
        q = q+1
pirog = 1
q = 0
for i in range (0,9999):
    k = 1.5*n 
    if k/2>k//2:
        k=k+0.5
        if pirog >= k:
            b = q
        else:
            pirog = pirog * 2
            q=q+1
pirog = 1
q = 0
for i in range (0,9999):
    if pirog >= n+10:
        c = q
        break
    else:
        pirog = pirog * 2
        q=q+1
print(a, b, c)