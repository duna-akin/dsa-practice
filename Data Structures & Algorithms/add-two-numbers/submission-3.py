# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode() # attach answer to this
        cur = d
        car = 0
        while l1 or l2 or car != 0:
            # extract digits
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0 
            summ = d1 + d2 + car    # extract raw sum
            d3 = summ % 10          # extract new digit
            car = summ // 10        # extract carry
            cur.next = ListNode(d3) # create new node and append to answer

            # move all pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next
            
        return d.next