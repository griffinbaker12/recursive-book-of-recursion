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
