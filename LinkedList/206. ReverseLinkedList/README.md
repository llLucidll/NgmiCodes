**Approach**



1. For reversing a linkedList we just need to switch all the connections between the nodes in the other direction
2. For doing this, first we make the loop end if current is undefined.
3. Otherwise, we remember the original current.next to a temp variable
4. Then we put the value of current.next to the prev node which we also saved
5. And finally after we reverse the connection, we move on to the next node after updating prev to be the current.
6. At the end we return prev as current ends up being None outside of the LinkedList at the end of the code.