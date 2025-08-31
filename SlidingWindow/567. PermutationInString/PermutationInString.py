def checkInclusion(s1: str, s2: str) -> bool:
    # Edge Case we can remove from the start
    if len(s1) > len(s2):
        return False

    s1Count, s2Count = [0] * 26, [0] * 26

    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1
    
    matches = 0
    for i in range(26):
        if s1Count == s2Count:
            matches += 1
    
    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True

        char = s2[r]
        s2Count[ord(char) - ord('a')] += 1

        if s1Count[ord(char) - ord('a')] == s2Count[ord(char) - ord('a')]:
            matches += 1
        elif s1Count[ord(char) - ord('a')] + 1 == s2Count[ord(char) - ord('a')]:
            matches -= 1
        
        char = s2[l]
        s2Count[ord(char) - ord('a')] -= 1
        if s1Count[ord(char) - ord('a')] == s2Count[ord(char) - ord('a')]:
            matches += 1
        elif s1Count[ord(char) - ord('a')] - 1 == s2Count[ord(char) - ord('a')]:
            matches -= 1
        l += 1

    return matches == 26 
    