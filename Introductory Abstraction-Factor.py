
"""
Factor:  Calculate temperature that a person feels because of the wind.
"""
def factor(A,B):
    C = 13.12 + 0.6215 * A * (0.3965 * A - 11.37) * (B**0.16)
    return C
factor(1,2)
Footer