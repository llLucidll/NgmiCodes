class Solution:
    def buildTree(self, preorder, inorder):
        pre_index = in_index = 0

        def dfs(limit):
            nonlocal pre_index, in_index
            if pre_index >= len(preorder):
                return None 
            if inorder[in_index] == limit:
                in_index += 1
                return None 
        
            root = TreeNode(preorder[pre_index])
            pre_index += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)

            return root 
    
        return dfs(float("inf"))