class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        frequencyMap = dict()

        for i in range(len(s)):
            frequencyMap[s[i]] = frequencyMap.get(s[i], 0) + 1
            frequencyMap[t[i]] = frequencyMap.get(t[i], 0) - 1
        for f in frequencyMap.values():
            if f != 0:
                return False
        return True