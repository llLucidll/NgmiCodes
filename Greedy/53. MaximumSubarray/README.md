**Approach**


1. First we initialize maxSum to first element in the list and curSum to 0
2. we traverse the list
    1. We add the number to curSum and update maxSum
    2. if curSum < 0 we set it to 0 before moving to the next iteration

Time: O(n) 1 for loop


Space: O(1)