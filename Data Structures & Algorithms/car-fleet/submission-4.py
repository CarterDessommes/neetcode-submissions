class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # each fleet is basically a "bottle neck" car, so we just need to find all the 
        # cars that wont catch up to another car
        combined = [(p, s) for p, s in zip(position, speed)]

        # monotonic decreasing list, working closest to furthest, easier to think about
        # what cars collide with what other cars if sorted.
        # bulk of time compexity o(nlogn)
        combined.sort(reverse=True)    

        stack = [] # space o(n)
        for p, s in combined:
            time = (target - p) / s
            stack.append(time)
            # if this car will get to destination sooner, it will catch up
            # to another car so we can pop it
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        # if it has not been popped, it is a bottle neck car.
        return len(stack)