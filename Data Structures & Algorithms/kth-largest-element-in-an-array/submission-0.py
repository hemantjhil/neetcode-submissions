class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap=[]
        for num in nums:
            minHeap.append(num)
        heapq.heapify(minHeap)
        l=len(nums)-k
        num=0
        while l>=0:
            num=heapq.heappop(minHeap)
            l-=1
        return num

        