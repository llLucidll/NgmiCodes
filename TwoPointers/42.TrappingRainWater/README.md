**Approach**



1. First we initialize the left and right pointers. Then we initialize the left pointer value to l_max and right pointer to r_max
2. Then we have a while loop which makes sure the pointers dont cross past each other.
3. To decide which pointer to move, we compare l_max and r_max and move the value which is lower.
    1. When we move the pointer, we calculate the newly added water which is the difference between the max and the current of either l or r
4. Return the total water we have calculated.


Time: O(n) We parse through the entire list once


Space: O(1) We store constant memory space.