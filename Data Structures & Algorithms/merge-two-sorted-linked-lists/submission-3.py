# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        # keep track of last node in merged list
        last_node = dummy

        # while both lists have nodes
        while list1 and list2:
            # attach the smaller node to the last node in the merged list
            if list1.val < list2.val:
                last_node.next = list1
                list1 = list1.next
            else:
                last_node.next = list2
                list2 = list2.next
            
            # move last node further
            last_node = last_node.next

        # attach whatever list might remain to the end of last node in the merged list
        last_node.next = list1 or list2

        return dummy.next