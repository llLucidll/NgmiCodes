def reorderList(head) -> None:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    second = slow.next
    slow.next = None
    prev = None

    while second:
        tmp = second.next
        second.next = prev

        prev = second
        second = second.next

    first, second = head, prev

    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next =  tmp1

        first = tmp1
        second = tmp2
    