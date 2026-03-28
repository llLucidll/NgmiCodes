from collections import deque
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        queue = deque([root])
        parent = {root: None}

        while p not in parent or q not in parent:
            node = queue.popleft()
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)

        ancestors = set() 

        while p:
            ancestors.add(p)
            p = parent[p]
        
        while q not in ancestors:
            q = parent[q]
        
        return q