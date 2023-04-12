# phonebook.py
with open('phonebook.txt', 'w') as file:
    pass

PHONEBOOK_FILE = "phonebook.txt"

def read_phonebook():
    phonebook = {}
    with open(PHONEBOOK_FILE, "r") as f:
        for line in f:
            name, number = line.strip().split(":")
            phonebook[name] = number
    return phonebook

def write_phonebook(phonebook):
    with open(PHONEBOOK_FILE, "w") as f:
        for name, number in phonebook.items():
            f.write(f"{name}:{number}\n")

def add_phonebook_entry(phonebook):
    name = input("Enter name: ")
    number = input("Enter number: ")
    phonebook[name] = number
    print(f"Added {name} to phone book")
    write_phonebook(phonebook) # Write to phonebook file after adding entry

def remove_phonebook_entry(phonebook):
    name = input("Enter name to remove: ")
    if name in phonebook:
        del phonebook[name]
        print(f"Removed {name} from phone book")
        write_phonebook(phonebook) # Write to phonebook file after removing entry
    else:
        print(f"{name} not found in phone book")

def display_phonebook(phonebook):
    print("Phone book:")
    for name, number in sorted(phonebook.items()):
        print(f"{name}: {number}")

def main():
    phonebook = read_phonebook()

    while True:
        print("1. Add phone book entry")
        print("2. Remove phone book entry")
        print("3. Display phone book")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_phonebook_entry(phonebook)
        elif choice == "2":
            remove_phonebook_entry(phonebook)
        elif choice == "3":
            display_phonebook(phonebook)
        elif choice == "4":
            write_phonebook(phonebook)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again")

if __name__ == "__main__":
    main()

