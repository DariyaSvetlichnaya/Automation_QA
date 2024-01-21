def create_shopping_list():
    # Step 1: Prompt the user to create a list
    user_input = input("Enter products for the shopping list (separated by spaces): ")

    # Step 2: Convert the string entered by the user to the list
    shopping_list = user_input.split()

    # Step 3: Print the initial list entered by the user
    print("Your initial shopping list:", shopping_list)

    # Step 4: Check if the list is empty
    if not any(shopping_list):
        print("The shopping list is empty. Exiting the program.")
        return

    while True:
        # Step 5: Prompt the user to enter the product and indicate add or delete
        action_input = input("Enter product and action (add or -delete): ").strip()

        # Step 6: Add/remove product
        if action_input.startswith('-'):
            # Remove product
            product_to_remove = action_input[1:]
            if product_to_remove in shopping_list:
                shopping_list.remove(product_to_remove)
                print(f"{product_to_remove} removed from the shopping list.")
            else:
                print(f"{product_to_remove} not found in the shopping list.")
        else:
            # Add product
            shopping_list.append(action_input)
            print(f"{action_input} added to the shopping list.")

        # Step 7: Print the updated list of products
        print("Updated shopping list:", shopping_list)

        # Step 8: Check if the list is empty using len
        if len(shopping_list) == 0:
            print("The shopping list is empty. Exiting the program.")
            break


# Call the function directly
create_shopping_list()
