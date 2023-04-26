class Sale:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    def set_price(self, price):
        self.price = price
        
    def get_price(self):
        return self.price
    
    def __str__(self):
        return f"Item: {self.name}, Price: ${self.price:.2f}"


class DiscountSale(Sale):
    def __init__(self, name, price, discount_rate):
        super().__init__(name, price)
        self.discount_rate = discount_rate
        
    def set_discount_rate(self, discount_rate):
        self.discount_rate = discount_rate
        
    def get_discount_rate(self):
        return self.discount_rate
    
    def get_discount_price(self):
        return self.price * (1 - self.discount_rate / 100)
    
    def __str__(self):
        return f"Item: {self.name}, Discount Price: ${self.get_discount_price():.2f}, Discount {self.discount_rate}%"
    

# Example program
sale_name = input("Enter the name of the sale item: ")
sale_price = float(input("Enter the price of the sale item: "))
sale = Sale(sale_name, sale_price)

print("Sale object created!")
print(sale)
print()

discount_name = input("Enter the name of the discount sale item: ")
discount_price = float(input("Enter the price of the discount sale item: "))
discount_rate = float(input("Enter the discount rate for the discount sale item (as a percentage): "))
discount_sale = DiscountSale(discount_name, discount_price, discount_rate)

print("DiscountSale object created!")
print(discount_sale)
print()

# Test set and get methods for Sale object
sale.set_name("New Item")
sale.set_price(5.99)
print("Sale set methods tested!")
print(sale.get_name())
print(sale.get_price())
print()

# Test set and get methods for DiscountSale object
discount_sale.set_discount_rate(20)
print("DiscountSale set methods tested!")
print(discount_sale.get_discount_rate())
print(discount_sale.get_discount_price())
print()

# Test string methods for both objects
print("Sale __str__ method tested!")
print(sale)
print("DiscountSale __str__ method tested!")
print(discount_sale)
