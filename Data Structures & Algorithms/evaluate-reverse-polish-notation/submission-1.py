class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        operatorSet = {'+', '-', '*', '/'}

        for c in tokens:
            if c not in operatorSet:
                numStack.append(int(c))
            elif c == '+':
                num1 = numStack.pop()
                num2 = numStack.pop()
                numStack.append(num2 + num1)
            elif c == '-':
                num1 = numStack.pop()
                num2 = numStack.pop()
                numStack.append(num2 - num1)
            elif c == '*':
                num1 = numStack.pop()
                num2 = numStack.pop()
                numStack.append(num2 * num1)
            elif c == '/':
                num1 = numStack.pop()
                num2 = numStack.pop()
                numStack.append(int(num2 / num1))
        return numStack[0]
