product_code = input("Enter product code: ")

# Check if product code has the correct format
if len(product_code) != 13:
    print("Invalid product code length")
else:
    # Split product code into three sections
    sections = product_code.split(":")
    if len(sections) != 3:
        print("Invalid product code format")
    else:
        # Check each section for valid format
        section1 = sections[0]
        section2 = sections[1]
        section3 = sections[2]
        if len(section1) != 3 or not section1.isalpha():
            print("Invalid product code section 1")
        elif len(section2) != 2 or not section2.isnumeric():
            print("Invalid product code section 2")
        elif len(section3) != 6 or not section3.isnumeric():
            print("Invalid product code section 3")
        else:
            print("Valid product code")
