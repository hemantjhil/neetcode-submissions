class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if graph is not cyclic then its valid tree
        if len(edges)!=n-1:
            return False
        
        # build adjacency graph
        graph={i:[] for i in range(n)}
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # build a visit set
        visitSet=set()

        # depth first search to detect cycle 
        def dfs(node,parent):

            # cycle detected if node in visited
            if node in visitSet:
                return False
            
            visitSet.add(node)

            # traversing across neighour of adjancency list
            for neighour in graph[node]:

                # ignore if node redirect to same node
                if neighour==parent:
                    continue
                if not dfs(neighour, node):
                    return False
            
            return True
        
        if not dfs(0,-1):
            return False
        return len(visitSet)==n
        