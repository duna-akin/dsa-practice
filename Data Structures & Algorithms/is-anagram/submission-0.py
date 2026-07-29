class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # for frequency counting, increment for s and decrement for t
        map = {}

        for i in range(0, len(s)):

            map[s[i]] = map.get(s[i], 0) + 1
            map[t[i]] = map.get(t[i], 0) - 1

        
        # return true if all map values are 0 and false if not

        for val in map.values():
            if val != 0:
                return False


        return True