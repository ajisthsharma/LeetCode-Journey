class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def solve(remaining,num,comb):
            if remaining==0:
                ans.append(comb.copy())
            
            else:
                for i in range(num,n+1):
                    comb.append(i)
                    solve(remaining-1,i+1,comb)
                    comb.pop()

        ans=[]
        solve(k,1,[])

        return ans