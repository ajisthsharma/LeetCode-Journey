class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor=0
        allzero=True

        for num in nums:
            xor^=num

            if num!=0:
                allzero=False

        if xor!=0:
            return len(nums)

        return len(nums)-1 if not allzero else 0