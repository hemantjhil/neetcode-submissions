class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if not arr:
            return 0
        n=len(arr)
        res=count=0
        sign=0
        for i in range(n-1):
            if arr[i+1]>arr[i]:
                count=count+1 if sign==1 else 1
                sign=-1
            elif arr[i+1]<arr[i]:
                count=count+1 if sign==-1 else 1
                sign=1
            else:
                count=0
                sign=0
            res=max(res,count)
        return res+1


        