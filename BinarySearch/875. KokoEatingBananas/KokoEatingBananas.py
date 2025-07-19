def minEatingSpeed(piles: List[int], h: int) -> int:
    l, r = 1, max(piles)

    while l <= r:
        k = (l + r) // 2

        time = 0
        for p in piles:
            time += -(-p//k)
        
        if time <= h:
            r = k - 1
        else:
            l = l + 1
    
    return l