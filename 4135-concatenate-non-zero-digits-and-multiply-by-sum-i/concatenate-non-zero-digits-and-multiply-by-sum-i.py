class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digit_sum = 0
        ans = 0

        for ch in str(n):
            digit = int(ch)
            digit_sum += digit
            if digit != 0:
                ans = ans * 10 + digit

        return ans * digit_sum