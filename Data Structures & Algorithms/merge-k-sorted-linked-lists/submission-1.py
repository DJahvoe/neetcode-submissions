# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeLinkedList(self, list_a, list_b):
        newHead = temp = ListNode()

        while list_a and list_b:
            if list_a.val < list_b.val:
                temp.next = list_a
                list_a = list_a.next
            else:
                temp.next = list_b
                list_b = list_b.next
            temp = temp.next
        temp.next = list_a or list_b
        return newHead.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if not lists[0]:
            return None
        
        newHead = None
        while len(lists) > 0:
            temp = lists.pop()
            newHead = self.mergeLinkedList(newHead, temp)
        return newHead

        