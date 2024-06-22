s = input("Enter a string: ")

if len(s) >= 2:
    result = s[:2] + s[-2:]
else:
    print("Enter longer string.")
    
print(result)
