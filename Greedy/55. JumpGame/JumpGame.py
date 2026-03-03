def canJump(nums) -> bool:
    if len(nums) == 1:
        return True 
    
    goal = len(nums) - 1

    for i in range(len(nums) - 2, -1, -1):
        if nums[i] + i >= goal:
            goal = i 
    
    return goal == 0