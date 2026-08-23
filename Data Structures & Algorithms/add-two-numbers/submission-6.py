# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode
        n = d
        c = 0

        while l1 or l2 or c:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0
            summ = d1 + d2 + c
            d3 = summ % 10
            c = summ // 10
            n.next = ListNode(d3)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            n = n.next

        if l1:
            n.next = l1
        if l2:
            n.next = l2

        return d.next