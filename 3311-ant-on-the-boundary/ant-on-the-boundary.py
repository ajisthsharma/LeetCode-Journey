class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ans=0
        count=0

        for num in nums:
            count+=num

            if count==0:
                ans+=1

        return ans