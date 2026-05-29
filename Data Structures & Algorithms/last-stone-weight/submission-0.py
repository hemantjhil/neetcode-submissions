class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # multiply with -1 as python only has minHeap
        maxHeap=[-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap)>1:
            first,second=heapq.heappop(maxHeap),heapq.heappop(maxHeap)
            if second>first:
                heapq.heappush(maxHeap,first-second)
        maxHeap.append(0)
        return abs(maxHeap[0])