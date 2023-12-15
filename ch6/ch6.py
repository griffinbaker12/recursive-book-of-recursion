# you get the head, and then combine it with all combinations of the tail
# and you do this recursively for each tail
def all_ps(str):
    if len(str) <= 1:
        return str

    perms = []   
    head = str[0]
    tail = str[1:]

    tail_perms = all_ps(tail)
    for tail_perm in tail_perms:
        for i in range(len(tail_perm) + 1):
            new_perm = tail_perm[0:i] + head + tail_perm[i:]
            perms.append(new_perm)

    return perms

print(all_ps("hey"))

# if you have A, B, C
# you would get {B, C} and {C, B}
# Then you place A at each place within these characters
# There are 3 positions for each match (first, second, third), so the 
# total combos is 6

# to generate all of the combinations, you put each letter in each combo
# so you get the list of characters, the length of the password, 
# and you have to build up each possible permutation from a certain prefix
def all_lock_ps(chars, perm_len=None, prefix=""):
    if perm_len is None:
        perm_len = len(chars)

    if perm_len == 0:
        return [prefix]
    
    results = []
    for char in chars:
        new_prefix = prefix + char
        results.extend(all_lock_ps(chars, perm_len - 1, new_prefix))

    return results

# calling it perm len is nice because that is the sub-problem that you are solving; for some suffix and tail, combine all the perms
# of a given length and then combine that with the suffix
print(len(all_lock_ps('248JPB', 4)))

# K: size of the combination
def get_combos(str, k):
    if k == 0:
        return [""]
    elif len(str) == 0:
        return []
    
    hd = str[0]
    tl = str[1:]

    combinations = []

    # you have A as the head, and then you want all of the 1 combos of the tail, because then you can just add that head to the 
    # result of the tail
    
    tail_combos = get_combos(tl, k-1)

    print(tail_combos, 'the tcs are')

    # there may be combos for the tail as well of the same length that do not involve the head
    for tc in tail_combos:
        combinations.append(hd + tc)
   
    combinations.extend(get_combos(tl, k))

    return combinations

print(get_combos('ABC', 2))

def get_balanced_paren(pairs, open_rem=None, close_rem=None, current=""):
    if open_rem == None:
        open_rem = pairs
    if close_rem == None:
        close_rem = pairs
    

