


def get_calculator():
    while True:
        num1 = get_valid_float(1)
        num2 = get_valid_float(2)
        op = get_valid_operator()
        calculate(num1, num2, op)
        print("\nThank you for using our Math Calculator!\n")
        break

def get_valid_float(pos):
    while True:
        try:
            num = float(input(f"Enter num{pos}: "))
            return num
        except ValueError:
            print("Not valid number!")

def get_valid_operator():
    print("\nSuitable Operators: +, -, *, /, // (integer division), % (modulo operator), ** (power)")
    op_list = ['+', '-', '*', '/', '//', '%', '**']
    while True:
        op_test = input("Enter operator: ")
        if op_test in op_list:
            return op_test
        else:
            print("Incorrect operator!")

def calculate(num1, num2, op):
    if op == '+':
        print("{0:.2f}".format(num1 + num2))
    elif op == '-':
        print("{0:.2f}".format(num1 - num2))
    elif op == '*':
        print("{0:.2f}".format(num1 * num2))
    elif op == '/':
        while True:
            try:
                print("{0:.2f}".format(num1 / num2))
                break
            except ZeroDivisionError:
                print("Cannot divide by zero!")
                num2 = get_valid_float(2)
                continue
    elif op == '//':
        while True:
            try:
                print("{0:.2f}".format(num1 // num2))
                break
            except ZeroDivisionError:
                print("Cannot divide by zero!")
                num2 = get_valid_float(2)
                continue
    elif op == '%':
        while True:
            try:
                print("{0:.2f}".format(num1 % num2))
                break
            except ZeroDivisionError:
                print("Cannot divide by zero!")
                num2 = get_valid_float(2)
                continue
    elif op == '**':
        print("{0:.2f}".format(pow(num1, num2)))