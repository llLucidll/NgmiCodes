class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        if not root:
            return False 
        if not subRoot:
            return True 
    
        if self.isSameTree(root, subRoot):
            return True 
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, root, subRoot) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False 

        return (root.val == subRoot.val and self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right))
    
