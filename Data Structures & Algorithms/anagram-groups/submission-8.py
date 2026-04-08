class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            charMap = [0]*26
            for ch in s:
                charMap[ord(ch) - ord('a')] += 1
            res[tuple(charMap)].append(s)

        return res.values()