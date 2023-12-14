def selection_sort(items, idx=None):
    if idx == None:
        idx = 0
    elif idx == len(items):
        return items
    min_idx = idx
    for i in range(idx, len(items)): 
        if items[i] < items[min_idx]:
            min_idx = i
    items[idx], items[min_idx] = items[min_idx], items[idx]
    return selection_sort(items, idx+1)

print(selection_sort([1,3,8,8,5,10,7,0,2]))
