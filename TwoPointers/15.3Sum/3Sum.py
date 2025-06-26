def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    for i in range(len(nums)):
        j = i + 1
        k = len(nums) - 1
        if i > 0:
            if nums[i] == nums[i-1] and i < k:
                continue
        while j < k:
            if j > 0:
                while nums[j] == nums[j-1] and j < k:
                    j += 1
            if nums[i] + nums[j] + nums[k] == 0:
                result.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
            
            if nums[i] + nums[j] + nums[k] > 0:
                k -= 1
            else:
                j += 1
    
    return result
