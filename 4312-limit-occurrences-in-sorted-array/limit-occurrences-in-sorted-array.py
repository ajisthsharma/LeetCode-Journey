class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        d = {}
        a = []

        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
            if d[num] <= k:
                a.append(num)
        return a