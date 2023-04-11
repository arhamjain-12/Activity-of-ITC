
"""
Arithmetic: Input some numbers, do some simple arithmetic, output results (Python3)
"""

n=int(input())
a=int(input())
b=int(input())
if n==1:
    print(a+b)
elif n==2:
    print(a-b)
elif n==3:
    print(a*b)
elif n==4:
    print(a/b)
elif n==5:
    print(a%b)
elif n==6:
    print(a//b)
elif n==7:
    print(a**b)
else:
    print('Invalid Input')