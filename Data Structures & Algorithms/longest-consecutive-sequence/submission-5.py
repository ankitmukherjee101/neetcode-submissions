class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        if len(nums) < 1:
            longest = 0
        else:
            longest = 1
        for num in numSet:
            if (num-1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                    longest = max(longest, length)
        return longest
