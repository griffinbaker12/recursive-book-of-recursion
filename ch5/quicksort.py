# works by repeatedly partinioning until you hit a base case
# so the algorithm is:
# pick a partition
# move everything less to the left
# everything greater to the right
# keep doing this recursively for each partition until you hit a base  case

# so the questions are...

def qs(items):
    return qs([x for x in items[1:] if x <= items[0]]) + [items[0]] + qs([x for x in items if x > items[0]]) if items else []

print(qs([1, 2, 5, 4, 5, 4, 4]))

def quicksort(items):
    if len(items) <= 1:
        return items
    partition = items[-1]
    l = [x for x in items if x < partition]
    m = [x for x in items if x == partition]
    r = [x for x in items if x > partition]
    return quicksort(l) + m + quicksort(r)

print(quicksort([1, 2, 5, 4, 5, 4, 4]))

def quicksort2(items, l=None, r=None):
    if l is None:
        l = 0
    if r is None:
        r = len(items) - 1

    if r <= l:
        return

    i = l
    pivot = items[r]
    for j in range(l, r):
        # move to the left of the array
        if items[j] <= pivot:
            items[i], items[j] = items[j], items[i]
            i += 1
    print(items)

    # swap the pivot with val at i
    items[r], items[i] = items[i], items[r]
    print(items)
    
    quicksort2(items, l, i-1)
    quicksort2(items, i+1, r)
     

myList = [1, 5, 20, 9]
quicksort2(myList)
print(myList)
