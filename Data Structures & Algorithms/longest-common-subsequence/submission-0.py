class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # create a 2 D matrix of size (n1+1,n2+1) and intialize every value as 0
        dp=[[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        # iterate through each cell of matrix
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                # if both text char matches add 1 to diagonal of matrix
                if text1[i]==text2[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                # otherwise text max of right and below
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]
        