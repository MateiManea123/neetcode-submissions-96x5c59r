# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dic = {}


        while head:
            dic[head] = dic.get(head,0)+1
            if dic[head] > 1:
                return True
            head = head.next

        return False
        