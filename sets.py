blacklist = set()
whitelist = set()

def add_to_blacklist(site):
    blacklist.add(site)

def add_to_whitelist(site):
    whitelist.add(site)

def remove_from_blacklist(site):
    blacklist.discard(site)

def remove_from_whitelist(site):
    whitelist.discard(site)

def display_blacklist():
    print("Blacklisted sites:")
    for site in blacklist:
        print(site)

def display_whitelist():
    print("Whitelisted sites:")
    for site in whitelist:
        print(site)

def display_unique():
    print("Unique sites:")
    unique = blacklist.symmetric_difference(whitelist)
    for site in unique:
        print(site)

def display_common():
    print("Common sites:")
    common = blacklist.intersection(whitelist)
    for site in common:
        print(site)

while True:
    print("\n")
    print("1. Add to blacklist")
    print("2. Add to whitelist")
    print("3. Remove from blacklist")
    print("4. Remove from whitelist")
    print("5. Display blacklist")
    print("6. Display whitelist")
    print("7. Display unique sites")
    print("8. Display common sites")
    print("9. Quit")
    choice = input("Enter your choice (1-9): ")

    if choice == "1":
        site = input("Enter site to add to blacklist: ")
        add_to_blacklist(site)
    elif choice == "2":
        site = input("Enter site to add to whitelist: ")
        add_to_whitelist(site)
    elif choice == "3":
        site = input("Enter site to remove from blacklist: ")
        remove_from_blacklist(site)
    elif choice == "4":
        site = input("Enter site to remove from whitelist: ")
        remove_from_whitelist(site)
    elif choice == "5":
        display_blacklist()
    elif choice == "6":
        display_whitelist()
    elif choice == "7":
        display_unique()
    elif choice == "8":
        display_common()
    elif choice == "9":
        break
    else:
        print("Invalid choice. Try again.")
