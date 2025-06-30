**Approach**



1. The reason we are using a stack for this is because, as soon as we run into an operator we can process the arithmetic for the last two values in the RPN.
2. If the tokens are numbers, we append them to the stack
3. If the tokens are operators, we pop the last two numbers in the stack and append the operation result to the stack again
4. At the end the top of the stack is the output of the program



Time: O(n) We parse through the entire list once.


Space: O(n) At worst case, we can have a stack that has the entire input list inside it.