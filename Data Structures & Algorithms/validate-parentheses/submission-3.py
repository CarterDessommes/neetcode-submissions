class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False
                recent = stack.pop()
                if char == ")":
                    if recent != "(":
                        return False
                elif char == "}":
                    if recent != "{":
                        return False
                elif char == "]":
                    if recent != "[":
                        return False

        return len(stack) == 0
        





# ({})((({[[]]})))