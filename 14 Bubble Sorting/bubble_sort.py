"""Bubble Sort."""

from random import sample


def bubble_sort(u):
    """Bubble Sort Function."""
    keep_sorting = True
    iteration_length = len(u)-1
    while keep_sorting:
        keep_sorting = False
        for i in range(iteration_length):
            if u[i] > u[i+1]:
                keep_sorting = True
                u[i], u[i+1] = u[i+1], u[i]
        iteration_length -= 1
    return u

n = int(raw_input("Random numbers to sort: "))
random_numbers = sample(range(n), n)
print "Unsorted:", random_numbers
bubble_sort(random_numbers)
print "Sorted:", random_numbers
