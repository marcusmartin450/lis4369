# Marcus Martin
# LIS4369 Skillset 7 - Using Lists
# Python Tuples — Skillset
# Hard-coded demo (no user input)

# 1) Create tuple using parentheses
my_tuple1 = ("cherries", "apples", "bananas", "oranges")
print("Print my_tuple1:")
print(my_tuple1)
print()

# 2) Create tuple WITHOUT parentheses (tuple packing)
my_tuple2 = 1, 2, "three", "four"
print("Print my_tuple2:")
print(my_tuple2)
print()

# 3) Tuple unpacking
fruit1, fruit2, fruit3, fruit4 = my_tuple1
print("Print my_tuple1 unpacking:")
print(fruit1, fruit2, fruit3, fruit4)
print()

# 4) Third element in my_tuple2
print("Print third element in my_tuple2:")
print(my_tuple2[2])  # 0-based index -> 'three'
print()

# 5) Slice (second and third elements) of my_tuple1
print('Print "slice" of my_tuple1 (second and third elements):')
print(my_tuple1[1:3])  # ('apples', 'bananas')
print()

# 6) Reassign my_tuple2 using parentheses
my_tuple2 = (1, 2, 3, 4)
print("Reassign my_tuple2 using parentheses.")
print("Print my_tuple2:")
print(my_tuple2)
print()

# 7) Reassign my_tuple2 using packing (no parentheses)
my_tuple2 = 5, 6, 7, 8
print('Reassign my_tuple2 using "packing" method (no parentheses).')
print("Print my_tuple2:")
print(my_tuple2)
print()

# 8) Number of elements in my_tuple1
print("Print number of elements in my_tuple1:")
print(len(my_tuple1))  # 4
print()

# 9) Type of my_tuple1
print("Print type of my_tuple1:")
print(type(my_tuple1))
print()

# 10) Delete my_tuple1 (attempting to print afterward will error)
print("Delete my_tuple1:")
del my_tuple1
# Demonstrate the error safely:
try:
    print(my_tuple1)  # this will raise NameError
except NameError:
    print("Note: my_tuple1 was deleted; printing it now raises a NameError.")
