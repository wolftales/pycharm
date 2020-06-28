string = input()

for char in string:
    if char.isupper():
        print(f'_{char.lower()}', end='')
    else:
        print(char, end='')
