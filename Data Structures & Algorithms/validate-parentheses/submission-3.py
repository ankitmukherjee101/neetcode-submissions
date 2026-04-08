class Solution:
    def isValid(self, s: str) -> bool:
        brmap = {']':'[', '}':'{', ')':'('}
        stack = []
        for c in s:
            if c in brmap:
                if stack and stack[-1] == brmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False