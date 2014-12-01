#!/usr/bin/env python3
# coding: utf-8

"""Hangman!"""

from getch import getch

def main():
    word = 'Bungalow'
    tries = 5
    tried = []
    wrong = []
    while 1:
        if not tries:
            break
        k = getch().lower()
        if k not in tried:
            tried.append(k)
            if k not in word.lower():
                wrong.append(k)
                tries -= 1
        left = len(word)
        for letter in word:
            if letter.lower() in tried:
                print(letter, end='')
                left -= 1
            else:
                print('*', end='')
        if not left:
            print('\nCongratulations!')
            break
        print(' Tries: {} Guesses: {}'.format(tries, ''.join(wrong)))

if __name__ == '__main__':
    main()

