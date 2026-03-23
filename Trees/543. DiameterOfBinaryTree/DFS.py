class Solution:
    def diameterOfBinaryTree(self, root) -> int: 
        def maxHeight(node):
            if not node: return 0
            return max(maxHeight(node.left), maxHeight(node.right)) + 1
        
        if not root: return 0
        return max(self.diameterOfBinaryTree(root.left), 
                   self.diameterOfBinaryTree(root.right), 
                   maxHeight(root.left) + maxHeight(root.right)
                   )
        