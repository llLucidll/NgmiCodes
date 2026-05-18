### Approach 

1. We use the concept of swapping in place instead of making a copy of the list at every point

2. So we start at a specific index in our backtracking function and then we swap index with another i in the range (index, len(nums))
3. Once we do this swap we start a backtracking call with it and then we undo this swap for future backtracking calls. (classic backtrack pattern)
4. This way our recursion tree does not store entire arrays in memory (The iteration solution would do this)




Time Complexity: O(n! * n). Explanation: There are n! possible orderings of a set so that's how many leaf nodes we have. At every leaf node we do nums.copy() which is an O(n) operation




Space Complexity: O(n) which is our deepest recursion depth.





