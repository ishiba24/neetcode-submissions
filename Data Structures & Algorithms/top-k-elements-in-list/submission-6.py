class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)
        for num in nums:
            freq[num]+=1
        buckets=[[] for i in range(len(nums)+1)]
        for val, f in freq.items():
            buckets[f].append(val)
        res=[]
        for f in range(len(nums),0,-1):
            for val in buckets[f]:
                res.append(val)
                if len(res)==k:
                    return res

