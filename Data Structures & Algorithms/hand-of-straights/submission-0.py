class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        # creating count map
        countMap={}
        for n in hand:
            countMap[n]=1+countMap.get(n,0)
        minH=list(countMap.keys())
        # creating minHeap of key to make them sorted
        heapq.heapify(minH)
        # iterating through minHeap
        while minH:
            first=minH[0]
            # getting the values till the size
            for i in range(first,first+groupSize):
                if i not in countMap:
                    return False
                countMap[i]-=1
                if countMap[i]==0:
                    if i!=minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
        