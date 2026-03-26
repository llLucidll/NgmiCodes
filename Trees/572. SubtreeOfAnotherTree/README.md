### Approach 


1. We basically want to find the right subTree to run our isSameTree algorithm on. This builds on top of isSameTree problem.
2. Basically if the current node.val == subTree.val then we run isSameTree from that point on. Otherwise we continue searching for the right node to start our isSameTree search from.



Time: O(n) Worst case we go through all nodes in the main tree.


Space: O(1) we don't store anything extra.