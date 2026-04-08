class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)

        maxlength = 0

        for n in hashset:
            if n-1 not in hashset:
                length = 1
                while n + length in hashset:
                    length += 1
                maxlength = max(maxlength, length)
        return maxlength
