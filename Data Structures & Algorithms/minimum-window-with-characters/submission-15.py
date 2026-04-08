class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = {}
        if t == "":
            return ""
        for c in t:
            tmap[c] = 1 + tmap.get(c, 0)

        have, need = 0, len(tmap)

        window = {}
        res, resLen = "", float("infinity")
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in tmap and window[s[r]] == tmap[s[r]]:
                have += 1
            while have == need:
                if r-l+1 < resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                window[s[l]] -= 1
                if s[l] in tmap and window[s[l]] < tmap[s[l]]:
                    have -= 1
                l += 1
        return res if resLen != float("infinity") else ""
