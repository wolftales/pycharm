x = float(input())
y = float(input())

if x > 0:
    if y > 0:
        print("I")
    elif x > 0 > y:
        print("IV")
    elif x < 0 < y:
        print("II")
    else:
        print("III")
elif x > 0 > y:
    print("IV")
elif x < 0 < y:
    print("II")
else:
    print("III")
