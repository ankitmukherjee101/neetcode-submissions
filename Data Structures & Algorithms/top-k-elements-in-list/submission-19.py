class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        bucket = [[] for i in range(len(nums)+1)]
        for num in nums: 
            freqMap[num] = 1 + freqMap.get(num, 0)
        for val,cnt in freqMap.items():
            bucket[cnt].append(val)
        res = []
        for i in range(len(bucket)-1, 0, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return
        