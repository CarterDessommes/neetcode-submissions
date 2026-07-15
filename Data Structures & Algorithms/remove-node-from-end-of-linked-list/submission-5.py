# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        cur = head
        l = 0
        while cur:
            l += 1
            cur = cur.next
        
        if n == l:
            head = head.next
            return head

        cur2 = head
        for _ in range(l - n - 1):
            cur2 = cur2.next
    
        cur2.next = cur2.next.next
        return head

        