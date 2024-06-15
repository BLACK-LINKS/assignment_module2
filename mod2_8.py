def vowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    letter = letter.lower()

    if letter in vowels:
        return True
    else:
        return False
print(vowel("a"))
print(vowel("b"))
