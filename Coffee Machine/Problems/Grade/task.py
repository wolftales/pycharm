a = float(input())
b = float(input())

score = (a / b) * 100

if score < 60.0:
    print("F")
elif score >= 60.0 and score < 70.0:
    print("D")
elif score >= 70.0 and score < 80.0:
    print("C")
elif score >= 80.0 and score < 90.0:
    print("B")
else:
    print("A")