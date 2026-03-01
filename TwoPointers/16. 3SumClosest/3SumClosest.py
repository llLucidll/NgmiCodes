def threeSumClosest(nums: list[int], target: int) -> int: 
    nums.sort() 
    result = None 
    diff = float("inf")

    for i in range(len(nums)):
        j = i + 1
        k = len(nums) - 1

        while j < k:
            res = nums[i] + nums[j] + nums[k]
            if res == target:
                return res 
            if abs(target - res) < diff:
                diff = abs(target - res)
                result = res 
            
            if res > target:
                k -= 1
            else:
                j += 1
    
    return result 
