matches = int(input())

# Gather Info
win_list = []
for i in range(matches):
    wins = input().split()
    if 'win' in wins:
        win_list.append(wins[0])

print(win_list)
print(len(win_list))
