class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        
        # start moving both size for each char and check palindrome
        for i in range(len(s)):
            # odd len palindromes
            j,k=i,i
            while j>=0 and k<len(s) and s[j]==s[k]:
                res+=1
                j-=1
                k+=1

            # even len palindromes
            j,k=i,i+1
            while j>=0 and k<len(s) and s[j]==s[k]:
                res+=1
                j-=1
                k+=1
        return res
            
        