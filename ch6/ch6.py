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

# for the k-combos, you start at a point in the string, and pair it in all the ways you can with the chars at the end of the
# string
# know see why the leap of faith is useful; declarative in the sense that you tell the function
# what you want, and then focus on how to combine those to get the final result
# you trust the each recursive call will do its job, and your job is just to worry about combining
# these results in these recursive calls to get the final outcome
def k_combos(str, k):
    # base case here    
    if k == 0:
        return [""]
    elif str == "":
        return [""]

    hd = str[0]
    tl = str[1:]

    all_combos = []
    tail_combos = k_combos(tl, k-1)
    for tc in tail_combos:
        all_combos.append(hd + tc)
         
    all_combos.extend(k_combos(tl, k))

    return all_combos

print(k_combos('ABC', 2))

# takes an integer of the number of pairs of parens and returns a list of balanced
# strings
# can only add opening if you have a paren still to add
# can only add a closing if you have added more open than closing
def balanced_parens(num_pairs, openRem=None, closeRem=None, current=""):
    if openRem is None:
        openRem = num_pairs
    if closeRem is None:
        closeRem = num_pairs 

    if openRem == 0 and closeRem == 0:
        return [current]
    
    results = []
    if openRem > 0:
        results.extend(balanced_parens(num_pairs, openRem-1, closeRem, current + "(")) 
    if closeRem > openRem:
        results.extend(balanced_parens(num_pairs, openRem, closeRem-1, current + ")"))

    return results

print(balanced_parens(2))

def gen_ps(chars):
    if chars == "":
        return [""]

    all_cs = []
    hd = chars[0]
    tl = chars[1:]

    tl_cs = gen_ps(tl)
    for tc in tl_cs:
        all_cs.append(hd + tc)

    all_cs += tl_cs

    return all_cs

print(gen_ps("ABC"))
