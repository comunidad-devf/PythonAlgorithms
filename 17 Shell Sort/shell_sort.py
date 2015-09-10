"""Shell Sort."""

from random import sample


def shell_sort(u):
    """Shell Sort."""
    for i in range(1, len(u)):
        temporal_value = u[i]
        index = i
        while index > 0 and temporal_value < u[index - 1]:
            u[index] = u[index - 1]
            index -= 1
        u[index] = temporal_value

n = int(raw_input("Random numbers to sort: "))
random_numbers = sample(range(1, n+1), n)
print "Unsorted:", random_numbers
shell_sort(random_numbers)
print "Sorted:", random_numbers
