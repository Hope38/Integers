inventory = ["104-12321:Dell Server:1811", "104-12322:Cisco Rack:1811"]

while True:
    print("\nInventory System")
    print("1. Add item")
    print("2. Remove item")
    print("3. Sort items (standard order)")
    print("4. Sort items (reverse order)")
    print("5. Display inventory")
    print("6. Clear inventory")
    print("7. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item details (fixed_asset_number: Item Name: Location): ")
        inventory.append(item)
        print("Item added successfully.")

    elif choice == "2":
        if len(inventory) == 0:
            print("Inventory is empty.")
        else:
            item = input("Enter the fixed asset number of the item to remove: ")
            try:
                inventory.remove(next(i for i in inventory if i.startswith(item)))
                print("Item removed successfully.")
            except StopIteration:
                print("Item not found in inventory.")

    elif choice == "3":
        inventory.sort()
        print("Inventory sorted in standard order.")

    elif choice == "4":
        inventory.sort(reverse=True)
        print("Inventory sorted in reverse order.")

    elif choice == "5":
        if len(inventory) == 0:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for item in inventory:
                print(item)

    elif choice == "6":
        inventory.clear()
        print("Inventory cleared successfully.")

    elif choice == "7":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")
