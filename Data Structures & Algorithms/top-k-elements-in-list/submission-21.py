class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+1)]
        count = {}
        for num in nums: 
            count[num] = 1 + count.get(num, 0)
        
        for n,c in count.items():
            bucket[c].append(n)
        res = []
        for i in range(len(bucket)-1, -1, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res

        return