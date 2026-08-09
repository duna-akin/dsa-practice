"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        otc = dict()
        otc[None] = None
        c = head
        while c:
            n = Node(c.val)
            otc[c] = n
            c = c.next  
        for o, c in otc.items():
            if c is None:
                continue
            c.next = otc[o.next]
            c.random = otc[o.random]    
        return otc[head]