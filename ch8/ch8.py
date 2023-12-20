def rev_str(str, accum=""):
    if len(str) == 0:
        return accum
    hd = str[0] 
    tl = str[1:]
    return rev_str(tl, hd + accum)

print(rev_str("hey"))

def find_sub_str(str, sub):
    if len(str) == 0:
        return ""
    elif str.startswith(sub):
        return True
    return find_sub_str(str[1:], sub) 

print(find_sub_str("hey", "ey"))
