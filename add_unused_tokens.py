# coding=utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
from os import listdir, remove
from os.path import isfile, join
import sys
import unicodedata

import string
import collections

vocab_file = "/bert/bert-vocab-builder/vocab/dewiki_limited_chars_100.txt"

def add_unused(vocab=vocab_file, n=1000):

    with open(vocab, 'r+') as vf:
        lines = vf.readlines()
        for i in range(0, n):
            vf.write("[unused" + str(i) + "]" + "\n")


def main():
    add_unused()


if __name__ == "__main__":
    main()

