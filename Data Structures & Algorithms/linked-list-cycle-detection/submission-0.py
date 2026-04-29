# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        counter = 1
        while fast != None:
            if counter % 2 == 0:
                slow = slow.next
            fast = fast.next
            counter += 1
            print(slow)
            print(fast)

            if slow == fast:
                print("test")
                return True
        return False