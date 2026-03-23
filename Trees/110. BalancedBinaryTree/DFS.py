def isBalanced(root) -> bool:
    def dfs(node):
        if not node:
            return (True, 0)
        
        left, right = dfs(node.left), dfs(node.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return (balanced, max(left[1], right[1]) + 1)
    
    return dfs(root)[0]