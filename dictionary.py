schools = {"NWHS": "North Wilkes High School", "SWHS": "South Wilkes High School"}

while True:
    print("1. Add High School")
    print("2. Delete High School")
    print("3. Display High Schools")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        key = input("Enter initials of High School: ")
        value = input("Enter full name of High School: ")
        schools[key] = value
        print("High School added")
    elif choice == "2":
        key = input("Enter initials of High School to delete: ")
        if key in schools:
            del schools[key]
            print("High School deleted")
        else:
            print("High School not found")
    elif choice == "3":
        print("High Schools:")
        for key, value in schools.items():
            print(key + ": " + value)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again")
