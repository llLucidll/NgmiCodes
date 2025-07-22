class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



def copyRandomList(head):
    cur = head
    hash = {None: None}

    while cur:
        copy = Node(cur.val)
        hash[cur] = copy
        cur = cur.next
    
    cur = head
    while cur:
        copy = hash[cur]
        copy.next = hash[cur.next]
        copy.random = hash[cur.random]
        cur = cur.next
    
    return hash[head]
