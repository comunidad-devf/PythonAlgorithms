# -*- coding: utf-8 -*-
"""Bouble sort sample."""

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
print "\n\t___Bubble Sorting___\n"
print "Unsorted elements:"
print numbers, "\n"
print_pyramid(numbers, color='\033[93m')
time.sleep(2)
keep_sorting = True
swaps = 0
iterations = 0
while keep_sorting:
    keep_sorting = False
    iterations += 1
    for i in range(len(numbers)):
        os.system('clear')
        j = numbers[i:i+2]
        if j[0] > j[-1]:
            swaps += 1
            numbers[i] = j[-1]
            numbers[i+1] = j[0]
            keep_sorting = True
        print "\n\t___Bubble Sorting___\n"
        print "Sorting Elementes:"
        print numbers, "\n"
        print_pyramid(numbers, i, i+1)
        time.sleep(.05)
os.system('clear')
print "\n\t___Bubble Sorting___\n"
print "Sorted Elementes:"
print numbers, "\n"
print_pyramid(numbers, color='\033[92m')
print "Swaps:", swaps
print "Iterations:", iterations, "\n"
