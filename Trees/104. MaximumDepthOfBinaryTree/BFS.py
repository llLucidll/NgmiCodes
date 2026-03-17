from collections import deque
class Solution:
    def maxDepth(self, root):
        queue = deque()
        if root:
            queue.append(root)
        
        level = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level += 1
        return level