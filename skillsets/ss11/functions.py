import random

def example1(beg, end):
    """Generate 10 random integers using randint()."""
    results = []
    for _ in range(10):
        results.append(random.randint(beg, end))
    return results


def example2(beg, end):
    """Generate 10 shuffled numbers from a range."""
    nums = list(range(beg, end + 1))
    random.shuffle(nums)
    return nums[:10]
