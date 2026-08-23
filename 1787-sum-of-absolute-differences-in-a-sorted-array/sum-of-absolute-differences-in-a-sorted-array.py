class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0
        result = []
        
        for i, val in enumerate(nums):
            right_sum = total_sum - left_sum - val
            
            left_total = (i * val) - left_sum
            right_total = right_sum - ((n - 1 - i) * val)
            
            result.append(left_total + right_total)
            
            left_sum += val
            
        return result