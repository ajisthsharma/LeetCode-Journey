class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        sign = 1
        curr = 0

        for ch in s:
            if ch == " ":
                continue
            elif ch.isdigit():
                curr = curr * 10 + int(ch)
            elif ch == '+':
                result += sign * curr
                sign = 1
                curr = 0
            elif ch == '-':
                result += sign * curr
                sign = -1
                curr = 0
            elif ch == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            else:
                result += sign * curr
                result *= stack.pop()
                result += stack.pop()
                curr = 0
        
        result += sign * curr
        return result