import random

# Generate two random whole numbers
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

# Generate two random float numbers
float1 = random.uniform(1.0, 10.0)
float2 = random.uniform(1.0, 10.0)

# Perform mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2
exponent = num1 ** num2

float_addition = float1 + float2
float_subtraction = float1 - float2
float_multiplication = float1 * float2
float_division = float1 / float2
float_exponent = float1 ** float2

# Display results
print(f"Whole number calculations:")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} % {num2} = {modulus}")
print(f"{num1} ** {num2} = {exponent}")
print("\n")
print(f"Float number calculations:")
print(f"{float1} + {float2} = {float_addition}")
print(f"{float1} - {float2} = {float_subtraction}")
print(f"{float1} * {float2} = {float_multiplication}")
print(f"{float1} / {float2} = {float_division}")
print(f"{float1} ** {float2} = {float_exponent}")
