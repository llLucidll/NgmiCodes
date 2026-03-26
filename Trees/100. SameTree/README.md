### Approach 



1. DFS:
    1. We define the base case which is if both nodes are null (return True) if one node is null while the other is not, or their values are not the same (return False) 
    2. Then we just recurisvely call the function on the left and right subtrees.


2. BFS:
    1. We maintain concurrent queues for both P tree and Q tree. 
    2. We run into two cases, if p_node and q_node are both None 



Time: O(n) at worst case we go through all nodes



Space: O(1) we don't store anything extra