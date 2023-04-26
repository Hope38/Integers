class Loan:
    def __init__(self, principal, interest_rate, num_years):
        self.principal = principal
        self.interest_rate = interest_rate
        self.num_years = num_years
        self.monthly_rate = self.interest_rate / 1200
        self.num_months = self.num_years * 12
        self.payment_amount = self.calculate_payment()
        
    def calculate_payment(self):
        payment = self.principal * (self.monthly_rate / (1 - (1 + self.monthly_rate) ** (-self.num_months)))
        return payment
    
    def get_payment_amount(self):
        return self.payment_amount

# Get user inputs
principal = float(input("Enter the loan amount: "))
interest_rate = float(input("Enter the interest rate (as a percentage): "))
num_years = int(input("Enter the number of years for the loan: "))

# Create a Loan object and calculate the payment amount
loan = Loan(principal, interest_rate, num_years)

# Output the payment amount
print("The monthly payment amount is: $", round(loan.get_payment_amount(), 2))
