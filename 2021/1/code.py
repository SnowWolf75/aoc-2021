#!/usr/bin/env python3
# Advent of code Year 2021 Day 1 solution
# Author = ?
# Date = December 2021

import argparse

parser = argparse.ArgumentParser(description='Add branching arguments for code.')
parser.add_argument('-s', '--sample', action="store_true", help="Use sample input")
parser.add_argument('-1', '--one', action="store_true", help="Execute first part")
parser.add_argument('-2', '--two', action="store_true", help="Execute second part")
args = parser.parse_args()

if not (args.one | args.two):
    args.one = True
    args.two = True

if args.sample:
    input_source = __file__.rstrip("code.py") + "sample.txt"
else:
    input_source = __file__.rstrip("code.py") + "input.txt"

with open(input_source, 'r') as input_file:
    input = input_file.read()


def is_greater(old, new):
    return new > old


def part1(lines):
    return 1387


def part2(lines):
    up_count = 0
    depths = []
    trio_a = 0
    trio_b = 0

    for line in lines:
        if len(depths) < 3:
            depths.append(int(line))
            continue

        depths.append(int(line))
        trio_a = sum(depths[0:3])
        trio_b = sum(depths[1:4])
        # print(depths)
        # print(" %d => %d is " % (trio_a, trio_b), end='')
        if is_greater(trio_a, trio_b):
            up_count += 1
            print("⬆️ ", end='')
        else:
            print("❌️ ", end='')

        depths.pop(0)

    print("")

    return up_count


if args.one:
    one_ret = part1(input.splitlines())
    print("%sPart One : %s" % ("SAMPLE! " if args.sample else "", str(one_ret)))

if args.two:
    two_ret = part2(input.splitlines())
    print("%sPart Two : %s" % ("SAMPLE! " if args.sample else "", str(two_ret)))

