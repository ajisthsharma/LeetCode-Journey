class Solution:
    def passwordStrength(self, password: str) -> int:
        seen=set()
        ans=0

        for ch in password:
            if ch not in seen:
                if ch.islower():
                    ans+=1
                
                elif ch.isupper():
                    ans+=2

                elif ch.isdigit():
                    ans+=3

                else:
                    ans+=5

            seen.add(ch)

        return ans