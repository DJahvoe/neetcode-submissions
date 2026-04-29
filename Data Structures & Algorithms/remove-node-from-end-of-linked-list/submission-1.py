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

        if length == 1 and n == 1:
            head = None
            return

        # second pass: remove the element
        pointer = head
        index = pos = length - n - 1
        print(index)
        while index > 0:
            pointer = pointer.next
            index -= 1
        print(pointer.val)
        if pos == -1:
            head = head.next
        else:
            pointer.next = pointer.next.next
        return head

