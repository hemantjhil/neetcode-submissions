class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap={}
        freq=[[] for i in range(len(nums)+1)]
        for num in nums:
            numMap[num]=1+numMap.get(num,0)
        for num,cnt in numMap.items():
            freq[cnt].append(num)
        res=[]
        for i in range(len(nums),-1,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res
        