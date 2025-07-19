**Approach**



1. Let us realize two facts about the problem first. Value of h is greater than or equal to length of piles array. This means
    1. Upper bound is maximum value in piles.
    2. Lower bound is 1 (if all the values in the array are 1, lowest positive value)
2. So now we have our search space defined as k is a value between [l,r] = [1, max(piles)]
3. We perform binary search algorithm to narrow the search space down. When we have a k, we calculate the time taken to eat all the bananas in the array and then:
    1. If time taken is less than/equal to the required h, we choose the left subarray as we can optimize the value further
    2. If time taken is more than the required h, we choose the right subarray so we can eat faster to hit the time quota.
    3. When the time taken is equal to h, we try to optimize it further by picking the left subarray and if no further optimizations are possible, then the while loop ends up exitting and we can return l which is basically the lowest optimal eating rate.


# Neat trick for calculating time (Instead of using math.ceil). // Is natively floor operation (math.floor) so to obtain math.ceil we take -(-p//k) which gives us the math.ceil.



Time: O(n * logm) where n is the size of the array (Finding the max in piles) and m is the highest number of bananas in the pile (We do logm binary search steps)




Space: O(1) We don't store anything extra.
