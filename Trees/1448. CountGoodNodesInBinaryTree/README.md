### Approach 


1. DFS 
    1. We have to maintain a curr_max for each path that we traverse. 
    2. Then we perform a depth first search passing this curr_max to each node.


2. BFS
    1. To our BFS queue we also append the curr_maximum to evaluate whether the node is good.
    2. Then we pass in the updated curr_max to all child nodes from that point


Time: O(n)


Space: O(1)
