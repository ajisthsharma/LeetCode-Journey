class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count={}
        ans=left=0

        for i,ch in enumerate(s):
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1

            while count[ch]>2:
                count[s[left]]-=1
                left+=1

            ans=max(ans,i-left+1)

        return ans