#!/usr/bin/env python3
# coding: utf-8

"""A simple stopwatch program"""

from time import time
from getch import getch

class StopWatch:
    def __init__(self):
        self.running = False
        self.laps = []

    def start(self):
        self.laps = []
        self.startt = time()
        self.running = True

    def lap(self):
        if self.running:
            self.laps.append(time())

    def stop(self):
        self.stopt = time()
        self.running = False

    def print(self):
        for l in range(len(self.laps)):
            print(self.laps[l] - self.laps[l-1] if l != 0
                  else self.laps[l] - self.startt)
        if not self.running:
            print('-> {}'.format(self.stopt - self.startt))

def main():
    sw = StopWatch()
    while True:
        k = getch()
        if k == 'h':
            print('h - help, j - start, k - stop, l - lap, p - print, q - quit')
        if k == 'j':
            sw.start()
        if k == 'k':
            sw.stop()
        if k == 'l':
            sw.lap()
        if k == 'p':
            sw.print()
        if k == 'q':
            return 0

if __name__ == '__main__':
    main()

