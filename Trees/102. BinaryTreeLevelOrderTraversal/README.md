### Approach 



1. BFS
    1. We only use BFS for this problem because we want a level by level traversal of the tree, using DFS for it makes it awkward
    2. use a for loop that iterates through the entire queue (entire level)



Time: O(n) We have to go through all nodes in the tree to get all the nodes in a level order traversal


Space: O(n) we store all n nodes in an array.