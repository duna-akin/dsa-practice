class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = [] # index
        for i in range(len(temperatures)):
            currTemp = temperatures[i]
            while stack and currTemp > temperatures[stack[-1]]:
                oldIndex = stack.pop()
                output[oldIndex] = (i - oldIndex)
            stack.append(i)
        return output