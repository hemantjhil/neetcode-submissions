class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # creating dp array to check if the string char can be segmented
        # into words from dict
        dp=[False]*(len(s)+1)

        # Empty char will be part of dict
        dp[len(s)]=True

        # start backtracking for string s and check each word
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                # check if the length match and index add less than string size
                if i+len(w)<=len(s) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                
                # if found match break from the loop
                if dp[i]:
                    break
        return dp[0]
        