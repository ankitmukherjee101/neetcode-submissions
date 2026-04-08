class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        if len(nums) < 1:
            mlength = 0
        else:
            mlength = 1
        for n in hashset:
            if (n-1) not in hashset:
                length = 1
                while (n+length) in hashset:
                    length += 1
                    mlength = max(mlength, length)
        return mlength
