class Solution:
    def isValidBST(self, root, low = float("-inf"), high = float("inf")) -> bool:
        if not root:
            return True
        if root.val <= low or root.val >= high:
            return False 

        return self.isValidBST(root.left, low, root.val) and self.isValidBST(root.right, root.val, high)
    