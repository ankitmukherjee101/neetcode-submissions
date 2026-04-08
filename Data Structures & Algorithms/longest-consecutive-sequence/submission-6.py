class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            longest = 0
        else:
            longest = 1
        hashSet = set(nums)
        for n in nums:
            if (n-1) not in hashSet:
                length = 1
                while (n + length) in hashSet:
                    length += 1
                longest = max(longest, length)
        return longest
                