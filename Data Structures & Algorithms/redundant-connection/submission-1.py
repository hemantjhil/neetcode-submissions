class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        par=list(range(n+1))

        # union
        def union(a,b):
            par[find(a)]=find(b)


        def find(a):
            if par[a]==a:
                return a
            else:
                par[a]= find(par[a])
                return par[a]
        
        res=None
        for a,b in edges:
            if find(a)==find(b):
                res=[a,b]
            union(a,b)
        return res
        