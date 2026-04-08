class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        mlength = 0
        for n in hashset:
            if (n-1) not in hashset:
                length = 0
                while (n+length) in hashset:
                    length += 1
                    mlength = max(mlength, length)
        return mlength
