class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        counter = 0
        res = []

        while counter < len(word1) or counter < len(word2):

            if counter < len(word1):
                res.append(word1[counter])
            
            if counter < len(word2):
                res.append(word2[counter])
            
            counter += 1

        return ''.join(res)