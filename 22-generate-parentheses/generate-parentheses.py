class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]

        def dfs(openp,closep,s):
            if openp==closep and openp+closep==n*2:
                res.append(s)
                return

            if openp<n:
                dfs(openp+1,closep,s+'(')
            
            if closep<openp:
                dfs(openp,closep+1,s+')')

        dfs(0,0,'')

        return res