#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    plays = ['rock', 'paper', 'scissors']
    result = []

    def helper(available_plays, rounds):
        if rounds == 0:
            result.append(available_plays)
        else:
            for i in range(len(plays)):
                helper(available_plays+[plays[i]], rounds - 1)

    helper([], n)
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
