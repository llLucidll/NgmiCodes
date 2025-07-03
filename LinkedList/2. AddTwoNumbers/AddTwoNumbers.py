
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    carry = 0

    while l1 or l2 or carry:
        # Our currentSum is equivalent to carry at the beginning
        currentSum = carry

        # Handling any null pointer errors
        if l1:
            currentSum += l1.val
            l1 = l1.next
        if l2:
            currentSum += l2.val
            l2 = l2.next
        # Carry is 1 if currentSum >= 10
        carry = currentSum // 10
        currentSum = currentSum % 10

        # Advancing our new LinkedList forward
        cur.next = ListNode(currentSum)
        cur = cur.next
    
    return dummy.next



        