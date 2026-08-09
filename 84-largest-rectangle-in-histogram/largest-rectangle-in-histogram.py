class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        ans=0
        stack=[]

        for i in range(n):
            while stack and heights[stack[-1]]>heights[i]:
                idx=stack.pop()

                left=stack[-1] if stack else -1
                width=i-left-1

                ans=max(ans,heights[idx]*width)

            stack.append(i)

        while stack:
            idx=stack.pop()

            left=stack[-1] if stack else -1
            width=n-left-1

            ans=max(ans,heights[idx]*width)

        return ans