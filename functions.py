def celsius_to_fahrenheit(celsius):
    return (9/5) * celsius + 32

def celsius_to_kelvin(celsius):
    return celsius + 273

def fahrenheit_to_kelvin(fahrenheit):
    return (5/9) * (fahrenheit - 32) + 273

def fahrenheit_to_celsius(fahrenheit):
    return (5/9) * (fahrenheit - 32)

def kelvin_to_fahrenheit(kelvin):
    return (9/5) * (kelvin - 273) + 32

def kelvin_to_celsius(kelvin):
    return kelvin - 273

while True:
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Kelvin")
    print("4. Fahrenheit to Celsius")
    print("5. Kelvin to Fahrenheit")
    print("6. Kelvin to Celsius")
    print("7. Quit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(fahrenheit, "F")
    elif choice == "2":
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = celsius_to_kelvin(celsius)
        print(kelvin, "K")
    elif choice == "3":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(kelvin, "K")
    elif choice == "4":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(celsius, "C")
    elif choice == "5":
        kelvin = float(input("Enter temperature in Kelvin: "))
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(fahrenheit, "F")
    elif choice == "6":
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin_to_celsius(kelvin)
        print(celsius, "C")
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again")
