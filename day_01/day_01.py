#! /usr/bin/env python

from itertools import combinations
from functools import reduce
import operator

with open("input") as fh:
    data = [int(l) for l in fh.readlines()]

# Part 1, the straightforward way
def part_1():
    for i, x in enumerate(data):
        for y in data[i+1:]:
            if x + y == 2020:
                print(f"{x} and {y} sum to 2020. Their product is {x * y}")


# General solution using itertools
def expense(target, n):
    for comb in combinations(data, n):
        if sum(comb) == target:
            product = reduce(operator.mul, comb, 1)
            print(f"{comb} sum to {target}. The product is {product}")
            return product
    print(f"No solution found for {target} over {n} numbers")

expense(2020, 2)
expense(2020, 3)
