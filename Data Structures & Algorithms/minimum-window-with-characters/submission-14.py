class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "":
            return ""

        tMap = {}
        for ch in t:
            tMap[ch] = 1 + tMap.get(ch, 0)

        windowMap = {}
        have = 0
        need = len(tMap)
        res, resLen = [-1,-1], float("infinity")

        l = 0
        for r in range(len(s)):
            windowMap[s[r]] = 1 + windowMap.get(s[r], 0)
            if s[r] in tMap and windowMap[s[r]] == tMap[s[r]]:
                have += 1

            while have == need:
                if r-l+1 < resLen:
                    resLen = r-l+1
                    res = [l,r]
                windowMap[s[l]] -= 1
                if s[l] in tMap and windowMap[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1
            

        return s[res[0]:res[1]+1] if resLen != float("infinity") else ""
            
