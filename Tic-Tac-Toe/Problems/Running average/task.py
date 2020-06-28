digits = input()
new_list = list()
tmp = int(digits[0])
for i in digits[1:]:
    new_list.append((int(i) + tmp)/2)
    tmp = int(i)

print(new_list)
