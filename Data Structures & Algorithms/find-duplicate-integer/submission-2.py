class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        # we can treat the array like a linked list, where indexing into the 
        # array is like movin to the next node in the list.
        # we can use the fast and slow pointer teqnique, which
        # basically jsut says if we have one pointer moving fast through the list
        # and one moving slow, they will eventually meet if there is a cycle. 
        # then, to figure out where this cycle starts, you set one of them back
        # to the head of the list, and advance each one one at a time untill they
        # intersect again. This second intersction is your cycel start, or in this case
        # the duplicate

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow