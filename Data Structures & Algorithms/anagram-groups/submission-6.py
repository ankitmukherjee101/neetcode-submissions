class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            charMap = [0]*26
            for i in range(len(s)):
                charMap[ord(s[i]) - ord('a')] += 1
            res[tuple(charMap)].append(s)
        return res.values()