#! /usr/bin/env python

import re

required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

with open('input') as fh:
    records = fh.read().split("\n\n")

valid = 0
for r in records:
    names = {field.split(sep=":")[0] for field in re.split(r"\s+", r)}
    if required_fields.issubset(names):
        valid = valid + 1

print(valid)
