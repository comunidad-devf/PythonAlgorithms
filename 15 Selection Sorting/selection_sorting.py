# -*- coding: utf-8 -*-
"""Selection sort sample."""

from random import sample
import os
import time


def print_pyramid(elements, a=None, b=None, color=None):
    """Print a number pyramid."""
    for i in range(len(elements)):
        if i == a:
            print '\033[95m' + ('■' * elements[i]) + '\033[0m'
        elif i == b:
            print '\033[94m' + ('■' * elements[i]) + '\033[0m'
        else:
            if color:
                print color + ('■' * elements[i]) + '\033[0m'
            else:
                print '■' * elements[i]
    print '\a'

os.system('clear')
numbers = sample(range(1, 11), 10)
print "\n\t___Selection Sorting___\n"
print "Unsorted elements:"
print numbers, "\n"
print_pyramid(numbers, color='\033[93m')
time.sleep(2)
swaps = 0
iterations = 0
for i in range(0, len(numbers)-1):
    unsorted_elementes = numbers[i:]
    smallest = unsorted_elementes[0]
    smallest_index = i
    for j in range(len(unsorted_elementes)):
        os.system('clear')
        if unsorted_elementes[j] < smallest:
            smallest = unsorted_elementes[j]
            smallest_index = i+j
        iterations += 1
        print "\n\t___Selection Sorting___\n"
        print "Sorting Elementes:"
        print numbers, "\n"
        print_pyramid(numbers, i, j)
        time.sleep(.05)
    numbers[smallest_index], numbers[i] = numbers[i], numbers[smallest_index]
    swaps += 1

os.system('clear')
print "\n\t___Selection Sorting___\n"
print "Sorted Elementes:"
print numbers, "\n"
print_pyramid(numbers, color='\033[92m')
print "Swaps:", swaps
print "Iterations:", iterations, "\n"

