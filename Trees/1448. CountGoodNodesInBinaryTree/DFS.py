class Solution:
    def goodNodes(self, root) -> int:
        result = 0
        def dfs(node, curr_max):
            nonlocal result 
            if not node:
                return 0
            
            if node.val >= curr_max:
                result += 1
                curr_max = node.val
            
            dfs(node.left, curr_max)
            dfs(node.right, curr_max)
        
        dfs(root, float("-inf"))
        return result
