**Approach**


1. We use a stack to store both the index and the value of the temperature in our input array. We also initialize a list array which is the size of the input.
2. Then we have a nested while loop which checks if the current temperature is greater than the one at the top of the stack
    1. If it is then we pop the last element in the stack and add it to our corresponding result index
3. At the end we return the results array



Time: O(n) Even though we have a nested loop it doesn't traverse more than O(n)



Space: O(n) We store the entire input array once in our results array