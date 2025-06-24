**Approach**


1. First we initialize a stack and our dictionary for mapping the closing brackets to the open brackets.
2. Then we validate our input, if it starts with a closing bracket return false
3. Finally we parse the string. If its an opening bracket we add it to our stack. If its a closing bracket, we check if theres a corresponding open bracket in the stack and then pop or if not we return False

4. Lastly we check if the stack is empty to return True and False otherwise


Time: O(n) 1 for loop


Space: O(n) it is possible in the worst case to store n-1 length string inside our stack at once.