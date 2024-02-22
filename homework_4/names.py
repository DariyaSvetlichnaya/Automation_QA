# Declare a list
name_list = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']

# Print only names
for item in name_list:
    if not isinstance(item, str):
        continue
    print(item)
