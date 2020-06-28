income = int(input())
tax = 0
if 0 <= income <= 15527:
    tax = 0
elif 15528 <= income <= 42707:
    tax = 15
elif 42708 <= income <= 132406:
    tax = 25
else:
    tax = 28

print(f'The tax for {income} is {tax}%. That is {round(income * (tax/100))} dollars!')
