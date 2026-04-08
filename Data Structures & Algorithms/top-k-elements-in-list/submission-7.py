class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        bucket = [[] for i in range(len(nums)+1)]
        res = []
        for cnt, freq in counts.items():
            bucket[freq].append(cnt)

        for i in range(len(bucket)-1, -1, -1):
            for j in bucket[i]:
                res.append(j)
            if len(res) == k:
                return res