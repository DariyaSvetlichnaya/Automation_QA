# Given list of strings
str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# Convert strings to integers
int_list = list(map(lambda x: int(x), str_list))

# Creating dictionary of square numbers
square_dict = dict(map(lambda x: (x, x * x), int_list))

# Print the dict of number squares
print(square_dict)
