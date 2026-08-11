class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        if "0000" == target:
            return 0

        q = deque(["0000"])

        # just put everything in one place to simplify code
        visited = set(deadends)
        visited.add("0000")
        steps = 0

        while q:
            steps += 1
            # process in layers so the step count stays
            # accurate. if we had no layers
            # it would be a number of nodes count 
            for _ in range(len(q)):
                cur = q.popleft()
                # for each digit
                for i in range(4):
                    # add and subtract to it looping around
                    # and ensuring it is positive
                    for j in [-1, 1]:
                        digit = str((int(cur[i]) + j + 10) % 10)
                        nxt = cur[:i] + digit + cur[i+1:]
                        if nxt in visited:
                            # skip ones we have seen
                            continue
                        if nxt == target:
                            # return correct answers
                            return steps
                        
                        q.append(nxt)
                        visited.add(nxt)

        return -1
        