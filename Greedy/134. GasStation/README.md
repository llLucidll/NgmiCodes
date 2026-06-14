### Approach 


1. We keep track of the current sum as we iterate through the array.
2. When our current sum drops below 0, we know there is no way we start from the index we were previously starting at
    (Impossible to get past this stretch), So we set the index to current + 1
3. At the end once we are done, we check if total_sum is negative in which case we know it's impossible to traverse the circuit.




Time: O(n) we only do one pass


Space: O(1) we don't store anything extra.

