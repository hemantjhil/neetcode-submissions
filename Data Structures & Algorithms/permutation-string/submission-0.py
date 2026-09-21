class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        s1Hash=[0]*26
        s2Hash=[0]*26
        left=right=0
        while right<len(s1):
            s1Hash[ord(s1[right])-ord('a')]+=1
            s2Hash[ord(s2[right])-ord('a')]+=1
            right+=1
        right-=1
        while right<len(s2):
            if s1Hash==s2Hash:
                return True
            right+=1
            if right!=len(s2):
                s2Hash[ord(s2[right])-ord('a')]+=1
            s2Hash[ord(s2[left])-ord('a')]-=1
            left+=1
        return False

        