class Solution:
    def maxPathSum(self, root) -> int:
        result = float("-inf")

        def dfs(node):
            nonlocal result
            if not node:
                return 0 
        
            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right), 0)

            result = max(result, node.val + left_sum + right_sum)
            return node.val + max(left_sum, right_sum)

        dfs(root)
        return result