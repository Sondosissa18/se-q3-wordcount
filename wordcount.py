#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Wordcount exercise

The main() function is already defined and complete. It calls the
print_words() and print_top() functions, which you fill in.

See the README for instructions.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure. Once that's working, try for the
next milestone.

Implement the create_word_dict() helper function that has been defined in
order to avoid code duplication within print_words() and print_top(). It
should return a dictionary with words as keys, and their counts as values.
"""

# Your name, plus anyone who helped you with this assignment
# Give credit where credit is due.
import sys
__author__ = "sondos with help from Gabby and jT"
# __references__ =
# 1:https: // www.codespeedy.com/sort-a-dictionary-by-key-in-python/
# 2:https://developers.google.com/edu/python/dict-files?hl=ko
# 3:https://stackoverflow.com/questions/14067267/lower-case-from-a-text-file


def create_word_dict(filename):
    # """Returns a word/count dict for the given file."""
    f = open(filename, 'r')
    counts = dict()
    for line in f:
        words = line.split()
        for word in words:
            counts[word.lower()] = counts.get(word.lower(), 0) + 1
    f.close()
    return counts


def print_words(filename):
    """Prints one per line '<word> : <count>', sorted
    by word for the given file.
    """
    counts = create_word_dict(filename)
    for key in sorted(counts.keys()):
        print(key, ":", counts[key])
    return counts
    # return [counts[key]:for key in sorted(counts.keys())]


def print_top(filename):
    """Prints the top count listing for the given file."""
    counts = create_word_dict(filename)
    sorted_counts = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
    for i in range(20):
        print(sorted_counts[i][0], ":", sorted_counts[i][1])
    return sorted_counts


# This basic command line argument parsing code is provided and calls
# the print_words() and print_top() functions which you must implement.
def main(args):
    if len(args) != 2:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = args[0]
    filename = args[1]

    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)


if __name__ == '__main__':
    main(sys.argv[1:])
