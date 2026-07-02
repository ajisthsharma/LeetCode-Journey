class Solution:
    def calculate(self, s: str) -> int:
        num,res,sign=0,0,1
        stack=[]

        for ch in s:
            if ch.isdigit():
                num=num*10 +int(ch)

            elif ch in '+-':
                res+=sign*num
                sign=-1 if ch=='-' else 1
                num=0

            elif ch=='(':
                stack.append(res)
                stack.append(sign)
                res=0
                sign=1

            elif ch==')':
                res+=sign*num
                res*=stack.pop()
                res+=stack.pop()
                num=0

        return res+num*sign