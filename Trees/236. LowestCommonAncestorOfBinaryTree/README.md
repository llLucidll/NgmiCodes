### Approach

There's just one concept you need to understand. If the current root is p or q, we should return the current root as that is the solution. If current root is None, we return None

If the current root is not p or q, we search the left subtree and the right subtree in parallel for p or q. If we find p or q in both that means our current root is the common ancestor between the two subtrees, but if only either one of the subtrees returns as true, then we just return that node (left or right) as that is the lowest common ancestor.


Time: O(n) We only traverse all n nodes once.


Space: O(1) We don't use any extra space for this algorithm