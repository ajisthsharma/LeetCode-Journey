class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        x = 0
        done = 0
        for i in nums :
            x += i
            done += (x == 0)
        return done