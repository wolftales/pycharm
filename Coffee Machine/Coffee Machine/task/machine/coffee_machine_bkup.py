# Write your code here
print("Write how many ml of water the coffee machine has:")
water = int(input())

print("Write how many ml of milk the coffee machine has:")
milk = int(input())

print("Write how many grams of coffee beans the coffee machine has:")
coffee_beans = int(input())

print("Write how many cups of coffee you will need:")
cups = int(input())

w_cup = int(water / 200)
m_cup = int(milk / 50)
cb_cup = int(coffee_beans / 15)



if w_cup > m_cup:
    total_cups = m_cup
else:
    total_cups = w_cup

if total_cups > cb_cup:
    total_cups = cb_cup

if total_cups < 0:
    total_cups = 0

if cups == total_cups:
    print("Yes, I can make that amount of coffee")
elif cups < total_cups:
    print("Yes, I can make that amount of coffee (and even", total_cups - cups, "more than that)")
elif cups > total_cups:
    print("No, I can make only", total_cups, "cups of coffee")

