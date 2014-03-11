#!/usr/bin/env python

import ast
import sys
import math

if len(sys.argv) < 2:
    print("Usage: analysis.py <result_file> [[excluding_entry] ..]");
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
count = "count"

# Read the input lines and calculate the scores.
# Format of result file is:
# ['file_a', 'file_b', '0/1']
# where 0 at the third value denotes file_a wins, otherwise 1.
#
# A score is calculated as a rate of wins.
# When a sample wins against another sample, the score is considered to be 1.
# Otherwise the score is 0.  Then the average score would be rate of winning.
# Deviation of a won comparison would be (1 - score).  It is (0 - score) in
# lost case.
# Thus, variance of scores for a sample would be
# ((1 - score)^2 * numWins + (0 - score)^2 * numLosts) / numComparisons
#
for line in f:
    # Parse line and retrieve file names
    #
    data = ast.literal_eval(line)
    first = data[0]
    second = data[1]
    if first in excludes or second in excludes:
        continue

    # make result entries if not yet existed
    #
    if not first in results:
        results[first] = { win:0, count:0 }
    if not second in results:
        results[second] = { win:0, count:0 }

    # calculate the score
    #
    if data[2] == '0':
        results[first][win] += 1
    else:
        results[second][win] += 1

    # accumulate number of comparisons
    #
    results[first][count] += 1
    results[second][count] += 1

# print the results
#
print('file name of sample\tscore\t95% confidence interval')
for key in sorted(results.keys()):
    numComparisons = float(results[key][count])
    numWins = float(results[key][win])
    score = numWins / numComparisons
    variance = ((math.pow(1.0 - score, 2.0) * numWins + math.pow(score, 2.0) * (numComparisons - numWins))) / numComparisons
    standard_deviation = math.sqrt(variance)
    confidence_interval = 1.96 * standard_deviation / math.sqrt(numComparisons)

    print('{0}\t{1:.2f}\t{2:.2f}'.format(key, score * 100, confidence_interval * 100))
