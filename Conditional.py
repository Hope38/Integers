# Prompt user for IP address
ip_address = input("Enter IP address: ")

# Split IP address into four octets
octets = ip_address.split(".")
if len(octets) != 4:
    print("Invalid IP address format")
else:
    # Validate each octet
    for octet in octets:
        if not octet.isnumeric() or int(octet) < 0 or int(octet) > 255:
            print("Invalid IP address format")
            break
    else:
        # Determine IP address class
        first_octet = int(octets[0])
        if first_octet >= 0 and first_octet <= 127:
            ip_class = "A"
        elif first_octet >= 128 and first_octet <= 191:
            ip_class = "B"
        elif first_octet >= 192 and first_octet <= 223:
            ip_class = "C"
        else:
            print("Invalid IP address format")
            exit()

        # Print results
        print("Valid IP address")
        print("IP address class:", ip_class)
