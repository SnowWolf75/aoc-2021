#!/usr/bin/env python3
import argparse

# Advent of code Year /Users/charles.wheeler/mygit/aoc-2021/2021 Day /Users/charles.wheeler/mygit/aoc-2021/2021/2 solution
# Author = Snow Wolf
# Date = December 2021
import sys

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


class DriveSub():
    def __init__(self):
        self.horiz = 0
        self.depth = 0

    def forward(self, val):
        self.horiz += val

    def down(self, val):
        self.depth += val

    def up(self, val):
        self.depth -= val

    def pos(self):
        return self.horiz * self.depth

class AimSub(DriveSub):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def print_cur(self):
        print("h: %d\td: %d\ta: %d" % (self.horiz, self.depth, self.aim))

    def forward(self, val):
        self.horiz += val
        self.depth += val * self.aim

    def down(self, val):
        self.aim += val

    def up(self, val):
        self.aim -= val


def part1(lines):
    sub = DriveSub()
    for line in lines:
        (op, v) = line.split()
        print(op,v)
        try:
            eval("sub." + op + "(int(v))")
        except:
            print("borky bork")
            sys.exit(1)

    pos = sub.pos()
    return pos


def part2(lines):
    aim = AimSub()
    for line in lines:
        (op, v) = line.split()
        # print(op,v)
        try:
            eval("aim." + op + "(int(v))")
        except:
            print("borky bork")
            sys.exit(1)
        aim.print_cur()

    pos = aim.pos()
    return pos


if args.one:
    one_ret = part1(input.splitlines())
    print("%sPart One : %s" % ("SAMPLE! " if args.sample else "", str(one_ret)))

if args.two:
    two_ret = part2(input.splitlines())
    print("%sPart Two : %s" % ("SAMPLE! " if args.sample else "", str(two_ret)))
