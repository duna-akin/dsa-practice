class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next # start from second half's head
        slow.next = None # kill first half's tail's connection to second half's head
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # start from first half's head, second half's head 
        # (prev holds original second half's tail and the reversed second half's head)
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2