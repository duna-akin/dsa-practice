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
        origToCopy = dict()
        curr = head 
        while curr:
            new = Node(curr.val)
            origToCopy[curr] = new
            curr = curr.next
        origToCopy[None] = None

        for orig, copy in origToCopy.items():
            if copy == None:
                continue
            copy.next = origToCopy[orig.next]
            copy.random = origToCopy[orig.random]
        
        return origToCopy[head]