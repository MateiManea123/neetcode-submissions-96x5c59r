# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        dummy = i = j = head
        while j.next and j.next.next:
            i = i.next
            j = j.next.next
        
        prev, middle = None, i.next
        i.next = None
        
        while middle:
            temp = middle.next
            middle.next = prev
            prev = middle
            middle = temp
        
        i = dummy
        j = prev

        while j:
            tempi = i.next
            tempj = j.next
            i.next = j
            j.next = tempi
            i = tempi
            j = tempj

            