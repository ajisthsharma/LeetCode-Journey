class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans=0
        freq=defaultdict(int)
        l=0

        for i,num in enumerate(nums):
            freq[num]+=1

            while freq[num]>k:
                freq[nums[l]]-=1
                l+=1
            
            ans=max(ans,i-l+1)

        return ans