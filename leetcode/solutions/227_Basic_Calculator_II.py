class Solution:
    def calculate(self, s: str) -> int:
        stack = [] 
        sign = '+'
        num = 0

        for i, c in enumerate(s):
            if c.isdigit(): 
                num = num * 10 + int(c)
            if ((not c.isdigit() and c != ' ') or i == len(s) - 1):
            # if u see a new operation u shld clean up the last 
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                if sign == '*':
                    val = stack.pop() * num
                    stack.append(val)
                if sign == '/':
                    val = (int) (stack.pop() / num)
                    stack.append(val)
                
                num = 0
                sign = c
            # expression whether a * b a/b a+b a-b
        
        return sum(stack)
        