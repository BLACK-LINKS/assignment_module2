s1 = input("Enter the main string: ")
s2 = input("Enter the string to insert: ")

middle_index = len(s1) // 2
result = s1[:middle_index] + s2 + s1[middle_index:]

print(result)
