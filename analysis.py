#!/usr/bin/env python

import ast
import sys

if len(sys.argv) < 2:
    print("Usage: analysis.py <result_file> [[exclude_result] ..]");
    exit(1)

excludes = set()

file = sys.argv[1]
iarg = 2
while iarg < len(sys.argv):
    excludes.add(sys.argv[iarg])
    iarg += 1

f =  open(file, 'r')

results = {}
win = "win"
lose = "lose"

for line in f:
    data = ast.literal_eval(line)
    first = data[0]
    second = data[1]
    if first in excludes or second in excludes:
        continue

    if not first in results:
        results[first] = { win:0, lose:0 }

    if not second in results:
        results[second] = { win:0, lose:0 }

    if data[2] == '0':
        results[first][win] += 1
        results[second][lose] += 1
    else:
        results[second][win] += 1
        results[first][lose] += 1

average = 0
for key in results.keys():
    average += results[key][win]
average = int(average / len(results.keys()))

for key in sorted(results.keys()):
    print(key, "\t", results[key][win] - average, "\t", results[key])

