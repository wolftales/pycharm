vowels = 'aeiou'
# create your list here
string = input()

new_list= list()

for char in string:
    if not char in vowels:
        continue
    new_list.append(char)

print(new_list)
