jack_age = int(input())
alex_age = int(input())
lana_age = int(input())

small_age = 0

if jack_age < alex_age:
    if jack_age < lana_age:
        small_age = jack_age
    else:
        small_age = lana_age
elif alex_age < lana_age:
    small_age = alex_age
elif lana_age < alex_age:
    small_age = lana_age

print(small_age)
