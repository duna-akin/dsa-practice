# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        nodes = list()
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        remove_index = len(nodes) - n
        if remove_index == 0:
            return head.next
        else:
            node = nodes[remove_index]
            prev = nodes[remove_index - 1]
            prev.next = node.next

        return head