# Make sure your output matches the assignment *exactly*
# print("how long, on average, they spend on a computer per day?", end="")
amt_time = float(input())

if amt_time < 2:
    print('That seems reasonable')
elif amt_time < 4:
    print('Do you have time for anything else?')
else:
    print('You need to get outside more!')
