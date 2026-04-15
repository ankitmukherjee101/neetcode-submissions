class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while l < r: 
            while l<r and self.isalphaNum(s[l]) == False:
                l += 1
            while r>l and self.isalphaNum(s[r]) == False:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True


    def isalphaNum(self, ch):
        if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z') or (ch >= '0' and ch <= '9'):
            return True
        return False