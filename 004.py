#!/usr/bin/env python3
# coding: utf-8

def main():
    numbers = ( (5, 3, 15), (4 ,2, 8), (6, 2, 12), (6, 2, 3), (9, 12, 108),
                (4, 16, 64) )
    for num in numbers:
        n = sorted(num)
        if (n[0] + n[1]) == n[2]:
            print('{} + {} = {}'.format(n[0], n[1], n[2]))
            print('{} + {} = {}'.format(n[1], n[0], n[2]))
            print('{} - {} = {}'.format(n[2], n[1], n[0]))
            print('{} - {} = {}'.format(n[2], n[0], n[1]))
        if (n[0] * n[1]) == n[2]:
            print('{} * {} = {}'.format(n[0], n[1], n[2]))
            print('{} * {} = {}'.format(n[1], n[0], n[2]))
            print('{} / {} = {}'.format(n[2], n[1], n[0]))
            print('{} / {} = {}'.format(n[2], n[0], n[1]))

if __name__ == '__main__':
    main()

