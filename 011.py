#!/usr/bin/env python3
# coding: utf-8

"""Print the current month's calendar, or take month/year from argv"""

from subprocess import call
from sys import argv

def main():
    if len(argv) != 3:
        call('cal')
    else:
        call(['cal', argv[1], argv[2]])

if __name__ == '__main__':
    main()

