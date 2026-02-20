### Approach

Initially when I solved this problem I split the sorted array into "good buys" and "good sells" (along the middle of the sort)

My thinking was too narrow for this problem, I was trying to think of the future too much, the trick to the question is realizing that you can make unlimited transactions, so you should be trying to buy and sell everytime the next value is higher than your current value.


1. If prices[i - 1] < prices[i] we should add the difference to our profit.
2. Then we just return that profit



Time: O(n) We do a single pass through the entire array 



Space: O(1) we just store our result array.
