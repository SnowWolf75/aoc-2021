#!/usr/bin/env python3
import argparse
# Advent of code Year /Users/charles.wheeler/mygit/aoc-2021/2021 Day /Users/charles.wheeler/mygit/aoc-2021/2021/11 solution
# Author = Snow Wolf
# Date = December 2021

parser = argparse.ArgumentParser(description='Add branching arguments for code.')
parser.add_argument('-s', '--sample', action="store_true", help="Use sample input")
parser.add_argument('-1', '--one', action="store_true", help="Execute first part")
parser.add_argument('-2', '--two', action="store_true", help="Execute second part")
args = parser.parse_args()

if not (args.one | args.two):
    args.one = True
    args.two = True
    
if args.sample:
    input_source = __file__.rstrip("code.py")+"sample.txt"
else:
    input_source = __file__.rstrip("code.py")+"input.txt"

with open(input_source, 'r') as input_file:
    input = input_file.read()

def part1(lines):
    return ""


def part2(lines):
    return ""


if args.one:
    one_ret = part1(input.splitlines())
    print("%sPart One : %s" % ("SAMPLE! " if args.sample else "", str(one_ret)))

if args.two:
    two_ret = part2(input.splitlines())
    print("%sPart Two : %s" % ("SAMPLE! " if args.sample else "", str(two_ret)))
    