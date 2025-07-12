**Approach**


![alt text](image.png)

1. First we declare a slow and fast pointer to get to the halfway point of the linked list
2. Second we reverse the second half of the linked list from slow -> fast after reaching the halfway point
3. Thirdly we set two pointers pointing to head and prev (prev is the node which we have after the second half is reversed. So prev.next traverses the list from the end in reverse)
4. We do an iterative process until second becomes undefined (As when we reverse the list we set the next node at the start of the half to None)
5. In this iterative process we reorder the list in the following way:
    1. Remember the first.next and second.next
    2. Set first.next = second
    3. Now we need first.next.next  = old first.next so we do second.next = tmp1 (second.next = first.next)