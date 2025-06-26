**Approach**


1. We want to take advantage of the fact the array is sorted. This means we dont have to remember anything to memory like the usual TwoSum.
2. We use two pointers at opposite ends of the list and there arises two cases:
    1. The current sum of the two is greater than the target -> move the right pointer left
    2. The current sum of the two is lesser than the target -> move the left pointer right
3. If we find the correct sum, we have to 1 index the indices so first we take the indices and put them in a list and then we add +1 to both values in the list.


Time: O(n) We parse through the entire list once


Space: O(1) We dont store anything new into memory.