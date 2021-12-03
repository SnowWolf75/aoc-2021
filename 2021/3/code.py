#!/usr/bin/env python3
import argparse
# Advent of code Year /Users/charles.wheeler/mygit/aoc-2021/2021 Day /Users/charles.wheeler/mygit/aoc-2021/2021/3 solution
# Author = Snow Wolf
# Date = December 2021
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

class Bits:
    def __init__(self, length):
        self.one = [0] * length
        self.zero = [0] * length
        self.length = length
        self.epsilon = 0
        self.gamma = 0

    def calc(self):
        ga = [None] * self.length
        for i in range(self.length):
            if self.one[i] >= self.zero[i]:
                ga[i] = '1'
            else:
                ga[i] = '0'

        ga_string = ''.join(ga)
        ga_int = int(ga_string, 2)
        self.gamma = ga_int
        bin_max = 2**self.length - 1
        self.epsilon = bin_max ^ self.gamma

    def parse(self, val):
        for i, v in enumerate(list(val), start=0):
            if v == '1':
                self.one[i] += 1
            else:
                self.zero[i] += 1

    def res(self):
        return self.epsilon * self.gamma


class LifeSupport:
    def __init__(self, sample):
        self.width = len(sample)
        self.length = 0
        self.grid = np.array([], np.dtype('i1'))
        self.o_rating = 0
        self.s_rating = 0

    def reshape(self):
        self.grid = self.grid.reshape(self.length, self.width)

    def parse(self, val):
        splits = [int(i) for i in list(val)]
        self.grid = np.append(self.grid, splits)
        self.length += 1

    def scrubber(self):
        g = self.grid
        for i in range(self.width):
            my_length = g.shape[0]
            zeros = np.count_nonzero(g==0, axis=0)
            if zeros[i] <= (my_length / 2):
                search = 0
            else:
                search = 1

            g = g[ np.where(( g[:,i] == search)) ]
            print("Index %d, CO2 G:\n" % i, g)
            if g.shape[0] == 1:
                break

        s = ''
        for i in g.flatten():
            s += str(i)
        self.s_rating = int(s, 2)

    def oxygen(self):
        g = self.grid
        for i in range(self.width):
            my_length = g.shape[0]
            ones = np.count_nonzero(g==1, axis=0)
            if ones[i] >= (my_length / 2):
                search = 1
            else:
                search = 0

            g = g[ np.where(( g[:,i] == search)) ]
            print("Index %d, New G:\n" % i, g)
            if g.shape[0] == 1:
                break

        s = ''
        for i in g.flatten():
            s += str(i)
        self.o_rating = int(s, 2)


def part1(lines):
    first = lines[0]
    b = Bits(len(first))
    for line in lines:
        b.parse(line)

    b.calc()
    return b.res()


def part2(lines):
    first = lines[0]
    ls = LifeSupport(first)
    for line in lines:
        ls.parse(line)

    ls.reshape()
    ls.oxygen()
    print(ls.o_rating)
    ls.scrubber()
    print(ls.s_rating)
    return ls.s_rating * ls.o_rating


if args.one:
    one_ret = part1(input.splitlines())
    print("%sPart One : %s" % ("SAMPLE! " if args.sample else "", str(one_ret)))

if args.two:
    two_ret = part2(input.splitlines())
    print("%sPart Two : %s" % ("SAMPLE! " if args.sample else "", str(two_ret)))
