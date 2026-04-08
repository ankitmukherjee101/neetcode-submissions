class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windowMap = {}
        l = 0
        maxf = 0
        length = 0
        for r in range(len(s)):
            windowMap[s[r]] = 1 + windowMap.get(s[r], 0)
            maxf = max(maxf, windowMap[s[r]])
            while (r-l+1) - maxf > k:
                windowMap[s[l]] -= 1
                l += 1
            length = max(length, (r-l+1))
        return length