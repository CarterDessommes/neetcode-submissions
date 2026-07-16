# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # we have a dummy list node to 
        # make this kind of problem a bit easier 

        dummy = ListNode(0, head)
        before_start = dummy

        prev = head
        cur = head.next
        
        i = 2
        while cur and i <= right:
            if left < i <= right:
                # walk forward and reverse
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
                i += 1
            else: 
                if i == left:
                    before_start = prev
                
                
                
                # walk forward
                prev = cur 
                cur = cur.next
                i += 1
            
        start = before_start.next
        before_start.next = prev
        start.next = cur


        return dummy.next