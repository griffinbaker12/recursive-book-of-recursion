# factorial
# iterative
def iter_factorial(number):
    product = 1
    for i in range(1, number + 1):
        product = product * i
    return product
print(iter_factorial(5))

# recursive
def rec_factorial(number):
    if number == 1:
        return 1
    return number * rec_factorial(number - 1)
print(rec_factorial(5))

# recursive to iterative
def rec_to_iter_factorial(number):
    retVal = None

    callStack = []
    callStack.append({'returnAddr': 'start', 'number': number})
    
    while len(callStack) > 0:
        # print(callStack, 'the stack is')
        number = callStack[-1]['number']
        # print(number, 'the number is')
        returnAddr = callStack[-1]['returnAddr']

        if returnAddr == 'start':
            if number == 1:
                retVal = 1
                callStack.pop()
                continue
            else: 
                callStack[-1]['returnAddr'] = 'after recursive call'
                callStack.append({'returnAddr': 'start', 'number': number - 1})
                continue
        elif returnAddr == "after recursive call":
            retVal = number * retVal
            callStack.pop()
            continue
    return retVal

print(rec_to_iter_factorial(5), 'ret to iter')

# fibonacci 
def iterative_fib(nthNumber):
    # the first 2 numbers are 1
    a, b = 1, 1
    for i in range(1, nthNumber):
        a, b = b, a + b # get the next number
    return a
print(iterative_fib(10))

def recursive_fib(nthNumber):
    if nthNumber == 1 or nthNumber == 2:
        return 1
    return recursive_fib(nthNumber - 1) + recursive_fib(nthNumber - 2)

def memo_recursive_fib(nthNumber, memo):
    if nthNumber == 1 or nthNumber == 2:
        return 1
    elif nthNumber in memo: 
        return memo[nthNumber]
    v = memo_recursive_fib(nthNumber - 1, memo) + memo_recursive_fib(nthNumber - 2, memo)
    memo[nthNumber] = v
    return v

print(memo_recursive_fib(50, {}))

def rec_print_hello_world(timesToPrint):
    if timesToPrint == 0:
        return
    print("hello world")
    rec_print_hello_world(timesToPrint - 1)

rec_print_hello_world(5)

def findSubStr(needle, haystack):
    i = 0
    while i < len(haystack):
        if haystack[i: i + len(needle)] == needle:
            return i
        i = i + 1
    return -1

print(findSubStr('cat', 'My cat sophie'))

def findSubStrRec(needle, haystack, i = 0):
    if i > len(haystack):
        return - 1
    elif haystack[i: i + len(needle)] == needle:
        return i
    else: 
        return findSubStrRec(needle, haystack, i + 1)

print(findSubStrRec('cat', 'My cat sophie'))

def sumSeries(n):
    if n == 1:
        return 1
    return n + sumSeries(n-1)

print(sumSeries(5))

# naive
def sumPowersOf2(pow):
    if pow == 0:
        return 1
    return 2 ** pow + sumPowersOf2(pow - 1)

print(sumPowersOf2(4))

# gotta be some way to optimize b/c
# 2 ** 4 is really (2 ** 2) * (2 ** 2)
# and 2 ** 5 is really 2 * (2 ** 4)
def recSumPowersOf2(pow):
    if pow == 0:
        return 1
    return 2 ** pow + sumPowersOf2(pow - 1)

print(recSumPowersOf2(4))  # This should now output the correct sum of 2^0 + 2^1 + 2^2 + 2^3 + 2^4
