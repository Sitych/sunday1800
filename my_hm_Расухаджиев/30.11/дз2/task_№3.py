n = 1000
a = n
for i1 in range (0,999):
    if a*0.02>=30:
        break 
    a = a+(0.02*a)
a=n
for i2 in range (0,999):
    a = a+0.02*a   
    if a>1200:
        break
print("за",i1,"месяц","," ,'через',i2,'месяцев')