# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        node = d
        carry = 0

        while l1 or l2 or carry:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0
            summ = d1 + d2 + carry
            d3 = summ % 10
            carry = summ // 10

            cur = ListNode(d3)
            node.next = cur
        
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            node = node.next
            
        return d.next


