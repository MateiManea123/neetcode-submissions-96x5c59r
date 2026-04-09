# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        leng = 1
        while head.next:
            head = head.next
            leng+=1
        print(leng)

        pos = 1
        head =dummy2 = dummy
        to_remove = leng-n+1

        if to_remove == 1:
            if head.next:
                return head.next
            return None

        while head.next:
            if pos+1 == to_remove:
                temp = head.next.next
                head.next.next = None
                head.next = temp
                break
            else:
                pos+=1
                head = head.next
        
        return dummy2

            