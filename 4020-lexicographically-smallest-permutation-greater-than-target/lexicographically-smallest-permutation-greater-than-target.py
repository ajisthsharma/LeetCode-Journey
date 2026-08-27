class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        S=[ord(ch)-97 for ch in s]
        T=[ord(ch)-97 for ch in target]
        S.sort(reverse=True)
        ans=[]

        for i,ch in enumerate(T):
            if ch in S:
                S.remove(ch)
                if S>T[i+1:]:
                    ans.append(ch)
                    continue
                S.append(ch)
                S.sort(reverse=True)

            S.sort()
            for x in S:
                if x>ch:
                    S.remove(x)
                    ans.append(x)
                    ans.extend(S)
                    break

            break

        return ''.join(chr(97+ch) for ch in ans)