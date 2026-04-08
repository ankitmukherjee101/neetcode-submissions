class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxAr = 0
        while l < r:
            tempArea = (r-l) * min(heights[r], heights[l])
            maxAr = max(maxAr, tempArea)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxAr