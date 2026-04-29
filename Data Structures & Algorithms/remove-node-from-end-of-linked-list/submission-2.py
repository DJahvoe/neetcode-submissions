# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # first pass: find length
        pointer = head
        length = 0
        while pointer:
            length += 1
            pointer = pointer.next

        # second pass: remove the element
        
        index = length - n
        if index == 0:
            return head.next
        
        pointer = head
        for i in range(length - 1):
            if (i + 1) == index:
                pointer.next = pointer.next.next
                break
            pointer = pointer.next
        return head