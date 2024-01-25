# Prompt to input name and username
letters = input("Please, enter your name and surname: ")

# Create dict with the results of counting
count = {}

# Counting letters
for l in letters:
    # Skip counting spaces
    if l == ' ':
        continue
    count[l] = count.get(l, 0) + 1

# Print the result
print(count)




