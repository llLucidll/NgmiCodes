### Approach:




1. BFS
    1. Most intuitive solution, at every level, we take the right most node and then clear our queue of that entire level. Once we have added a node at a specific level, we set the added flag to true and just empty our queue.

2. DFS
    1. We keep track of the height and if our current height is less than the length of our result array, this means we haven't got a node for this level yet
    2. So we add that node.
    3. We go down right subtrees before we go down left subtrees and the constraint above ensures that we always get the right most side view





Time: O(n) We do need to visit every single node in the tree



Space: O(n) At worst case, we may have a tree with n nodes at n levels meaning we have to store all n.