
def maxSubArray(nums) -> int:
    #
    maxSum = nums[0]
    curSum = 0

    # Kadane's Algorithm
    for num in nums:
        curSum += num
        maxSum = max(curSum, maxSum)
        if curSum < 0:
            curSum = 0
    
    return maxSum