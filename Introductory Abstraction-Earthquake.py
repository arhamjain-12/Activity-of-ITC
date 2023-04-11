
"""
Earthquake Impact: Input some numbers, do some simple arithmetic, output results.
"""
def Earthquake_Impact(A):
    if A<2:
        return "Micro Earthquake"
    elif 2<=A<3:
        return "Very Minor Earthquake"
    elif 3<=A<4:
        return "Minor Earthquake"
    elif 4<=A<5:
        return "Light Earthquake"
    elif 5<=A<6:
        return "Moderate Earthquake"
    elif 6<=A<7:
        return "Strong Earthquake"
    elif 7<=A<8:
        return "Major Earthquake"
    else:
        return "Great Earthquake"
print(Earthquake_Impact(5))