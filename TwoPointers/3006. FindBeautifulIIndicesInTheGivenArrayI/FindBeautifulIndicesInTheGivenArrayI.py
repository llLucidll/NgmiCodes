def beautifulIndices(s, a, b):

    # Count occurences
    i = 0
    a_occur = []
    b_occur = []
    while i < len(s):
        if i + len(a) <= len(s) and s[i: i + len(a)] == a:
            a_occur.append(i)
        if i + len(b) <= len(s) and s[i: i + len(b)] == b:
            b_occur.append(i)
        i += 1
    
    # Calculate distance between occurences:

    l = 0
    r = 0
    result = []
    while l < len(a_occur):
        while r < len(b_occur) and b_occur[r] < a_occur[l] - k:
            r += 1
        if r < len(b_occur) and b_occur[r] <= a_occur[l] + k:
            result.append(i)
        l += 1
    
    return result
