import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b)
        }
        stack = []
        for c in tokens:
            if c in ops:
                b, a = stack.pop(), stack.pop()
                stack.append(ops[c](a, b))
            else:
                stack.append(int(c))
        return stack[0]