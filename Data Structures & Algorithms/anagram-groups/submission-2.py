class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for s in strs:
            charMap = [0]*26
            for i in range(0, len(s)):
                charMap[ord(s[i]) - ord('a')] += 1
            dict[tuple(charMap)].append(s)
        return dict.values()