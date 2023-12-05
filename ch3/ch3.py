def sumArray(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sumArray(arr[1:])

print(sumArray([5, 2, 4, 8]))

def reverseString(str):
    if len(str) == 0:
        return ""
    else:
        return str[-1] + reverseString(str[:-1])

print(reverseString("hey"))

def isPalindrome(str):
    if len(str) == 0:
        return True
    head = str[0]
    tail = str[-1]
    mid = str[1:-1]
    return head == tail and isPalindrome(mid)

print(isPalindrome("racecar"))

def ackermann(m, n, indentation = None):
    if indentation is None:
        indentation = 0
    print('%sackermann(%s, %s)' % (' ' * indentation, m, n))

    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1, indentation + 1)
    elif m > 0 and n > 0:
       return ackermann(m - 1, ackermann(m, n - 1, indentation + 1), indentation + 1)

print('Starting with m = 1, n = 1:')
print(ackermann(1, 1))
print('Starting with m = 2, n = 3:')
print(ackermann(2, 3))

# ack (1, 1)
    # ack (1, 0) returns 2
        # ack (0, 1) returns 2
    # ack (0, 2) returns 3

def concatStr(strLst):
    if len(strLst) == 0:
        return ""
    return strLst[0] + concatStr(strLst[1:])

print(concatStr(['hello', 'world']))

# recursive sum, but what was really cool in the Art of FP book we read was that we then brought this a level
# up to apply some transormation (add, mult, etc) within a new abstraction we made called fold
def multArr(lst): 
    if len(lst) == 0:
        return 1
    return lst[0] * multArr(lst[1:])

print(multArr([1, 3, 5, 4]))


