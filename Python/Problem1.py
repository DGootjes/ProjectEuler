"""
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def find_sum_of_multiples_below(max_number: int):
    summed_total = 0
    for i in range(0, max_number):
        if (i % 5 == 0) | (i % 3 == 0):
            summed_total += i
    return summed_total


# Main
print(find_sum_of_multiples_below(1000))
