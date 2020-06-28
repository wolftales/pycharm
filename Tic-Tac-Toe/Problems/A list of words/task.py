# work with the preset variable `words`
new_list = list()

# words = ['apple', 'pear', 'banana', 'Ananas']

for word in words:
    if word.startswith('a') or word.startswith('A'):
        new_list.append(word)

print(new_list)
