**Approach**



1. First we initalize the result array to be the same length as our nums array
2. Then we do the prefix update to result which means we multiply each element in result with prefix and update prefix *= nums[i]
3. Then we do the postfix update to result where we multiply each element in result with postfix in reverse order.
4. Return this accumulated result



Time Complexity: O(n) We parse through n inputs twice



Space Complexity: O(1) We store one element for prefix and one for postfix so we dont use any extra space 