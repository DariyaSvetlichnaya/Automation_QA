def create_shopping_list():
    # Step 1: Prompt the user to create a list
    user_input = input("\n"
                       "You have a unique chance to create your own shopping list!\n"
                       "Please, enter the products separated by spaces: \n"
                       "    ")

    # Step 2: Convert the string entered by the user to the list
    shopping_list = user_input.split()

    # Step 3: Check if the user entered products and print the list
    if any(shopping_list):
        print(f"Here is your shopping list: {shopping_list}")
    else:
        print("Unfortunately, your shopping list is empty :( See you next time!")
        return

    # Step 5: Prompt the user to enter the product
    while True:
        action_input = input('''
        To ADD the product to the list: just enter the product name (ex., 'milk')
        To REMOVE the product from the list: enter '-' before the product's name (ex., '-banana'): ''').strip()

    # Step 6: Add/remove product
        if action_input.startswith('-'):
            # Remove product:
            product_to_remove = action_input[1:]
            if product_to_remove in shopping_list:
                shopping_list.remove(product_to_remove)
                print(f"{product_to_remove} removed from the shopping list.")
            else:
                print(f"{product_to_remove} is not found in the shopping list.")
        else:
            # Add product
            shopping_list.append(action_input)
            print(f"{action_input} is added to the shopping list.")

        # Step 7: Print the updated list of products
        print(f"Here is the updated shopping list: {shopping_list}")

        # Step 8: Check if the list is empty using len
        if len(shopping_list) == 0:
            print("The shopping list is empty. That's all for today!")
            break


# Call the function directly
create_shopping_list()
