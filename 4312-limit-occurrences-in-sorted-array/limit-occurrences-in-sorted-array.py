class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        freq={}
        ans=[]

        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
            
            if freq[num]<=k:
                ans.append(num)

        return ans