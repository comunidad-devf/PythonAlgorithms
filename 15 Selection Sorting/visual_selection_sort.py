# -*- coding: utf-8 -*-
"""Selection sort sample."""

from random import sample
import os
import time

colors = {
    'HEADER': '\033[95m',
    'OKBLUE': '\033[94m',
    'OKGREEN': '\033[92m',
    'WARNING': '\033[93m',
    'FAIL': '\033[91m',
    'ENDC': '\033[0m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m',
}


def print_simple_pyramid(l, color):
    """Print simple pyramid."""
    for i in range(len(l)):
        print color, '■' * l[i], l[i], colors['ENDC']

os.system('clear')
n = int(raw_input("Random numbers to sort: "))
random_numbers = sample(range(1, n+1), n)
print_simple_pyramid(random_numbers, colors['WARNING'])
time.sleep(2)
os.system('clear')
for i in range(len(random_numbers)):
    minimum_value = random_numbers[i]
    min_index = i
    for j in range(i, len(random_numbers)):
        time.sleep(.1)
        os.system('clear')
        for k in range(len(random_numbers)):
            if k == min_index:
                print colors['OKBLUE'], '■' * random_numbers[k], random_numbers[k], colors['ENDC']
            elif k == j + 1:
                print colors['HEADER'], '■' * random_numbers[k], random_numbers[k], colors['ENDC']
            else:
                print colors['BOLD'], '■' * random_numbers[k], random_numbers[k], colors['ENDC']
        if random_numbers[j] < minimum_value:
            minimum_value = random_numbers[j]
            min_index = j
    random_numbers[i], random_numbers[min_index] = random_numbers[min_index], random_numbers[i]

os.system('clear')
print_simple_pyramid(random_numbers, colors['OKGREEN'])
