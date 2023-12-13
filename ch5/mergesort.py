import math

def mergesort(items):
    if len(items) == 0 or len(items) == 1:
        return items

    i_middle = math.floor(len(items) / 2)

    # ensure each half is sorted
    l = mergesort(items[:i_middle])
    r = mergesort(items[i_middle:])
    
    sorted_res = []
    i_left = 0
    i_right = 0

    # by the time you get to here, each half is in sorted order
    while len(sorted_res) < len(items):
        if l[i_left] < r[i_right]:
            sorted_res.append(l[i_left])
            i_left += 1
        else:
            sorted_res.append(r[i_right])
            i_right += 1

        if i_left == len(l):
            sorted_res.extend(r[i_right:])
            break
        elif i_right == len(r):
            sorted_res.extend(l[i_left:])
            break

    return sorted_res

my_l = [2, 9, 8, 5, 3, 4, 8, 6]
print(mergesort(my_l))
