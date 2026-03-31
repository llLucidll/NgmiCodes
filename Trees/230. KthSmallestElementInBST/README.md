### Approach 

Why do we only have a DFS solution? -> think about it, we have a BST, and we want to maintain this sorted order (by traversing the left then the root then the right), BFS does not do anything for this so it is counter productive to use BFS.

1. DFS 
    1. We traverse the left then the root then the right node. 
    2. We return the node.val our k hits zero.



Time: O(n)


Space: O(1) we don't store anything extra