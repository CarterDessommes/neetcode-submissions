class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        # maybe a bit tricky to find on your own
        # but the idea is simply to work backwards, seeing if each index 
        # can get you where you need to go. like for each index -> can this get me to 
        # the next step I need to get to the end? if yes then this can be the new goal
        # because we know that from here I can get to the end.
        goal = len(nums) - 1
        for i in reversed(range(len(nums) - 1)):
            if i + nums[i] >= goal:
                goal = i
        
        # if we move the goal all the way to the start, it means that we can get
        # to the end from the start.
        return goal == 0




        