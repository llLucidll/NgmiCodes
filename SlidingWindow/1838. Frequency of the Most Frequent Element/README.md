### Approach

1. First we initialize our sliding window l and r pointers both starting at 0
2. We increment the right pointer as part of our for loop.
3. Then we check if we can up the entire sliding window to the current nums[r]
4. If we can, then we update result to be that new length 
5. We have a while loop on the inside for when we cannot increment the entire sliding window (formula > k)
6. In this case, we start increment the left pointer (since the left value is the one that's costing us the most operations currently)


### Time Complexity:

O(nlogn) from the sorting that we are required to do to be able to solve this question


### Space Complexity:

We are not storing anything extra so the space complexity is 0.