class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freqMap = dict()

        for sch, tch in zip(s, t):
            freqMap[sch] = freqMap.get(sch, 0) + 1
            freqMap[tch] = freqMap.get(tch, 0) - 1

        for value in freqMap.values():
            if value != 0:
                return False



        return True