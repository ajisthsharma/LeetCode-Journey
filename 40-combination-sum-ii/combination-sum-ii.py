class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def solve(start,target,comb):
            if target==0:
                ans.append(comb)
                return

            if target<0:
                return 

            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                solve(i+1,target-candidates[i],comb+[candidates[i]])

        ans=[]
        candidates.sort()
        solve(0,target,[])

        return ans