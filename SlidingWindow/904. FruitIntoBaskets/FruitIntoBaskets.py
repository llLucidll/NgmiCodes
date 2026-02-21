def totalFruit(fruits):
    l = 0
    r = 0

    freq = {}
    result = 0
    
    while l <= r and r < len(fruits):
        freq[fruits[r]] = freq.get(fruits[r], 0) + 1

        while len(freq.keys()) > 2:
            freq[fruits[l]] -= 1
            if freq[fruits[l]] == 0:
                del freq[fruits[l]]
            l += 1
        
        result = max(result, r - l + 1)
        r += 1
    
    return result