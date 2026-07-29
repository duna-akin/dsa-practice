class Solution:
    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for s in strs:
            encodedString += str(len(s)) + '@' + s
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedStrings = list()
        i = 0

        while i < len(s):
            j = i
            while s[j] != '@':
                j += 1
            length = int(s[i:j])
            decodedString = s[j + 1: j + 1 + length]
            decodedStrings.append(decodedString)

            i = j + 1 + length

        return decodedStrings
