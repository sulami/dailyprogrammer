#!/usr/bin/env python3
# coding: utf-8

"""Play rock paper scissors against itself"""

from random import randint

def tra(num):
    if num == 1:
        return 'Rock'
    if num == 2:
        return 'Paper'
    if num == 3:
        return 'Scissors'

def main():
    numruns = 25
    wins = [0, 0]
    for i in range(numruns):
        black = randint(1, 3)
        white = randint(1, 3)
        winner = None
        if black - 1 == white or black == 1 and white == 3:
            winner = 'Black'
            wins[0] += 1
        elif white - 1 == black or white == 1 and black == 3:
            winner = 'White'
            wins[1] += 1
        print('Game {}:\n  {} vs {} - '.format(i+1, tra(black), tra(white)),
              end='')
        if winner:
            print('{} wins'.format(winner))
        else:
            print('Draw')
    print('\nStatistics:\n  Black: {}\n  White: {}\n  Draws: {}'.format(
        wins[0], wins[1], numruns - (wins[0] + wins[1])))

if __name__ == '__main__':
    main()

