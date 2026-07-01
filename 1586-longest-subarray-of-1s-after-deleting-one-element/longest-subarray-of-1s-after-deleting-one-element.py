class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev = 0
        curr = 0
        max_len = 0
        for num in nums:
            if num == 1:
                curr += 1
            else:
                max_len = max(max_len, prev + curr)
                prev = curr
                curr = 0
        max_len = max(max_len, prev + curr)
        return max_len - 1 if max_len == len(nums) else max_len