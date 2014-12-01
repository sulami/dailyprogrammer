#!/usr/bin/env python3
# coding: utf-8

"""Don't ask."""

def calc(instr):
    t = []
    skipped = 0
    for n, l in enumerate(instr):
        b = n + skipped
        c = 1
        while b + c < len(instr) and instr[b+c] == instr[b]:
            c += 1
            skipped += 1
        if b + c - 1 < len(instr):
            t.append(instr[b:b+c])
    result = ''
    for e in t:
        result += str(len(e)) + e[0]
    return result

def main():
    instr = '1'
    print(instr)
    for i in range(14):
        instr = calc(instr)
        print(instr)

if __name__ == '__main__':
    main()

