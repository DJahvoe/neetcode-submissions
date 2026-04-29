# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        # find which one is longer
        while cur1 and cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        
        
        if cur1 == None:
            l1, l2 = l2, l1

        cur1 = l1
        cur2 = l2
        carrier = 0
        while cur1:
            current_sum = cur1.val + carrier
            if cur2:
                current_sum += cur2.val
                cur2 = cur2.next
            carrier = current_sum // 10
            current_sum %= 10
            
            cur1.val = current_sum
            print(cur1.val)
            if cur1.next == None and carrier == 1:
                cur1.next = ListNode(0, None)
            cur1 = cur1.next
        
        return l1
