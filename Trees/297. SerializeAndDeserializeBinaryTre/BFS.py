from collections import deque
class Codec:
    def serialize(self, root) -> str:
        if not root:
            return "N"

        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                result.append("N")
            else:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        
        return ",".join(result) 

    def deserialize(self, data):
        data = data.split(",")

        if data[0] == "N":
            return None
    
        head = TreeNode(int(data[0]))
        queue = deque([head])
        index = 1
        while queue:
            node = queue.popleft()
            if data[index] != "N":
                node.left = TreeNode(int(data[index]))
                queue.append(node.left)
            index += 1
            if data[index] != "N":
                node.right = TreeNode(int(data[index]))
                queue.append(node.right)
            index += 1
        return head
