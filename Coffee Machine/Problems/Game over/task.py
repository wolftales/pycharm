scores = input().split()
# put your python code here

count = 0
correct = 0
incorrect = 0

for char in scores:
    if char != ' ':
        if char.lower() == 'c':
            correct += 1
        if char.lower() == 'i':
            incorrect += 1
        if incorrect >= 3:
            print('Game over')
            print(correct)
            break
else:
    print('You won')
    print(correct)
