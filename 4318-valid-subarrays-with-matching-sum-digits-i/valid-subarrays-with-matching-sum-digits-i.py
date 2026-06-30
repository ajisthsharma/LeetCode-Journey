class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        def isvalid(summ):
            if summ%10!=x:
                return False

            temp=summ
            while temp>=10:
                temp//=10

            return temp==x

        ans=0
        for i in range(len(nums)):
            summ=0
            for j in range(i,len(nums)):
                summ+=nums[j]

                if isvalid(summ):
                    ans+=1

        return ans