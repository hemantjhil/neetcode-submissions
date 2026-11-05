class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # if open==closed==n return the res
        # if closed>open dont add close
        #

        stack=[]
        res=[]

        def backtrack(openN,closedN):
            if openN==closedN==n:
                res.append("".join(stack))
                return
            
            if openN<n:
                stack.append("(")
                backtrack(openN+1,closedN)
                stack.pop()

            if closedN<openN:
                stack.append(')')
                backtrack(openN,closedN+1)
                stack.pop()
        backtrack(0,0)
        return res
        