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
        origToCopy = collections.defaultdict(lambda: Node(0))
        origToCopy[None] = None

        curr = head
        while curr:
            origToCopy[curr].val = curr.val
            origToCopy[curr].next = origToCopy[curr.next]
            origToCopy[curr].random = origToCopy[curr.random]

            curr = curr.next

        return origToCopy[head]