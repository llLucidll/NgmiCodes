**Approach**



1. For the set method, we will employ a hashmap with an array in the values to hold timestamp data along with the associated value at that timestamp. {key: [[value, time], []]}
2. For the get method, we need to find the value at the timestamp equal to or less than the target timestamp. For this we can employ classic binary search as the timestamps are always sorted in ascending value
    1. We declare the l, r pointers
    2. We have two cases.
        1. If the mid value is > the target timestamp, we can discard the right subarray to lower our value
        2. If the mid value is <= the target timestamp, we can remember the value as our current best and remove the left subarray to find a more suitable candidate




Time: set: O(1) Hashmap setting operation. get: O(logn) where n is the length of the values array obtained during each get.



Space: O(m * n) Where m is the total number of keys and n is the highest number of values associated with any of the keys.