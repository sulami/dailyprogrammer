#!/usr/bin/env python3
# coding: utf-8

"""Plays Nim"""

from functools import reduce

def nim(heaps, misere=True):
    """
    Computes next move for Nim in a normal or misère (default) game, returns
    tuple (chosen_heap, nb_remove)
    """
    X = reduce(lambda x,y: x ^ y, heaps)
    if X == 0: # Will lose unless all non-empty heaps have size one
        for i, heap in enumerate(heaps):
            if heap > 0: # Empty any (non-empty) heap
                chosen_heap, nb_remove = i, heap
                break
    else:
        sums = [t ^ X < t for t in heaps]
        chosen_heap = sums.index(True)
        nb_remove = heaps[chosen_heap] - (heaps[chosen_heap] ^ X)
        heaps_twomore = 0
        for i, heap in enumerate(heaps):
            n = heap-nb_remove if chosen_heap == i else heap
            if n > 1: heaps_twomore += 1
        # If move leaves no heap of size 2 or larger, leave an odd (misère) or
        # even (normal) number of heaps of size 1
        if heaps_twomore == 0:
            chosen_heap = heaps.index(max(heaps))
            heaps_one = sum(t == 1 for t in heaps)
            # misère (resp. normal) strategy: if it is even (resp. odd) make it
            # odd (resp. even), else do not change
            nb_remove = (heaps[chosen_heap] - 1 if heaps_one % 2 != misere
                         else heaps[chosen_heap])
    return chosen_heap, nb_remove

def main():
    game = [3, 4, 5]
    playing = True
    while playing:
        print(game)
        heap, num = nim(game, misere=False)
        print(heap, num)
        game[heap] -= num
        for stack in game:
            if stack == 0:
                playing = False
                break
    print(game)

if __name__ == '__main__':
    main()

