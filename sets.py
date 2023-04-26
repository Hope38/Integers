blacklist = set()
whitelist = set()

while True:
    print("1. Add site to blacklist")
    print("2. Add site to whitelist")
    print("3. Remove site from blacklist")
    print("4. Remove site from whitelist")
    print("5. Display blacklist")
    print("6. Display whitelist")
    print("7. Display common sites")
    print("8. Display all unique sites")
    print("9. Quit")

    choice = input("Enter your choice (1-9): ")

    if choice == "1":
        site = input("Enter the site to blacklist: ")
        blacklist.add(site)
        print("Site added to blacklist")
    elif choice == "2":
        site = input("Enter the site to whitelist: ")
        whitelist.add(site)
        print("Site added to whitelist")
    elif choice == "3":
        site = input("Enter the site to remove from blacklist: ")
        if site in blacklist:
            blacklist.remove(site)
            print("Site removed from blacklist")
        else:
            print("Site not found in blacklist")
    elif choice == "4":
        site = input("Enter the site to remove from whitelist: ")
        if site in whitelist:
            whitelist.remove(site)
            print("Site removed from whitelist")
        else:
            print("Site not found in whitelist")
    elif choice == "5":
        print("Blacklisted sites:")
        for site in blacklist:
            print(site)
    elif choice == "6":
        print("Whitelisted sites:")
        for site in whitelist:
            print(site)
    elif choice == "7":
        common_sites = blacklist.intersection(whitelist)
        print("Common sites:")
        for site in common_sites:
            print(site)
    elif choice == "8":
        all_sites = blacklist.union(whitelist)
        print("All unique sites:")
        for site in all_sites:
            print(site)
    elif choice == "9":
        print("Goodbye!")
        break
    else:
        print("invalid choice, try again")
