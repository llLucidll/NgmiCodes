def longestConsecutive(nums) -> int:
    numSet = set(nums)
    longest = 0

    for num in numSet:
        # To prevent duplicating our effort for subsets again
        if (num - 1) not in numSet:
            length = 1
            while (num + length) in numSet:
                length += 1
            longest = max(longest, length)
        
    
    return longest