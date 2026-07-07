class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            # the only situation in which there is a collision
            # is if we see a negative and the top of the stack is positive
            # in this case there are three things that can happen

            # keep processing untill there is nothing left to colide with
            while stack and a < 0 and stack[-1] > 0:
                # if the asteroid is bigger we destroy the 
                # positive asteroid
                if abs(a) > abs(stack[-1]):
                    stack.pop()
                # if it is smaller we dont append it
                elif abs(a) < abs(stack[-1]):
                    a = 0
                # if it is equal we don't append it and also destroy the top asteroid
                else:
                    a = 0
                    stack.pop()
            # allows us to conditionally set it because asteroid of 0 doesnt 
            # need to be appended.
            if a:
                stack.append(a)
               
        return stack
            
