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
        otc = {}
        otc[None] = None

        cur = head
        while cur:
            otc[cur] = Node(cur.val)
            cur = cur.next
        
        for orig, copy in otc.items():
            if not copy:
                continue
            copy.next = otc[orig.next]
            copy.random = otc[orig.random]
        
        return otc[head]