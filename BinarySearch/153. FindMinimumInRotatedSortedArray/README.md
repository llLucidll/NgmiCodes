**Approach**


Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].


1. First we declare l and r pointers for carrying out our binary search.
2. Now the prime difference here is that the array might be a mix of sorted subarrays or it might just be randomness (n rotations) or it might be a completely sorted array (0 rotations)
3. So when we start our while loop we eliminate the condition that the current subarray we are in is already sorted. If we find l value is less than r value then we can just return the l value to be the minimum
4. If this is not the case, this might mean the r value is lesser or equal due to rotations, so we find the mid of the subarray and check if the mid is less than l or r value.
5. We decide the next subarray to continue binary search on by using this mid value to filter out the other half of the array.



Time: O(logn) Binary Search Time Complexity due to splitting



Space: O(1)