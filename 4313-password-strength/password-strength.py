class Solution:
    def passwordStrength(self, password: str) -> int:
        strength = 0
        for i in set(password):
            if i.islower():
                strength += 1
            elif i.isupper():
                strength += 2
            elif i.isdigit():
                strength += 3
            else:
                strength += 5

        return strength