class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freqMap = dict()
        n = len(s1)

        for c in s1:
            freqMap[c] = freqMap.get(c, 0) + 1
        
        for i in range(len(s2) - n + 1):
            freqMapCopy = freqMap.copy()
            for j in range(i, i+n):
                freqMapCopy[s2[j]] = freqMapCopy.get(s2[j], 0) - 1
            if set(freqMapCopy.values()) == {0}:
                return True

        return False