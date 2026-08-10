class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = head
        f = head
        while f and f.next:
            s = s.next
            f = f.next.next
        
        p = None
        c = s.next
        s.next = None
        while c:
            n = c.next
            c.next = p
            p = c
            c = n
        
        l1, l2 = head, p
        while l2:
            n1, n2 = l1.next, l2.next
            l1.next = l2
            l2.next = n1
            l1 = n1
            l2 = n2
