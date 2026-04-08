class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        bucket = [[] for i in range(len(nums)+1)]
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        for n, freq in hashMap.items():
            bucket[freq].append(n)
        result = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return