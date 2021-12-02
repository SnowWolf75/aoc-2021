#!/usr/bin/env python3
# Advent of code Year 2021 Day 1 solution
# Author = ?
# Date = December 2021

print("Part One : "+ str(1387))

def isGreater(old, new):
    return new > old

upCount = 0
depths = []
trio_a = 0
trio_b = 0
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    for line in input_file:
        if len(depths) < 3:
            depths.append(int(line))
            continue

        depths.append(int(line))
        trio_a = sum(depths[0:3])
        trio_b = sum(depths[1:4])
        #print(depths)
        #print(" %d => %d is " % (trio_a, trio_b), end='')
        if isGreater(trio_a, trio_b):
            upCount += 1
            print("⬆️ ", end='')
        else:
            print("❌️ ", end='')


        depths.pop(0)

print("")

print("Part Two : "+ str(upCount))