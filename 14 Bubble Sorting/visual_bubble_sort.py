# -*- coding: utf-8 -*-
"""Visual Bubble Sort."""

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
keep_sorting = True
iteration_length = len(random_numbers)-1
while keep_sorting:
    keep_sorting = False
    for i in range(iteration_length):
        time.sleep(0.1)
        os.system('clear')
        for j in range(len(random_numbers)):
            if j == i:
                print colors['HEADER'], '■' * random_numbers[i], random_numbers[i], colors['ENDC']
            elif j == i+1:
                print colors['OKBLUE'], '■' * random_numbers[i+1], random_numbers[i+1], colors['ENDC']
            else:
                print colors['BOLD'], '■' * random_numbers[j], random_numbers[j], colors['ENDC']
        if random_numbers[i] > random_numbers[i+1]:
            time.sleep(0.15)
            os.system('clear')
            random_numbers[i], random_numbers[i+1] = random_numbers[i+1], random_numbers[i]
            keep_sorting = True
            for j in range(len(random_numbers)):
                if j == i:
                    print colors['HEADER'], '■' * random_numbers[i], random_numbers[i], colors['ENDC']
                elif j == i+1:
                    print colors['OKBLUE'], '■' * random_numbers[i+1], random_numbers[i+1], colors['ENDC']
                else:
                    print colors['BOLD'], '■' * random_numbers[j], random_numbers[j], colors['ENDC']
    iteration_length -= 1

os.system('clear')
print_simple_pyramid(random_numbers, colors['OKGREEN'])
