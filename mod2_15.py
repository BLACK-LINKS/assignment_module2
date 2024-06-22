string = 'python is popular programming language'
substring = 'p'

count = 0
for i in range(len(string)):
    if string[i:i+len(substring)] == substring:
        count += 1

print('Number of occurrence of', substring, ':', count)
