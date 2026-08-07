# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy pointer pointing to head for edge case where we remove the first node. dummy node makes the head node nothing special
        dummy = ListNode(0, head)

        # start l one step behind r so that it hits the node before the node we want to remove
        l, r = dummy, head 

        # move r n steps
        for i in range(n):
            r = r.next
        
        # move both until r hits end
        while r:
            l = l.next
            r = r.next
        # l is the node right before the node to remove

        l.next = l.next.next
        return dummy.next
        

