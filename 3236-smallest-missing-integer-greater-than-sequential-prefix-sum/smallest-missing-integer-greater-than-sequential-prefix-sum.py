class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        pref=nums[0]
        
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                break

            pref+=nums[i]

        for i in range(pref,52):
            if i not in nums:
                return i

        return pref