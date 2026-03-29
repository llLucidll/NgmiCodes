from collections import deque
class Solution:
    def isValidBST(self, root) -> bool:
        queue = deque([(root, float("-inf"), float("inf"))])
    
        while queue:
            node, low, high  = queue.popleft()
            if node.val <= low or node.val >= high:
                return False 

            if node.left:
                queue.append((node.left, low, node.val))
            if node.right:
                queue.append((node.right, node.val, high))
        
        return True 