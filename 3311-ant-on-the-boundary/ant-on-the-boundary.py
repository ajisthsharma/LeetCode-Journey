class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        
        curr = 0
        res = 0
        for num in nums:
            curr += num
            if curr == 0:
                res += 1
        return res 