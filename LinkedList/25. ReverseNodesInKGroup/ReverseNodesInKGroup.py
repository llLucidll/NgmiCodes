def reverseKGroup(head, k: int):
    # helper functions 
    def reverse(node, end):
        prev = None 
        while node:
            if node == end:
                return prev 
            temp = node.next 
            node.next = prev 
            prev = node 
            node = prev 
        return prev 

    def skip(node, curr_k):
        while node and curr_k > 0:
            node = node.next
            curr_k -= 1
        else:
            if curr_k > 0:
                return None, False 
            else:
                return node, True 
    
    slow = fast = head 
    cursor = ListNode(0)
    temp_head = cursor.next 

    while fast:
        fast, valid = skip(fast, k)
        if not valid:
            break 
        
        group_tail = slow 
        slow = reverse(slow, fast)
        temp_head.next = slow 
        group_tail.next = fast 
        temp_head = group_tail 
        slow = fast 
    
    return cursor.next 