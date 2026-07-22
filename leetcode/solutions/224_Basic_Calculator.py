class Solution:
    def calculate(self, s: str) -> int:
        # so we have 4 things we are building 
        # the total output this should be per level
        # curr which is the current number that we are building
        # sign = which is the sign that preceeds the output operation
        # stack that keeps in memory all the math and operation not done at that level

        total, curr, sign, stack = 0, 0, 1, []
        for c in s:
            if c.isdigit():
                curr = curr * 10 + int(c) 
            elif c in "+-":
                total += sign * curr
                curr = 0
                if c == '+':
                    sign = 1
                else:
                    sign = -1
            elif c == '(':
                stack.append(total)
                stack.append(sign)
                # you have to reset the total, curr, and sign like a recursive step
                total = curr = 0
                sign = 1
            elif c == ')' :
                total += sign * curr
                total *= stack.pop()
                total += stack.pop() # abvoe level
                curr = 0
        
        return total + sign * curr