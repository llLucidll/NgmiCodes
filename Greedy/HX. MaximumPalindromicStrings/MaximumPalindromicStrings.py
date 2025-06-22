from collections import Counter
def countPalindromes(arr) -> int:
    total_counter = Counter()
    lengths = []
    for s in arr:
        # Append our length so we can greedily make palindromes later
        lengths.append(len(s))
        # mapping the letters in s to its count
        total_counter.update(s)
    
    # Counting the letters we have 
    C = 0 # Pair letters
    S = 0 # Single characters
    for c in range(ord('a'), ord('z') + 1):
        char = chr(c)
        count = total_counter[char]
        C += count // 2
        S += count % 2
    
    lengths.sort()

    P = 0 # How many pairs we have used
    O = 0 # How many single letters we have used
    count = 0

    for length in lengths:
        # pairs needed
        P_needed = length // 2
        # Singles needed (if odd length)
        O_needed = length % 2

        #Total we have used so far
        Pt = P + P_needed
        Ot = O + O_needed

        # If we have exceeded the number of pairs we can use
        if Pt > C:
            break
        # For the edge case where we have more pairs than singles, we may break up the pairs
        singles = 2 * (C - Pt) + S
        # If we have exceeded the number of singles we can use
        if Ot > singles:
            break
        
        
        P = Pt
        O = Ot
        count += 1
    
    return count




    



    
