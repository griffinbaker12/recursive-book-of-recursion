def recBinSearch(lst, to_find, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(lst) - 1

    mid = (start + end) // 2
    found = lst[mid]

    if start > end:
        return "Not found"

    if to_find == found:
        return mid
    elif found > to_find:
        return recBinSearch(lst, to_find, mid+1, end)
    else:
        return recBinSearch(lst, to_find, start, mid - 1)

print(recBinSearch([1, 7, 9], 7))

def iterBinSearch(lst, to_find):
    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = (start + end) // 2
        found = lst[mid]

        print(found, 'found')

        if to_find == found:
            return mid
        elif found > to_find:
            end = mid - 1
        else:
            start = mid + 1

    return "Not Found"

print(iterBinSearch([1, 5, 7, 9], 5))
