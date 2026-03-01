### Approach 


1. The constraint on the problem is that we need to find the peak element in O(logn)
2. So we employ binary search to essentially just look for a local maxima. 
3. If an element is at the end of an array, we assume the element outside the array is lower than our element, ie any element on the edge of the array just needs to be checked against it's previous element inside of the array.




Time: O(logn) Binary Search reduces the search space in half each time



Space: O(1) we don't store anything extra