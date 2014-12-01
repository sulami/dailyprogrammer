#!/usr/bin/env python3
# coding: utf-8

"""Give the value of a coordinate in a pascal's triangle"""

from math import factorial as fac

def main():
    n = 4
    k = 2
    result = fac(n) // (fac(n-k) * fac(k))
    print(result)

if __name__ == '__main__':
    main()

