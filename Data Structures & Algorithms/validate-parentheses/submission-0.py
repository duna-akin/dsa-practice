class Solution:
    def isValid(self, s: str) -> bool:
        parMap = {'}' : '{', ']' : '[', ')' : '('}
        stack = []

        for char in s:

            # if character is a closing paranthesis
            if char in parMap:

                # check if the opening is in stack and pop
                if stack and stack[-1] == parMap[char]:
                    stack.pop()
                else:
                    return False

            # if character is an opening paranthesis
            else:
                stack.append(char) # add to stack

        return True if not stack else False