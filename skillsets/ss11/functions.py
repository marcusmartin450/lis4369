import random

def example1(beg, end):
    results = []
    for _ in range(10):
        results.append(random.randint(beg, end))
    return results


def example2(beg, end):
    nums = list(range(beg, end + 1))
    random.shuffle(nums)
    return nums[:10]
