from math import sqrt
from itertools import count


def count_dividers(num):
    # deduplication for perfect squares
    factors = set()
    # From: https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    largest_factor = int(sqrt(num)) + 1
    for n in range(1, largest_factor):
        if num % n == 0:
            factors.add(n)
            factors.add(num // n)
    print(", dividers:", len(factors), flush=True)
    return len(factors)


def main():
    trinum = 0
    for next_int in count(1):
        trinum += next_int
        print("Triangle number:", trinum, end="", flush=True)
        if count_dividers(trinum) > 500:
            return trinum


if __name__ == "__main__":
    triangle_number = main()
    print("Result:", triangle_number)
    # 76576500
