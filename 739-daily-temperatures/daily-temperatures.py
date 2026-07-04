class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans=[0]*(len(temperatures))

        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
                continue

            else:
                while stack and temperatures[stack[-1]]<temperatures[i]:
                    ind=stack.pop()
                    ans[ind]=i-ind

                stack.append(i)

        return ans