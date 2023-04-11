
"""
Arithmetic: Input some numbers, do some simple arithmetic, output results.
"""
a=int(input())
b=int(input())
def add(a,b):
    c=a+b
    return c
print("Addition:",add(a,b))
def subtract(a,b):
    c=a-b
    return c
print("Subtraction:",subtract(a,b))
def multiply(a,b):
    c=a*b
    return c
print("Multiplication:",multiply(a,b))
def divide(a,b):
    c=a/b
    return c
print("Division:",divide(a,b))
def power(a,b):
    c=a**b
    return c
print("Power:",power(a,b))
def remainder(a,b):
    c=a%b
    return c
print("Remainder:",remainder(a,b))
def floor_division(a,b):
    c=a+b
    return c
print("Floor division:",floor_division(a,b))