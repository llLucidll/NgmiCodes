### Approach 

1. We use a monotonic queue to solve this problem (strictly decreasing queue)
2. Everytime we increment the right pointer, we check two things:
    1. It's a valid window (of length k), then we also increment the left pointer and find the current max and append that from the queue
    2. We check if the new right pointer value is greater than the bottom of our queue. If it is, we pop the values until this is not true
3. We return the result array at the end once we reach the end of the subarray.



Time: O(n) Since we only pass through the array once

Space: O(1) We are not storing anything extra (not counting the array we are using to hold the results)