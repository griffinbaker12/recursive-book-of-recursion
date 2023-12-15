# P1: Generate all of the permutations given a string of characters
# So you have:
# A, and you want to generate {B, C} and {C, B}, and then place A in between all of those elements
# B, and you want to gen {A, C} and {C, A}, and then...
# C ...
# These do really lead themselves to recursion
# The steps that the author lays out are definitely a systematic approach to tackle a recursive problem
# Boils down to: how are you going to split the smaller problems into sub-problems that approach a base case, and then how to do you plan
# to combine the returned values to gen the ultimate return value (final answer) (how do the sub-problem answers combine to form the ult. ans)
def all_perms(str):
    # if it is 0 or 1, then just return the str
    if len(str) < 2:
        return str

    hd = str[0]
    tl = str[1:]

    # b/c you combine the head will all of the combos of the tail
    tail_perms = all_perms(tl)

    final_perms = []

    for perm in tail_perms:
        for i in range(len(perm) + 1):
            final_perms.append(perm[0:i] + hd + perm[i:])

    return final_perms

res = all_perms("ABCD")
print(res, len(res))

# you are going to take each number, and then iterate through all of the other characters at each position
# so if you have ABC, and 2 positions, you want to do:
# these are combinations, but the order matters (so perm with replacement I think is the proper term)
# "Permutation w/ repetition"
# A -> AA, AB, AC
# B -> BA, BB, BC
# C -> CA, CB, CC
# Base case: str length that is the the same as the len of the locks (issue is how would you distinguish from the base)
# So cleaner just to say when the index is OOB
# Recursive case: return the letter + the recursive combos for the tail
def all_locks_ps(chars, pwd_len, prefix=None):
    if prefix is None:
        prefix = ""
    elif len(prefix) == pwd_len:
        return [prefix]

    tail_prefixes = []
    for char in chars:
        new_prefix = prefix + char
        tail_prefixes.extend(all_locks_ps(chars, pwd_len, new_prefix))
    
    return tail_prefixes

print(all_locks_ps('ABC', 2))
