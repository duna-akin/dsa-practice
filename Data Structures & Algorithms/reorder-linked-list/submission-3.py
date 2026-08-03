class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split list into two halves
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # now slow points at first half tail and fast at second half tail

        # reverse second list
        curr = slow.next
        slow.next = None # kill first half's tail's connection to second half
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # prev is the new head of reversed list and curr is none
        
        first, second = head, prev
        while second and first:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
