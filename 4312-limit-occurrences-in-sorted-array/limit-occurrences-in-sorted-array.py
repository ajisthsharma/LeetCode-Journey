class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:

        dict1 = {}
        ans = []
        for i in nums:
            if i not in dict1:
                dict1[i] = 1
                ans.append(i)

            elif dict1[i]<k:
                dict1[i]+=1
                ans.append(i)

        return ans


        

            
        