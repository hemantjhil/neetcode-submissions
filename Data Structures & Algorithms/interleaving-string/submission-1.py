class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # if length do not add up s3 cant be formed by interleaving s1 and s2
        if len(s1)+len(s2)!=len(s3):
            return False
        # initalize a 2D array 
        dp=[[False]*(len(s2)+1) for i in range(len(s1)+1)]
        # if both s1 and s2 exhausted s3 is formed
        dp[len(s1)][len(s2)]=True

        # iterated from bottom right to top left
        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):
                # take the next char from s1 if it match next req char in s3
                if i<len(s1) and s1[i]==s3[i+j] and dp[i+1][j]:
                    dp[i][j]=True
                # take the next char from s2 if it matches the req char in s3
                if j<len(s2) and s2[j]==s3[i+j] and dp[i][j+1]:
                    dp[i][j]=True
        #return final match condition
        return dp[0][0]
        