class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        bucket = [[] for i in range(len(nums)+1)]
        res = []
        for n in nums:
            frequencies[n] = frequencies.get(n,0) + 1
        for num, freq in frequencies.items():
            bucket[freq].append(num)
        for i in range(len(bucket)-1, -1, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return
