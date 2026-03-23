from collections import deque
def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root

    queue = deque([root])

    while queue:
        node = queue.popleft()
        if p.val < node.val and q.val < node.val:
            queue.append(node.left)
        elif p.val > node.val and q.val > node.val:
            queue.append(node.right)
        else:
            return node