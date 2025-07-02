**Approach**


1. We initialize two pointers one is slow and the other is fast
    1. The slow pointer moves one node at a time while the fast pointer moves two nodes ahead at a time.
    2. This means if there is a cycle, eventually the fast pointer will be able to catch up to the slow pointer and they will equate and break the loop
2. If there is no cycle, this condition will not be fulfilled until all nodes have been processed and the loop breaks



Time: O(n) Worst Case, we will have to go through the entire linked list once.


Space: O(1) We don't store anything extra