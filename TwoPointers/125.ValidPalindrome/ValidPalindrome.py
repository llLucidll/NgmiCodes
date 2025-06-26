def isPalindrome(s: str) -> bool:
    l = 0
    r = len(s) - 1

    while l < r:
        while l < r and not alphanum(s[l]):
            l += 1
        while r > l and not alphanum(s[r]):
            r -= 1
        
        if s[l].islower() != s[r].islower():
            return False
        
        else:
            l += 1
            r -= 1
    
    return True
    

def alphanum(s: str) -> bool:
    if (ord('a') <= ord(s) <= ord('z') or
        ord('A') <= ord(s) <= ord('Z') or
        ord('0') <= ord(s) <= ord('9')):
        return True
    else:
        return False