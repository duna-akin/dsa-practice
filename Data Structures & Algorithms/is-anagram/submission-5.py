class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freqMap = {}

        for sChar, tChar in zip(s, t):
            freqMap[sChar] = freqMap.get(sChar, 0) + 1
            freqMap[tChar] = freqMap.get(tChar, 0) - 1


        for values in freqMap.values():
            if values != 0:
                return False

        return True