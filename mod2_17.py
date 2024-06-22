str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

str1_swapped = str1[1] + str1[0] + str1[2:]
str2_swapped = str2[1] + str2[0] + str2[2:]

result = str1_swapped + " " + str2_swapped

print(result)
