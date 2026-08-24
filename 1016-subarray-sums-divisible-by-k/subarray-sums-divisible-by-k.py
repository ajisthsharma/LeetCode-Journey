class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref_sum=0
        sums={0:1}
        ans=0

        for num in nums:
            pref_sum+=num
            key=pref_sum%k

            if key in sums:
                ans+=sums[key]
                sums[key]+=1
                continue
            sums[key]=1

        return ans