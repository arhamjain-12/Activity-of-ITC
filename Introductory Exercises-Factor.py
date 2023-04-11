
"""
Factor:  Calculate temperature that a person feels because of the wind (Python3)
"""
A=float(input('Input air temperature in degree celsius: '))
B=float(input('Input wind speed in km/h: '))
C = 13.12 + 0.6215 * A * (0.3965 * A - 11.37) * (B**0.16)
print(C)