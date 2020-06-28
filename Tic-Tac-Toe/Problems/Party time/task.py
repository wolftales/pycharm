# names = [name for name in input().split() if name != '.']
guest_list = list()

guest = input()

while guest != '.':
    guest_list.append(guest)
    guest = input()

print(f'{guest_list}\n{len(guest_list)}')
