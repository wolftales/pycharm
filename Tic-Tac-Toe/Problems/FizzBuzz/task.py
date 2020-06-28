for num in range(1, 101):

    if int(num) % 5 == 0 and int(num) % 3 == 0:
        print('FizzBuzz')
    elif int(num) % 3 == 0:
        print('Fizz')
    elif int(num) % 5 == 0:
        print('Buzz')
    else:
        print(num)
