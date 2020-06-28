a = int(input())
b = int(input())
h = int(input())

if a <= h <= b:
    print('Normal')
elif a > h:
    print('Deficiency')
else:
    print('Excess')
