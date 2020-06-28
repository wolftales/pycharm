def buy(drink_type):
    global water, milk, coffee_beans, cups, money

    if drink_type == 1:
        if water - 250 <= 0 or coffee_beans - 16 <= 0 or cups -1 <= 0:
            print('Sorry, not enough water!')
            return
    elif drink_type == 2:
        if water - 350 <= 0 or milk -75 <= 0 or coffee_beans - 20 <= 0 or cups - 1 <= 0:
            print('Sorry, not enough water!')
            return

    elif drink_type == 3:
        if water - 200 <= 0 or milk - 100 <= 0 or coffee_beans - 12 <= 0 or cups - 1 <= 0:
            print('Sorry, not enough water!\n')
            return
    else:
        pass

    if drink_type == 1:
        water -= 250
        coffee_beans -= 16
        cups -= 1
        money += 4
    elif drink_type == 2:
        water -= 350
        milk -= 75
        coffee_beans -= 20
        cups -= 1
        money += 7
    elif drink_type == 3:
        water -= 200
        milk -= 100
        coffee_beans -= 12
        cups -= 1
        money += 6

    print('I have enough resources, making you a coffee!\n')

def fill():
    global water, milk, coffee_beans, cups, money
    print("Write how many ml of water the coffee machine has:")
    water += int(input())

    print("Write how many ml of milk the coffee machine has:")
    milk += int(input())

    print("Write how many grams of coffee beans the coffee machine has:")
    coffee_beans += int(input())

    print("Write how many cups of coffee you will need:")
    cups += int(input())

def take():
    global money
    print(f'I gave you ${money}')
    money = 0

def print_supplies(water, milk, coffee_beans, cups, money):
    print('The coffee machine has:')
    print(f'{water} of water')
    print(f'{milk} of milk')
    print(f'{coffee_beans} of coffee beans')
    print(f'{cups} of disposable cups')
    print(f'{money} of money')
    print()

# Initial supplies
water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550

# print(print_supplies(water, milk, coffee_beans, cups, money))

# Loop to service multiple requests
while True:
    print('Write action (buy, fill, take, remaining or exit):')
    action = input().lower()

    if action == 'buy':
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        drink_type = input()
        if drink_type == 'back':
            continue
        else:
            buy(int(drink_type))
    elif action == 'fill':
        fill()
    elif action == 'take':
        take()
    elif action == 'remaining':
        print_supplies(water, milk, coffee_beans, cups, money)
    elif action == 'exit':
        break
