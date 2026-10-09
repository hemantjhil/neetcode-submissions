class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        def binary(l,r):
            if l==r:
                return l
            m=(l+r)//2
            total=0
            for pile in piles:
                total+=math.ceil(pile/m)
            if total<=h:
                return binary(l,m)
            else:
                return binary(m+1,r)
        return binary(1,max(piles))
        