s = input("Enter a string: ")

poor_index = s.find('poor')
not_index = s.find('not')

if poor_index == -1 or not_index == -1 or poor_index > not_index:
    pass
else:
    s = s.replace(s[poor_index:not_index+3], 'good')
print(s)
