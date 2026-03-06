### Approach 


1. First we sort the array based on the start value of every interval
2. Then we go through the array to make our new output array. There are two distinct cases:
    1. The ending value of the current thing at the top of our output is greater than or equal to the start value of the new interval to be added, in this case we merge the intervals (by setting the last value to the greater of our old end value or the newly incoming end value)
    2. Otherwise, we just append the interval regularly to our new output array




Time: O(n) We do this in a single pass of the array 


Space: O(n) we store a copy of the array at worst case (no merges done)