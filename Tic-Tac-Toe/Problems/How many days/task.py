seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# create a list of days here
full_day = list()

for i in seconds:
    full_day.append((i//86400))

print(full_day)