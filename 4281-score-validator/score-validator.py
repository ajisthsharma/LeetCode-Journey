class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score=count=0

        for ch in events:
            if ch=='W':
                count+=1

            elif ch=='WD' or ch=='NB':
                score+=1

            else:
                score+=int(ch)

            if count==10: break

        return [score,count]