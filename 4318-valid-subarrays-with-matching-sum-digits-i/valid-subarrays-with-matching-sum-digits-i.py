class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        n = len(nums)
        ans = 0
        s = str(x)
        for i in range(n):
            summ = 0
            for j in range(i, n):
                summ += nums[j]
                if summ % 10 == x:
                    if str(summ)[0] == s:
                        ans += 1
        return ans

            