# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        print(length)
        rem = length - n
        if rem == 0:
            return head.next
        i = 0
        curr = head
        while curr:
            i += 1
            if i == rem:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head
            


