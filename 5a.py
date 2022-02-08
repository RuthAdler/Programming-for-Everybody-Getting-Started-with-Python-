hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
if h<=40:
    a=h*r
    print(a)
elif h>40:
    b=h-40
    c=r*1.5
    d=h-b
    print(d*r+b*c)

