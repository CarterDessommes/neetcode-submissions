# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # o(n), o(1) solution

         # count the length of the list
        cur = head
        l = 0
        while cur:
            l += 1
            cur = cur.next

        # edge case where if the node we need to remove 
        # is first one we have to handle that seperately
        if n == l:
            head = head.next
            return head


        # loop forward to find the node
        # before the one we want to remove
        cur2 = head
        # we wanna remove the l-n th node, so pointer must move forward
        # l-n-1 times
        for _ in range(l - n - 1):
            cur2 = cur2.next
    
        cur2.next = cur2.next.next
        return head


        