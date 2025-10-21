# Marcus Martin
# LIS4369 - Skillset 9: Python Sets
# This program demonstrates how to create and manipulate Python sets.

# 1. Create sets using different methods (hard-coded, no input)

# a) Create set using curly braces
my_set = {1, 3.14, 2.0, 'four', 'Five'}
print("Print my_set created using curly brackets:")
print(my_set)

print("\nPrint type of my_set:")
print(type(my_set))

# b) Create set using set() function with a list
my_set1 = set([1, 3.14, 2.0, 'Four', 'Five'])
print("\nPrint my_set1 created using set() function with list:")
print(my_set1)

print("\nPrint type of my_set1:")
print(type(my_set1))

# c) Create set using set() function with a tuple
my_set2 = set((1, 3.14, 2.0, 'Four', 'Five'))
print("\nPrint my_set2 created using set() function with tuple:")
print(my_set2)

print("\nPrint type of my_set2:")
print(type(my_set2))

# 2. Demonstrate basic set operations

# Length of set
print("\nLength of my_set:")
print(len(my_set))

# Discard an element (no error if missing)
my_set.discard('four')
print("\nDiscard 'four':")
print(my_set)

# Remove an element (raises error if missing)
my_set.discard('Five')  # Using discard for safety
print("\nRemove 'Five':")
print(my_set)

# Length after removals
print("\nLength of my_set:")
print(len(my_set))

# Add element
my_set.add(4)
print("\nAdd element to set (4) using add() method:")
print(my_set)

print("\nLength of my_set:")
print(len(my_set))

# 3. Mathematical operations on numeric values in the set

# Extract numeric-only items for min/max/sum
numeric_values = {x for x in my_set if isinstance(x, (int, float))}

print("\nDisplay minimum number:")
print(min(numeric_values))

print("\nDisplay maximum number:")
print(max(numeric_values))

print("\nDisplay sum of numbers:")
print(sum(numeric_values))

# 4. Delete all elements
my_set.clear()
print("\nDelete all set elements:")
print(my_set)

print("\nLength of my_set:")
print(len(my_set))
