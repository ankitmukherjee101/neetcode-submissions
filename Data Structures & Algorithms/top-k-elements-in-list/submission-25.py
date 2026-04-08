class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+1)]

        freq = {}

        for n in nums:
            freq[n] = 1 + freq.get(n,0)
        
        for val,fr in freq.items():
            bucket[fr].append(val)
        
        res = []
        for i in range(len(bucket)-1, -1, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return