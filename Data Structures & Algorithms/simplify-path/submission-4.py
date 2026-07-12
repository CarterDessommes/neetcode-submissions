class Solution:
    def simplifyPath(self, path: str) -> str:

        # o(n) time and space
        dirs = path.split('/')
        stack = []
        for d in dirs:
            # .. means we go back up a directory. so if we can pop off the last directory
            if d == "..":
                # this if stack must be nested, as if we have .. and no stack to pop from
                # we do NOT want to enter the elif and append ..
                if stack:
                    stack.pop()
            # a "." effectively does nothing, and a "" occurs if we have sonmething like
            # "//" or "/egg"
            elif d != "." and d != "":
                stack.append(d)


        # put a / at the start and between each entry
        return "/" + "/".join(stack)

        