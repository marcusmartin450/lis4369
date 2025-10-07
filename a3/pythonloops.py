# Python Looping Structures
# Program Requirements:
# 1. Print while loop.
# 2. Print for loops using range() function, and implicit and explicit lists.
# 3. Use break and continue statements.
# 4. Replicate display below.
# Note: In Python, for loop used for iterating over a sequence (i.e., list, tuple, dictionary, set, or string).

# 1. while loop:
print("1. while loop:")
i = 1
while i <= 3:
    print(i)
    i += 1

# 2. for loop: using range() function with 1 arg
print("\n2. for loop: using range() function with 1 arg")
for x in range(4):
    print(x)

# 3. for loop: using range() function with two args
print("\n3. for loop: using range() function with two args")
for x in range(1, 4):
    print(x)

# 4. for loop: using range() function with three args (interval 2)
print("\n4. for loop: using range() function with three args (interval 2):")
for x in range(1, 4, 2):
    print(x)

# 5. for loop: using range() function with three args (negative interval)
print("\n5. for loop: using range() function with three args (negative interval):")
for x in range(3, 0, -2):
    print(x)

# 6. for loop using (implicit) list (i.e., list not assigned to variable)
print("\n6. for loop using (implicit) list (i.e., list not assigned to variable):")
for x in [1, 2, 3]:
    print(x)

# 7. for loop iterating through (explicit) string list
print("\n7. for loop iterating through (explicit) string list:")
states = ["Michigan", "Alabama", "Florida"]
for s in states:
    print(s)

# 8. for loop using break statement (stops loop)
print("\n8. for loop using break statement (stops loop):")
for s in states:
    if s == "Alabama":
        break
    print(s)

# 9. for loop using continue statement (stops and continues with next)
print("\n9. for loop using continue statement (stops and continues with next):")
for s in states:
    if s == "Alabama":
        continue
    print(s)

# 10. print list length
print("\n10. print list length:")
print(len(states))
