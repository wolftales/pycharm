# 87113420
seq = input()
total = 0
new_list = []
tmp_list = [x for x in map(int, seq)]
for i in tmp_list:
    new_list.append(i + total)
    total += i
print(new_list)
