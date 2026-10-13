class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        distMatrix=[[float("inf")]*(len(word2)+1) for i in range(len(word1)+1)]

        j=len(word2)
        for i in range(len(word1)+1):
            distMatrix[i][j]=len(word1)-i
        i=len(word1)
        for j in range(len(word2)+1):
            distMatrix[i][j]=len(word2)-j

        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i]==word2[j]:
                    distMatrix[i][j]=distMatrix[i+1][j+1]
                else:
                    distMatrix[i][j]=1+min(
                    distMatrix[i+1][j],
                    distMatrix[i+1][j+1],
                    distMatrix[i][j+1]
                    )
        return distMatrix[0][0]