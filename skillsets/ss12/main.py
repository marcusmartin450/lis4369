import functions 

# ss12_temperature_conversion.py
# Developer: Marcus Martin
def main():
    print("Temperature Converter")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")

    choice = input("Choose a conversion (1 or 2): ")

    if choice == "1":
        f = float(input("Enter temperature in Fahrenheit: "))
        c = functions.f_to_c(f)
        print(f"{f}°F is {c:.2f}°C")

    elif choice == "2":
        c = float(input("Enter temperature in Celsius: "))
        f = functions.c_to_f(c)
        print(f"{c}°C is {f:.2f}°F")

if __name__ == "__main__":
    main()