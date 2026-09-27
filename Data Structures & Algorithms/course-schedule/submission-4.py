class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cycle=set()
        visit=set()
        preMap={i:[] for i in range(numCourses)}
        for pre,crs in prerequisites:
            preMap[crs].append(pre)
        def dfs(crs):
            # cycle detected
            if crs in visit:
                return False
            if preMap[crs]==[]:
                return True
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            preMap[crs]=[]
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True