def check_numbers():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if a == b or a + b == 5 or abs(a - b) == 5:
        return True
    else:
        return False

print(check_numbers())
