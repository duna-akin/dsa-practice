class Solution:
    def isValid(self, s: str) -> bool:
        Hmap = {'}': '{', ']': '[', ')': '('}
        stack = []

        for c in s:
            if c in Hmap.keys():
                if stack and stack[-1] == Hmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0