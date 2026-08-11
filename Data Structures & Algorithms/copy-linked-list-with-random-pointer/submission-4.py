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
        # two pass with hash map

        # map original nodes to their copy nodes
        originalToCopy = dict()

        # store null to prevent errors down the line
        originalToCopy[None] = None
        
        # iterate through the list, make a copy (only with value) and store in map
        original = head
        while original:
            copy = Node(original.val)
            originalToCopy[original] = copy
            original = original.next
        
        # iterate through map and tie each copy based on original's pointers
        for original, copy in originalToCopy.items():
            if copy is None:
                continue
            copy.next = originalToCopy[original.next]
            copy.random = originalToCopy[original.random]
        
        return originalToCopy[head]
