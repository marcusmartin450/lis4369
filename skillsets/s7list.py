# Marcus Martin
# LIS4369 Skillset 7 - Using Lists
# This program demonstrates Python list operations: create, insert, delete, sort, and count

# Step 1: Get number of elements
num = int(input("Enter number of list elements: "))

# Step 2: Create empty list
my_list = []

# Step 3: Input elements
for i in range(num):
    element = input(f"Please enter list element {i+1}: ")
    my_list.append(element)

# Step 4: Display list
print("\nPrint my_list:")
print(my_list)

# Step 5: Insert element into specific position
new_item = input("\nPlease enter list element to insert: ")
position = int(input("Please enter list *index* position (must convert to int): "))
my_list.insert(position, new_item)

print("\nInsert element into specific position in my_list:")
print(my_list)

# Step 6: Count number of elements in list
print("\nCount number of elements in list:")
print(len(my_list))

# Step 7: Sort list alphabetically
my_list.sort()
print("\nSort elements in list alphabetically:")
print(my_list)

# Step 8: Reverse list
my_list.reverse()
print("\nReverse list:")
print(my_list)

# Step 9: Remove last element
my_list.pop()
print("\nRemove last list element:")
print(my_list)

# Step 10: Delete 2nd element (index 1)
del my_list[1]
print("\nDelete second element from list by *index*:")
print(my_list)

# Step 11: Delete element by value
if "cherries" in my_list:
    my_list.remove("cherries")
print("\nDelete element from list by *value* ('cherries'):")
print(my_list)

# Step 12: Delete all elements
my_list.clear()
print("\nDelete all elements from list:")
print(my_list)
