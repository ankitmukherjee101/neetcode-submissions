class Solution:
    def isValid(self, s: str) -> bool:
        br = {']':'[', '}':'{', ')':'('}
        stack = []

        for c in s:
            if c in br:
                if stack and stack[-1] == br[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if not stack:
            return True
        else:
            return False