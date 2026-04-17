# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        w = dummy
        while list1 and list2:
            if list1.val < list2.val:
                w.next = list1
                w = w.next
                list1 = list1.next
            elif list2.val <= list1.val:
                w.next = list2
                w = w.next
                list2 = list2.next
        
        w.next = list1 or list2
        return dummy.next





            
        # if we here it means we have exhausted a list

#list1=[]
#               w
# temp = None
# temp2 = None
#list2=[1, 2]
#       i