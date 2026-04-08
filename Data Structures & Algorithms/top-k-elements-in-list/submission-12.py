class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        bucket = [[] for i in range(len(nums)+1)]

        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for val, cnt in freq.items():
            bucket[cnt].append(val)

        res = []
        for i in range(len(bucket)-1, -1, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return