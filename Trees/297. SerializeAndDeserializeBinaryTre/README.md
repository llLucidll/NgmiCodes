### Approach 



1. DFS:
    1. Serialize
        Use dfs preorder.
        If node is null → append "N".
        Else append node value.
        Recursively process left child, then right child.
        Join list with commas → return string.
        



    2. Deserialize
        Split string into list vals.
        Use an index to process values in order.
        If current value is "N" → return None.
        Otherwise create a node.
        Recursively build left subtree.
        Recursively build right subtree.
        Return the root.





2. BFS:
    1. Serialize
        If root is None → return "N".
        Initialize a queue with root.
        While queue is not empty:
        Pop a node.
        If node exists → append its value, push left & right children.
        If node is missing → append "N".
        Join the list with commas and return.




    2. Deserialize
        Split string into list vals.
        If first value is "N" → return None.
        Create root from first value and push it into a queue.
        Use an index to read the next values:
        For each node popped from queue:
        If vals[index] is not "N" → create left child & push.
        Move index.
        Repeat for right child.
        Return the root of the rebuilt tree.
    



Time: O(N) we go through all N nodes of the tree for both methods.




Space: O(N) We store the entire tree in serialized format, N extra space 