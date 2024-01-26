# Prompt to input name and username
letters = input("Please, enter your name and surname: ")

# Create dict with the results of counting
count = {}

# Counting letters
for t in letters:
    # Skip counting spaces
    if t == ' ':
        continue
    count[t] = count.get(t, 0) + 1

# Print the result
print(count)
