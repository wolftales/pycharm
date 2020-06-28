A = int(input())
B = int(input())
H = int(input())

if A <= H < B:
    print('Normal')
elif H < A:
    print('Deficiency')
else:
    print('Excess')
