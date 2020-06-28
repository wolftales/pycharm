# put your python code here
first_num = float(input())
second_num = float(input())
operation = input()

if operation == '+':
    sum = first_num + second_num
    print(sum)
elif operation == '-':
    diff = first_num - second_num
    print(diff)
elif operation == '*':
    product = first_num * second_num
    print(product)
elif operation == 'pow':
    power = first_num ** second_num
    print(power)
elif operation == '/':
    if second_num == 0:
        print("Division by 0!")
    else:
        quiotient = first_num / second_num
        print(quiotient)
elif operation == 'mod':
    if second_num == 0:
        print("Division by 0!")
    else:
        quiotient = first_num % second_num
        print(quiotient)
elif operation == 'div':
    if second_num == 0:
        print("Division by 0!")
    else:
        quiotient = first_num // second_num
        print(quiotient)
else:
    print("Unknown operation")

