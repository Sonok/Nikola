
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # i think we should use a stack that goes backward
        # so we have symbol and then have two numbers that we then pair 

        stack = []
        for i, s in enumerate(tokens):
            if s not in '+-*/':
                stack.append(int(s))
                continue
            m, n = stack.pop(), stack.pop()
            if s == '+':
                stack.append(n+m)
            elif s == '-':
                stack.append(n-m)
            elif s == '*':
                stack.append(n*m)
            else:
                stack.append(int(n/m))
        return stack[0]
            

