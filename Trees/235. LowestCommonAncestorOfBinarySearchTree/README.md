### approach


1. If both the nodes are less than our root node, we know the left subtree has the LCA, so we search that
2. Elif condition is that both are greater than so they are both in right subtree, search that
3. The else condition encompasses two things after passing through prior if elif:
    1. If the current node is not equal to p or not equal to q -> it is the LCA ( both are in diff subtrees)
    2. If the current node is equal to either p or q -> it is the LCA




Time: O(h) where h is the height of the subtree


Space: O(1) we don't use any additional space.