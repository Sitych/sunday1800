def bubble_sort (a):
    for i in range(len(a)):
        for i in range(0,len(a)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
    return a
a = bubble_sort(a)
print(a)
