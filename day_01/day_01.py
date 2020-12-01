#! /usr/bin/env python

from itertools import combinations

with open("input") as fh:
    data = [int(l) for l in fh.readlines()]

# Part 1, the straightforward way
for i, x in enumerate(data):
    for y in data[i+1:]:
        if x + y == 2020:
            print(f"{x} and {y} sum to 2020. Their product is {x * y}")

# Part 2, using itertools
for (x, y, z) in combinations(data, 3):
    if x + y + z == 2020:
        print(f"{x}, {y}, and {z} sum to 2020. Their product is {x * y * z}")
