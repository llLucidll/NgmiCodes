**Approach**



1. We will be discussing the Doubly Linked List Solution.
2. First we initialize the Node class which has attributes next and prev.
3. Then we initialize the LRU cache with capacity, a cache to store key-value pairs and self.left and self.right which are the bounds of our LRU
4. We define two operations insert and remove:
    1. Remove: We remove that node from the double linked list and make adjustments to make this work
    2. Insert: We insert the element on the right most point and make adjustments to make this work
5. For the get operation, we first remove the element from the list then add it back in making it the most recently accessed element (LRU) then we return its value
6. For the put operation, first if the key already exists in our cache, we remove it from the linked list, then we set the new value of that key to the Node (key, value). If we are at capacity we remove the leftmost element 



Time: O(1) for get and put 



Space: O(n) We store all the n elements