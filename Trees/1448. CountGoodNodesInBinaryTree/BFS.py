from collections import deque
class Solution:
    def goodNodes(self, root) -> int:
        queue = deque([(root, root.val)])
        result = 0

        while queue:
            node, curr_max = queue.popleft()

            if node.val >= curr_max:
                result += 1
                curr_max = node.val
            
            if node.left:
                queue.append((node.left, curr_max))
            if node.right:
                queue.append((node.right, curr_max))
        
        return result 