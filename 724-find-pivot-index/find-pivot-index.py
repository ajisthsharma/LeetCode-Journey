class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        summ=0

        for i in range(len(nums)):
            if summ==total-summ-nums[i]:
                return i
            
            summ+=nums[i]

        return -1