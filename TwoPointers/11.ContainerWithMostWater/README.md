**Approach**



1. First we initialize a max_area and left and right pointers on the heights array.
2. At each loop iteration we calculate the current volume of water held and update our max if the current is greater
3. To decide which pointer to move, we check which of the values are greater in the heights array.


Time: O(n) We parse through the entire heights array once


Space: O(1) We only store constant amount in memory.