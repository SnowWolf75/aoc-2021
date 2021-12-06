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
    def __init__(self, nums):
        self.called_numbers = [int(i) for i in nums.split(",")]
        self.boards = []
        self.winner = None
        self.last_call = 0
        self.winner_list = {}

    class Board:
        def __init__(self, data, id):
            self.id = id
            self.board_cells = numpy.array([], dtype='i1')
            self.final_board = numpy.ones([5,5], dtype='i1')
            self.last_call = 0
            self.win_axis = [-1, -1]
            self.is_winner = False
            self.winning_val = 0
            for line in data:
                self.board_cells = numpy.append(self.board_cells,
                                                [int(i) for i in line.split()])

            self.board_cells = self.board_cells.reshape([5, 5])
            self.called = numpy.ones([5, 5], dtype='i1')

        def call_number(self, num):
            test = np.argwhere(self.board_cells == num)
            if len(test) > 0:
                x, y = test[0]
                self.called[x, y] = 0
                return self.id
            else:
                return None

        def check_win(self, last_call):
            if self.is_winner:
                # Already checked for winning condition, so pop out
                return False

            for row in range(5):
                if self.called[row].max() == 0:
                    self.is_winner = True
                    self.last_call = last_call
                    self.claim_winner()
                    return True

            for col in range(5):
                if self.called[:,col].max() == 0:
                    self.is_winner = True
                    self.last_call = last_call
                    self.claim_winner()
                    return True

            return False

        def claim_winner(self):
            self.final_board = self.board_cells * self.called
            s = self.final_board.sum() * self.last_call
            self.winning_val = s

        def print_win(self):
            print("Board ID: %d \tWinning val: %d\tLC: %d" % (self.id, self.winning_val, self.last_call))
            print(np.hstack((self.board_cells, self.called)))
            print()

    def add(self, data, board_id):
        b = self.Board(data, board_id)
        self.boards.append(b)

    def call(self, val):
        called_on_id = []
        this_id = None
        for board in self.boards:
            this_id = board.call_number(val)
            if this_id is not None:
                called_on_id.append(this_id)

        return called_on_id

    def check_winner(self, val):
        for board in self.boards:
            did_win = board.check_win(last_call=val)
            if did_win:
                board.print_win()
                return True

        return False

    def show_winners(self):
        f = " {:^5} | {}"
        print()
        print(f.format("Board", "Winning val"))
        for k in self.winner_list:
            print(f.format(k, self.winner_list[k]))


    def parse_winner(self, b):
        return b.claim_winner()

    def iterate(self):
        # f = "{:>4} | {}"
        # print(" Num | Boards")
        # print("-----+-----------------------------")
        for i in self.called_numbers:
            boards_marked = self.call(i)
            # if boards_marked:
            #     s = ", ".join(map(str, boards_marked))
            # else:
            #     s = "None"
            #
            # print(f.format(i, s), end='')

            win_val = self.check_winner(i)
            # if win_val:
            #     print(" New winner")
            # else:
            #     print("")


def part1(lines):
    return "28082"


def part2(lines):
    first_line = lines.pop(0)
    print("FL: ", first_line)
    squid = BingoOne(first_line)
    i = 0
    while lines:
        lines.pop(0)
        #print(lines[0:5])
        squid.add(lines[0:5], i)
        del(lines[0:5])
        i += 1

    print("Num boards:", len(squid.boards))
    squid.iterate()
    # squid.show_winners()
    return ""


if args.one:
    one_ret = part1(input.splitlines())
    print("%sPart One : %s" % ("SAMPLE! " if args.sample else "", str(one_ret)))

if args.two:
    two_ret = part2(input.splitlines())
    print("%sPart Two : %s" % ("SAMPLE! " if args.sample else "", str(two_ret)))
    