# List
my_list = [99, 5, None, 9, 5]

for item in my_list:
    # None is found in the list
    if item == None:
        print("There is None")
        break
else:
    print("There is no None")
