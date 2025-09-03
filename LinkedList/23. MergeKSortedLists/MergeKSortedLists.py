import heapq
class NodeWrapper:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val

def mergeKLists(lists):
    if len(lists) == 0:
        return None

    minHeap = []
    res = ListNode(0)
    curr = res

    for lst in lists:
        heapq.heappush(minHeap, NodeWrapper(lst))
    
    while minHeap:
        node_wrapper = heapq.heappop(minHeap)
        curr.next = node_wrapper.node
        curr = curr.next

        if node_wrapper.node.next:
            heapq.heappush(minHeap, NodeWrapper(node_wrapper.node))
    
    return res.next
