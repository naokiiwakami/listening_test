#!/usr/bin/env python

import sys
import random

if len(sys.argv) < 3:
    print("Usage: makepairs.py <wav_list_file> <output_pairs_file>")
    exit(1)

ins = open(sys.argv[1], "r")

candidates = []

for line in ins:
    candidates.append(line.strip())
ins.close

length = len(candidates)

lines = []

for i in range(length):
    for j in range(length):
        if i != j:
            line = candidates[i]
            line += "\t"
            line += candidates[j]
            lines.append(line)

random.shuffle(lines)

out = open(sys.argv[2], "w")
for line in lines:
    out.write(line + "\n")
out.close
