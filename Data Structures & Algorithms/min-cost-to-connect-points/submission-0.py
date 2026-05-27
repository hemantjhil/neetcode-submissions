class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N=len(points)
        # create adjacency list
        adj={i:[] for i in range(N)}

        for i in range(N):
            x1,y1=points[i]
            for j in range(i+1,N):
                x2,y2=points[j]
                dist=abs(x2-x1)+abs(y2-y1)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        
        # Prim's Algo
        res=0
        visit=set()
        minHeap=[[0,0]] # cost,point
        while len(visit)<N:
            cost,point=heapq.heappop(minHeap)
            if point in visit:
                continue
            res+=cost
            visit.add(point)
            for neighCost,nei in adj[point]:
                if nei not in visit:
                    heapq.heappush(minHeap,[neighCost,nei])
        return res


        