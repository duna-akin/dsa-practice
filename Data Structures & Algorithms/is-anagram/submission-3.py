class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # they can't be anagrams if lengths are not equal
        if len(s) != len(t):
            return False
        
        # frequency table with each chars as keys
        map = {}

        # increment frequency when a char is in s and decrement when in t
        for s_char, t_char in zip(s, t):
            map[s_char] = map.get(s_char, 0) - 1
            map[t_char] = map.get(t_char, 0) + 1

        # if they truly have same frequency of letters they will negate each other
        for val in map.values():
            if val != 0:
                return False

        return True