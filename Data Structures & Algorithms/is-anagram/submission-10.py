class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charmap = [0]*26
        for i in range(len(s)):
            charmap[ord(s[i]) - ord('a')] += 1
            charmap[ord(t[i]) - ord('a')] -= 1
        for n in charmap:
            if n != 0:
                return False

        return True
