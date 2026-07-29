class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = [] # pairs: [index, temp]
        for i in range(len(temperatures)):
            currTemp = temperatures[i]
            while stack and currTemp > stack[-1][1]:
                oldIndex, oldTemp = stack.pop()
                output[oldIndex] = (i - oldIndex)
            stack.append([i, currTemp])
        return output