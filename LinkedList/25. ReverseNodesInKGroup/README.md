### Approach 


1. We use two pointers one fast to go ahead by k nodes and one slow that reverses the list up and until the fast node is reached.
2. Once the list is reversed we need to take care of connecting the two ends of it. One end must be connected to the previously reversed group and the other end must be connected to the "to be reversed" group in front of it as seen below: 

.. prev_group_tail → ? ...  [new_head → ... → group_tail] → next_group ...


3. So we keep track of the prev_group_trail to make the connection on the back and the current reversed list head to make the new connection to the rest of the list. 
4. This approach does reversing of k node groups in place



Time: O(n) we do this in a single pass



Space: O(1) we use no extra space, not even a recursion stack.