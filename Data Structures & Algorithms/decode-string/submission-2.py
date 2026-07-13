class Solution:
    def decodeString(self, s: str) -> str:
  # stack of strings
        stringStack = []
        # stack of counts
        countStack = []

        cur = ""
        k = 0

        # a good way to think about this is that we are saving
        # what we have and pushing it to the stack each time we enter
        # new brackets.
        for char in s:
            # if it is a digit, we update our multiplier 
            if char.isdigit():
                # doing it this way lets us hadnle
                # multiple sigits. like 12 or wahtever.
                k = k * 10 + int(char)
            elif char == "[":
                # if we are beginning a new string, 
                # append the string and count we are working on
                stringStack.append(cur)
                countStack.append(k)
                # reset our cur and multipliers
                k = 0
                cur = ""
            elif char == "]":
                # if we are ending a string, aka coming out of nested brackets
                # we save what we have made in this bracket, pop off the 
                # prevoius string, and then pop off the corresponding multiplier 
                # to append the string the right amount of times
                temp = cur
                cur = stringStack.pop()
                count = countStack.pop()
                cur += temp * count
            else: 
                # otherwise it is a char and we can add it to the string we are working on
                cur += char
        return cur