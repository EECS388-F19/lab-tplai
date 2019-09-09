list = ["Sam", "Joe", "Sophy"]
list.sort()
print(list)

first_name = list[0]
first_name = first_name[:-1]
print (first_name)


longest_name = ''

for name in list:
    if len(name) > len(longest_name):
        longest_name = name

print(longest_name)
