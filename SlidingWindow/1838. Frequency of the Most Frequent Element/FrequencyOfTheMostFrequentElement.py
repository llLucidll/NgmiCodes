def maxFrequency(nums, k):
    # First we sort the array 
    nums.sort()

    # Then we initialize the pointers and the variables we are going to use
    result = total = 0
    l = 0

    for r in range(len(nums)):
        # increment our total by our right pointer extension's value
        total += nums[r]

        # the cost to raise the entire sliding window to the value of r is: nums[r] * len(window) - current_sum
        while nums[r] * (r - l + 1) - total > k:
            total -= nums[l]
            l += 1
        
        result = max(result, r - l + 1)
    
    return result
