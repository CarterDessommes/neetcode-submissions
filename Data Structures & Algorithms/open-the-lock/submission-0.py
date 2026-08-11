class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        if "0000" == target:
            return 0

        q = deque(["0000"])

        visited = set(deadends)
        visited.add("0000")
        steps = 0

        while q:
            steps += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for i in range(4):
                    for j in [-1, 1]:
                        digit = str((int(cur[i]) + j + 10) % 10)
                        nxt = cur[:i] + digit + cur[i+1:]
                        if nxt in visited:
                            continue
                        if nxt == target:
                            return steps
                        
                        q.append(nxt)
                        visited.add(nxt)

        return -1
        