import math
# does mult using addition, subtraction, and a precomputed mult table

# create the lookup table
# using more mem lets us speed up the algo
mult_table = {}
for i in range(10):
    for j in range(10):
        mult_table[(i, j)] = i * j

print(mult_table)

def pad_zeros(number_str, num_zeros, insert_side):
    if insert_side == "left":
        return '0' * num_zeros + number_str
    else:
        return number_str + '0' * num_zeros

def k_mult(x, y):
    # need to split x -> (a, b) and y -> (c, d)
    # mult a and c from the table or on a recursive call
    # mult b and d from table or recursive call
    x = str(x)
    y = str(y)

    if len(x) == 1 and len(y) == 1:
        return mult_table[(int(x), int(y))]
    
    if len(x) < len(y):
        x = pad_zeros(x, len(y) - len(x), 'left')
    elif len(y) < len(x):
        y = pad_zeros(y, len(x) - len(y), 'left')

    half_of_digs = math.floor(len(x) / 2)
   
    # x and y are the same len at this point (adding the vals to the L doesn't change anything)
    a = int(x[:half_of_digs])
    b = int(x[half_of_digs:])
    c = int(y[:half_of_digs])
    d = int(y[half_of_digs:])

    step1 = k_mult(a, c)
    step2 = k_mult(b, d)
    step3 = k_mult(a + b, c + d)

    step4 = step3 - step2 - step1

    step1Padding = (len(x) - half_of_digs) + (len(x) - half_of_digs)
    step1PaddedNum = int(pad_zeros(str(step1), step1Padding, 'right'))

    step4Padding = (len(x) - half_of_digs)
    step4PaddedNum = int(pad_zeros(str(step4), step4Padding, 'right'))

    return step1PaddedNum + step2 + step4PaddedNum

print(k_mult(1357, 2468))
