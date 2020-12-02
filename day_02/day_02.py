#! /usr/bin/env python

import re

def part_1():
    count = 0
    with open('input') as fh:
        for line in fh.readlines():
            match = re.match(r"(\d+)-(\d+)\s+(.):\s+(\S+)\s*", line)
            (min_times, max_times) = [int(i) for i in match.group(1, 2)]
            (char, password) = match.group(3, 4)

            times = sum(1 for c in password if c == char)

            if times in range(min_times, max_times + 1):
                count = count + 1
        return count


def part_2():
    count = 0
    with open('input') as fh:
        for line in fh.readlines():
            if match := re.match(r"(\d+)-(\d+)\s+(.):\s+(\S+)\s*", line):
                (char, password) = match.group(3, 4)
                (a, b) = [password[int(i) - 1] for i in match.group(1, 2)]

                if (a == char) ^ (b == char):
                    count = count + 1
        return count

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
