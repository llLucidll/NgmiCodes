**Approach**



1. Binary search works by splitting a subarray in half each time we don't find the element in the subarray
2. This reduces our time complexity to logn to find the number in the array 
3. In binary search:
    1. We calculate the middle of the subarray
    2. If the middle value is less than the target then we increase the l pointer
    3. If the middle value is more than the target then we decrease the r pointer



Time: O(logn) Iterative splitting of the array at each step


Space: O(1)
