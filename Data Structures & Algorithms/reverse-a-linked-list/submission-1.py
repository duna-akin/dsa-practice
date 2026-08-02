# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev    # rewire pointer to point back
            prev = curr         # advance prev to where curr is
            curr = nxt          # advance curr to stored next node
        return prev

        