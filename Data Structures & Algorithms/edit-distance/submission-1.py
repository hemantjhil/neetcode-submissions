class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # initialize a 2D array 
        # where cache[i][j] represent min no of operations
        # covert word1[i:] to word2[j:]
        cache=[[float("inf")]* (len(word2)+1) for i in range(len(word1)+1)]
        # case 1 when word2 is exhausted
        # remaining char in word1 must be deleted
        j=len(word2)
        for i in range(len(word1)+1):
            cache[i][j]=len(word1)-i
        
        #case 2 when word 1 in exhausted
        # remaining char in word 2 must be inserted
        i=len(word1)
        for j in range(len(word2)+1):
            cache[i][j]=len(word2)-j
        

        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                # when both char match no operations required
                if word1[i]==word2[j]:
                    cache[i][j]=cache[i+1][j+1]
                # check the min of operations
                else:
                    cache[i][j]=1+min(cache[i+1][j] # delete
                    ,cache[i][j+1] #insert
                    ,cache[i+1][j+1]) #replace
        #return cumulative opertions
        return cache[0][0]
        


        