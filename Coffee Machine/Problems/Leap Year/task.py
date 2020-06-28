# put your python code here
year = int(input())

if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print("Leap\n")
    else:
        print("Ordinary\n")
else:
    print("Ordinary\n")
