#!/usr/bin/env python3
# coding: utf-8

"""The computer tries to guess a number you give it"""

from sys import argv
from time import sleep

def main():
    if len(argv) != 2:
        print('Please pass exactly number to guess as a parameter')
        exit(1)

    try:
        n = int(argv[1])
    except ValueError:
        print('Please pass a valid integer as parameter')
        exit(2)

    if n < 1 or n > 100:
        print('Please choose a number between 1 and 100')
        exit(3)

    guess = 0
    count = 0
    min = 0
    max = 100
    while guess != n:
        count += 1
        guess = min + (max + 1 - min) / 2
        print('Guess: {}'.format(guess))
        if guess < n:
            print('Too low :(')
            min = guess
        elif guess > n:
            print('Too high :(')
            max = guess
        else:
            print('I found it! It is {}. It took me {} guesses.'.format(
                guess, count))
            exit(0)
        sleep(.5)

if __name__ == '__main__':
    main()

