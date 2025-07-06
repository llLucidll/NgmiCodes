**Approach**



1. We need to remove the nth node from the end of the linked list. So we initialize two pointers one delayed n-1 steps behind the current
![alt text](image.png)
2. Here we run into a special case. If ptr points to a null after n movements then the nth node from the end ends up being head. So we return head.next
3. now our delayed pointer is n-1 steps behind the normal one, so we move the normal one until the end and the delayed will be the n-1th node from the end
4. We remove the nth node by setting the n-1th next node as the next.next node, skipping the connection to the nth node.



Time:O(n) We move through the entire list once'


Space:O(1) We don't store anything extra.