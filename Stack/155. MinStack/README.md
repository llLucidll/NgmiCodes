**Approach**


1. Whenever we push an element into the stack, we add the difference between the current min and the value being added (current - self.min)
    1. This works because whenever we remove the minimum element from the stack, we update the minimum and since we can only pop in the order the elements were added, the minimum will change as required
    2. We do this so that we do not have to do an O(n) operation for finding the minimum
2. For the pop, we change the minimum by the value being popped if its negative. If stack is empty then we just return
3. For obtaining the top element, we just add the minimum to the current value if its postive and otherwise we just return the minimum.



Time: O(1) 


Space: O(n) We will store n elements as required in our stack.