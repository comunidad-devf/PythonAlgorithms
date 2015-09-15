"""Binary Search."""

from random import randint


def binary_search(l, value):
    """Bynary Search."""
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) / 2
        if l[mid] > value:
            high = mid - 1
        elif l[mid] < value:
            low = mid + 1
        else:
            return mid
    return "{} It isn't in the list.".format(value)

n = int(raw_input("Into how many numbers do you want to search: "))
rn = set()
while len(rn) < n:
    rn.add(randint(1, 1000))

rn = sorted(list(rn))
print rn
n = int(raw_input("Which number do you want to find? "))
print binary_search(rn, n)
