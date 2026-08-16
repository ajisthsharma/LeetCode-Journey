class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def solve(start,target,comb):
            if target==0:
                ans.append(comb)
            if target<0:
                return

            for i in range(start,len(candidates)):
                solve(i,target-candidates[i],comb+[candidates[i]])

        ans=[]
        candidates.sort()
        solve(0,target,[])

        return ans