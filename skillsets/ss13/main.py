import functions

def main():
    print("Sphere Volume Program\n")
    print("Program Requirements:")
    print("1. Program calculates sphere volume in liquid U.S. gallons from user-entered diameter value in inches,")
    print("   and rounds to two decimal places.")
    print("2. Must use Python's *built-in* PI and pow() capabilities.")
    print("3. Program checks for nonpositive integers and non-numeric values.")
    print("4. Program continues to prompt for user entry until no longer requested, prompt accepts upper or lower case letters.\n")
    functions.sphere_volume()

if __name__ == "__main__":
    main()
