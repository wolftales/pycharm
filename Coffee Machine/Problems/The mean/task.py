count = 0
sum = 0

while True:
    num = input()
    if num == '.':
        break
    else:
        sum += int(num)
        count += 1

print(sum / count)
