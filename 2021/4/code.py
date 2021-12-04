#!/usr/bin/env python3
import argparse
# Advent of code Year /Users/charles.wheeler/mygit/aoc-2021/2021 Day /Users/charles.wheeler/mygit/aoc-2021/2021/4 solution
# Author = Snow Wolf
# Date = December 2021
import numpy
import numpy as np


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


class BingoOne:
    def __init__(self):
        self.called_numbers = []
        self.boards = []

    class Board:
        def __init__(self, data):
            self.board_cells = numpy.array([])
            for line in data:
                self.board_cells = numpy.append(self.board_cells,
                                                [int(i) for i in line.split()])

            self.board_cells = self.board_cells.reshape([5, 5])
            self.called = numpy.ndarray([5, 5], dtype=bool)

        def call_number(self, num):
            test = np.argwhere(self.board_cells == num)
            if len(test) > 0:
                x, y = test[0]
                self.called[x, y] = True
                if self.check_win():
                    return True

            return False

        def check_win(self):
            for row in range(5):
                if self.called[row].min():
                    return True

            for col in range(5):
                if self.called[:,col].min():
                    return True

            if self.called.diagonal().min():
                return True

            if np.flipud(self.called).diagonal().min():
                return True

            return False

    def add(self, data):
        b = self.Board(data)
        self.boards.append(b)
0
    def call(self, val):
        for board in self.boards







def part1(lines):
    pass


def part2(lines):
    pass


if args.one:
    one_ret = part1(input.splitlines())
    print("%sPart One : %s" % ("SAMPLE! " if args.sample else "", str(one_ret)))

if args.two:
    two_ret = part2(input.splitlines())
    print("%sPart Two : %s" % ("SAMPLE! " if args.sample else "", str(two_ret)))
    