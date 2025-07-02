# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    prev = None
    current = head
    
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    
    return prev