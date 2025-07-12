def search(nums: List[int], target:int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = l + ((r-l)//2)

        if nums[m] > target:
            r -= 1
        elif nums[m] < target:
            l += 1
        else:
            return m
    
    return -1