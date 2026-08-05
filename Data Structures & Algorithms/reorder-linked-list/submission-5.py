class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ## split the list into two using fast slow ##
        slow = head
        fast = head

        # ensure fast and fast.next are both Nodes
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow: tail of first half, fast: tail of second half

        ## reverse second half ##
        curr = slow.next
        prev = None
        # kill first half's connection to second
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        ## tie the two new lists iteratively ##
        first = head
        second = prev
        while first and second:
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first, second = nxt1, nxt2