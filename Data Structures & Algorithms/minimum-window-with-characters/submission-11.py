class Solution:
    def minWindow(self, s: str, t: str) -> str:
        windowmap = {}
        tmap = {}
        if t == "":
            return ""
        for c in t:
            tmap[c] = tmap.get(c, 0) + 1
        
        have = 0
        need = len(tmap)

        res = [-1, -1]
        resLen = float("infinity")

        l = 0

        for r in range(len(s)):
            windowmap[s[r]] = windowmap.get(s[r], 0) + 1
            if s[r] in tmap and windowmap[s[r]] == tmap[s[r]]:
                have += 1
            while have == need:
                
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res = [l,r]
                windowmap[s[l]] -= 1
                if s[l] in tmap and windowmap[s[l]] < tmap[s[l]]:
                    have -= 1
                l += 1
        
        return s[res[0]:res[1]+1] if resLen != float("infinity") else ""
