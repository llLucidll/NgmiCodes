class Solution:
    def maxDepth(self, root):
        if not root: return 0

        depth = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return depth 