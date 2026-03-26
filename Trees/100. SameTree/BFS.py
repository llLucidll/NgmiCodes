from collections import deque
class Solution:
    def isSameTree(self, p, q) -> bool:
        pQ = deque([p])
        qQ = deque([q])

        while pQ or qQ:
            p_node = pQ.popleft()
            q_node = qQ.popleft()

            if p_node == None and q_node == None:
                continue 
            elif p_node == None or q_node == None or p_node.val != q_node.val:
                return False 

            pQ.append(p_node.left)
            pQ.append(p_node.right)
            qQ.append(q_node.left)
            qQ.append(q_node.right)
            
        return True 