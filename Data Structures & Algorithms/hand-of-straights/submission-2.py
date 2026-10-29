class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        keyMap={}
        for num in hand:
            keyMap[num]=1+keyMap.get(num,0)
        keyHeap=list(keyMap.keys());
        heapq.heapify(keyHeap)
        while keyHeap:
            first=keyHeap[0]
            for i in range(first,first+groupSize):
                if i not in keyMap:
                    return False
                keyMap[i]-=1
                if keyMap[i]==0:
                    if i!=keyHeap[0]:
                        return False
                    heapq.heappop(keyHeap)
                
        return True
            

        