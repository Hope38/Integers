# Function to convert binary to decimal
def binary_to_decimal(binary):
    decimal = 0
    binary = str(binary)
    binary = binary[::-1]
    for i in range(len(binary)):
        if binary[i] == '1':
            decimal += 2 ** i
    return decimal

# Function to convert decimal to binary
def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

# Function to convert binary to octal
def binary_to_octal(binary):
    decimal = binary_to_decimal(binary)
    octal = decimal_to_octal(decimal)
    return octal

# Function to convert octal to binary
def octal_to_binary(octal):
    decimal = octal_to_decimal(octal)
    binary = decimal_to_binary(decimal)
    return binary

# Function to convert decimal to octal
def decimal_to_octal(decimal):
    octal = ''
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal = decimal // 8
    return octal

# Function to convert octal to decimal
def octal_to_decimal(octal):
    decimal = 0
    octal = str(octal)
    octal = octal[::-1]
    for i in range(len(octal)):
        decimal += int(octal[i]) * (8 ** i)
    return decimal

# Main function for menu-driven program
def main():
    while True:
        print("Menu:")
        print("1. Binary to Decimal")
        print("2. Decimal to Binary")
        print("3. Binary to Octal")
        print("4. Octal to Binary")
        print("5. Decimal to Octal")
        print("6. Octal to Decimal")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            binary = input("Enter binary number: ")
            decimal = binary_to_decimal(binary)
            print("Decimal: ", decimal)
        elif choice == '2':
            decimal = int(input("Enter decimal number: "))
            binary = decimal_to_binary(decimal)
            print("Binary: ", binary)
        elif choice == '3':
            binary = input("Enter binary number: ")
            octal = binary_to_octal(binary)
            print("Octal: ", octal)
        elif choice == '4':
            octal = input("Enter octal number: ")
            binary = octal_to_binary(octal)
            print("Binary: ", binary)
        elif choice == '5':
            decimal = int(input("Enter decimal number: "))
            octal = decimal_to_octal(decimal)
            print("Octal: ", octal)
        elif choice == '6':
            octal = input("Enter octal number: ")
            decimal = octal_to_decimal(octal)
            print("Decimal: ", decimal)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == '__main__':
    main()
