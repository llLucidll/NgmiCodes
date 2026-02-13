from collections import deque
def maxSlidingWindow(nums, k):
    if k >= len(nums):
        return [max(nums)]
    
    queue = deque()
    result = []

    l = 0 
    for r in range(len(nums)):
        if queue and l > queue[0]:
            queue.popleft()

        while queue and nums[r] > nums[queue[-1]]:
            queue.pop()
        
        queue.append(r)
        if r - l + 1 >= k:
            result.append(nums[queue[0]])
            l += 1
    
    return result
