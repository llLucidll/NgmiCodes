class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNthFromEnd(head, n:int):
    ptr = delayed = head
    
    for i in range(n):
        ptr = ptr.next
    
    if not ptr:
        return head.next
    
    while ptr.next:
        ptr = ptr.next
        delayed = delayed.next

    # removing the nth element
    delayed.next  = delayed.next.next      

    return head