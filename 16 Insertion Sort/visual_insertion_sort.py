# -*- coding: utf-8 -*-
"""Insertion sort sample."""

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

for i in range(1, len(random_numbers)):
    time.sleep(.2)
    os.system('clear')
    temporal_value = random_numbers[i]
    index = i
    for k in range(len(random_numbers)):
        if k == i:
            print colors['HEADER'], '■' * random_numbers[k], random_numbers[k], colors['ENDC']
        else:
            print colors['BOLD'], '■' * random_numbers[k], random_numbers[k], colors['ENDC']
    while index > 0 and temporal_value < random_numbers[index - 1]:
        time.sleep(.2)
        os.system('clear')
        random_numbers[index] = random_numbers[index - 1]
        index -= 1
        for j in range(len(random_numbers)):
            if j == index:
                print colors['HEADER'], '■' * random_numbers[j], random_numbers[j], colors['ENDC']
            elif j == i:
                print colors['OKBLUE'], '■' * random_numbers[j], random_numbers[j], colors['ENDC']
            else:
                print colors['BOLD'], '■' * random_numbers[j], random_numbers[j], colors['ENDC']
    random_numbers[index] = temporal_value
    time.sleep(.2)
    os.system('clear')
    for j in range(len(random_numbers)):
        if j == index:
            print colors['HEADER'], '■' * random_numbers[j], random_numbers[j], colors['ENDC']
        elif j == i:
            print colors['OKBLUE'], '■' * random_numbers[j], random_numbers[j], colors['ENDC']
        else:
            print colors['BOLD'], '■' * random_numbers[j], random_numbers[j], colors['ENDC']

os.system('clear')
print_simple_pyramid(random_numbers, colors['OKGREEN'])
