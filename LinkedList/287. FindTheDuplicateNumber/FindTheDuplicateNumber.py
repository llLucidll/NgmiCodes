def findDuplicate(nums) -> int:
    # First we need to set the slow pointer to the correct location before the duplicate

    slow = 0
    fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        print(fast, slow)
        print()

        if slow == fast:
            break
    
    # Now we need to find the duplicate element
    slow2 = 0
    while True:
        slow2 = nums[slow2]
        slow = nums[slow]
        print(slow, slow2)
        print()

        if slow2 == slow:
            return slow

