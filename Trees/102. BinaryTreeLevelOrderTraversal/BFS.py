from collections import deque 
class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            curr = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(curr) 
        return result