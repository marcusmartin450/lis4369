import random

def main():
    print("Developer: Marcus Martin, Pseudo-Random Number Generator Program")
    print('-' * 50)

    beg = int(input("Enter beginning value: "))
    end = int(input("Enter ending value: "))
    
    print("Example 1: Using range() and randint() functions:")
    for _ in range(10):
        print(random.randint(beg, end), end=' ')
    print()
    
    print("Example 2: Using a list, with range() and shuffle() functions:")
    nums = list(range(beg, end + 1))
    random.shuffle(nums)
    for n in nums[:10]:
        print(n, end=' ')
    print()
