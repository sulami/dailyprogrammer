#!/usr/bin/env python3
# coding: utf-8

from urllib.request import urlopen

def main():
    word_list = [w.decode('utf-8') for w
        in urlopen('http://pastebin.com/raw.php?i=jSD873gL').read().split()]
    words = ( 'mkeart', 'sleewa', 'edcudls', 'iragoge', 'usrlsle', 'nalraoci',
              'nsdeuto', 'amrhat', 'inknsy', 'iferkna' )

    for s in sorted(words, key=len):
        matches = [w for w in word_list if sorted(s) == sorted(w)]
        print('{}: {}'.format(s, ''.join(matches)))

if __name__ == '__main__':
    main()

