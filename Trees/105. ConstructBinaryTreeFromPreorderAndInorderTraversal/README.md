### Approach



1. DFS
    1. We use our pointer on pre_order to determine what node we need to make next
    2. Inorder tells us whether continue putting the processed pre_order node on the left subtree or not.
    3. So basically, let's say we are at the root node, when we call dfs on the left node, we have to pass the root node's value as "limit" as that is the node at which this left subtree ends. So then it prunes off the DFS call attempting to put that node in the wrong place.




Time: O(n)



Space: O(n)

