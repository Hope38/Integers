# Prompt user for starting dollar amount
start_amount = float(input("Enter starting dollar amount: "))

# Print column headings
print("{:>10s} {:>15s}".format("Price", "Discounted Price"))

# Generate discount table
for i in range(21):
    # Calculate price and discount
    price = start_amount + i * 0.5
    discount = 0.1 + i * 0.04
    discounted_price = price * (1 - discount)

    # Print row headings and data
    print("${:<8.2f} {:>10.0%} {:>10.2f}".format(price, discount, discounted_price))
