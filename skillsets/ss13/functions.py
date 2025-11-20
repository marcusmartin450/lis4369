import math


def sphere_volume():
    choice = input("Do you want to calculate a sphere volume (y or n)? ").lower()
    while choice[0] == 'y':
        diameter = input("Please enter diameter in inches (positive integers only): ")
        test = True
        while test == True:
            try:
                diameter = int(diameter)
                if diameter < 0:
                    raise ValueError
                volume = (4.0 / 3.0) * math.pi * math.pow(diameter / 2.0, 3)
                gallons = volume / 231
                print("\nSphere volume: {0:.2f} liquid U.S. gallons\n".format(gallons))
                test = False
            except ValueError:
                print("\nNot valid positive integer!")
                diameter = input("Please enter diameter in inches: ")
                continue
        choice = input("Do you want to calculate another sphere volume? ").lower()
    print("\nThank you for using our Sphere Volume Calculator!")
