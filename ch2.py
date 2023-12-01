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
