class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        charMap = [0]*26
        for i in range(len(s)):
            charMap[ord(s[i]) - ord('a')] += 1
            charMap[ord(t[i]) - ord('a')] -= 1
        for i in charMap: 
            if i != 0:
                return False
        return True
