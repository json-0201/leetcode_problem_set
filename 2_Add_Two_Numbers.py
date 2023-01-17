# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Returns the sum of two linked lists in a reverse order."""
        
        # initialize dummy node
        node_initial = ListNode()
        node_current = node_initial
        
        # initialize carry
        carry = 0

        # loop until both lists are empty and carry is 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # check carry and sum
            v_sum = v1 + v2 + carry
            carry = v_sum // 10
            v_sum = v_sum % 10
            node_current.next = ListNode(v_sum)
            
            # new pointer
            node_current = node_current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return node_initial.next