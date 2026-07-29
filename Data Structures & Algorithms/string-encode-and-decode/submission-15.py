class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""

        for string in strs:
            result += str(len(string)) + "#" + string

        return result

    def decode(self, s: str) -> List[str]:
        result = list()
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i : j]) # the part before the # is where the length was stored

            currString = s[j + 1 : j + 1 + length]
            result.append(currString)

            i = j + 1 + length

        return result