num1=float(int(input("Enter First Number: ")))
num2=float(int(input("Enter Second Number: ")))

print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/,^,%: ")

result= 0

if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
elif ch == "^":
    result = num1 ** num2
elif ch == '%':
    result = num1 % num2
else:
    print("Input character is not recognized!")

print(float(num1))