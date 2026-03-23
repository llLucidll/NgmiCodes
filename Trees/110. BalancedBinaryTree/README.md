### Approach 

1. We need to check if the height of the left subtree and right subtree's differences are less than or equal to 1. Otherwise we return false

2. Our DFS base case is if the current node is None, we return True and a height of 0
3. Otherwise we check left and right and make sure their difference is valid and then propogate this up through the tree from the base case of a None node.



Time: O(n)


Space: O(1)
