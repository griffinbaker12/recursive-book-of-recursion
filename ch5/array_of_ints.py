# one advantage to implementing this in a way similar to mergesort by breaking things out to
# diff arrays, is that we could farm out the subproblems to diff. computers and have them work
# in parallel
# if cpus aren't getting much faster, makes coordinating work across multiple CPUs more
# important
# by "way similar to ms", you mean divide and conquer...lol

import math

def array_of_ints(items):
    if len(items) == 0:
        return 0
    # elif len(items) == 1:
    #     return items[0]

    mid = math.floor(len(items) / 2)
    l = array_of_ints(items[:mid])
    r = array_of_ints(items[mid:])

    return l + r

print(array_of_ints([10, 5, 8, 7, 2]))
