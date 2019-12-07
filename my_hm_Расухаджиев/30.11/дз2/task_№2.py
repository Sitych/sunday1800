a = 1
n = int(0)
i= int()
c = 5**0.5
while a!= 0:
    x=1/c*(((1+c)/2)**(n+1)-((1-c)/2)**(n+1))
    fib1 = 0
    fib2 = 1
    for i in range(2, n):
         fib1, fib2 = fib2, fib1 + fib2
    if (x-fib2) >=  0.001:
        print(n)
        break
    else:
        n=n+1