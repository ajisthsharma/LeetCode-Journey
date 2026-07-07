class Solution:
    def sumAndMultiply(self, n: int) -> int:
        summ=0
        x=''

        if n==0: return 0

        while n>0:
            digit=n%10
            n//=10

            if digit==0: continue

            summ+=digit
            x+=str(digit)

        x=x[::-1]
        x=int(x)

        return x*summ