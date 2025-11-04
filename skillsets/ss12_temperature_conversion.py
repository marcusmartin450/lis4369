# ss12_temperature_conversion.py
# Developer: Marcus Martin
# Description: Converts user-entered temperatures between Fahrenheit and Celsius.

def f_to_c(f):
    return (f - 32) * 5 / 9

def c_to_f(c):
    return c * 9 / 5 + 32

def main():
    print("Developer: Marcus Martin, Temperature Conversion Program")
    print('-' * 50)

    while True:
        ans = input("Do you want to convert a temperature (y or n)? ").lower()
        if ans == 'n':
            print("Thank you for using our Temperature Conversion Program!")
            break
        elif ans != 'y':
            print("Incorrect entry. Please try again.")
            continue

        conv = input("Fahrenheit to Celsius? Type 'f', or Celsius to Fahrenheit? Type 'c': ").lower()
        if conv == 'f':
            f = float(input("Enter temperature in Fahrenheit: "))
            print("Temperature in Celsius =", f_to_c(f))
        elif conv == 'c':
            c = float(input("Enter temperature in Celsius: "))
            print("Temperature in Fahrenheit =", c_to_f(c))
        else:
            print("Incorrect entry. Please try again.")

if __name__ == '__main__':
    main()
