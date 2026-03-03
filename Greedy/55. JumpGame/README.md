### Approach 


1. We start searching from the end of the array and at each new index, if we can have jumped to our current goal state with it, then we take that as our goal state


2. This helps us prune away bad indices that may have led to non-end of array goal states.



Time: O(n) we only do a single pass


Space: O(1) We don't store anything extra