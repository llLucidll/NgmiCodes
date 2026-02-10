def minimumWindowSubstring(s: str, t: str) -> str:
    if len(t) > len(s):
        return ""
    
    window = {}
    required = {}
    have, need = 0, len(t)
    res = [0, 0]
    res_length = float("inf")

    for char in t:
        required[char] = required.get(char, 0) + 1
    
    l = 0
    for r in range(len(s)):
        window[s[r]] = window.get(s[r], 0) + 1
        if s[r] in required and window[s[r]] == required[s[r]]:
            have += 1
        
        while have == need:
            if r - l + 1 < res_length:
                res = [l, r]
                res_length = r - l + 1
            window[s[l]] -= 1
            l += 1
            if s[l] in required and window[s[l]] < required[s[l]]:
                have -= 1
    
    r, l = res
    return s[l: r + 1] if res_length < float("inf") else ""
            
