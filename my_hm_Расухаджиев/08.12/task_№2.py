fib1 = 0
fib2 = 1
mass=[1, 2, 3, 4, 5]
a=int()
b=int()
c=int()
x=int()
def fun_task_3(a,b=0,c=0):
    a,c=c,a
    if (a!=0 and b!=0) or (a != 0 and c!=0):
        c, a=a, c
    elif a!=0 and b!=0 and c!=0:
        x = c
        return x
    else: 
        x = 1
        return x
    for i in range(0,5):
        if x == mass[i]:
            if x == 1:
                for q in range(0,c):
                    n = q**2
                print(n,end=','+" ")
            if x == 2:
               for q in range (0,c):
                   n= q**3
                   print(n,end=','+" ")
            if x == 3:
               for q in range(0,c):
                   n = q**0,5
                   print(n,end=','+" ")
            if x == 4:
               for q in range(0,c):
                   break
            if x == 5:
               for q in range(a,c):
                   fib1, fib2 = fib2, fib1 + fib2
                   print(fib2, end=','+" ")
print(fun_task_3(1,5,2))