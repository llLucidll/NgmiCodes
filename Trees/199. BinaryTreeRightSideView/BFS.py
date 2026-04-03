from collections import deque 
class Solution:
    def rightSideView(self, root) -> list[int]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            added = False 
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                if not added:
                    added = True 
                    result.append(node.val)
        
        return result 