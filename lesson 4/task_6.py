# Prompt to input name and username
letters = input("Please, enter your name and surname: ")

# Counting letters
print({char: letters.count(char) for char in letters})
