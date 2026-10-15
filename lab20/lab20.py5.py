#shopping list
#build a menu-driven program that keeps running until the user picks quit
#add item , remove item, view list , sort list, quit
#don't add duplicates and print a friendly message when the user tries to remove an item that is not on the list
shopping= []
print("1. Add item")
print("2. Remove item")
print("3. view list")
print("4. sort list")
print("5. quit")

while True:                                     # Repeat menu
    print("\n1.Add  2.Remove  3.View  4.Sort  5.Quit")
    choice = input("Enter choice: ")             # Get choice
    if choice == "1":
        item = input("Enter item: ")             # Get item
        if item.lower() in [x.lower() for x in items]:  # Check duplicate
            print("Item already exists!")
        else:
            items.append(item)                  # Add item
    elif choice == "2":
        item = input("Enter item: ")             # Get item
        for x in items:                          # Check list
            if x.lower() == item.lower():       # Ignore case
                items.remove(x)                 # Remove item
                break
        else:
            print("Item not found!")             # Not in list
    elif choice == "3":
        print(items)
    elif choice == "4":
        items.sort()                             # Sort list
        print("List sorted!")
    elif choice == "5":
        break                                    # Exit program
    else:
        print("Invalid choice!")                 # Wrong choice