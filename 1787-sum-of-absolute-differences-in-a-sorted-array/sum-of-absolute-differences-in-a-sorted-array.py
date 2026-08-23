class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pref=[0]*n
        suff=[0]*n
        ans=[0]*n

        pref[0]=nums[0]
        suff[n-1]=nums[n-1]

        for i in range(1,n):
            pref[i]=pref[i-1]+nums[i]
            suff[n-i-1]=suff[n-i]+nums[n-i-1]

        for i in range(n):
            diff=(nums[i]*i - pref[i]) + (suff[i] - nums[i]*(n-i-1))
            ans[i]=diff

        return ans