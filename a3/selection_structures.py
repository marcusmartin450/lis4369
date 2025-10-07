# Python Selection Structures
# Program Requirements:
# 1. Use Python selection structure.
# 2. Prompt user for two numbers, and a suitable operator.
# 3. Test for correct numeric operator.
# 4. Replicate display below.

# Python Calculator

# Input
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

print("\nSuitable Operators: +, -, *, /, // (integer division), % (modulo operator), ** (power)")
operator = input("Enter operator: ")

# Selection structure (if/elif/else)
if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
elif operator == '//':
    print(num1 // num2)
elif operator == '%':
    print(num1 % num2)
elif operator == '**':
    print(num1 ** num2)
else:
    print("Incorrect operator!")
