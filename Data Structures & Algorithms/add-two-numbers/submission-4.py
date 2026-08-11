# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy to append the solution to
        dummy = ListNode()
        # track the last item in the solution list
        last_node = dummy
        
        # move through the lists digit by digit until there are no more digits (including a carry)
        carry = 0
        while l1 or l2 or carry != 0:
            # extract the digits if the node exists and calculate raw sum
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            raw_sum = digit1 + digit2 + carry

            # calculate the value of current digit and new carry
            digit3 = raw_sum % 10
            carry = raw_sum // 10

            # create the new node and then tie it to solution
            new_node = ListNode(digit3)
            last_node.next = new_node

            # move the pointers forward
            last_node = last_node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
            

