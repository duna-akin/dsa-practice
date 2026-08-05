# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use three variables, one for prev, one for curr, one for next
        curr = head
        prev = None

        # iterate until curr is None
        while curr:
            nxt = curr.next
            curr.next = prev    # relink curr's pointer to one before it
            prev = curr         # move prev to curr
            curr = nxt          # move curr to next

        # prev will be the last node
        return prev