class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digit_sum,square_sum=0,0

        while n:
            digit=n%10
            digit_sum+=digit
            square_sum+=digit*digit
            n//=10

        return (square_sum-digit_sum)>=50