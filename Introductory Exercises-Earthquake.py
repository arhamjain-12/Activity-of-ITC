
"""
Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)
"""
A = float(input("Enter magnitude of Earthquake: "))

if A<2:
    print("Micro Earthquake")
elif 2<=A<3:
    print("Very Minor Earthquake")
elif 3<=A<4:
    print("Minor Earthquake")
elif 4<=A<5:
    print("Light Earthquake")
elif 5<=A<6:
    print("Moderate Earthquake")
elif 6<=A<7:
    print("Strong Earthquake")
elif 7<=A<8:
    print("Major Earthquake")
else:
    print("Great Earthquake")