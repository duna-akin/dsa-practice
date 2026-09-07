# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = head
        f = head
        while f and f.next:
            s = s.next
            f = f.next.next
        
        cur = s.next
        prev = None
        s.next = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        l1 = head
        l2 = prev
        while l1 and l2:
            nxt1, nxt2 = l1.next, l2.next if l2 else None
            l1.next = l2
            l2.next = nxt1
            l1 = nxt1
            l2 = nxt2