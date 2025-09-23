**Approach**



1. We predefine an array in memory which is twice the size of nums
2. We start inserting the elements from nums into both the 0th index and the 0 + len(nums) index
3. We do this for all elements



Time: O(n) we only need a single n pass for both halves of the array



Space: O(2n) we have an array double the size of original