import random

from functions import *

def main():
    print("Developer: Marcus Martin, Pseudo-Random Number Generator Program")
    print('-' * 50)

    beg = int(input("Enter beginning value: "))
    end = int(input("Enter ending value: "))

    print("\nExample 1: Using range() and randint() functions:")
    print(*example1(beg, end))

    print("\nExample 2: Using a list, with range() and shuffle() functions:")
    print(*example2(beg, end))


if __name__ == "__main__":
    main()


