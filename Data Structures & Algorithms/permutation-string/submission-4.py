class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1, freqWindow = [0] * 26, [0] * 26
        n, m = len(s1), len(s2)
        matches, l, r = 0, 0, n

        if n > m:
            return False

        for i in range(n):
            indexs1, indexs2 = ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a')
            freq1[indexs1] += 1
            freqWindow[indexs2] += 1

        for i in range(26):
            if freq1[i] == freqWindow[i]:
                matches += 1

        if matches == 26:
            return True

        while r < m:
            rIndex = ord(s2[r]) - ord('a')
            freqWindow[rIndex] += 1
            if freq1[rIndex] == freqWindow[rIndex]:
                matches += 1
            elif freq1[rIndex] == freqWindow[rIndex] - 1:
                matches -= 1
            
            lIndex = ord(s2[l]) - ord('a')
            freqWindow[lIndex] -= 1
            if freq1[lIndex] == freqWindow[lIndex]:
                matches += 1
            elif freq1[lIndex] == freqWindow[lIndex] + 1:
                matches -= 1
            
            l += 1
            r += 1

            if matches == 26:
                return True
        
        return False


