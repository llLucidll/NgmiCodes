### Approach 


1. How do we prevent duplicates in our final result array? Think of it like this:
[1,2,1] -> sort -> [1,1,2]
2. Now, if our current pointer (index i) value is equal to the next, then we skip ahead for the next call. Why? because we already generate subsets with that from our pointer at i (dfs(i + 1) call) so we don't need to start that process again and duplicate it after.

3. So the flow goes like this ->
    1. We add the number and make a dfs call with that subset
    2. Then we pop the number and we check if the next index we would call is the same number. If it is, then we just skip it.
    3. We add to our result array whenever our i goes out of bounds.




Time: O(n * 2^n)   at each level of the backtracking tree, we generate k*2 new nodes where k is the number of nodes in that level.
So for n = 3, we get this 1 node (no elements) -> 2 nodes -> 4 nodes -> 8 nodes == 2^n. For a list of unique elements. It's multiplied by n because at each of these nodes, we copy subset into our result.



Space: O(n) extra space and O(2^n) space for results.