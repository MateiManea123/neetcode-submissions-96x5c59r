# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = 0
        dummy = l3 = ListNode()

        while l1 and l2:
            sums = l1.val+l2.val+temp
            l3.next = ListNode(sums%10)
            temp = sums//10
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next

        while l1:
            sums = l1.val + temp
            l3.next = ListNode(sums%10)
            temp = sums//10
            l1 = l1.next
            l3 = l3.next
        while l2:
            sums = l2.val + temp
            l3.next = ListNode(sums%10)
            temp = sums//10
            l2 = l2.next
            l3 = l3.next
        if temp!=0:
            l3.next = ListNode(temp)
            
        return dummy.next