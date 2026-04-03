class Solution:
    def rightSideView(self, root) -> list[int]:
        result = []

        def dfs(node, height):
            if not node:
                return 
            height += 1
            if len(result) < height:
                result.append(node.val)
            
            dfs(node.right)
            dfs(node.left)
        
        dfs(root, 0)
        return result