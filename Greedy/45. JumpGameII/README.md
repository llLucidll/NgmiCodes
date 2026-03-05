### Approach 


1. We need to find the *Minimum* number of jumps to get to the end of the array.
2. At each point there is a farthest jump that we can get to, we keep track of this as we go through the subarray that we can jump through
3. Once we complete our scan, we start looking for the next farthest jump we can take
4. So we use the right pointer to track the current farthest jump we can take, as soon as the left pointer reaches the right pointer, we take our next farthest jump (which we scanned as we advanced our left pointer forwards) and increase our number of jumps by 1
5. An edge case is to only advance l until len(nums) - 1, this is because in the cases where we land exactly at the end of the array, we actually count one more jump for no reason (even though our farthest jump has already taken us to the end of the array and right pointer is on it)



Time: O(n) We only do one scan of the entire array 


Space: O(1) we dont store anything extra 