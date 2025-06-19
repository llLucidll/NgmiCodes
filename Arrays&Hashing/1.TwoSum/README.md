**Approach**

1. Initialize a hashmap.
2. We parse through the array but at every index we do two things:
    i) We check if (target - current) is in our hashmap -> Return the pair
    ii) If not we remember this value to our hashmap.


Time: O(n) One for loop
Space: O(n) Copies all elements in original list