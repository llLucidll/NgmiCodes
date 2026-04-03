### Approach 



1. DFS
    1. At each node, we update our max_result = max(node.val + left + right, max_result).
    2. Then we use a separate value to bubble upwards for any other calculation which is max(node.val + left, node.val + right)
    3. At the end once we process all nodes our max_result will hold the maximum path sum we ever came across.


Time: O(n)



Space: O(1) We don't store anything extra 