def jump(nums) -> int:
    l = r = 0
    res = 0
    farthest = 0

    while l < len(nums) - 1:
        farthest = max(farthest, nums[l] + l)
        if l == r:
            res += 1
            r = farthest
        l += 1
    
    return res 
        
        