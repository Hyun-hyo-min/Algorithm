# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        carry = 0
        result = None

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        while stack1 or stack2 or carry:
            if stack1:
                val1 = stack1.pop()
            else:
                val1 = 0

            if stack2:
                val2 = stack2.pop()
            else:
                val2 = 0
            
            val = val1 + val2 + carry
            carry = val // 10
            node = ListNode(val % 10)
            node.next = result
            result = node

        return result
            
